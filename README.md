# Analisador de Grafos - Trabalho Prático UFLA (GCC218)

Este projeto foi desenvolvido como parte do **Trabalho Prático Final da disciplina GCC218 - Algoritmos em Grafos**, ministrada na Universidade Federal de Lavras (UFLA).

## 🧠 Entendendo o Projeto

Este projeto é um **analisador de grafos** desenvolvido em Python, voltado para a leitura e análise de arquivos `.dat` contendo dados sobre grafos — estruturas que representam redes de conexões entre elementos. Em termos simples, um grafo pode ser comparado a um **mapa de cidades conectadas por estradas**.

O programa lê esses dados, interpreta os elementos do grafo (como os “pontos” e as “ligações” entre eles), e calcula uma série de **estatísticas úteis** para entender como essa rede se comporta.

### 🤔 Para quem não conhece grafos, pense assim:

Imagine que temos um mapa com cidades (os **vértices**) e estradas (as **arestas**) que ligam essas cidades. Algumas dessas estradas são obrigatórias — por exemplo, ruas que precisam ser percorridas por um caminhão de coleta. O nosso programa ajuda a responder perguntas como:

- **Qual cidade fica "no meio do caminho" com mais frequência?**  
  Isso indica pontos estratégicos na rede (chamado de **intermediação**).

- **Qual é a distância média entre dois pontos qualquer no mapa?**  
  Isso ajuda a entender o "tamanho médio" da rede (**caminho médio**).

- **Qual é a maior menor distância entre dois pontos?**  
  Essa medida é chamada de **diâmetro** — mostra a maior distância possível entre dois pontos acessíveis.

Essas métricas são úteis em áreas como logística, transporte, redes de computadores, redes sociais e muito mais.

---

## 📚 Sobre o Trabalho

Este projeto foi desenvolvido como parte da disciplina de **Grafos** do curso de Sistemas de Informação da Universidade Federal de Lavras (UFLA). O objetivo principal do trabalho é aplicar conceitos teóricos de grafos na prática, por meio da análise de instâncias reais ou simuladas de problemas clássicos da área.

### 🔍 O que o software faz?

- **Lê e interpreta arquivos `.dat` contendo descrições de grafos**, incluindo vértices (nós), arestas (conexões bidirecionais), arcos (conexões direcionadas), e quais desses elementos são obrigatórios.
- **Executa o algoritmo de Floyd-Warshall**, um método clássico que calcula todos os caminhos mínimos entre todos os pares de vértices.
- **Calcula e exibe diversas estatísticas estruturais do grafo**, como:
  - Grau mínimo e máximo dos vértices;
  - Densidade do grafo;
  - Caminho médio entre vértices;
  - Diâmetro do grafo;
  - Intermediação (Betweenness Centrality).

---

## 💡 Qual problema o projeto resolve?

Este analisador foi pensado para lidar com instâncias de problemas reais de otimização de rotas, como o **Rural Postman Problem (RPP)**. Nesse tipo de problema, é necessário percorrer certas ruas obrigatórias com o menor custo possível — algo bastante comum em tarefas como:

- Coleta de lixo;
- Entrega de correspondências;
- Inspeções em redes de energia ou rodovias.

Ao calcular as estatísticas do grafo, o sistema permite que pesquisadores e desenvolvedores compreendam melhor a estrutura da rede antes de aplicar algoritmos de otimização.

---

## 👤 Autores

- Leonardo Gonçalves
- Matheus Coelho

## 📁 Repositório

Acesse o projeto completo em: [https://github.com/liugoncalves/tp-grafos-ufla](https://github.com/liugoncalves/tp-grafos-ufla)

---

## 🔧 Como Usar

1. **Clone o repositório:**

```bash
git clone https://github.com/liugoncalves/tp-grafos-ufla
cd tp-grafos-ufla
```

2. **(Opcional) Crie um ambiente virtual Python:**

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Certifique-se de que o arquivo `teste.dat` está na raiz do projeto.**

4. **Execute o analisador:**

```bash
python3 analise_grafo.py
```

---

## 🗂️ Formato do Arquivo `.dat`

O arquivo `.dat` segue uma estrutura textual, contendo:

- **EDGE**: arestas (ligações bidirecionais)
- **ARC**: arcos (ligações com direção)
- **ReN.**: vértices obrigatórios
- **ReE.**: arestas obrigatórias
- **ReA.**: arcos obrigatórios

O script usa expressões regulares para encontrar e extrair esses dados automaticamente.

---

## 📊 Métricas Calculadas

| Nº | Métrica                        | Descrição                                                                 |
|----|--------------------------------|---------------------------------------------------------------------------|
| 1  | Quantidade de vértices         | Total de nós (pontos) no grafo                                            |
| 2  | Quantidade de arestas          | Conexões bidirecionais                                                    |
| 3  | Quantidade de arcos            | Conexões direcionadas                                                     |
| 4  | Arestas obrigatórias           | Arestas que obrigatoriamente devem ser percorridas (ex: ruas essenciais) |
| 5  | Arcos obrigatórios             | Versão direcionada das arestas obrigatórias                              |
| 6  | Vértices obrigatórios          | Pontos obrigatórios                                                       |
| 7  | Grau mínimo                    | Mínimo de conexões por vértice                                            |
| 8  | Grau máximo                    | Máximo de conexões por vértice                                            |
| 9  | É direcionado?                 | O grafo possui arcos?                                                     |
| 10 | Densidade                      | Grau de conectividade geral do grafo                                      |
| 11 | Centralidade de intermediação | Importância dos nós em caminhos entre outros pares                        |
| 12 | Caminho médio                  | Distância média entre todos os pares de nós conectados                   |
| 13 | Diâmetro                       | Maior distância mínima entre dois nós do grafo                            |

---

## 🧠 Tecnologias e Algoritmos Usados

- Linguagem: **Python 3**
- Leitura com: `re` (expressões regulares)
- Matrizes de caminhos mínimos: **Floyd-Warshall**
- Cálculo de intermediação: baseado em contagem de caminhos mínimos
- Cálculo de densidade e graus: diretamente com base na estrutura

---

## 🔍 Exemplo de Saída

Após rodar o programa, você verá algo como:

```text
Estatísticas do Grafo:
1- Quantidade de vértices: 15
2- Quantidade de arestas: 22
3- Quantidade de arcos: 0
4- Quantidade de arestas obrigatórias: 5
5- Quantidade de arcos obrigatórios: 0
6- Quantidade de vértices obrigatórios: 3
7- Grau mínimo: 2
8- Grau máximo: 5
9- O grafo é direcionado? Não
10- Densidade: 0.2095
11- Intermediação (top 3): [(3, 0.28), (7, 0.23), (1, 0.17)]
12- Caminho médio: 6.41
13- Diâmetro: 16
```

---

## ✏️ Personalização

Você pode trocar o arquivo analisado modificando a linha final do `analise_grafo.py`:

```python
caminho_arquivo = "teste.dat"
```

Substitua `"teste.dat"` pelo nome de outro arquivo no mesmo formato.

---

## 🧾 Licença

Este projeto é de uso acadêmico e livre para estudo. Contribuições e adaptações são bem-vindas, desde que referenciem o autor.

---

Em caso de dúvidas ou sugestões, abra uma *issue* no repositório!
