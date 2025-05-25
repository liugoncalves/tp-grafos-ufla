  # Analisador de Grafos - Trabalho Prático UFLA (GCC218)

  Este projeto foi desenvolvido como parte do **Trabalho Prático Final da disciplina GCC218 - Algoritmos em Grafos**, ministrada na Universidade Federal de Lavras (UFLA).

  ## 🧠 Entendendo o Projeto

  Este projeto é um **analisador de grafos** feito em Python. Mas o que é um grafo? Imagine um **mapa** que mostra vários pontos (como cidades) e as conexões entre eles (como estradas). Esse mapa é um jeito de representar redes de conexões entre diferentes elementos.

  O programa lê arquivos `.dat` que trazem essas informações — quais são os pontos, como eles estão ligados, e quais conexões são importantes para serem visitadas obrigatoriamente.

  Com esses dados, o programa calcula várias **estatísticas** para ajudar a entender melhor como essa rede funciona e quais pontos são mais importantes.

  Além disso, o projeto também ajuda a **planejar rotas eficientes** para cumprir todas as tarefas que precisam ser feitas no mapa, como visitar lugares específicos ou percorrer ruas que são obrigatórias.

  Para isso, ele usa um método chamado **Path Scanning**. Funciona assim: o programa monta uma rota, sempre escolhendo o próximo lugar mais próximo que ainda falta visitar e que cabe na capacidade do veículo (como um caminhão). Quando o veículo atinge seu limite, ele volta ao ponto inicial, e uma nova rota começa com outro veículo. Isso continua até que todas as tarefas sejam feitas.

  O objetivo é garantir que todas as ruas ou pontos obrigatórios sejam visitados gastando o menor tempo e distância possível, sem sobrecarregar os veículos.

  ### 🤔 Para quem não conhece grafos, pense assim:

  Imagine um mapa com cidades (que chamamos de **vértices**) e estradas que ligam essas cidades (que chamamos de **arestas**). Algumas estradas são obrigatórias, como ruas que precisam ser percorridas por um caminhão de coleta.

  Nosso programa ajuda a responder perguntas como:

  - **Qual cidade está mais frequentemente "no meio do caminho" entre outras?**  
    Isso mostra quais pontos são estratégicos na rede, um conceito chamado **intermediação**.

  - **Qual a distância média entre dois pontos qualquer no mapa?**  
    Isso ajuda a entender o "tamanho médio" da rede, chamado de **caminho médio**.

  - **Qual é a maior distância mínima entre dois pontos?**  
    Essa medida é o **diâmetro** do grafo, ou seja, a maior distância que ainda é o menor caminho possível entre dois pontos.

  Essas informações são muito úteis para áreas como logística, transporte, redes de computadores, redes sociais, entre outras.

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
  - **Utiliza o algoritmo Path Scanning** para construir rotas, selecionando sempre o próximo serviço mais próximo que o veículo ainda consegue atender.

  ---

  ## 💡 Qual problema o projeto resolve?

  Este analisador foi desenvolvido para resolver problemas reais de otimização de rotas, onde é necessário percorrer ruas ou visitar pontos obrigatórios com o menor custo possível. Esse tipo de problema é comum em atividades como:

  - Coleta de lixo;
  - Entrega de correspondências;
  - Inspeções em redes de energia ou rodovias.

  Além de calcular diversas estatísticas que ajudam a entender melhor a estrutura da rede, o sistema também gera um plano de rotas eficiente para atender a todos os serviços obrigatórios do grafo. Esse plano considera a capacidade máxima dos veículos e busca minimizar o custo total das viagens, levando em conta tanto o trajeto percorrido quanto os serviços realizados.

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

  ```bash
  pip install -r requirements.txt
  ```

  4. **Certifique-se de que o arquivo `.dat` que deseja analisar está na pasta `dados/`.**

  5. **Execute o notebook principal via terminal:**

  ```bash
  jupyter notebook main.ipynb
  ```

  Durante a execução, será solicitado que você digite o nome do arquivo de saída para as rotas geradas.


  ---

### 📌 Observação importante

  O arquivo `main.ipynb` é o **arquivo principal** para executar o projeto.  
  Ele é responsável por:

  - Carregar os dados do grafo logístico;
  - Realizar os cálculos e análises necessárias;
  - Exibir as estatísticas do grafo;
  - Mostrar a visualização gráfica da estrutura do problema;
  - Calcular as melhores rotas e salvar os resultados.

  Portanto, **execute apenas o `main.ipynb` para rodar o projeto completo**.

  ## 🗂️ Formato do Arquivo `.dat`

  O arquivo `.dat` deve seguir uma estrutura textual, contendo:

  - **EDGE**: define arestas — conexões bidirecionais entre vértices.
  - **ARC**: define arcos — conexões direcionadas entre vértices.
  - **ReN.**: nós (vértices) obrigatórios que devem ser atendidos.
  - **ReE.**: arestas obrigatórias — conexões obrigatórias bidirecionais.
  - **ReA.**: arcos obrigatórios — conexões obrigatórias direcionadas.

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
    - **Path Scanning:** para geração das rotas otimizadas


  ## 🚚 Geração de Rotas e Solução do Problema

  Além de calcular estatísticas sobre o grafo, este projeto também resolve um problema prático: **gerar rotas otimizadas que atendem a todos os serviços obrigatórios da rede**, como ruas que precisam ser percorridas, pontos que precisam ser visitados, etc.

  ### 💡 O que é isso na prática?

  Imagine que você está planejando a rota de caminhões de coleta de lixo, ou de entrega de correspondências. Nem todas as ruas precisam ser percorridas, apenas algumas específicas. Além disso, os caminhões têm um limite de carga. Nosso programa monta automaticamente essas rotas, garantindo que:

  - Todos os pontos e ruas obrigatórias sejam atendidos;
  - Nenhum caminhão ultrapasse sua capacidade máxima;
  - O caminho seguido entre os pontos seja sempre o menor possível.

  ---

 ## 🔧 Como funciona o algoritmo?

  O algoritmo usado é chamado **Path Scanning** e funciona assim, de um jeito simples para entender:

  1. O caminhão começa no depósito, que é sempre o **ponto número 1**.
  2. Entre todos os serviços que ainda precisam ser feitos, ele procura aquele que:
    - Está mais perto do lugar onde o caminhão está agora;
    - E que o caminhão ainda pode atender, ou seja, que cabe na capacidade que ainda sobra.
  3. O caminhão vai até esse serviço, realiza a tarefa, e atualiza o quanto de carga (ou demanda) ele já usou.
  4. Quando não der para atender mais nenhum serviço sem passar do limite de carga, a rota termina:
    - O caminhão volta para o depósito;
    - E outro caminhão começa uma nova rota para atender os serviços restantes.
  5. Isso se repete até que todos os serviços obrigatórios tenham sido feitos.

  **Importante:**  
  O caminho que o caminhão usa para ir de um ponto a outro é sempre o **mais curto possível**, e esses caminhos já são calculados antes com um algoritmo chamado **Floyd-Warshall** — que ajuda a encontrar as distâncias menores entre todos os pontos do mapa.

---


## 📄 Arquivo de saída gerado

  Depois de rodar o programa, ele cria um arquivo texto que mostra:

  - ✅ O custo total somando todas as rotas feitas;  
  - 🚚 Quantas rotas foram necessárias;  
  - ⏱️ Quanto tempo o programa levou para rodar todo o processo;  
  - 🚗 Quanto tempo foi usado só para criar as rotas;  
  - 🔍 A descrição detalhada de cada rota.

  ### 📝 Como aparece cada rota no arquivo?

  Cada linha com uma rota mostra, nessa ordem:

  depósito (sempre 0)
  dia da roteirização (sempre 1)
  número da rota (começa em 1)
  demanda total da rota (quantidade total que o veículo precisa atender)
  custo total da rota (distância ou tempo gasto)
  total de visitas feitas (inclui voltar ao depósito e serviços)
  (X i,j,k) ...

  - `(D i,j,k)` significa deslocamento do ponto i para o ponto j, com custo k.  
  - `(S i,j,k)` significa que o serviço i foi feito entre os pontos j e k.

  Exemplos:  
  - `(D 0,1,1)` indica que o veículo saiu do depósito (ponto 0) até o ponto 1.  
  - `(S 2,3,3)` indica que o serviço 2 foi realizado no ponto 3 (serviço em nó único).  
  - `(S 14,7,8)` indica que o serviço 14 foi realizado na rua entre os pontos 7 e 8.

  O arquivo só mostra as visitas aos serviços (não mostra deslocamentos sem serviço). Assim, é possível entender o caminho que cada veículo fez, quais serviços realizou e o custo de cada trecho da rota.

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

  ## 🧾 Licença

  Este projeto é de uso acadêmico e livre para estudo. Contribuições e adaptações são bem-vindas, desde que referenciem o autor.

  ---


  ## 👤 Autores

  - Leonardo Gonçalves
  - Matheus Coelho

  ## 📁 Repositório

  Acesse o projeto completo em: [https://github.com/liugoncalves/tp-grafos-ufla](https://github.com/liugoncalves/tp-grafos-ufla)

