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

Este analisador foi pensado para lidar com instâncias de problemas reais de otimização de rotas. Nesse tipo de problema, é necessário percorrer certas ruas obrigatórias com o menor custo possível, algo bastante comum em tarefas como:

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

3. **Instale as dependências:**

Certifique-se de que o arquivo `requirements.txt` possui o seguinte conteúdo:

```
notebook
```

E instale com:

```bash
pip install -r requirements.txt
```

4. **Certifique-se de que o arquivo `.dat` que deseja analisar está na pasta `dados/`.**

5. **Execute o notebook principal via terminal:**

```bash
jupyter notebook main.ipynb
```

---

### 📌 Observação importante

O arquivo `main.ipynb` é o **arquivo principal** para executar o projeto.  
Ele:

- Carrega os dados do grafo;
- Executa os cálculos;
- Exibe as estatísticas;
- Mostra a visualização gráfica da estrutura.

O arquivo `analise_grafo.py` é **um módulo auxiliar**, responsável apenas pelo cálculo das estatísticas.  
Ele **não deve ser executado diretamente**, apenas importado pelo notebook.

## 🗂️ Formato do Arquivo `.dat`

O arquivo `.dat` deve seguir uma estrutura textual, contendo:

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

- **Linguagem**: Python 3
- **Bibliotecas**:
  - `matplotlib`: visualização do grafo.
  - `random`: geração de posições aleatórias para visualização.
  - `re`: leitura e extração de dados usando expressões regulares.
  - `itertools`: combinações para cálculo de centralidade.
  - `numpy`: estrutura de apoio
- **Algoritmos e Cálculos**:
  - **Floyd-Warshall**: cálculo da matriz de caminhos mínimos e predecessores.
  - **Centralidade de Intermediação**: com base em contagem dos caminhos mínimos entre pares de nós.
  - **Densidade do Grafo**: calculada com base no número de arestas/arcos e vértices.
  - **Grau mínimo e máximo**: contagem das conexões por nó.
  - **Caminho Médio**: média das distâncias mínimas entre pares de nós.
  - **Diâmetro do Grafo**: maior distância mínima entre quaisquer dois nós.

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

Você pode trocar o arquivo analisado modificando a sexta linha do `main.ipynb`:

```python
caminho_arquivo = "dados/teste.dat"
```

Substitua `"teste.dat"` pelo nome de outro arquivo no mesmo formato. 
OBS: Você deve ter esse arquivo dentro da pasta dados e ele deve seguir a estrutura textual citada acima no tópico *Formato do Arquivo*.

---

## 🧾 Licença

Este projeto é de uso acadêmico e livre para estudo. Contribuições e adaptações são bem-vindas, desde que referenciem o autor.

---

Em caso de dúvidas ou sugestões, abra uma *issue* no repositório!
