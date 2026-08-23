# Fila do banco

Você foi contratado para ser o programador do novo banco físico BL (Banco dos Lisos). Ao entrar nesse banco, o cliente puxa um papel com um código indicando sua senha de atendimento. Essa senha é eventualmente exibida em uma tela quando for sua vez de ser atendido.

Seu chefe te passou as regras da fila:

1. Se há algum cliente que requer atendimento preferencial (idoso, gestante, etc), esse deve ser atendido antes de qualquer outro cliente.
2. Seja entre o cliente preferencial ou o cliente não-preferencial, aquele que está esperando a mais tempo deve ser atendido primeiro.
3. A senha possui o seguinte formato (onde XXXX é uma sequencia de 4 dígitos):
   1. Atendimento preferencial: "PRE-XXXX"
   2. Atendimento normal: "NOR-XXXX"

Sua tarefa agora é, dado o histórico de senhas geradas no sistema, definir qual é a próxima pessoa que deve ser atendida quando o caixa estiver livre.


## Entrada

A primeira linha da entrada contém um inteiro $N$, indicando a quantidade de operações que você deve processar. Cada uma das próximas $N$ linhas contém uma operação, que pode ser de dois tipos:

1. `CHEGOU <senha>`: indica que um cliente chegou ao banco e puxou a senha `<senha>`.
2. `ATENDIDO`: indica que o caixa está livre e deve atender o próximo cliente.

## Saída

Para cada operação do tipo `ATENDIDO`, imprima a senha do cliente que deve ser atendido. Caso não haja nenhum cliente na fila, imprima `VAZIO`.

## Restrições

- $1 \leq N \leq 100$

## Exemplos

### Exemplo 1

**Entrada**
```text
6
CHEGOU NOR-0001
CHEGOU NOR-0002
ATENDIDO
CHEGOU PRE-0001
ATENDIDO
ATENDIDO
```

**Saída**
```text
NOR-0001
PRE-0001
NOR-0002
```

---

### Exemplo 2

**Entrada**
```text
11
CHEGOU PRE-3321
CHEGOU PRE-1542
CHEGOU PRE-6111
ATENDIDO
CHEGOU NOR-1001
ATENDIDO
ATENDIDO
ATENDIDO
CHEGOU PRE-6111
ATENDIDO
ATENDIDO
```

**Saída**
```text
PRE-3321
PRE-1542
PRE-6111
NOR-1001
PRE-6111
VAZIO
```