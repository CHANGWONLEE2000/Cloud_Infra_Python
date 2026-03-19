#Step06_Tuple.py

'''
    
    - tuple
    1. list 와 유사한 자료형
    2. 읽기전용 즉 값을 변경할 수 없다.
    3. 기능이 적어 list 보다 빠르다.
    
    만드는법   
    (value1, value2, value3, ...)
       
'''

# "one", "two", "three" 3개의 문자열이 tuple1 이라는 변수에 순서대로 담긴다.
from string import Template


tuple1: tuple = ("one", "two", "three")
result1 = tuple1[0]
result2 = tuple1[1]
result3 = tuple1[2]   


# index가 1개인 tuple을 만들때는 뒤에 , 를 붙여야 한다.
tuple2: tuple = ("kim",)

# 괄호 없이도 tuple을 만들 수 있다.
tuple3: tuple = 10, 20, 30

a, b, c = tuple3 # tuple3에 담긴 10, 20, 30이 순서대로 a, b, c에 담긴다.

# 두 변수에 있는 값을 서로 교체하기

first = "girl"
second = "boy"

# 교체하기 위해서 임시로 값을 담을 변수 tmp를 만든다.
'''
tmp = first
first = second
second = tmp  
'''
first, second = second, first # tuple을 이용해서 간단하게 교체하기

print("종료")
