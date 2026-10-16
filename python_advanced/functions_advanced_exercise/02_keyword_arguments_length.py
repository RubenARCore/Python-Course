def kwargs_length(**keywords):

    return len(keywords)

dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))