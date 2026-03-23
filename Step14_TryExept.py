
# main 으로 실행했을때(현재 파일엣 run 했을때) 실행할 code 블럭
if __name__ == "__main__" :
    try:
        num1_str : str = input("젯수 입력: ")
        num2_str : str = input("피젯수 입력: ")
        
        num1 = int(num1_str)
        num2 = int(num2_str)
        
        result1 : int = num2/num1
        print(f"{num2}를 {num1}으로 나눈 결과값 : {result1}")
    except ValueError as VE:
        print(VE)
        print("숫자로 입력하시오")
    except ZeroDivisionError as ZDE :
        print(ZDE)
        print("어떤 수를 0으로 나눌수는 없습니다.")    
        
    print("종료")


