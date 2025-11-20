from django.shortcuts import render
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Booking, Payment

class InitializePayment(APIView):
    def post(self, request):
        booking_id = request.data.get("booking_id")
        amount = request.data.get("amount")  

        booking = Booking.objects.get(id=booking_id, customer=request.user)

        reference = f"BOOK-{booking_id}-{booking.customer.id}"

        Payment.objects.create(
            booking=booking,
            amount=int(amount) * 100,  # convert to kobo
            reference=reference
        )

        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json"
        }

        data = {
            "email": request.user.email,
            "amount": int(amount) * 100,
            "reference": reference,
            "callback_url": "http://localhost:5173/payment-success"
        }

        r = requests.post(f"{settings.PAYSTACK_BASE_URL}/transaction/initialize", json=data, headers=headers)
        return Response(r.json())
    
class VerifyPayment(APIView):
    def get(self, request):
        reference = request.GET.get("reference")
        payment = Payment.objects.get(reference=reference)

        headers = {"Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"}
        url = f"{settings.PAYSTACK_BASE_URL}/transaction/verify/{reference}"

        r = requests.get(url, headers=headers).json()

        if r["data"]["status"] == "success":
            payment.status = "success"
            payment.save()

            booking = payment.booking
            booking.status = "paid"
            booking.save()

            return Response({"status": "payment verified"})

        payment.status = "failed"
        payment.save()
        return Response({"status": "payment failed"}, status=400)


# Create your views here.
