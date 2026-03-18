# List type에 대해 알아보자

"""
        -list type
        1. 순서가 있다.
        2. 여러 type의 data를 담을 수 있다.
        3. 값 변경 가능
"""

# 대부분 한가지 data type을 담지만 여러 type의 data를 담을 수 있다.
nums = [10,20,30]
name = ["김구라", "해골", "원숭이"]
datas = [10, "xxx", True]

# 추가
nums.append(40)

# len() built in function : list의 길이(개수)를 리턴하는 함수
nums_len = len(nums)

# index를 이용해서 참조
name0 = name[0]

# 값에 의한 삭제
name.remove("원숭이")

# index를 이용해서 삭제
del name[0]

# 맨마지막 index를 삭제하면서 값 가져오기
nums.pop()
result = nums.pop()





print("종료")