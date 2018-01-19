from django.shortcuts import render
from django.http import HttpResponse

def index(requsest):
#    return HttpResponse("Hello,World!")
    return render(requsest, 'index.html', {'hello': 'Hello,World!!'})
# 第一个参数为对象本身，第二个为模板文件，字符串，第三个参数是后台传递到前端的数据
# Create your views here.
