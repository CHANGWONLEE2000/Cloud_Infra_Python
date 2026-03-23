
a = 0b1100
b = 0b1010

# a와 b를 비트 And 연산

print(a & b)
print(bin(a & b))

# _사용해도 인식됨
info = 0b1111_1111_1111_0000 #65520
print(bin(info))
print("------------------------------------------------------------------")
data1 = 0b1100_0011_1010_0001
data2 = 0b1100_0011_1010_1001
data3 = 0b1100_0011_1010_1011
data4 = 0b1100_0011_1010_1100
data5 = 0b1111_0000_1010_1111

print(bin(info&data1))
print(bin(info&data2))
print(bin(info&data3))
print(bin(info&data4))
print(bin(info&data5))



