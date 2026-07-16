data = input().split("\\")
final = data[-1].split(".")

print(f'File name: {final[0]}')
print(f'File extension: {final[1]}')