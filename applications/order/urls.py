# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from applications.order.views import OrderViewSet, OrderListViewSet, OrderConfirmAPIView


# router = DefaultRouter()
# router.register("history", OrderListViewSet)
# router.register("", OrderViewSet)


# urlpatterns = [
#     path("confirm/<uuid:code>", OrderConfirmAPIView.as_view()),
#     path("", include("router.urls"))
# ]