limit = int(input("Limit: "))
num = 0
sum_num = 0
sum_str = ""

while sum_num < limit:
    num += 1
    sum_num += num
    if sum_num < limit:
        sum_str += f"{num} + "
    else:
        sum_str += f"{num}"

print (f"The consecutive sum: {sum_str} = {sum_num}")
