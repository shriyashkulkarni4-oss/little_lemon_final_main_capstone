from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Booking, MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "inventory"]


class BookingSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = ["id", "name", "no_of_guests", "booking_date", "booking_time", "created_by"]
        read_only_fields = ["id", "created_by"]

    def validate_no_of_guests(self, value):
        if value < 1:
            raise serializers.ValidationError("A booking must include at least one guest.")
        return value


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "password"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
