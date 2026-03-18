#yaml 형식의 문자열 다루기
#yaml 형식의 문자열을 dict로 변환하기 위해서는 pyyaml 라이브러리를 설치해야 한다.


info = '''
name: 이창원
addr: 인천
foods:
  - 피자
  - 치킨
isMan: true
body:
  height: 183
  weight: 85
'''
###과제### 
#검색 혹은 ai 도움을 받아서 info에 들어잇는 문자열을 dict type으로 바꾸기
#dict에 들어있는 내용 확인후 해당 내용으로 yaml로 변환
import yaml


result = yaml.safe_load(info)


for i in result:
    print(result[i])
result2 = yaml.dump(result, allow_unicode=True)
print(result2)
