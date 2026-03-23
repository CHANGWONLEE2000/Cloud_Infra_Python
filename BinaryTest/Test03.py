# a와 b를 비트 Or , Xor , Not

a = 0b1100
b = 0b1010

# bit or 연산
print(bin(a | b))

# bit xor 연산
print(bin(a ^ b))

# bit not 연산
print(bin(~a & 0xF))
print(bin(~b))


