# Biblioteca CRUD — Paradigmas Imperativo e Funcional em Python

Sistema simples de cadastro de livros (CRUD) construído em Python com o objetivo
**didático** de demonstrar a coexistência dos paradigmas **imperativo** e
**funcional** dentro do mesmo projeto, mostrando onde cada um se encaixa melhor.

---

## 📁 Estrutura do projeto

```
biblioteca-crud/
├── main.py                # Ponto de entrada — menu interativo (imperativo)
├── imperativo.py          # CRUD com mutação de estado (imperativo)
├── funcional.py           # Consultas e agregações (funcional puro)
├── armazenamento.py       # Persistência em JSON
├── cadastro_em_massa.py   # Script de seeds para popular o sistema com dados de teste
├── livros.json            # Arquivo gerado em tempo de execução
└── README.md              # Este arquivo
```

A separação por arquivo foi proposital: cada módulo carrega claramente a
"intenção" do paradigma que utiliza. Isso facilita a leitura, a manutenção e
deixa explícito **onde o estado muda** (imperativo) e **onde os dados são
apenas consultados** (funcional).

---

## ▶️ Como executar

Basta ter Python 3.8+ instalado. Não há dependências externas.

```bash
python main.py
```

Os dados são persistidos no arquivo `livros.json`, criado automaticamente na
primeira inserção.

### Cadastro em massa (dados de teste)

Para facilitar a validação do sistema sem precisar cadastrar livro por livro
pela tela, existe o script `cadastro_em_massa.py`. Ele carrega uma lista
pré-definida com **30 livros de 17 autores diferentes**, com variedade ampla
de épocas (de 1813 a 1997) e de tamanhos (de 96 a 1225 páginas):

```bash
python cadastro_em_massa.py
```

A lista inclui obras clássicas da literatura brasileira (Machado de Assis,
Jorge Amado, Clarice Lispector, Graciliano Ramos, etc.) e da literatura
mundial (Tolstói, Dostoiévski, Orwell, Tolkien, García Márquez, entre outros).
Vários autores aparecem com mais de uma obra, o que torna úteis tanto os
filtros por autor quanto o cálculo de média de páginas por autor.

Se já houver livros cadastrados, o script pergunta se você deseja
adicionar mesmo assim (modo apêndice). Para começar do zero, apague o
arquivo `livros.json` antes de executar.

---

## 🧠 Como os dois paradigmas trabalham juntos

A divisão de responsabilidades é a seguinte:

| Operação                          | Paradigma     | Arquivo         |
|-----------------------------------|---------------|-----------------|
| Adicionar livro                   | Imperativo    | `imperativo.py` |
| Atualizar livro                   | Imperativo    | `imperativo.py` |
| Remover livro                     | Imperativo    | `imperativo.py` |
| Buscar por ID                     | Imperativo    | `imperativo.py` |
| Filtrar por autor / título / ano  | Funcional     | `funcional.py`  |
| Listar títulos / autores únicos   | Funcional     | `funcional.py`  |
| Total de páginas                  | Funcional     | `funcional.py`  |
| Mais antigo / mais recente        | Funcional     | `funcional.py`  |
| Média de páginas por autor        | Funcional     | `funcional.py`  |
| Loop de menu                      | Imperativo    | `main.py`       |

**A regra que guiou a divisão**: tudo que **muda o estado** do sistema (cria,
atualiza ou remove) ficou no paradigma imperativo, pois envolve naturalmente
mutação. Tudo que apenas **lê e transforma** dados ficou no paradigma funcional,
onde funções puras brilham.

---

## 🔧 Parte 1 — Paradigma Imperativo (`imperativo.py`)

O paradigma imperativo descreve o programa como uma **sequência de comandos
que alteram o estado** da memória. O computador executa passo a passo, o
desenvolvedor controla manualmente o fluxo de execução.

### Características aplicadas no projeto

- **Variáveis mutáveis**: a lista `livros` é compartilhada e modificada
  diretamente. Em `gerar_proximo_id`, usamos `maior_id` e `indice` como
  contadores que mudam a cada iteração.
- **Estruturas de controle (`if`, `for`, `while`)**: a função
  `gerar_proximo_id` usa `while` clássico; `remover_livro` usa `for` com `if`
  para localizar o item; `atualizar_livro` usa `while` com vários `if`s
  encadeados para decidir quais campos serão alterados.
- **Manipulação direta de estado**: `livros.append(...)` e `livros.pop(...)`
  modificam a lista original *in-place*. Quem chamou a função enxerga
  imediatamente a alteração.
- **Código sequencial e estruturado**: o fluxo é linear — primeiro busca,
  depois decide, depois muda.

### Exemplo (trecho de `remover_livro`)

```python
for indice in range(len(livros)):
    if livros[indice]["id"] == id_livro:
        livros.pop(indice)   # mutação direta da lista
        return True
return False
```

Repare como o código descreve **passo a passo**: percorra, compare, mute a
estrutura, retorne o resultado.

---

## 🧬 Parte 2 — Paradigma Funcional (`funcional.py`)

O paradigma funcional trata a computação como **avaliação de funções
matemáticas**: a partir das mesmas entradas, sempre se obtém a mesma saída,
e nada do mundo externo é alterado.

### Características aplicadas no projeto

- **Funções puras**: nenhuma função em `funcional.py` modifica a lista
  recebida nem qualquer outra variável externa. O retorno depende
  exclusivamente dos parâmetros.
- **Imutabilidade**: todas as funções de filtragem retornam uma **nova lista**
  via `list(filter(...))` ou `list(map(...))`. A lista original permanece
  intacta.
- **Funções de ordem superior**: `map`, `filter` e `reduce` recebem outras
  funções (lambdas) como argumento. Isso elimina a necessidade de loops
  manuais.
- **Sem efeitos colaterais**: nenhuma chamada faz `print`, escreve em arquivo
  ou modifica estado.
- **Separação clara entre dados e operações**: os livros são apenas
  dicionários; as funções são externas e não pertencem a nenhuma classe.

### Exemplos

**Filtragem com `filter`**:
```python
def filtrar_por_autor(livros, autor):
    autor_lower = autor.lower()
    return list(filter(
        lambda livro: autor_lower in livro["autor"].lower(),
        livros
    ))
```

**Transformação com `map`**:
```python
def listar_titulos(livros):
    return list(map(lambda livro: livro["titulo"], livros))
```

**Agregação com `reduce`**:
```python
def total_de_paginas(livros):
    return reduce(lambda acc, livro: acc + livro["paginas"], livros, 0)
```

**Composição (filter + map + reduce)** em `media_paginas_por_autor`: primeiro
filtramos os livros do autor, depois mapeamos para extrair só as páginas, e
finalmente reduzimos somando tudo. Cada etapa é uma transformação pura.

---

## ⚖️ Vantagens e desvantagens de cada paradigma (visão teórica)

### Paradigma Imperativo

**Vantagens**
- **Familiaridade**: é como a maioria das pessoas aprende a programar; o
  raciocínio "faça isso, depois aquilo" é natural.
- **Performance e controle fino**: como você controla cada passo, é mais fácil
  otimizar laços, parar com `break`, evitar criar listas intermediárias.
- **Eficiência de memória**: ao mutar a estrutura existente, evitamos alocar
  novas cópias — útil para listas muito grandes.
- **Depuração com `print`/debugger é direta**: o estado em qualquer ponto é
  observável passo a passo.

**Desvantagens**
- **Bugs de estado compartilhado**: como várias partes do código podem alterar
  a mesma lista, é fácil introduzir efeitos colaterais inesperados.
- **Difícil de paralelizar**: mutação concorrente exige locks, semáforos e
  outros mecanismos de sincronização.
- **Mais verboso**: laços manuais com flags, contadores e índices ocupam mais
  linhas do que uma única chamada a `filter` ou `map`.
- **Menos testável**: funções que mutam estado externo precisam de setup
  cuidadoso para serem testadas isoladamente.
- **Acoplamento implícito**: ao olhar a assinatura `remover_livro(livros, id)`,
  só lendo o corpo da função é que descobrimos que `livros` será mutado.

### Paradigma Funcional

**Vantagens**
- **Previsibilidade**: a mesma entrada sempre produz a mesma saída. Isso
  facilita raciocinar sobre o programa.
- **Testabilidade**: funções puras são triviais de testar — basta passar
  entradas e comparar saídas, sem mocks ou setup.
- **Composição**: funções pequenas se combinam para formar pipelines elegantes
  (ex.: `filter` → `map` → `reduce` em `media_paginas_por_autor`).
- **Paralelização segura**: como não há mutação compartilhada, pedaços do
  trabalho podem rodar em threads/processos sem risco de corrida.
- **Código mais declarativo**: você descreve **o que** quer, não **como**
  obter. `list(filter(...))` é mais expressivo que um loop com `if` e
  `append`.

**Desvantagens**
- **Custo de memória**: criar listas novas a cada operação consome mais RAM do
  que mutar uma existente.
- **Pode ser mais lento** em casos simples, devido às alocações e ao overhead
  de chamadas de função (especialmente em Python, que não é otimizado para
  recursão e funções pequenas como linguagens funcionais puras).
- **Curva de aprendizado**: `reduce`, lambdas, composição e imutabilidade são
  conceitos que assustam quem vem de uma base imperativa.
- **Difícil para I/O**: arquivos, banco de dados, rede, prints — tudo isso é
  efeito colateral. Em algum momento o programa precisa "sujar as mãos", e
  o paradigma funcional puro precisa de abstrações (como mônadas) para
  lidar com isso.
- **Em Python**, o suporte funcional é parcial: não há otimização de tail
  call, lambdas só aceitam expressões, e `reduce` foi movido para `functools`
  (sinal de que a comunidade prefere alternativas como list comprehensions e
  `sum`/`max`/`min`).

---

## 🎯 Quando usar cada um?

A regra prática que adotamos neste projeto:

- **Use imperativo** para a "casca" do sistema: menu, leitura de input,
  loops principais, operações que naturalmente envolvem mutação (CRUD em
  uma estrutura compartilhada).
- **Use funcional** para o "miolo" das regras de negócio: cálculos,
  filtros, transformações, relatórios. Funções puras tornam a lógica
  fácil de testar e raciocinar.

A maioria dos sistemas reais é **híbrida** — assim como este. Linguagens
modernas (Python, JavaScript, Kotlin, Scala, C#) abraçaram essa mistura
justamente porque cada paradigma resolve melhor um conjunto diferente de
problemas.

---

## 🧪 Exemplo de uso

```
==================================================
       BIBLIOTECA - SISTEMA DE LIVROS
==================================================
--- Operações IMPERATIVAS (mudam estado) ---
1. Adicionar livro
2. Atualizar livro
3. Remover livro
4. Buscar livro por ID
--- Operações FUNCIONAIS (consultas) ---
5. Listar todos os livros
6. Filtrar por autor
...
Escolha uma opção: 1

-- Adicionar Livro --
Título: Dom Casmurro
Autor: Machado de Assis
Ano de publicação: 1899
Número de páginas: 256

✓ Livro adicionado com sucesso! ID: 1
```

---

## 🎓 Conclusões dos autores

Esta seção reúne as reflexões pessoais dos autores do projeto sobre a
experiência de implementar o sistema usando os dois paradigmas em conjunto.
Ao contrário da seção teórica acima, aqui o foco é o que **percebemos na
prática** durante a construção da biblioteca.

### 1. Diferenças percebidas entre os paradigmas

**Resposta:**

No paradigma imperativo, o sistema utiliza uma lista global que é modificada
ao longo da execução. As funções acessam e alteram diretamente o estado do
acervo, o que caracteriza uma abordagem baseada em mudanças de estado.

Já no paradigma funcional, a lista não é alterada diretamente. Cada operação
recebe o acervo como parâmetro e retorna uma nova lista atualizada, mantendo
a original intacta. Além disso, no imperativo são utilizados dicionários
(mutáveis), enquanto no funcional são utilizadas tuplas (imutáveis).

---

### 2. Vantagens e desvantagens observadas na prática

**Resposta:**

**Imperativo:**
No paradigma imperativo, o código é mais simples e direto, facilitando o
entendimento inicial. O uso de estruturas como `for` e `if` torna o fluxo
mais claro e sequencial.
Por outro lado, o uso de estado global pode gerar erros difíceis de
identificar, já que qualquer função pode modificar os dados a qualquer
momento.

**Funcional:**
No paradigma funcional, as funções são puras e não possuem efeitos
colaterais, o que aumenta a segurança e facilita os testes. O uso de
funções como `map`, `filter` e `reduce` permite manipular os dados de
forma mais declarativa e organizada.
Como desvantagem, essa abordagem exige mais atenção, pois sempre é
necessário retornar uma nova lista, o que pode aumentar o consumo de
memória em alguns cenários.

---

### 3. Qual abordagem foi mais fácil / mais difícil e por quê

**Resposta:**

O paradigma imperativo foi mais fácil de implementar, pois segue um modelo
mais comum, baseado na alteração direta de variáveis e execução sequencial.

Já o paradigma funcional exigiu uma adaptação maior, pois não permite
modificar diretamente os dados. Em operações como edição, empréstimo e
devolução, foi necessário utilizar funções como `map` para gerar uma nova
versão do acervo, substituindo apenas os elementos necessários.

---

### 4. Impacto na legibilidade e manutenção de código

**Resposta:**

O código imperativo é mais fácil de entender inicialmente, pois segue uma
lógica mais direta e sequencial. No entanto, a dependência de variáveis
globais pode dificultar a manutenção, já que o estado pode ser alterado em
diferentes partes do sistema.

O código funcional, apesar de mais complexo no início, tende a ser mais
organizado e previsível. Como as funções não alteram o estado externo, fica
mais fácil identificar problemas, testar e manter o sistema ao longo do
tempo.

---

## 📌 Observações finais

- O arquivo `livros.json` é gerado automaticamente; **não há banco de dados**
  envolvido. Caso queira evoluir o projeto para usar SQLite, PostgreSQL ou
  outro SGBD, o ideal é criar um *script* de migração separado e jamais
  executar comandos diretamente no banco — toda alteração estrutural deve
  passar por revisão humana.
- Toda alteração no código deve ser proposta via **Pull Request**, nunca
  commitada diretamente na branch `main`.
