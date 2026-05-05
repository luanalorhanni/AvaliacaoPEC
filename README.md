# AvaliacaoPEC
atividade avaliativa de paradigmas da programação - EECP0005


# AvaliacaoPEC
atividade avaliativa de paradigmas da programação - EECP0005

# AvaliacaoPEC
Atividade avaliativa de Paradigmas da Programação - EECP0005

---

## 📊 Comparações Obrigatórias

### 🔹 Diferenças percebidas entre os paradigmas

No paradigma imperativo, o sistema utiliza uma lista global que é modificada ao longo da execução. As funções acessam e alteram diretamente o estado do acervo, o que caracteriza uma abordagem baseada em mudanças de estado.

Já no paradigma funcional, a lista não é alterada diretamente. Cada operação recebe o acervo como parâmetro e retorna uma nova lista atualizada, mantendo a original intacta. Além disso, no imperativo são utilizados dicionários (mutáveis), enquanto no funcional são utilizadas tuplas (imutáveis).

---

### 🔹 Vantagens e desvantagens de cada abordagem

**Imperativo:**

No paradigma imperativo, o código é mais simples e direto, facilitando o entendimento inicial. O uso de estruturas como `for` e `if` torna o fluxo mais claro e sequencial.  
Por outro lado, o uso de estado global pode gerar erros difíceis de identificar, já que qualquer função pode modificar os dados a qualquer momento.

**Funcional:**

No paradigma funcional, as funções são puras e não possuem efeitos colaterais, o que aumenta a segurança e facilita os testes. O uso de funções como `map`, `filter` e `reduce` permite manipular os dados de forma mais declarativa e organizada.  
Como desvantagem, essa abordagem exige mais atenção, pois sempre é necessário retornar uma nova lista, o que pode aumentar o consumo de memória em alguns cenários.

---

### 🔹 Qual abordagem foi mais fácil/difícil e por quê?

O paradigma imperativo foi mais fácil de implementar, pois segue um modelo mais comum, baseado na alteração direta de variáveis e execução sequencial.

Já o paradigma funcional exigiu uma adaptação maior, pois não permite modificar diretamente os dados. Em operações como edição, empréstimo e devolução, foi necessário utilizar funções como `map` para gerar uma nova versão do acervo, substituindo apenas os elementos necessários.

---

### 🔹 Impacto na legibilidade e manutenção do código

O código imperativo é mais fácil de entender inicialmente, pois segue uma lógica mais direta e sequencial. No entanto, a dependência de variáveis globais pode dificultar a manutenção, já que o estado pode ser alterado em diferentes partes do sistema.

O código funcional, apesar de mais complexo no início, tende a ser mais organizado e previsível. Como as funções não alteram o estado externo, fica mais fácil identificar problemas, testar e manter o sistema ao longo do tempo.

---

## ⚙️ Instruções de uso do programa funcional

O programa funcional funciona sem alterar diretamente os dados. Todas as operações retornam uma nova versão do acervo.

### ▶️ Como utilizar:

1. Execute o arquivo principal:
   ```bash
   python main.py
