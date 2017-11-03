from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse, FileResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render_to_response("index.html")


@csrf_exempt
def file_upload(request):
    print 'file_upload called'

    if request.FILES:
        file_list = request.FILES.getlist('file')
        file_list_cnt = len(request.FILES.getlist('file'))

        print file_list_cnt
        for f in file_list:
            print type(f)

    return_json = {
        'result': 'ok'
    }
    return JsonResponse(return_json)
