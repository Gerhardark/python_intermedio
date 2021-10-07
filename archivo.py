def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["gerhard", "hans", "isabellas"]
    with open("./archivos/names.txt", "a", encoding="utf-8") as n:
        for name in names:
            n.write(name)
            n.write("\n")

def main():
    write()

if __name__ == "__main__":
    main()