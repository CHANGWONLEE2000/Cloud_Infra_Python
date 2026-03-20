from jinja2 import Template

my_template = '''
    번호 : {{ num }}
    이름 : {{ name }}
    키: {{body.height}}
    몸무게 : {{body.weight}} 
    취미 :
        {% for i in hobby %}
        - {{i}}
        {% endfor %}
'''

info : dict = {
    "num" : 1,
    "name" : "김구라",
    "body" : {
        "weight" : 80 ,
        "height" : 170
        },
    "hobby" : ["피아노","당구","프로그래밍"]
    
}

temp = Template(my_template)
result1 = temp.render(info)
print(result1)

