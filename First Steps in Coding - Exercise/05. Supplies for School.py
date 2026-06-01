pens = float(input())
markers = float(input())
cleaning_liquid = float(input())
discount = float(input())

pens = pens * 5.8
markers = markers * 7.20
cleaning_liquid = cleaning_liquid * 1.20

sum = pens + markers + cleaning_liquid
discount = discount * sum / 100
sum = sum - discount

print(sum)