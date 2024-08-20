import uuid
import requests
from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from payments.models import Gateway, Payment
from payments.serializers import GatewaySerializer
from subscriptions.models import Package, Subscription


# Create your views here.
class GatewayView(APIView):
    def get(self, request):
        gateways = Gateway.objects.filter(is_active=True)
        serializer = GatewaySerializer(gateways, many=True)
        return Response(serializer.data)


class PaymentView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        gateway_id = request.query_params.get('gateway')
        package_id = request.query_params.get('package')

        try:
            package = Package.objects.get(id=package_id, is_active=True)
            gateway = Package.objects.get(id=gateway_id, is_active=True)

        except (Package.DoesNotExist, Gateway.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

        payment = Payment.objects.create(
            user=request.user,
            package=package,
            gateway=gateway,
            price=package.price,
            phone_number=request.user.phone_number,
            token=str(uuid.uuid4()),

        )

        # return redirect
        return Response({'token': payment.token, 'callback_url': 'https://my-site.com/payments/pay/'})

    def post(self, request):
        token = request.data.get('token')
        stat = request.data.get('status')

        try:
            payment = Payment.objects.get(token=token)

        except Payment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if stat != 10:
            payment.status = Payment.STATUS_CANCELED
            payment.save()
            return Response({'detail': 'payment Canceled.'},
                            status=status.HTTP_400_BAD_REQUEST)
        r = requests.post('bank_verify_url', data={})
        if r.status_code // 100 != 2:
            payment.status = Payment.STATUS_ERROR
            payment.save()
            return Response({'detail': 'payment verification failed'},
                            status=status.HTTP_400_BAD_REQUEST)
        payment.status = Payment.STATUS_PAID
        payment.save()

        Subscription.objects.create(
            user=request.user,
            package=payment.package,
            expired=timezone.now() + timezone.timedelta(days=payment.package.duration.days),
        )
        return Response({'detail': 'payment is successfully paid.'},)