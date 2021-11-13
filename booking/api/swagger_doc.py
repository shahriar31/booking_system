from rest_framework import serializers
from drf_yasg import openapi
from collections import OrderedDict
from ..models import *

#============Request & Response Body for Booking Create API ============================#

class BookingCreateRequestSerializer(serializers.Serializer):
    booking_place_id = serializers.IntegerField(required=True)
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)
    customer_name = serializers.CharField(required=True)
    customer_phone = serializers.CharField(required=True)
    customer_email = serializers.CharField(required=False)



booking_create_response = {
        "201": openapi.Response(
            description="success description",
            examples={
                "application/json": {
                    'message': 'Booking created successfully!',
                    'success': True,
                    'total_price': 3000,
                    'status_code': 201
                }
            }
        ),
        "400": openapi.Response(
            description="failed description",
            examples={
                "application/json": {
                    'message': ['Error message'],
                    'success': [False],
                    'status_code': [400]
                }
            }
        ),
    }