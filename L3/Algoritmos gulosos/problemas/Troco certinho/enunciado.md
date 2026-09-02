# Troco certinho

Seu Zé é dono da budega mais famosa de seu bairro. Ele vende de tudo, mas seus produtos mais conhecidos são seus doces (bombom, chiclete, pastilha, pirulito, etc).

Como ele não pode dar o troco em bala ao vender balas, ele tenta sempre manter suas moedas de 5, 10, 25, 50 e 1 real organizadas.

Sua tarefa é ajuda-lo a, dado um valor de um produto, o valor que o cliente pagou e a quantidade de moedas de cada tipo, calcular o troco exato em moedas que ele deve devolver ao cliente, ou informar que é impossível retornar esse troco exato. Caso haja mais de uma forma de devolver o troco, Seu Zé prefere devolver o troco com a menor quantidade de moedas possível.

---

## Entrada

A primeira linha da entrada contém um inteiro $V$ ($1 \le V \le 10^{9}$), indicando o valor que o cliente pagou em centavos.

A segunda linha da entrada contém um inteiro $P$ ($1 \le P \le V$), indicando o valor da compra em centavos.

A terceira linha da entrada contém $5$ inteiros: $f_{5}, f_{10}, f_{25}, f_{50}, f_{100}$ ($0 \le f_i \le 10^{9}$), indicando, respectivamente, a quantidade de moedas de $5$, $10$, $25$, $50$, $100$ centavos que Seu Zé possui.

---

## Saída

Caso seja possível devolver o troco exato, imprima uma linha com cinco inteiros, indicando a quantidade de moedas de $5$, $10$, $25$, $50$ e $100$ centavos que Seu Zé deve devolver ao cliente.

Caso contrário, imprima "impossivel".

---

## Exemplos

### Exemplo 1

**Entrada:**
```text
150
100
8 4 0 0 3
```

**Saída:**
```text
2 4 0 0 0
```

---

### Exemplo 2

**Entrada:**
```text
100
100
1 1 2 1 3
```

**Saída:**
```text
0 0 0 0 0
```

---
