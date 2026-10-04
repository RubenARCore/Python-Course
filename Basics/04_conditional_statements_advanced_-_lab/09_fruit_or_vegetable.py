food_type = input()

if food_type in {'banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes'}:
    print('fruit')
elif food_type in {'tomato', 'cucumber', 'pepper', 'carrot'}:
    print('vegetable')
else:
    print('unknown')