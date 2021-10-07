from functools import reduce

def main ():
    my_list = [2,2,2,2]
    #odd = list(filter(lambda x: x%2 != 0, my_list))
    #odd = list(map(lambda x: x**2, my_list))
    #odd = [i**2 for i in my_list]
    odd = reduce(lambda a, b: a*b, my_list)
    print(odd)

if __name__ == '__main__':
    main()