from django.shortcuts import get_object_or_404
from rest_framework import views
from .serializers import MasterSerializer
from .models import MasterModel, OrderModel
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from rest_framework import status


class AllMasterView(views.APIView):
    def get(self, request):
        all_master = MasterModel.objects.all()
        serializer = MasterSerializer(all_master, many=True)
        return Response(serializer.data)


class CreateMasterView(views.APIView):
    def post(self, request):
        serializer = MasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class UpdateMasterView(views.APIView):
    def patch(self, request, *args, **kwargs):
        master = get_object_or_404(MasterModel, id=kwargs['master_id'])
        serializer = MasterSerializer(master, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class DeleteMasterView(views.APIView):
    def delete(self, request, *args, **kwargs):
        master = get_object_or_404(MasterModel, id=kwargs['master_id'])
        master.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
