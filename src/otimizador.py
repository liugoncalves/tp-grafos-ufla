def otimizar_solucao(grafo, solucao_inicial, max_iter=10):
    solucao = list(solucao_inicial)  # copia da solucao inicial
    iteracoes_sem_melhora = 0

    while iteracoes_sem_melhora < max_iter:
        melhorou = False

        # ordena as rotas por custo decrescente para priorizar otimizacao nas piores
        indices_rotas = sorted(range(len(solucao)), key=lambda i: solucao[i]["custo"], reverse=True)

        for i in indices_rotas:
            for j in range(len(solucao)):
                if i == j:
                    continue

                rota_origem = solucao[i]
                rota_destino = solucao[j]

                # ordena os servicos da origem por custo de servico decrescente (prioriza mais caros)
                servicos_ordenados = sorted(
                    rota_origem["servicos_atendidos"],
                    key=lambda s: custo_servico(grafo, s),
                    reverse=True
                )

                for servico in servicos_ordenados:
                    nova_rota_origem = rota_origem["servicos_atendidos"].copy()
                    nova_rota_origem.remove(servico)
                    nova_rota_destino = rota_destino["servicos_atendidos"] + [servico]

                    if calcular_demanda(grafo, nova_rota_destino) > grafo.capacidade:
                        continue

                    nova_info_origem = reconstruir_rota(grafo, nova_rota_origem)
                    nova_info_destino = reconstruir_rota(grafo, nova_rota_destino)

                    novo_custo_total = nova_info_origem["custo"] + nova_info_destino["custo"]
                    custo_antigo_total = rota_origem["custo"] + rota_destino["custo"]

                    if novo_custo_total < custo_antigo_total:
                        solucao[i] = nova_info_origem
                        solucao[j] = nova_info_destino
                        melhorou = True
                        break  # melhora imediata

                if melhorou:
                    break
            if melhorou:
                break

        if melhorou:
            iteracoes_sem_melhora = 0
        else:
            iteracoes_sem_melhora += 1

    return solucao


def custo_servico(grafo, servico):
    tipo, dado = servico
    if tipo == "no":
        return grafo.get_demanda_no(dado)
    elif tipo == "aresta":
        u, v = dado
        return grafo.get_demanda_aresta(u, v)
    elif tipo == "arco":
        u, v = dado
        return grafo.get_demanda_arco(u, v)
    return 0


def calcular_demanda(grafo, servicos):
    total = 0
    for tipo, dado in servicos:
        if tipo == "no":
            total += grafo.get_demanda_no(dado)
        elif tipo == "aresta":
            u, v = dado
            total += grafo.get_demanda_aresta(u, v)
        elif tipo == "arco":
            u, v = dado
            total += grafo.get_demanda_arco(u, v)
    return total


def reconstruir_rota(grafo, lista_servicos):
    rota = [1]
    custo = 0
    carga = 0
    detalhes = [{"servico": {"tipo": "D"}}]
    atual = 1

    for tipo, dado in lista_servicos:
        if tipo == "no":
            no = dado
            caminho = grafo.obterCaminhoMinimo(atual, no)
            rota += caminho[1:]
            custo += grafo.obterDistanciaMinima(atual, no)
            custo += grafo.get_demanda_no(no)
            carga += grafo.get_demanda_no(no)
            detalhes.append({"servico": {"tipo": "no", "id": -1, "origem": no, "destino": no}})
            atual = no

        elif tipo == "aresta":
            u, v = dado
            chegada, outro = (u, v) if grafo.obterDistanciaMinima(atual, u) <= grafo.obterDistanciaMinima(atual, v) else (v, u)
            caminho = grafo.obterCaminhoMinimo(atual, chegada)
            rota += caminho[1:]
            custo += grafo.obterDistanciaMinima(atual, chegada)
            custo += grafo.get_demanda_aresta(u, v)
            carga += grafo.get_demanda_aresta(u, v)
            detalhes.append({"servico": {"tipo": "aresta", "id": -1, "origem": u, "destino": v}})
            atual = outro

        elif tipo == "arco":
            u, v = dado
            caminho = grafo.obterCaminhoMinimo(atual, u)
            rota += caminho[1:]
            custo += grafo.obterDistanciaMinima(atual, u)
            custo += grafo.get_demanda_arco(u, v)
            carga += grafo.get_demanda_arco(u, v)
            detalhes.append({"servico": {"tipo": "arco", "id": -1, "origem": u, "destino": v}})
            atual = v

    if atual != 1:
        caminho = grafo.obterCaminhoMinimo(atual, 1)
        rota += caminho[1:]
        custo += grafo.obterDistanciaMinima(atual, 1)

    detalhes.append({"servico": {"tipo": "D"}})

    return {
        "rota": rota,
        "servicos_atendidos": list(lista_servicos),
        "demanda": carga,
        "custo": custo,
        "detalhes": detalhes
    }
