def divisors(num):
            assert num >= 0, "debes ingresar un numero positivo"
            divisors = [i for i in range (1, num +1) if num % i == 0] 
            return divisors

def main ():
    try:
        num = int(input("ingresa un numero: "))
        print(divisors(num))
        print("termino del programa, !gracias¡")
    except ValueError:
        print("debes ingresar un numero")

if __name__ == '__main__':
    main()