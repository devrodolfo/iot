from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .serializers import ReadSensorsSerializer
from django.contrib.auth.decorators import login_required
from .models import ReadSensors
from rest_framework.permissions import AllowAny
import json


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

@login_required
def grafico_sensores(request):
    leituras = ReadSensors.objects.order_by('-criado_em')[:20]
    leituras = list(reversed(leituras))

    context = {
        "datas": json.dumps([l.criado_em.strftime("%d/%m %H:%M") for l in leituras]),
        "sensor_1": json.dumps([l.sensor_1 for l in leituras]),
        "sensor_2": json.dumps([l.sensor_2 for l in leituras]),
        "sensor_3": json.dumps([l.sensor_3 for l in leituras]),
        "sensor_4": json.dumps([l.sensor_4 for l in leituras]),
        "sensor_5": json.dumps([l.sensor_5 for l in leituras]),
        "sensor_6": json.dumps([l.sensor_6 for l in leituras]),
    }

    return render(request, "grafico.html", context)