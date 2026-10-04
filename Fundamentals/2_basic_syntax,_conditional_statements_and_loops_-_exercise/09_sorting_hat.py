while True:

    data = input()

    if data == "Welcome!":
        print("Welcome to Hogwarts.")
        exit()
    elif data == "Voldemort":
        print("You must not speak of that name!")
        exit()
    elif len(data) < 5:
        print(f'{data} goes to Gryffindor.')
    elif len(data) == 5:
        print(f'{data} goes to Slytherin.')
    elif len(data) == 6:
        print(f'{data} goes to Ravenclaw.')
    else:
        print(f'{data} goes to Hufflepuff.')