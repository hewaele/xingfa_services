from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse
from .models import user
from django.views.decorators.csrf import csrf_exempt
import sys
from .predict_model import load_modle_to_predict
import os
image_path = '/home/hewaele/PycharmProjects/django/xingfa_services/mysite/upload/'
# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(required=False)
    headImg = forms.ImageField(required=False)
@csrf_exempt
def index(request):
    if request.method == "POST":
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            print(request.FILES)
            #获取表单信息request.FILES是个字典
            User = user(headImg=request.FILES['file'])
            #保存之前清空文件夹
            p = os.listdir(image_path)
            for pi in p:
                os.remove(image_path+pi)
            #保存在服务器
            User.save()
            p = os.listdir(image_path)

            #执行预测
            result = load_modle_to_predict()
            print(result)
            return HttpResponse(str(result))
    return render(request, 'blog/index.html')

# httCreate your views here.
# def index(request):
#     return render(request, 'blog/index.html')