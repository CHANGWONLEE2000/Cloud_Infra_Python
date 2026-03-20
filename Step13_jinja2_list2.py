#Step13_jinja2.list2.py

# 게시글 목록이 담긴 리스트

from jinja2 import Template

my_template = """
    글목록입니다.
    {%for post in posts%}
    -글번호 : {{post.id}} 작성자 : {{post.Writer}} 제목 : {{post.Title}}
    {%endfor%}
"""

posts : list = [
    
    { "id" : 1 , "Writer" : "작성자1" , "Title" : "제목1" },
    { "id" : 2 , "Writer" : "작성자2" , "Title" : "제목2" },
    { "id" : 3 , "Writer" : "작성자3" , "Title" : "제목3" }   
] 


temp  = Template(my_template)
result1 = temp.render(posts = posts)
print(result1)

