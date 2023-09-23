from django.http import JsonResponse


def err_result(msg, code=500):
    return JsonResponse({"code": code, "msg": msg})


def result(data):
    return JsonResponse({"code": 200, "data": data})




ResError = err_result
ResSuccess = result

