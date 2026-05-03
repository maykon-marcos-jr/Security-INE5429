"""Exercício:

Implemente teste de primalidade de Fermat e o algoritmo de Miller-Rabin para testar se um número n é provavelmente primo ou composto.

O algoritmo deve receber dois números, um inteiro para a base "a" e outro inteiro para ser testado "p".

# Passos:
1. Implemente o teste de primalidade de Fermat e o algoritmo de Miller-Rabin.
2. Realize o teste com os valores de entrada, cada teste deve apresentar o seu resultado de Fermat e Miller-Rabin nessa ordem.
3. Para cada teste a saída deve ser provavelmente primo ou composto.
4. Deve ser impressa uma terceira linha que deve ser o resultado composto dos dois testes.

# Observação:

Como o pequeno teorema de Fermat e o algoritmo de Miller-Rabin são probabilísticos, pode haver uma pequena chance de que o número seja classificado incorretamente como provavelmente primo.

Aumentar o número de execuções com diferentes valores de "a" diminui essa probabilidade, porém, para a correção automatica você deve implementar o teste apenas com a base "a" informada.
"""

def euclides_extendido(a, b):
    x0 = 1
    y0 = 0
    x1 = 0
    y1 = 1

    while b > 0:
        q = a // b
        r = a % b

        a = b
        b = r

        tmp = x1
        x1 = x0  - (q * x1)
        x0 = x1

        tmp = y1
        y1 = y0  - (q * y1)
        y0 = y1

    # mdc, x, y
    return a, x0, y0

def euclides(a: int, b: int) -> int:
    """ # MDC
    O Algoritmo de Euclides é utilizado para verificar se o número "a" escolhido é relativamente primo com "p".

    Esse algoritmo funciona através de uma sequência de divisões, onde o resto da divisão anterior é usado como o novo divisor até que o resto seja zero.
    - O último divisor não nulo é o MDC.
    """
    while b > 0:
        a, b = b, a % b

    return a

def fermat(a: int, p: int) -> bool:
    """ # Pequeno Teorema de Fermat:

    $$
    a^{p - 1} ≡ 1 (mod p)
    $$

    Para a utilização do Pequeno Teorema de Fermat "a" e "p" devem ser relativamente primos, será usado o algoritmo de Euclides para garantir que o MDC entre a e p seja 1.

    # Primalidade de Fermat:
    ---
    O Teste de Primalidade de Fermat utiliza esse teorema de forma reversa para verificar se um número é provavelmente primo.

    Para testar um número "p", escolhemos valores aleatórios para a base "a" e aplicamos a fórmula:
    - Se calcularmos $a^{p-1} (mod p)$ e o resultado for diferente de 1, então "p" com certeza é um número composto.

    Se o resultado for igual a 1, "p" é provavelmente primo, chamado de pseudo-primo na base "a".

    Quanto mais bases "a" aleatórias testarmos e obtivermos 1, maior a confiança de que o número é primo.
    """
    if euclides(a, p) == 1:
        return (a**(p-1) % p) == 1
    return False

def miller_rabin(a: int, n: int) -> bool:
    """ # Miller-Rabin:

    O Algoritmo de Miller-Rabin se baseia em propriedades da aritmética modular e na decomposição de números compostos em fatores.

    A principal ideia é que, dado um número ímpar n ele pode ser representado como:

    $n-1 = 2^k * m$

    onde m é um número ímpar e k é o número de vezes que 2 divide n-1.

    O teste é feito para um número base "a" escolhido aleatoriamente, onde o valor a^m mod n e as repetições sucessivas $a^{(2^r)*m} mod n$ são verificadas para determinar se n é provavelmente primo ou composto.
    """
    m = n-1
    k = 0
    # while it can be divided by 2
    while m % 2 == 0:
        m = m >> 1
        k += 1

    x = (a**m) % n
    if (x == 1) or (x == n-1):
        return True

    for i in range(k):
        x = m*(2**i)
        if (a**x) % n == n-1:
            return True
    return False

def main(a: int, n: int):
    """ # Requisitos de Entrada e Saída:

    A entrada é composta por um número inteiro "a" e outro número inteiro "n" separados por " " (espaço em branco).

    A saída deve possuir 3 linhas:
    - A primeira é o resultado do pequeno teorema de Fermat para n calculado com o valor de a;
    - A segunda é o resultado do algoritmo de Miller-Rabin para n calculada com o valor de a;
    - A terceira é a conclusão baseada nos dois resultados anteriores;

    ```
    Fermat ${n} -> ${resultado}
    Miller-Rabin ${n} -> ${resultado}
    Resultado final: ${n} é (provavelmente primo ou composto)
    ```

    # Exemplo de Entrada e Saída:

    Entrada:

    ```
    2 7
    ```

    Saída:
    ```
    Fermat 7 -> Provavelmente primo
    Miller-Rabin 7 -> Provavelmente primo
    Resultado final: 7 é provavelmente primo
    ```

    ---

    Entrada:
    ```
    2 561
    ```

    Saída:
    ```
    Fermat 561 -> Provavelmente primo
    Miller-Rabin 561 -> Composto
    Resultado final: 561 é composto
    ```
    """

    r1 = fermat(a, n)
    r2 = miller_rabin(a, n)
    res1 = "Provavelmente primo" if r1 else "Composto"
    res2 = "Provavelmente primo" if r2 else "Composto"
    resF = "provavelmente primo" if (r1 and r2) else "composto"
    print(f"Fermat {n} -> {res1}")
    print(f"Miller-Rabin {n} -> {res2}")
    print(f"Resultado final: {n} é {resF}")

if __name__ == "__main__":
    ent = input().split()
    a, n = [int(i) for i in ent]
    main(a,n)