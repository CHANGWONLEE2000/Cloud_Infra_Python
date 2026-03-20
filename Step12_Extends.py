#Step12_Extends.py

#클래스 상속에 대해 알아보자

class Phone:
    def call(self):
        print("전화를 건다")
        return 10

# 가상의 핸드폰을 찍어낼 클래스, Phone 클래스를 extends 해서 정의한다
class HandPhone(Phone): #클래스명(상속받을 클래스)
    def mobile_call(self):
        print("이동중 전화")
    def take_picture(self):
        print("사진 찍기")

class SmartPhone(HandPhone):
    def do_internet(self):
        print("인터넷 사용")
    # 부모 클래스(HandPhone)의 사진찍는 기능을 재정의(Overriding)
    def take_picture(self):
        print("스마트폰 사진찍기")
    


if __name__ == "__main__" :
    p1:Phone = Phone()
    p1.call()
    
    p2:HandPhone = HandPhone()
    p2.call()
    p2.mobile_call()
    p2.take_picture()
    
    p3:SmartPhone = SmartPhone()
    p3.call()
    p3.mobile_call()
    p3.take_picture()
    p3.do_internet()
    