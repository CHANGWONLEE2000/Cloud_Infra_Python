# Step05_Function.py

'''
    function type
   -특정시점에 여러줄의 code를 일괄 실행하고자 할때 사용한다.
   -함수도 data이다. (변수에 담을수 있다)
   -함수안에 저장된 code를 일괄실행 하는 것을 함수를 call(호출)한다고 한다.
   -함수는 젖아된 code를 다 실행하고 나면 원래 호출 했던 시점으로 실행의 흐름이 넘어온다.
   -호출했던 위치로 돌아오면서 어떤 data를 반드시 가져온다.
'''

def test1():
    print("test1() 호출됨.")

test1()
result = test1()

def test2(arg):
    print("전달받은 내용 :" , arg)
    print(f"전달받은 내용 : {arg} ")
    
#test2() # 매개변수가 입력되지 않아 오류뜸
test2(10)
test2("kim")


def print_sum(n1: int, n2: int):
    sum = n1 + n2
    print(f"{n1} + {n2} = {sum}")

print_sum(10, 20)
print_sum(30, 40)

def print_info(name: str, addr: str):
    print(f"이름은 {name} 이고 주소는 {addr}입니다.")



print_info("김구라","노량진")
print_info(addr="행신동", name="해골")

def get_sum(n1: int, n2: int):
    sum = n1 + n2
    return sum

result2 = get_sum(10, 20)


print ("종료")
