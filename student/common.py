import json


def ConverJson(data):
    return json.dumps([{'name': i[0], 'id': i[2], 'age': i[1]} for i in data], indent=4, ensure_ascii=False)

def ConverJsonwithData(data):
    return json.dumps({'data': [{'name': i[0], 'id': i[2], 'age': i[1]} for i in data]}, indent=4,ensure_ascii=False)