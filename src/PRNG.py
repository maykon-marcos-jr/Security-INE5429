"""Descrição
implementa duas abordagens computacionais para gerar números pseudo-aleatórios e compara seus resultados.

Implemente o LCG e o algoritmo de BBS para gerar um número pseudo-aleatório grande. O algoritmo deve receber um número que define o tamanho em bits do valor a ser gerado.
"""

"""Parâmetros Fixos:
Parâmetros do LCG:
    m = 2147483648
    a = 1103515245
    c = 12345
    Semente Inicial (X0) = 12345

Parâmetros do BBS:
    p = 499
    q = 503
    Semente de Entrada (s) = 12345
"""

"""Execução
Para que ambos os algoritmos gerem um número com a exata quantidade de bits especificada na entrada, siga esta regra estritamente para ambos os geradores (1º LCG e depois BBS):

    Em cada iteração, calcule o próximo X[n+1] utilizando a fórmula do respectivo algoritmo.

    Extraia o bit menos significativo do estado atual calculando: X[n+1] mod 2.

    Concatene os bits gerados da esquerda para a direita. O bit extraído na 1ª iteração será o mais à esquerda (MSB), e o bit da última iteração será o mais à direita (LSB).

    Após realizar N iterações, converta a string binária formada de volta para um número decimal inteiro e imprima-o

cada execução deve apresentar o resultado do LCG e do BBS nessa ordem.

"""


def LCG(m: int, a: int, c: int, seed: int, nbits: int) -> int:
    """LCG:
    Linear Congruential Generator:
    - O LCG é um algoritmo clássico, extremamente rápido e simples, porém não é considerado seguro para fins criptográficos.
    - O próximo número da sequência é gerado através da relação linear:

    $$
    X[n+1] = (a * X[n] + c) mod m
    $$

    Para a utilização do LCG, devem ser definidos os parâmetros m (módulo), a (multiplicador), c (incremento) e uma semente inicial X0.
    """
    X = seed

    bits = ""

    for n in range(nbits):
        X = (a * X + c) % m
        lsb = X % 2
        bits += str(lsb)

    rn = int(bits, 2)
    return rn


def BBS(p: int, q: int, seed: int, nbits: int) -> int:
    """BBS:
    Blum Blum Shub:
    - O Algoritmo BBS se baseia em propriedades da teoria dos números e na dificuldade computacional de fatorar grandes números compostos.
    - A principal ideia é utilizar a seguinte equação de recorrência:
        $$
        X[n+1] = X[n]^2 (mod M)
        $$

    - onde M = p * q (sendo p e q dois números primos grandes congruentes a 3 módulo 4).

    O gerador é executado iterativamente e, a cada passo, extrai-se apenas um bit (como a paridade de X[n+1] ou seu bit menos significativo) para compor, bit a bit, o número pseudo-aleatório final.
    """
    X = seed
    m = p*q

    bits = ""

    for n in range(nbits):
        X = (X*X) % m
        lsb = X % 2
        bits += str(lsb)

    rn = int(bits, 2)
    return rn


def main(nbits):
    """# Entrada e Saída

    A entrada é composta por um único número inteiro representando a quantidade de bits desejada para o número gerado.

    A saída deve possuir 2 linhas:

    A primeira é o número pseudo-aleatório gerado pelo LCG no tamanho solicitado;

    A segunda é o número pseudo-aleatório gerado pelo BBS no tamanho solicitado;

    LCG -> ${resultado}
    BBS -> ${resultado}

    ---

    # Exemplo de Entrada e Saída:

    Entrada:

    40

    Saída:

    LCG -> 366503875925

    BBS -> 500307395413

    ---

    Entrada:

    8

    Saída:

    LCG -> 85

    BBS -> 116
    """

    seed = 12345

    m = 2147483648
    a = 1103515245
    c = 12345
    rn1 = LCG(m, a, c, seed, nbits)
    p = 499
    q = 503
    rn2 = BBS(p, q, seed, nbits)

    print(f"LCG -> {rn1}")
    print(f"BBS -> {rn2}")

if __name__ == "__main__":
    nbits = int(input())
    main(nbits)