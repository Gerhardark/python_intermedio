def divisors(num):
    divisors = [i for i in range (1, num +1) if num % i == 0] 
    return divisors

def main ():
    num = int(input("ingresa un numero"))
    print(divisors(num))
    print("termino del programa")

if __name__ == '__main__':
    main()