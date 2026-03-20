#Step_jinja2_list.py

from jinja2 import Template


my_template : str = '''               
    친구목록
    {% for name in friends %}
    -{{ name }}
    {% endfor %}
'''

# Template 객체 생성
temp : Template = Template(my_template)

#Template 객체에 전달할 list
name = ["김구라" , "해골" , "원숭이"]

#Template 객체의 render() 메소드 호출하면서 friends에 name 전달하기
result1 : str = temp.render(friends = name)

print(result1)
