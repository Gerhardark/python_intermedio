def main():
    square = [i for i in range(1,1000) if i % 4 ==0 and i % 6 == 0 and i % 9 == 0]

    print(square)

if __name__ == '__main__':
    main()