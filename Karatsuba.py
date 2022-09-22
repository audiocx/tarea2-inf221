import sys

# Añade "cant" ceros a la izquierda del número "num"


def añadir_ceros_izq(num, cant):
    res = num
    for i in range(cant):
        res = "0" + res
    return res


# Añade "cant" ceros a la derecha del número "num"
def añadir_ceros_der(num, cant):
    res = num
    for i in range(cant):
        res = res + "0"
    return res


# Multiplica mediante el algoritmo de Karatsuba el número "x" con el número "y"
def Karatsuba(x, y):

    # Se dejan ambos números con los mismos dígitos
    if len(x) < len(y):
        x = añadir_ceros_izq(x, len(y) - len(x))
    elif len(y) < len(x):
        y = añadir_ceros_izq(y, len(x) - len(y))

    # Se calcula el tamaño de los números, y la mitad de este
    n = len(x)
    if (n <= 1):
        resultado = bin(int(x, 2) * int(y, 2))[2:]
        return resultado
    else:
        n_mitad = n // 2
        entra = 0
        if (n % 2 != 0):
            entra = 1
            n_mitad += 1

        # Se separan los números por la mitad
        xS = x[:n_mitad]
        xI = x[n_mitad:]
        yS = y[:n_mitad]
        yI = y[n_mitad:]

        x3 = bin(int(xS, 2) + int(xI, 2))[2:]
        y3 = bin(int(yS, 2) + int(yI, 2))[2:]

        # Se aplica Karatsuba a las diversas combinaciones de números
        p1 = Karatsuba(xS, yS)
        p2 = Karatsuba(xI, yI)
        p3 = Karatsuba(x3, y3)

        if entra == 1:
            n_mitad -= 1

        # Se obtienen los dígitos para aplicar la multipicación de gauss
        r1 = añadir_ceros_der(p1, n_mitad*2)
        r2 = añadir_ceros_der(
            bin(int(p3, 2) - int(p1, 2) - int(p2, 2)), n_mitad)
        r3 = p2

        return bin((int(r1, 2) + int(r2, 2) + int(r3, 2)))[2:]

# Funcion principal que ejecuta el script de entrada y salida de datos


def main():
    data = sys.stdin.readlines()

    for i in data:
        _, a, b = i.strip().split(" ")
        print(Karatsuba(a, b))


if __name__ == "__main__":
    main()
