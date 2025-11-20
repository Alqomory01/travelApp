from django.urls import path
from .views import InitializePayment, VerifyPayment

urlpatterns = [
    path("pay/", InitializePayment.as_view(), name="pay"),
    path("verify/", VerifyPayment.as_view(), name="verify"),
]
