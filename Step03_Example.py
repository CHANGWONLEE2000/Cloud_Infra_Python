# Step03_Example.py

""" 
    화원 한명의 정보는 번호, 이름, 주소 로 이루어져 있다.
    그리고 그러한 회원이 여러명이다.
    여러명의 회원 목록을 하나의 묶음으로(하나의 data)로 관리하고 싶다면...
"""

# 3명의 회원정보를 각각 dict 에 담은 다음 그 dict 를 list 에 담는 코드를 작성해서 채팅창에 보내 보세요

ID1 = {"num": "123-456-789", "name": "kim" , "addr": "서울"}
ID2 = {"num": "456-789-123", "name": "park", "addr": "부산"}
ID3 = {"num": "789-123-456", "name": "choi", "addr": "대구"}

members = [ID1, ID2, ID3]

a = members
b = members[0]
c = members[0]["num"]
d = members[0]["name"]