
from rest_framework import serializers

from portfolio.models import (
    Resumee,
    # Experience,
    # Contact
)


class ResumeeSerializer(serializers.ModelSerializer):
    """
    Serializer for Tournament model
    """

    class Meta:
        model = Resumee
        fields = "__all__"

