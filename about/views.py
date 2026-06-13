from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, \
    CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from .serializers import AboutSerializer, TechnologySerializer
from .models import About, Technology


class AboutListAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

class TechnologyListAPIView(ListAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

class TechnologyDetailAPIView(RetrieveAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

class TechnologyCreateAPIView(CreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

class TechnologyUpdateAPIView(UpdateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

class TechnologyDestroyAPIView(DestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
#
# class TechnologyDetailUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Technology.objects.all()
#     serializer_class = TechnologySerializer

class TechnologyDetailUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

class TechnologyListCreateAPIView(ListCreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

class TechnologyRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer




