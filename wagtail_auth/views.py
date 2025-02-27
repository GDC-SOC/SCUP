from django.shortcuts import render

# Create your views here.
from two_factor.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

class WagtailOTPLoginView(LoginView):
    """
    Custom login view to integrate django-otp with Wagtail’s admin login.
    """
    template_name = 'wagtailadmin/login.html'  # Uses Wagtail’s existing login template

@login_required
def wagtail_admin_redirect(request):
    """
    Redirect authenticated users to the Wagtail admin after OTP verification.
    """
    return redirect('wagtailadmin_home')
