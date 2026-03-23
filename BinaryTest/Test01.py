# 2진수는 숫자를 만들대 prefix로 0b 2진수 -> 10진수
num1 = 0b1010 
result = num1 +5
print(result)

# 10 진수를 2진수를 변환
num2 = 150
result2 : str = bin(num2) # 2진수로 변환
print(result2)
# 츨력시 0b제거
print(result2[2:])

print("----------------------------------------------------------------")

line = "abcde12345"
print(line[4:len(line)])

