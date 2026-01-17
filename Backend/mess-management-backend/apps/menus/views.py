from rest_framework import viewsets
from rest_framework.response import Response
from .models import Menu
from .serializers import MenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def list(self, request):
        menus = self.get_queryset()
        serializer = self.get_serializer(menus, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        menu = serializer.save()
        return Response(MenuSerializer(menu).data, status=201)

    def retrieve(self, request, pk=None):
        menu = self.get_object()
        serializer = self.get_serializer(menu)
        return Response(serializer.data)

    def update(self, request, pk=None):
        menu = self.get_object()
        serializer = self.get_serializer(menu, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        menu = serializer.save()
        return Response(MenuSerializer(menu).data)

    def destroy(self, request, pk=None):
        menu = self.get_object()
        menu.delete()
        return Response(status=204)