
print("Step01 시작")

#int type
num1 = 10
# float type
num2 = 10.1
# str type
myName = '김구라'
yourName = '해골'
ourName = """
    KT CLoud Infra
    화아팅!
"""

# 순서가 중요한 여러개의 데이터를 관리하고 싶다면 .... 
foods = ["삼겹살", "김밥", "닭발"] #list 변수,list,정수 타입상관없이 다집어넣기 가능
print(foods)
 
# 순서가 중요치 않지만 여러개의 데이터를 관리하고 싶다면...
mem1 = {"num":1 , "name":"김구라" , "addr":"노량진"}#dict {"key":"value"}
print(mem1)

# 순서가 중요치 않은 데이터를 하나의 묶음으로 관리(키값 없이)
mySet = {"빨강사탕", "초록사탕", "노랑사탕"}#set
print(mySet)

# 특정 code 블럭을 필요한 시점에 일괄 실행하고 싶다면...
def store():
    print("냉장고 문을 연다.")
    print("물건을 저장한다.")
    print("냉장고 문을 닫는다.") # 함수 파이썬에서는 함수도 데이터 타입으로 빠짐


store()
returnValue = store()

# 어떤 변수를 빈 상태로 만들고 값을 나중에 넣고 싶다면? None
a = None
print("어떤 작업을 하고")
print("필요할때 값을 넣는다")
a = "test"

# 참과 거짓을 나타내는 data type (Bool)
isMan = True
isWoman = False
isDifferent = True
isRun = False  
canEat = True 