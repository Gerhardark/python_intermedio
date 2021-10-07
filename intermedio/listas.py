def main ():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'firstname': 'gerhard', 'lastname': 'reinike'}

    super_list = [
        {'firstname': 'gerhard', 'lastname': 'reinike'},
        {'firstname': 'hans', 'lastname': 'reinike'},
        {'firstname': 'karime', 'lastname': 'gonzalez'},
        {'firstname': 'isabella', 'lastname': 'reinike'},
    ]

    super_dict = {
        'natulral': [1,2,3,4,5],
        'integer_num': [-1,-2,-3,0],
        'floating_nums': [3.4,3.5,7.0,10.5]
    }

    for key, value in super_dict.items():
        print(key, " ", value, " ")

if __name__ == "__main__":
    main()
