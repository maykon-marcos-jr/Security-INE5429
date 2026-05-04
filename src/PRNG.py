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
import math
def monobit(bin_data: str):
    """
    Note that this description is taken from the NIST documentation [1]
    [1] http://csrc.nist.gov/publications/nistpubs/800-22-rev1a/SP800-22rev1a.pdf

    The focus of this test is the proportion of zeros and ones for the entire sequence. The purpose of this test is
    to determine whether the number of ones and zeros in a sequence are approximately the same as would be expected
    for a truly random sequence. This test assesses the closeness of the fraction of ones to 1/2, that is the number
    of ones and zeros ina  sequence should be about the same. All subsequent tests depend on this test.

    :param bin_data: a binary string
    :return: the p-value from the test
    """
    count = 0
    # If the char is 0 minus 1, else add 1
    ones = bin_data.count('1')
    count = ones - (len(bin_data) - ones)
    # Calculate the p value
    sobs = count / math.sqrt(len(bin_data))
    p_val = math.erfc(math.fabs(sobs) / math.sqrt(2))
    return p_val

def LCG(m: int, a: int, c: int, seed: int, nbits: int) -> tuple[int, float]:
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
    p_value = monobit(bits)
    return rn, p_value


def BBS(p: int, q: int, seed: int, nbits: int) -> tuple[int, float]:
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
    p_value = monobit(bits)
    return rn, p_value


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
    rn1, pv1 = LCG(m, a, c, seed, nbits)
    p = 499
    q = 503
    rn2, pv2 = BBS(p, q, seed, nbits)

    print(f"LCG -> {rn1} | {pv1}")
    print(f"BBS -> {rn2} | {pv2}")

if __name__ == "__main__":
    nbits = int(input())
    main(nbits)