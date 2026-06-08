username = input()
password = input()
l = ""
while l != password:
    l = input()
    if l == password:
        print(f'Welcome {username}!')
