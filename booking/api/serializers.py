from rest_framework import serializers
from ..models import *
from rest_framework import status
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


class BookingCreateSerializer(serializers.ModelSerializer):

    def validate(self, data):

        try:
            self.booking_place = BookingPlace.objects.get(id=data['booking_place_id'])
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'message': 'Booking Place not found!', 'success': False, 'status': status.HTTP_400_BAD_REQUEST})

        occupancy_count = Booking.objects.filter(
            Q(booking_place_id=data['booking_place_id'], start_date__range=[data['start_date'], data['end_date']]) | Q(
                booking_place_id=data['booking_place_id'],
                start_date__range=[data['start_date'], data['end_date']])).count()

        if occupancy_count >= self.booking_place.daily_vacancy:
            raise serializers.ValidationError({'success': False, 'message': 'No vacancy available!', 'status_code': status.HTTP_400_BAD_REQUEST})
        return data

    class Meta:
        model = Booking
        exclude = ['create_by', 'create_at', 'update_at', 'update_by', 'delete_status', 'is_confirm', 'is_cancel']

        