import sys
import json
from rest_framework.exceptions import ValidationError
from rest_framework import exceptions
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import CreateAPIView
from .serializers import *
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from datetime import date, datetime
from ..models import *
from .import swagger_doc

class BookingCreateAPIView(CreateAPIView):
    serializer = BookingCreateSerializer

    @swagger_auto_schema(request_body=swagger_doc.BookingCreateRequestSerializer, responses=swagger_doc.booking_create_response)
    def post(self, request, **kwargs):
        if 'booking_place_id' not in request.data.keys() or request.data['booking_place_id'] == '':
            raise exceptions.ValidationError({'success': [False], 'message': ['booking_place_id is required'], 'status_code': [status.HTTP_400_BAD_REQUEST]})
        if 'start_date' not in request.data.keys() or request.data['start_date'] == '':
            raise exceptions.ValidationError({'success': [False], 'message': ['start_date is required'], 'status_code': [status.HTTP_400_BAD_REQUEST]})
        if 'end_date' not in request.data.keys() or request.data['end_date'] == '':
            raise exceptions.ValidationError({'success': [False], 'message': ['end_date is required'], 'status_code': [status.HTTP_400_BAD_REQUEST]})
        if 'customer_name' not in request.data.keys() or request.data['customer_name'] == '':
            raise exceptions.ValidationError({'success': [False], 'message': ['customer_name is required'], 'status_code': [status.HTTP_400_BAD_REQUEST]})
        if 'customer_phone' not in request.data.keys() or request.data['customer_phone'] == '':
            raise exceptions.ValidationError({'success': [False], 'message': ['customer_phone is required'], 'status_code': [status.HTTP_400_BAD_REQUEST]})

        serializer = self.serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        booking_place = BookingPlace.objects.get(id=request.data['booking_place_id'])
        day_count = (datetime.strptime(request.data['end_date'], "%Y-%m-%d") - datetime.strptime(request.data['start_date'], "%Y-%m-%d")).days + 1
        total_price = booking_place.daily_price*day_count
        customer = Customer.objects.create(name=request.data['customer_name'], phone=request.data['customer_phone'], email=request.data.get('customer_email', '' ))
        serializer.save(customer=customer, total_price = total_price, day_count = day_count)

        response = {
            'success': True,
            'status_code': status.HTTP_201_CREATED,
            'message': 'Booking created successfully!',
            'total_price': total_price
        }

        return Response(response, status=status.HTTP_201_CREATED)