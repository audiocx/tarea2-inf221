import sys

# Añade n ceros a la derecha de a (equivalente a shift)


def fillRight(a, n):
    res = a
    for _ in range(n):
        res += "0"
    return res

# Añade n ceros a la izquierda de a


def fillLeft(a, n):
    res = a
    for _ in range(n):
        res = "0" + res
    return res

# Logica para la suma de dos bits, con su respectivo carry


def sumaBit(a, b, c):
    if a == "0":
        if b == "0":
            if c == "0":
                return ("0", "0")
            elif c == "1":
                return ("1", "0")
        elif b == "1":
            if c == "0":
                return ("1", "0")
            elif c == "1":
                return ("0", "1")
    elif a == "1":
        if b == "0":
            if c == "0":
                return ("1", "0")
            elif c == "1":
                return ("0", "1")
        elif b == "1":
            if c == "0":
                return ("0", "1")
            elif c == "1":
                return ("1", "1")

# Sumador de 2 numeros binarios


def sumaBin(a, b):
    tam = len(a)
    res = ""
    carry = "0"
    for i in range(tam - 1, -1, -1):
        bit, carry = sumaBit(a[i], b[i], carry)
        res = bit + res
    if carry == "1":
        res = "1" + res
    return res

# Multiplicador fuerza bruta para 2 numeros binarios de n bits


def multiplicar(n, a, b):
    res = fillRight("", 2*n)
    for i in range(n):
        if a[n - i - 1] == "1":
            temp = fillRight(b, i)
            temp = fillLeft(temp, n - i)
            res = sumaBin(res, temp)
    pos = 0
    for c in res:
        if c == "0":
            pos += 1
        else:
            break
    if pos == 2*n:
        return "0"
    else:
        return res[pos:]

# Funcion principal que ejecuta el script de entrada y salida de datos


def main():
    data = sys.stdin.readlines()

    for i in data:
        N, a, b = i.strip().split(" ")
        print(multiplicar(int(N), a, b))


if __name__ == "__main__":
    main()
