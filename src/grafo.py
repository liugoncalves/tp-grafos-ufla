import re

class GrafoCARP:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.num_vertices = 0
        self.num_arestas = 0
        self.num_arcos = 0
        self.num_arestas_req = 0
        self.num_arcos_req = 0
        self.capacidade = 0

        self.arestas_nao_obrigatorias = []  # Arestas não obrigatórias
        self.arestas_obrigatorias = []      # Arestas obrigatórias
        self.arcos_nao_obrigatorios = []    # Arcos não obrigatórios
        self.arcos_obrigatorios = []        # Arcos obrigatórios
        self.nos_obrigatorios = []          # Nós obrigatórios (ReN)

        self.adj_matrix = None
        self.distancias_minimas = None
        self.predecessores = None

        self.info = {}
        self._carregar_dados()
        self._inicializar_matriz_adj()

    def _carregar_dados(self):
        with open(self.caminho_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()

        self._extrair_info_basica(linhas)
        self._processar_secoes(linhas)
        self.capacidade = self.info.get('capacidade', 0)

    def _extrair_info_basica(self, linhas):
        padroes = {
            'nome': r'Name:\s+(\S+)',
            'valor_otimo': r'Optimal value:\s+(-?\d+)',
            'veiculos': r'#Vehicles:\s+(-?\d+)',
            'capacidade': r'Capacity:\s+(\d+)',
            'deposito': r'Depot Node:\s+(\d+)',
            'nos': r'#Nodes:\s+(\d+)',
            'arestas': r'#Edges:\s+(\d+)',
            'arcos': r'#Arcs:\s+(\d+)',
            'nos_obrigatorios': r'#Required N:\s+(\d+)',
            'arestas_obrigatorias': r'#Required E:\s+(\d+)',
            'arcos_obrigatorios': r'#Required A:\s+(\d+)'
        }

        for linha in linhas:
            for chave, regex in padroes.items():
                m = re.search(regex, linha)
                if m:
                    valor = m.group(1)
                    self.info[chave] = int(valor) if valor.isdigit() else valor

        self.num_vertices = self.info.get('nos', 0)

    def _processar_secoes(self, linhas):
        lendo = {
            'nos': False,
            'arestas_req': False,
            'arestas_nreq': False,
            'arcos_req': False,
            'arcos_nreq': False
        }

        for linha in linhas:
            linha = linha.strip()

            if linha.startswith('ReN.'):
                self._reset_lendo(lendo)
                lendo['nos'] = True
                continue
            elif linha.startswith('ReE.'):
                self._reset_lendo(lendo)
                lendo['arestas_req'] = True
                continue
            elif linha.startswith('ReA.'):
                self._reset_lendo(lendo)
                lendo['arcos_req'] = True
                continue
            elif linha.startswith('EDGE'):
                self._reset_lendo(lendo)
                lendo['arestas_nreq'] = True
                continue
            elif linha.startswith('ARC'):
                self._reset_lendo(lendo)
                lendo['arcos_nreq'] = True
                continue

            if lendo['nos']:
                self._processar_no(linha)
            elif lendo['arestas_req']:
                self._processar_aresta_ou_arco(linha, obrigatorio=True, tipo='aresta')
            elif lendo['arestas_nreq']:
                self._processar_aresta_ou_arco(linha, obrigatorio=False, tipo='aresta')
            elif lendo['arcos_req']:
                self._processar_aresta_ou_arco(linha, obrigatorio=True, tipo='arco')
            elif lendo['arcos_nreq']:
                self._processar_aresta_ou_arco(linha, obrigatorio=False, tipo='arco')

    def _reset_lendo(self, lendo_dict):
        for chave in lendo_dict:
            lendo_dict[chave] = False

    def _processar_no(self, linha):
        partes = linha.split()
        if len(partes) == 3 and partes[0].startswith('N'):
            try:
                id_no = int(partes[0][1:])
                demanda = int(partes[1])
                custo_servico = int(partes[2])
                self.nos_obrigatorios.append({'no': id_no, 'demanda': demanda, 'custo': custo_servico})
            except ValueError:
                pass

    def _processar_aresta_ou_arco(self, linha, obrigatorio, tipo):
        partes = linha.split()
        if (obrigatorio and len(partes) == 6) or (not obrigatorio and len(partes) == 4):
            try:
                u = int(partes[1])
                v = int(partes[2])
                custo = int(partes[3])
                demanda = int(partes[4]) if obrigatorio else 0

                tupla = (u, v, custo, demanda)

                if tipo == 'aresta':
                    self.num_arestas += 1
                    if obrigatorio:
                        self.arestas_obrigatorias.append(tupla)
                        self.num_arestas_req += 1
                    else:
                        self.arestas_nao_obrigatorias.append(tupla)
                else:  # tipo == 'arco'
                    self.num_arcos += 1
                    if obrigatorio:
                        self.arcos_obrigatorios.append(tupla)
                        self.num_arcos_req += 1
                    else:
                        self.arcos_nao_obrigatorios.append(tupla)
            except ValueError:
                pass

    def _inicializar_matriz_adj(self):
        n = self.num_vertices
        self.adj_matrix = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            self.adj_matrix[i][i] = 0

        # Preenche com arestas não obrigatórias (simétricas)
        for u, v, custo, _ in self.arestas_nao_obrigatorias:
            self.adj_matrix[u-1][v-1] = custo
            self.adj_matrix[v-1][u-1] = custo

        # Preenche com arestas obrigatórias (simétricas)
        for u, v, custo, _ in self.arestas_obrigatorias:
            self.adj_matrix[u-1][v-1] = custo
            self.adj_matrix[v-1][u-1] = custo

        # Preenche com arcos não obrigatórios (direcionados)
        for u, v, custo, _ in self.arcos_nao_obrigatorios:
            self.adj_matrix[u-1][v-1] = custo

        # Preenche com arcos obrigatórios (direcionados)
        for u, v, custo, _ in self.arcos_obrigatorios:
            self.adj_matrix[u-1][v-1] = custo

    def calcular_floyd_warshall(self):
        n = self.num_vertices
        INF = float('inf')

        dist = [row[:] for row in self.adj_matrix]
        pred = [[None] * n for _ in range(n)]

        for u in range(n):
            for v in range(n):
                if u != v and dist[u][v] != INF:
                    pred[u][v] = u + 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        pred[i][j] = pred[k][j]

        self.distancias_minimas = dist
        self.predecessores = pred

    def obterDistanciaMinima(self, origem, destino):
        if self.distancias_minimas is None or self.predecessores is None:
            self.calcular_floyd_warshall()
        return self.distancias_minimas[origem-1][destino-1]

    def obterCaminhoMinimo(self, origem, destino):
        if self.distancias_minimas is None or self.predecessores is None:
            self.calcular_floyd_warshall()

        u = origem - 1
        v = destino - 1

        if self.predecessores[u][v] is None:
            return []  # Sem caminho

        caminho = []
        while v != u:
            caminho.insert(0, v + 1)
            v = self.predecessores[u][v] - 1
        caminho.insert(0, origem)

        return caminho

    def caminho_minimo(self, origem, destino):
        return self.obterCaminhoMinimo(origem, destino)

    def get_dados(self):
        nos_dict = {item['no']: {'demanda': item['demanda'], 'custo': item['custo']} for item in self.nos_obrigatorios}

        return {
            'arestas_obrigatorias': self.arestas_obrigatorias,
            'arestas_nao_obrigatorias': self.arestas_nao_obrigatorias,
            'arcos_obrigatorios': self.arcos_obrigatorios,
            'arcos_nao_obrigatorios': self.arcos_nao_obrigatorios,
            'nos': nos_dict
        }
