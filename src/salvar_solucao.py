def salvar_resultado_arquivo(solucao, tempo_total_ns, tempo_solucao_ns, nome_arquivo_saida, grafo):
    with open(nome_arquivo_saida, "w", encoding="utf-8") as arquivo:
        custo_total = sum(rota["custo"] for rota in solucao)
        arquivo.write(f"{custo_total}\n")
        arquivo.write(f"{len(solucao)}\n")
        arquivo.write(f"{tempo_total_ns}\n")
        arquivo.write(f"{tempo_solucao_ns}\n")

        for i, rota in enumerate(solucao, start=1):
            visitas = rota["detalhes"]
            demanda_rota = 0

            for visita in visitas:
                serv = visita["servico"]
                tipo = serv["tipo"]

                if tipo == "D" or tipo == "Deposito":
                    continue

                origem = serv["origem"]
                destino = serv["destino"]

                if tipo == "no":
                    demanda_rota += grafo.get_demanda_no(origem)
                elif tipo == "aresta":
                    demanda_rota += grafo.get_demanda_aresta(origem, destino)
                elif tipo == "arco":
                    demanda_rota += grafo.get_demanda_arco(origem, destino)

            custo_rota = rota["custo"]
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
