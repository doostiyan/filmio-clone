from django.shortcuts import render
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from subscriptions.models import Package, Subscription
from subscriptions.serializers import PackageSerializer, SubscriptionSerializer


# Create your views here.

class PackageView(APIView):
    def get(self, request):
        packages = Package.objects.filter(is_active=True)
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)


class SubscriptionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        subscriptions = Subscription.objects.filter(
            user=request.user,
            expired_time__gt=timezone.now()
        )
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)