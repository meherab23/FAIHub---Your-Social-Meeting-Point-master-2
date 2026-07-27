from email import message
import os
import requests
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile


# In production (Render), SITE_URL should be set to your live https:// domain.
# Locally it falls back to 127.0.0.1:8000 (the usual default runserver port).
SITE_URL = os.environ.get("SITE_URL", "http://127.0.0.1:8000")

# Render's free tier blocks outbound SMTP ports (25/465/587), so in production
# we send email via Brevo's HTTPS API instead. Locally (no BREVO_API_KEY set),
# it falls back to normal Gmail SMTP so nothing changes for local testing.
BREVO_API_KEY = os.environ.get("BREVO_API_KEY")


def _send_email(subject, message, recipient_email):
    if BREVO_API_KEY:
        response = requests.post(
            "https://api.brevo.com/v3/smtp/email",
            headers={
                "api-key": BREVO_API_KEY,
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            json={
                "sender": {"email": settings.EMAIL_HOST_USER},
                "to": [{"email": recipient_email}],
                "subject": subject,
                "textContent": message,
            },
            timeout=10,
        )
        response.raise_for_status()
        return True
    else:
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])
        return True


def forget_pass_sendmail(email,token):
    
    subject = "Reset Password"
    message = f'Click This Link to reset your Password:  {SITE_URL}/resetPassword/{token}/'
    return _send_email(subject, message, email)

def verify_account_sendmail(email,token):
    subject = "Activate Your Account"
    message = f'Click This Link to activate your account:  {SITE_URL}/verify_email/{token}/'
    return _send_email(subject, message, email)