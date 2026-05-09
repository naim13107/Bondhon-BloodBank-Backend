from django.urls import path, include
from rest_framework.routers import DefaultRouter
from donors.views import DonorViewSet
from blood_request.views import BloodRequestViewSet, MyRequestsViewSet
# ADD AdminDashboardSummaryView HERE
from dashboard.views import (
    UserDashboardViewSet, 
    AdminDeleteRequestView, 
    AdminDeleteUserView,
    AdminDashboardSummaryView  # Added this
)
from blood_request.views import (
    initiate_payment, 
    payment_history, 
    payment_success, 
    payment_cancel, 
    payment_fail
)

router = DefaultRouter()
router.register('donors', DonorViewSet, basename='donors')
router.register('requests', BloodRequestViewSet, basename='requests')
router.register('dashboard', UserDashboardViewSet, basename='dashboard')
router.register('my-requests', MyRequestsViewSet, basename='my-requests')

urlpatterns = [
    path('', include(router.urls)),
    
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    
    # Payment Routes
    path("payment/initiate/", initiate_payment, name='initiate-payment'),
    path('payment/history/', payment_history, name='payment_history'),
    path('payment/success/', payment_success, name='payment_success'),
    path('payment/fail/', payment_fail, name='payment_fail'),
    path('payment/cancel/', payment_cancel, name='payment_cancel'),

    # Admin Panel Routes
    # Add the summary route here for the frontend hook to call
    path('admin-panel/summary/', AdminDashboardSummaryView.as_view(), name='admin-summary'),
    path('admin-panel/users/<int:user_id>/', AdminDeleteUserView.as_view(), name='admin-delete-user'),
    path('admin-panel/requests/<int:request_id>/', AdminDeleteRequestView.as_view(), name='admin-delete-request'),
]