from django.shortcuts import render
import datetime
# Create your views here.
from feedback.models import Feedback


def add(request):
    if request.method == "POST":
        obj = Feedback()
        obj.feedback = request.POST.get('feedback')
        obj.date = datetime.date.today()
        obj.u_id = "1"
        obj.save()
    return render(request, 'feedback/post_feedback.html')


def view(request):
    obj = Feedback.objects.all()
    context = {
        'msg': obj
    }
    return render(request, 'feedback/view_feedback.html', context)


from django.http import HttpResponse
from rest_framework.views import APIView, Response
from feedback.serializer import android
import datetime


class feedback_view(APIView):
    def get(self, request):
        ob = Feedback.objects.all()
        ser = android(ob, many=True)
        return Response(ser.data)

    def post(self, request):
        ob = Feedback()
        ob.u_id = request.data['u_id']

        ob.date = datetime.datetime.today()
        ob.feedback = request.data['feedback']
        ob.save()
        return HttpResponse('POST')
