# Importaciones necesarias de Django Rest Framework y otros módulos
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, JSONParser
from apps.Tarjeta.models import Tarjeta
from apps.Movimiento.models import Movimiento
from apps.Movimiento.serializers import MovimientoSerializer, MovimientoSerializerListar
from apps.Tarjeta.serializers import TarjetaSerializer, TarjetaSerializerListar

@api_view(['GET', 'POST'])
@parser_classes([MultiPartParser, JSONParser])
def movimiento_api_view(request):
    if request.method == 'GET':
        mov = Movimiento.objects.all()  
        mov_serializado = MovimientoSerializerListar(mov, many=True)  
        return Response(mov_serializado.data, status=status.HTTP_200_OK)  

   
    elif request.method == 'POST':
        mov_serializado = MovimientoSerializer(data=request.data)  # Serializar los datos recibidos
        if mov_serializado.is_valid():  # Validar los datos
            mov_serializado.save()  # Guardar la nueva tarjeta
            return Response({'message': 'Movimiento creado correctamente!'}, status=status.HTTP_201_CREATED) # Respuesta de éxito
        return Response(mov_serializado.errors, status=status.HTTP_400_BAD_REQUEST)  # Manejo de errores