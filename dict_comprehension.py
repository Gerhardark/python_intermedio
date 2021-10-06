def main():
    my_dict = {"numero: " + str(i) : round(i**3) for i in range (1,101) if i % 3 != 0}
    print(my_dict)

if __name__ == '__main__':
    main()