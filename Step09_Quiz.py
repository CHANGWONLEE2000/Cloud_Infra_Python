#Step09_Quiz.py

'''
    비밀번호를 입력받아서 입력한 비밀번호가 8자 이상이면
    "사용가능한 비밀 번호 입니다"
    그렇지 않으면
    "사용 불가 입니다."
    "

'''

input_password :str = input("사용할 비밀번호를 입력하시오.")


if len(len_password) > 7 :
    print("사용가능한 비밀 번호입니다.")
else:
    print("사용 불가 입니다.")