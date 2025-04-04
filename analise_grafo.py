import re
import itertools
import numpy as np


def ler_arquivo_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    info_grafo = {}
    nos = {}
    arestas_obrigatorias = []
    arestas_nao_obrigatorias = []
    arcos_obrigatorios = []
    arcos_nao_obrigatorios = []

    padroes_info = { # padrao das instancias teste disponibilizadas no campusvirtual
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

    # percorre cada linha do arquivo para encontrar informacoes do grafo
    for linha in linhas:
        for chave, padrao in padroes_info.items():  # percorre cada padrao definido
            correspondencia = re.search(padrao, linha)  # busca a informacao na linha
            if correspondencia:  # se encontrou uma correspondencia
                info_grafo[chave] = int(correspondencia.group(1)) if correspondencia.group(1).isdigit() else correspondencia.group(1)

    total_nos = info_grafo.get('nos', 0)  # obtem o numero total de nos

    lendo_nos = False  
    lendo_arestas_obrigatorias = False 
    lendo_arestas_nao_obrigatorias = False  
    lendo_arcos_obrigatorios = False
    lendo_arcos_nao_obrigatorios = False


    # percorre novamente as linhas do arquivo para extrair os nos e arestas
    for linha in linhas:
        linha = linha.strip()  # remove espacos extras no inicio e no fim da linha

        # identifica o inicio de cada secao no arquivo
        if linha.startswith('ReN.'):
            lendo_nos = True
            lendo_arestas_obrigatorias = False
            lendo_arestas_nao_obrigatorias = False
            continue
        elif linha.startswith('ReE.'):
            lendo_nos = False
            lendo_arestas_obrigatorias = True
            lendo_arestas_nao_obrigatorias = False
            continue
        elif linha.startswith('ReA.'):
            lendo_arcos_obrigatorios = True
            lendo_nos = lendo_arestas_obrigatorias = lendo_arestas_nao_obrigatorias = False
            continue
        elif linha.startswith('EDGE'):
            lendo_nos = False
            lendo_arestas_obrigatorias = False
            lendo_arestas_nao_obrigatorias = True
            continue
        elif linha.startswith('ARC'):
            lendo_arcos_nao_obrigatorios = True
            lendo_nos = lendo_arestas_obrigatorias = lendo_arestas_nao_obrigatorias = lendo_arcos_obrigatorios = False
            continue

        # se estamos lendo nos, extrai os dados dos nos
        if lendo_nos:
            partes = linha.split()
            if len(partes) == 3:
                id_no = int(partes[0][1:])
                demanda = int(partes[1])
                custo_servico = int(partes[2])
                nos[id_no] = {'demanda': demanda, 'custo_servico': custo_servico}

        # se estamos lendo arestas obrigatorias, extrai os dados delas
        elif lendo_arestas_obrigatorias:
            partes = linha.split()
            if len(partes) == 6:
                de_no = int(partes[1])
                para_no = int(partes[2])
                custo_viagem = int(partes[3])
                demanda = int(partes[4])
                custo_servico = int(partes[5])
                arestas_obrigatorias.append((de_no, para_no, custo_viagem, demanda, custo_servico))

        # se estamos lendo arestas nao obrigatorias, extrai os dados delas
        elif lendo_arestas_nao_obrigatorias:
            partes = linha.split()
            if len(partes) == 4:
                de_no = int(partes[1])
                para_no = int(partes[2])
                custo_viagem = int(partes[3])
                arestas_nao_obrigatorias.append((de_no, para_no, custo_viagem))

        # se estamos lendo arcos obrigatorios, extrai os dados deles
        elif lendo_arcos_obrigatorios:
            partes = linha.split()
            if len(partes) == 6:
                de_no = int(partes[1])
                para_no = int(partes[2])
                custo_viagem = int(partes[3])
                demanda = int(partes[4])
                custo_servico = int(partes[5])
                arcos_obrigatorios.append((de_no, para_no, custo_viagem, demanda, custo_servico))

        # se estamos lendos arcos nao obrigatorios, extrai os dados deles
        elif lendo_arcos_nao_obrigatorios:
            partes = linha.split()
            if len(partes) == 4:
                de_no = int(partes[1])
                para_no = int(partes[2])
                custo_viagem = int(partes[3])
                arcos_nao_obrigatorios.append((de_no, para_no, custo_viagem))


    # armazena os dados coletados no dicionario de informacoes do grafo
    info_grafo['nos'] = nos
    info_grafo['arestas_obrigatorias'] = arestas_obrigatorias
    info_grafo['arestas_nao_obrigatorias'] = arestas_nao_obrigatorias
    info_grafo['arcos_obrigatorios'] = arcos_obrigatorios
    info_grafo['arcos_nao_obrigatorios'] = arcos_nao_obrigatorios


    return info_grafo, total_nos  # retorna o dicionario com os dados e o numero total de nos


def floyd_warshall(grafo, total_nos):
    INF = float('inf')  # define o valor infinito para representar distancias muito grandes
    distancias = [[INF] * total_nos for _ in range(total_nos)]  # cria matriz de distancias inicializada com infinito
    proximo_no = [[-1] * total_nos for _ in range(total_nos)]  # cria matriz para armazenar o proximo no no caminho mais curto

    # inicializa a distancia de cada no para ele mesmo como zero
    for i in range(total_nos):
        distancias[i][i] = 0

    # preenche a matriz de distancias com os valores das arestas do grafo
    for aresta in grafo['arestas_obrigatorias'] + grafo['arestas_nao_obrigatorias']:
        de_no, para_no, custo_viagem = aresta[:3]
        distancias[de_no - 1][para_no - 1] = custo_viagem
        distancias[para_no - 1][de_no - 1] = custo_viagem
        proximo_no[de_no - 1][para_no - 1] = para_no - 1
        proximo_no[para_no - 1][de_no - 1] = de_no - 1

    # algoritmo de floyd warshall para calcular todos os caminhos minimos entre os nos
    for k in range(total_nos):  # percorre todos os nos intermediarios
        for i in range(total_nos):  # percorre os nos de origem
            for j in range(total_nos):  # percorre os nos de destino
                if distancias[i][k] != INF and distancias[k][j] != INF and distancias[i][k] + distancias[k][j] < distancias[i][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]  # atualiza a distancia minima
                    proximo_no[i][j] = proximo_no[i][k]  # atualiza o caminho

    return distancias, proximo_no  # retorna a matriz de distancias e a matriz de predecessores


def calcular_intermediacao(dados_grafo, total_nos):
    distancias, proximo_no = floyd_warshall(dados_grafo, total_nos)  # calcula caminhos minimos
    intermediacao = {i: 0 for i in range(1, total_nos + 1)}  # inicializa dicionario de intermediacao

    # percorre todos os pares de nos para verificar quais passam por outros nos
    for u, v in itertools.combinations(range(total_nos), 2):
        if distancias[u][v] == float('inf'):
            continue  # se nao ha caminho entre os nos, ignora

        caminho = []  # lista para armazenar o caminho entre os nos
        atual = u
        while atual != v:  # percorre o caminho ate chegar ao destino
            caminho.append(atual + 1)
            atual = proximo_no[atual][v]
        caminho.append(v + 1)

        for no in caminho[1:-1]:  # exclui o primeiro e o ultimo no
            intermediacao[no] += 1  # aumenta a contagem para cada no intermediario

    return intermediacao  # retorna a centralidade de intermediacao dos nos


def calcular_diametro(matriz_distancias):
    diametro = 0
    for i in range(len(matriz_distancias)): # percorre a matriz de distancias
        for j in range(len(matriz_distancias)):
            if matriz_distancias[i][j] != float('inf'):  # ignora caminhos inalcancaveis
                diametro = max(diametro, matriz_distancias[i][j])  # encontra a maior distancia minima
    return diametro  # retorna o diametro do grafo


def calcular_caminho_medio(matriz_distancias):
    total_distancia = 0
    contador = 0
    for i in range(len(matriz_distancias)): 
        for j in range(len(matriz_distancias)): 
            if matriz_distancias[i][j] != float('inf') and i != j:  # ignora caminhos inalcancaveis e loops
                total_distancia += matriz_distancias[i][j]
                contador += 1
    return total_distancia / contador if contador > 0 else float('inf')  # calcula a media das distancias


def calcular_estatisticas(dados_grafo, total_nos):
    quantidade_vertices = total_nos
    quantidade_arestas = dados_grafo.get('arestas', 0) 
    quantidade_arcos = dados_grafo.get('arcos', 0)
    quantidade_vertices_obrigatorios = dados_grafo.get('nos_obrigatorios', 0)
    quantidade_arestas_obrigatorias = len(dados_grafo['arestas_obrigatorias'])
    quantidade_arcos_obrigatorios = len(dados_grafo['arcos_obrigatorios'])

    graus = {i: 0 for i in range(1, total_nos + 1)}  # inicializa dicionario de graus dos nos

    # calcula o grau de cada no somando suas conexoes
    for aresta in dados_grafo['arestas_obrigatorias'] + dados_grafo['arestas_nao_obrigatorias']:
        de_no, para_no = aresta[0], aresta[1]
        graus[de_no] += 1
        graus[para_no] += 1

    grau_minimo = min(graus.values()) if graus else 0  # encontra o menor grau
    grau_maximo = max(graus.values()) if graus else 0  # encontra o maior grau

    is_direcionado = quantidade_arcos > 0  # verifica se o grafo e direcionado

    # calcula a densidade do grafo
    if is_direcionado:
        densidade = quantidade_arcos / (quantidade_vertices * (quantidade_vertices - 1)) if quantidade_vertices > 1 else 0
    else:
        densidade = (2 * quantidade_arestas) / (quantidade_vertices * (quantidade_vertices - 1)) if quantidade_vertices > 1 else 0

    intermediacao = calcular_intermediacao(dados_grafo, total_nos)  # calcula intermediacao dos nos
    distancias, _ = floyd_warshall(dados_grafo, total_nos)  # calcula matriz de distancias
    caminho_medio = calcular_caminho_medio(distancias)  # calcula caminho medio
    diametro = calcular_diametro(distancias)  # calcula diametro do grafo

    return {
        "\nEstatísticas do Grafo:\n"
        "1- Quantidade de vértices": quantidade_vertices,
        "2- Quantidade de arestas": quantidade_arestas,
        "3- Quantidade de arcos": quantidade_arcos,
        "4- Quantidade de vértices obrigatórios": quantidade_vertices_obrigatorios,
        "5- Quantidade de arestas obrigatórias": quantidade_arestas_obrigatorias,
        "6- Quantidade de arcos obrigatórios": quantidade_arcos_obrigatorios,
        "7- É direcionado?": is_direcionado,
        "8- Densidade": densidade,
        "9- Grau mínimo": grau_minimo,
        "10- Grau máximo": grau_maximo,
        "11- Intermedição": intermediacao,
        "12- Caminho Médio": caminho_medio,
        "13- Diâmetro": diametro    
        }
