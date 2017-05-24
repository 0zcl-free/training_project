

input_str = input("")

li = input_str.split(" ")

input_price = input("")
price_list = input_price.split(" ")

sum = 0
for i in range(len(price_list)):
    price = int(price_list[i])
    sum1 = 0
    for j in range(len(price_list)):
        if int(price_list[j]) >= price:
            sum1 += price

    if sum1 > sum:
        sum = sum1
        max_price = price


print(max_price)
