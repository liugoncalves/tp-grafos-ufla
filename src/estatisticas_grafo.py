from collections import Counter
from grafo import GrafoCARP

class EstatisticasGrafo:
    def __init__(self, grafo_carp: GrafoCARP):
        self.grafo = grafo_carp

    def grau_vertices(self):
        n = self.grafo.num_vertices
        grau_saida = [0]*n
        grau_entrada = [0]*n

        for u, v, _, _ in self.grafo.arestas_nao_obrigatorias + self.grafo.arestas_obrigatorias:
            grau_saida[u-1] += 1
            grau_saida[v-1] += 1
            grau_entrada[u-1] += 1
            grau_entrada[v-1] += 1

        for u, v, _, _ in self.grafo.arcos_nao_obrigatorios + self.grafo.arcos_obrigatorios:
            grau_saida[u-1] += 1
            grau_entrada[v-1] += 1

        graus = [grau_saida[i] + grau_entrada[i] for i in range(n)]
        return graus

    def intermediacao(self):
        n = self.grafo.num_vertices
        self.grafo.calcular_floyd_warshall()
        dist = self.grafo.distancias_minimas

        contagem = [0]*n
        total_pares = 0

        for s in range(n):
            for t in range(n):
                if s != t and dist[s][t] < float('inf'):
                    total_pares += 1
                    caminho = self.grafo.obterCaminhoMinimo(s+1, t+1)
                    for v in caminho[1:-1]:
                        contagem[v-1] += 1

        if total_pares == 0:
            return 0
        return sum(contagem)/total_pares

    def caminho_medio(self):
        n = self.grafo.num_vertices
        self.grafo.calcular_floyd_warshall()
        dist = self.grafo.distancias_minimas
        soma = 0
        contador = 0

        for i in range(n):
            for j in range(n):
                if i != j and dist[i][j] < float('inf'):
                    soma += dist[i][j]
                    contador += 1
        if contador == 0:
            return float('inf')
        return soma / contador

    def diametro(self):
        n = self.grafo.num_vertices
        self.grafo.calcular_floyd_warshall()
        dist = self.grafo.distancias_minimas
        maior = 0
        for i in range(n):
            for j in range(n):
                if i != j and dist[i][j] < float('inf'):
                    if dist[i][j] > maior:
                        maior = dist[i][j]
        return maior

    def densidade(self):
        n = self.grafo.num_vertices
        m = self.grafo.num_arestas + self.grafo.num_arcos
        if n <= 1:
            return 0
        if self.grafo.num_arcos > 0:
            max_arestas = n * (n-1)
            return m / max_arestas
        else:
            max_arestas = n * (n-1) / 2
            return m / max_arestas

    def is_direcionado(self):
        return self.grafo.num_arcos > 0

    def calcular(self):
        graus = self.grau_vertices()
        grau_min = min(graus) if graus else 0
        grau_max = max(graus) if graus else 0

        stats = {
            "1- Quantidade de vértices": self.grafo.num_vertices,
            "2- Quantidade de arestas": self.grafo.num_arestas,
            "3- Quantidade de arcos": self.grafo.num_arcos,
            "4- Quantidade de vértices obrigatórios": len(self.grafo.nos_obrigatorios),
            "5- Quantidade de arestas obrigatórias": self.grafo.num_arestas_req,
            "6- Quantidade de arcos obrigatórios": self.grafo.num_arcos_req,
            "7- É direcionado?": self.is_direcionado(),
            "8- Densidade": self.densidade(),
            "9- Grau mínimo": grau_min,
            "10- Grau máximo": grau_max,
            "11- Intermedição": self.intermediacao(),
            "12- Caminho Médio": self.caminho_medio(),
            "13- Diâmetro": self.diametro()
        }
        return stats