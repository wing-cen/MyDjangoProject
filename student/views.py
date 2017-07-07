import self as self
from django.http import HttpResponse
import datetime ,json
from django.shortcuts import render, render_to_response
from MyDjangoProject import  selectSQL
from student.common import ConverJson,ConverJsonwithData
from django.views.decorators.csrf import csrf_exempt
from student.models import User,Wing
import types
from enum import Enum
from student.Enums import LoginStatue
from student import check_code
from io import BytesIO

def showInfo(request):
     user = User.objects.all()
     return render_to_response('student.html',{'students': user})

def showLoginPage(request):
    return render(request,'login.html')   #render 相当于打包的意思，第一个参数固定

@csrf_exempt   #取消当前的跨站请求伪造功能
def UserLogin(request):
    if request.method == "POST":
        data = request.POST
        name = data["name"]
        pwd = data["password"]
        code = data["code"]

        try:
            user = User.objects.get(name=name)
            if user.statue == 1:
                return HttpResponse(json.dumps({"statue": LoginStatue.UserAlive_ERR.value}),
                                    content_type='application/json') #用户已经登录
            else:
                if pwd == user.password:
                    if code.lower() == request.session["check_code"].lower():
                        user.statue = 1
                        user.save()
                        print(user.statue)
                        return render(request, 'main_menu.html')
                    else:
                        return HttpResponse(json.dumps({"statue": LoginStatue.Code_ERR.value}),
                                            content_type='application/json')  # 验证码错误
                else:
                    return HttpResponse(json.dumps({"statue": LoginStatue.PassWord_ERR.value}),
                                        content_type='application/json')  # 密码错误
        except User.DoesNotExist:
             return HttpResponse(json.dumps({"statue": LoginStatue.UserName_ERR.value}), content_type='application/json')  # 用户名错误

@csrf_exempt #ajax post 过来调用必须加上
def checkInput(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        if data["flag"] == "1":      #ajax 传过来变成字符串
            try:
                user = User.objects.get(name=data["name"])
                return HttpResponse(json.dumps({"statue": LoginStatue.Checking_OK.value}),
                                    content_type='application/json')
            except User.DoesNotExist:
                return HttpResponse(json.dumps({"statue": LoginStatue.UserName_ERR.value}),
                                    content_type='application/json')  # 用户名错误
        elif data["flag"] == "2":
            try:
                user = User.objects.get(password=data["password"])
                return HttpResponse(json.dumps({"statue": LoginStatue.Checking_OK.value}),
                                    content_type='application/json')
            except User.DoesNotExist:
                return HttpResponse(json.dumps({"statue": LoginStatue.PassWord_ERR.value}),
                                    content_type='application/json')  # 密码错误

def create_code_img(request):
    f = BytesIO()  # 直接在内存开辟一点空间存放临时生成的图片
    img, code = check_code.create_validate_code()  # 调用check_code生成照片和验证码
    request.session['check_code'] = code  # 将验证码存在服务器的session中，用于校验
    img.save(f, 'JPEG')  # 生成的图片放置于开辟的内存中
    return HttpResponse(f.getvalue())  # 将内存的数据读取出来，并以HttpResponse返回

@csrf_exempt
def loginout(request):
    if request.method == "POST":
        data = request.POST
        name = data["name"]
        user = User.objects.get(name=name)
        user.statue = 0
        print(user)
        user.save()
        return HttpResponse(json.dumps({"statue": LoginStatue.Checking_OK.value}),
                                    content_type='application/json')