from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
 
User = get_user_model()
 
 
class ForgotPasswordView(APIView):
    """
    POST /api/accounts/forgot-password/
    Body: { "email": "user@example.com" }
    Sends a password reset email with a token link.
    """
    permission_classes = []  # allow any (no auth required)
 
    def post(self, request):
        email = request.data.get("email", "").strip()
        if not email:
            return Response({"error": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)
 
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # Don't reveal whether user exists — always return 200
            return Response({"message": "If that email exists, a reset link has been sent."})
 
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
 
        # Replace with your actual frontend URL
        frontend_url = getattr(settings, "FRONTEND_URL", "https://bondhon-blood-bank.vercel.app")
        reset_link = f"{frontend_url}/reset-password/{uid}/{token}/"
 
        send_mail(
            subject="Bondhon – Password Reset Request",
            message=(
                f"Hi {user.get_full_name() or user.username},\n\n"
                f"Click the link below to reset your password:\n{reset_link}\n\n"
                f"This link expires in 1 hour. If you did not request this, ignore this email."
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )
        return Response({"message": "If that email exists, a reset link has been sent."})
 
 
class ResetPasswordView(APIView):
    """
    POST /api/accounts/reset-password/
    Body: { "uid": "...", "token": "...", "new_password": "..." }
    Validates token and sets new password.
    """
    permission_classes = []
 
    def post(self, request):
        uid = request.data.get("uid")
        token = request.data.get("token")
        new_password = request.data.get("new_password", "")
 
        if not uid or not token or not new_password:
            return Response({"error": "uid, token, and new_password are required."}, status=status.HTTP_400_BAD_REQUEST)
 
        if len(new_password) < 8:
            return Response({"error": "Password must be at least 8 characters."}, status=status.HTTP_400_BAD_REQUEST)
 
        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_id)
        except (User.DoesNotExist, ValueError, TypeError):
            return Response({"error": "Invalid reset link."}, status=status.HTTP_400_BAD_REQUEST)
 
        if not default_token_generator.check_token(user, token):
            return Response({"error": "Reset link is invalid or has expired."}, status=status.HTTP_400_BAD_REQUEST)
 
        user.set_password(new_password)
        user.save()
        return Response({"message": "Password reset successfully. You can now log in."})