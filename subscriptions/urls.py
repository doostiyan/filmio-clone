from django.urls import path

from subscriptions import views

urlpatterns = [
    path('package/', views.PackageView.as_view(), name='package'),
    path('subscription/', views.SubscriptionView.as_view(), name='subscription'),
]