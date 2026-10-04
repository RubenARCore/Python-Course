deposit_sum = float(input())
deadline = float(input())
glp = float(input())

interest = deposit_sum * glp / 100
interest_per_month = interest / 12
total_sum = deposit_sum + (deadline * interest_per_month)
print(total_sum)