# Step04_Str2.py
'''
    json,xml,yaml

'''


# json은 javascript 객체 표기법을 따르는 문서 형식이다.  info는 str 타입이지만 json 형식의 문자열이다.
import json


info = '''{
    "name":"이창원",
    "addr":"인천",
    "foods":["피자","돈까스"]
}
'''

# json 형식의 문자열을 dict로 변환
result = json.loads(info) 

print(result["name"])
print(result["addr"])
print(result["foods"][0])
print(result["foods"][1])



# dict를 json 형식의 문자열로 변환
result2 = json.dumps(result) 




print("종료")