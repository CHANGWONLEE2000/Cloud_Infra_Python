#list type 에 대해 알아보기

nums = [10, 20, 30, 40, 50]
names = ["kim", "park", "jo", "oh", "choi"]

#list에 들어 있는 데이터를 앞에서 부터 순서대로 참조하면서 어떤동작을 할 일들이 많이 발생한다.



#nums 에 저장되어 있는 데이터를 순서대로 참조하며서 콘솔창에 출력
for i in nums:
    print(i)
for i in names:
    print("names를 순서대로 출력중....")
    print(i)



r1 = range(5)
r2 = range(10)

print(r1)
print(r2)

for i in range(5):
    print(i)

result2 = range(len(names))

for i in range(len(names)):
    print("list의 index와 함께 출력합니다.")
    print(i, names[i])
print("종료")