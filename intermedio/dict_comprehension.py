import math 

def main():
    my_dict = {'raiz cuadrada de ' + str(i) : round(math.sqrt(i),2) for i in range (1,1001)}
    print(my_dict)

if __name__ == '__main__':
    main()