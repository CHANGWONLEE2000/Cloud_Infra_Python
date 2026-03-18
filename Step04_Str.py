# str type 에 대해서 알아보자 (중요!)

text = "      Cloud Infra  "
result = text.strip() # 양쪽 공백 제거

myIp = "192.168.0.2"


# . 을 기준으로 문자열을 나눠서 list로 리턴
result2 = myIp.split(".") 

# list에 들어 있는 문자열을 .로 연결해서 하나의 문자열로 리턴
result3 = ".".join(result2) 

# 특정 문자열 찾아서 대체하기
result4 = "hello mimi!".replace("mi","ma")

# 대문자로 변환
result5 = "python".upper() 

# 소문자로 변환
result6 = "PYTHON".lower() 

print ("제거합니다.")
