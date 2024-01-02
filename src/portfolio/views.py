import json

from django.shortcuts import render

from core.permissions import IsAdminOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from portfolio.models import (
    Resumee,
    # Experience,
    # Contact
)
from portfolio.serializers import (
    ResumeeSerializer,
    # ExperienceSerializer,
    # ContactSerializer
)

def index(request):
    resumee_instance = Resumee.objects.get(id=1)
    serializer = ResumeeSerializer(resumee_instance)

    json_data = json.dumps(serializer.data, indent=4)

    return render(request, 'portfolio/index.html', {'json_data': json_data})

class ResumeeList(generics.ListAPIView):
    """
    List View for Match model
    """

    serializer_class = ResumeeSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Resumee.objects.all()


class ResumeeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail, update and delete view for Match model
    """

    permission_classes = [IsAdminOrReadOnly]
    queryset = Resumee.objects.all()
    serializer_class = ResumeeSerializer

