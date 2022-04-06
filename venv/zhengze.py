import re

html = '''
        <li data-view="2">一路上有你</li>
        <li data-view="7"> <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        <li data-view="4" class="active">
        <li data-view="6"><a href="/4.mp3" singer="41132">光辉岁月</a></li>/li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">
        <li data-view="5"><a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''
result = re.search('<li.data-view="5".*?href="(.*?)".singer="(.*?)">.*?class=(.*?)</i>', html, re.S)
# for i in len(result):
#     print(i)
# print(result)
if result:
    print(result)
    print(result.group(1), result.group(2), result.group(3))

#
# result1 = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
# # print(result1)
# if result1:
#     # print(result1)
#     print(result1.group(1), result1.group(2))

# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html) beyond 光辉岁月print(result)
# if result:
#     print(result)
#     print(result.group(1), result.group(2))