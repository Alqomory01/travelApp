from .models import Booking
from rest_framework import serializers
from .models import Booking, Location, MultiCitySegment


class LocationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Location
        fields = ['id', 'city', 'country']


class MultiCitySegmentSerializer(serializers.ModelSerializer):
    origin = LocationSerializer()
    destination = LocationSerializer()

    class Meta:
        model = MultiCitySegment
        fields = ['id', 'origin', 'destination', 'depart_date'] 

class BookingSerializer(serializers.ModelSerializer):
    origin = LocationSerializer()
    destination = LocationSerializer()
    segments = MultiCitySegmentSerializer(many=True, required=False)

    class Meta:
        model = Booking
        fields = [
            'id', 'customer', 'agent', 'service', 'trip_type', 'travel_class',
            'origin', 'destination', 'depart_date', 'return_date', 'number_of_travelers',
            'date', 'status', 'segments', 'created_at'
        ]
        read_only_fields = ['customer']  

    def create(self, validated_data):
        segments_data = validated_data.pop('segments', None)
        origin_data = validated_data.pop('origin')
        destination_data = validated_data.pop('destination')

        origin, _ = Location.objects.get_or_create(**origin_data)
        destination, _ = Location.objects.get_or_create(**destination_data)

        booking = Booking.objects.create(
            customer=self.context['request'].user,
            origin=origin,
            destination=destination,
            **validated_data
        )

     
        if segments_data and validated_data.get('trip_type') == 'multi_city':
            for segment in segments_data:
                seg_origin_data = segment.pop('origin')
                seg_destination_data = segment.pop('destination')

                seg_origin, _ = Location.objects.get_or_create(**seg_origin_data)
                seg_destination, _ = Location.objects.get_or_create(**seg_destination_data)

                MultiCitySegment.objects.create(
                    booking=booking,
                    origin=seg_origin,
                    destination=seg_destination,
                    **segment
                )

        return booking
