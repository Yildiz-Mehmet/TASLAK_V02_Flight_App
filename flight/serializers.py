from rest_framework import serializers
from .models import Flight, Reservation, Passenger
from rest_framework.validators import UniqueValidator 

class FlightSerializer(serializers.ModelSerializer):
    
    flight_number = serializers.CharField(  
        validators=[UniqueValidator(queryset=Flight.objects.all())],
        )
    
    class Meta:
        model = Flight
        fields = (
            'id',
            "flight_number",
            "operation_airlines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "estimated_time_of_departure",
        )


class PassengerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Passenger
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    
    passenger = PassengerSerializer(many=True,)
    flight = serializers.StringRelatedField()
    flight_id = serializers.IntegerField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Reservation
        # fields = "__all__"
        fields = ("id", "flight", "flight_id", "user", "passenger")


