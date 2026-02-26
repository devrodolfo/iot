from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import ReadSensorsSerializer
from django.contrib.auth.decorators import login_required
from .models import ReadSensors
from rest_framework.permissions import AllowAny



@api_view(['POST'])
def receber_leitura(request):
    serializer = ReadSensorsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "ok"})
    return Response(serializer.errors)




@login_required
def dashboard(request):
    leituras = ReadSensors.objects.order_by('-criado_em')[:20]
    return render(request, 'sensores/dashboard.html', {'leituras': leituras})
#sensores/templates/dashboard.html