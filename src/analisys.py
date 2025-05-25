import sys
from src import grafo

def path_scanning(grafo):
    grafo.calcular_floyd_warshall()
    
    servicos_pendentes = []
    servico_info = {}
    mapeamento_id = {}
    contador_id = 1
    
    for no_info in sorted(grafo.nos_obrigatorios, key=lambda x: x['no']):
        no = no_info['no']
        chave = ("no", no)
        servicos_pendentes.append(chave)
        servico_info[chave] = {
            "demanda": no_info.get("demanda", 1),
            "custo": no_info.get("custo", 0),
            "extremos": (no, no),
        }
        mapeamento_id[chave] = contador_id
        contador_id += 1
    
    for u, v, custo, demanda in sorted(grafo.arestas_obrigatorias, key=lambda x: (min(x[0], x[1]), max(x[0], x[1]))):
        chave = ("aresta", (u, v) if u < v else (v, u))
        servicos_pendentes.append(chave)
        servico_info[chave] = {
            "demanda": demanda,
            "custo": custo,
            "extremos": (u, v),
        }
        mapeamento_id[chave] = contador_id
        contador_id += 1
    
    for u, v, custo, demanda in sorted(grafo.arcos_obrigatorios, key=lambda x: (x[0], x[1])):
        chave = ("arco", (u, v))
        servicos_pendentes.append(chave)
        servico_info[chave] = {
            "demanda": demanda,
            "custo": custo,
            "extremos": (u, v),
        }
        mapeamento_id[chave] = contador_id
        contador_id += 1
    
    solucao = []
    deposito = 1
    capacidade_max = grafo.capacidade
    
    while servicos_pendentes:
        rota = [deposito]
        carga = 0
        custo = 0
        servicos_rota = []
        detalhes_visitas = [{"servico": {"tipo": "D"}}]  # Depósito inicial
        no_atual = deposito
        
        while True:
            melhor_servico = None
            menor_custo = float('inf')
            melhor_chegada = None
            melhor_outro_extremo = None
            
            for serv in sorted(servicos_pendentes, key=lambda x: mapeamento_id[x]):
                info = servico_info[serv]
                if carga + info["demanda"] > capacidade_max:
                    continue
                
                extremos = info["extremos"]
                
                if serv[0] == "no":
                    dist = grafo.obterDistanciaMinima(no_atual, extremos[0])
                    chegada = extremos[0]
                    outro_extremo = extremos[0]
                else:
                    dist1 = grafo.obterDistanciaMinima(no_atual, extremos[0])
                    dist2 = grafo.obterDistanciaMinima(no_atual, extremos[1])
                    if dist1 <= dist2:
                        dist = dist1
                        chegada = extremos[0]
                        outro_extremo = extremos[1]
                    else:
                        dist = dist2
                        chegada = extremos[1]
                        outro_extremo = extremos[0]
                
                if dist < menor_custo:
                    melhor_servico = serv
                    menor_custo = dist
                    melhor_chegada = chegada
                    melhor_outro_extremo = outro_extremo
            
            if melhor_servico is None:
                break

            caminho = grafo.obterCaminhoMinimo(no_atual, melhor_chegada)
            if caminho and len(caminho) > 1:
                custo += menor_custo
                rota.extend(caminho[1:])
            
            info = servico_info[melhor_servico]
            custo += info["custo"]
            carga += info["demanda"]
            servicos_rota.append(melhor_servico)
            no_atual = melhor_outro_extremo
            
            id_servico = mapeamento_id[melhor_servico]
            visita = {
                "servico": {
                    "tipo": melhor_servico[0],
                    "id": id_servico,
                    "origem": info["extremos"][0],
                    "destino": info["extremos"][1] if melhor_servico[0] != "no" else info["extremos"][0],
                }
            }
            detalhes_visitas.append(visita)
            servicos_pendentes.remove(melhor_servico)
        
        if no_atual != deposito:
            caminho_volta = grafo.obterCaminhoMinimo(no_atual, deposito)
            if caminho_volta:
                dist_volta = grafo.obterDistanciaMinima(no_atual, deposito)
                custo += dist_volta
                rota.extend(caminho_volta[1:])
        
        detalhes_visitas.append({"servico": {"tipo": "D"}})  # Depósito final
        
        solucao.append({
            "rota": rota,
            "servicos_atendidos": servicos_rota,
            "demanda": carga,
            "custo": custo,
            "detalhes": detalhes_visitas,
        })
    
    return solucao


def criar_id_servicos(grafo):
    identificadores = {}
    proximo_id = 1

    for info_no in grafo.nos_obrigatorios:
        nodo = info_no['no']
        identificadores[("no", nodo)] = proximo_id
        proximo_id += 1

    for u, v, _, _ in grafo.arestas_obrigatorias:
        par = (u, v) if u < v else (v, u)
        chave = ("aresta", par)
        if chave not in identificadores:
            identificadores[chave] = proximo_id
            proximo_id += 1

    for u, v, _, _ in grafo.arcos_obrigatorios:
        chave = ("arco", (u, v))
        identificadores[chave] = proximo_id
        proximo_id += 1

    return identificadores

def salvar_resultado_arquivo(solucao, tempo_total_ns, tempo_solucao_ns, nome_arquivo_saida):
    with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo:
        custo_soma = sum(rota["custo"] for rota in solucao)
        num_rotas = len(solucao)

        arquivo.write(f"{custo_soma}\n")
        arquivo.write(f"{num_rotas}\n")
        arquivo.write(f"{tempo_total_ns}\n")
        arquivo.write(f"{tempo_solucao_ns}\n")

        for i, rota in enumerate(solucao, start=1):
            demanda_rota = rota["demanda"]
            custo_rota = rota["custo"]
            visitas = rota["detalhes"]
            total_visitas = len(visitas)

            linha = f"0 1 {i} {demanda_rota} {custo_rota} {total_visitas}"
            for visita in visitas:
                serv = visita["servico"]
                tipo = serv["tipo"]

                if tipo == "D" or tipo == "Deposito":
                    linha += " (D 0,1,1)"
                else:
                    id_s = serv["id"]
                    origem = serv["origem"]
                    destino = serv["destino"]
                    linha += f" (S {id_s},{origem},{destino})"
            arquivo.write(linha + "\n")
