from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django_otp.middleware import OTPMiddleware
from django_otp.plugins.otp_totp.models import TOTPDevice

class EnforceAdmin2FA(OTPMiddleware):
    def process_request(self, request):
        if request.path.startswith('/django-admin/') and request.user.is_authenticated:
            if not TOTPDevice.objects.filter(user=request.user, confirmed=True).exists():
                return redirect('two_factor:setup')  # Redirect to 2FA setup page
