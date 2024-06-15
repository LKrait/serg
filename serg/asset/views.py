from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import time
import random
from .models import Asset


@login_required
def dashboard(request):
    info = "Access Notice: "+str(random.randrange(1000,9999,1))
    send_mail(info, f"Dashboard_001 has been accessed from IP=127.0.0.1:8000 on {time.ctime()}", "afiokevin@gmail.com", ["afio.kev@gmail.com"], fail_silently=True)
    # asset = Asset.objects.all()
    return render(request, 'asset/dashboard.html', {'asset': 'asset'})

