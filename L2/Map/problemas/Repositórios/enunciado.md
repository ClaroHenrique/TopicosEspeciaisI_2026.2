# Repositórios

Fonte: OBI [https://olimpiada.ic.unicamp.br/pratique/p2/2007/f1/repos/](https://olimpiada.ic.unicamp.br/pratique/p2/2007/f1/repos/)


## Descrição

Uma das boas práticas ao administrar um conjunto de computadores é manter os aplicativos sempre atualizados. Entretanto, em uma grande corporação com milhares de aplicativos instalados, a simples verificação do que precisa ser atualizado pode tornar-se uma tarefa bem complicada. Para facilitar isso, alguns fabricantes armazenam todos os aplicativos existentes em grandes bases de dados chamadas repositórios e um programa é responsável por verificar esse repositório e atualizar as versões dos aplicativos.

M.V.Lzr, um administrador de sistemas e rapper nas horas vagas, trabalha em uma empresa que, infelizmente, não utiliza um sistema com repositórios. Para facilitar sua vida, ele decidiu que era a hora de ter o seu próprio sistema e pediu a sua ajuda.

Periodicamente ele varre a Internet em busca das páginas que possam conter os aplicativos e constrói uma lista com as versões dos aplicativos que deseja instalar disponíveis em cada página. Um programa deve verificar então qual a versão de cada programa instalado nos computadores (todos eles possuem os mesmos aplicativos instalados e nas mesmas versões) e instalar todos aqueles que ainda não foram instalados ou cuja versão instalada seja anterior à versão mais recente. Como ele não sabe programar direito, ele pediu sua ajuda.

## Tarefa

Dada uma lista de aplicativos instalados nos computadores da empresa, com suas respectivas versões, e uma lista de aplicativos disponíveis na internet que devem ser instalados, determinar quais devem ser instalados e em quais versões.

## Entrada

A entrada contém um único conjunto de testes, que deve ser lido do dispositivo de entrada padrão (normalmente o teclado).

A primeira linha da entrada contém dois inteiros $C$ ($1 \le C \le 10.000$) e $N$ ($1 \le N \le 1.000$) que representam o número total de aplicativos e versões disponíveis na internet e o número total de programas instalados na empresa, respectivamente.

As $C$ linhas seguintes possuem dois inteiros cada, $P_c$ ($1 \le P_c \le 1.000.000.000$) e $V_c$ ($1 \le V_c \le 1.000.000.000$), representando o número do programa e o número da versão instalada nos computadores. Todo aplicativo está instalado uma única vez em cada máquina e em uma única versão.

Em seguida, as $N$ linhas seguintes possuem dois inteiros cada, $P_n$ ($1 \le P_n \le 1.000.000.000$) e $V_n$ ($1 \le V_n \le 1.000.000.000$), representando o número do programa e o número da versão disponível na internet. Um dado programa pode estar disponível em mais de uma versão na internet.

## Saída

Seu programa deve imprimir, na saída padrão, diversas linhas, cada uma contendo dois inteiros, $P_s$ e $V_s$, com o número do programa e a versão que deve ser instalada (aviso: ordene a saída pelo valor de $P_s$). Em todo caso de teste existe pelo menos um programa que deve ser instalado.

---

## Exemplos

### Exemplo 1

**Entrada**
```text
1 1
5215 1
5215 3
```

**Saída**
```text
5215 3
```

---

### Exemplo 2

**Entrada**
```text
3 2
1640 1
2540 4
1870 3
2540 1
1640 4
```

**Saída**
```text
1640 4
```

---

### Exemplo 3

**Entrada**
```text
2 5
2000 4
2001 5
2000 1
2001 4
2001 6
2000 2
2000 3
```

**Saída**
```text
2001 6
```