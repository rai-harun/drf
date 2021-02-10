from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serialized_data = StudentSerializer(data=python_data)

        if serialized_data.is_valid():
            serialized_data.save()
            response = {'msg':'Data Created Successfully!'}
            response_json_data = JSONRenderer().render(response)
            # return JsonResponse(response_json_data)
            return HttpResponse(response_json_data, content_type='application/json')
        response_json_data = JSONRenderer().render(serialized_data.errors)
        return HttpResponse(response_json_data, content_type='application/json')

