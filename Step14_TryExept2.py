
# main 으로 실행했을때(현재 파일엣 run 했을때) 실행할 code 블럭
if __name__ == "__main__" :
    try:
        num1_str : str = input("젯수 입력: ")
        num2_str : str = input("피젯수 입력: ")
        
        num1 = int(num1_str)
        num2 = int(num2_str)
        
        result1 : int = num2/num1
        print(f"{num2}를 {num1}으로 나눈 결과값 : {result1}")
    except Exception as ae:
        print("어떠한 에러가 발생했습니다",e)
    else: # 예외가 발생하지 않으면 실행이 되는 블럭
        pass
    finally: # 정상수행 or 예외가 발생해도 반드시 실행이 보장된 블럭
        pass
        
    print("종료")


