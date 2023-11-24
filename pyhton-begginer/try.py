base_number = 1234
reversedNum = 0
while base_number != 0:
    last_digit = base_number % 10
    reversedNum = (reversedNum * 10) + last_digit
    base_number = base_number // 10
print(reversedNum)
