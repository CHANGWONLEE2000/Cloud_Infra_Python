
ip_addr = input("ip 주소입력: ")

ip_parts = ip_addr.split(".")

print(ip_parts)
binary_parts = []
for i in ip_parts:
    # :08b는 뒤에서 부터 읽으면 b(2진수)로 변환한되 총 8자리로 변환하고 빈곳은 0으로 채움
    print(f"{int(i):08b}")
    binary_parts.append(f"{int(i):08b}")
    
print(binary_parts)
# list에 저장된 각각의 아이템과 "."을 join 한다 (split의 반대 동작)
result = ".".join(binary_parts)

print(result)

print(f" 입력한 ip: {ip_addr}")
print(f" 2진수로 변환한 ip : {result}")