# MyDjangoProject
python web

author:wing
time:17-7-10 

使用Django 框架搭建的前后台交互demo，数据库使用mysql。有Django自带的接口调用不需要自己编写数据库语句。
使用模板展示前台数据，前台调用异步接口向后台发出请求，在没有添加@csrf_exempt会出现500错误。为避免此错误后台view中的处理函数需要加上这句。
后续继续完善。。。。
