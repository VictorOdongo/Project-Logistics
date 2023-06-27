from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from customer.models import *


@csrf_exempt
@login_required(login_url="/driver-login/")
def available_jobs_api(request):
    jobs = list(Job.objects.filter(status=Job.PROCESSING_STATUS).values())

    return JsonResponse({
        "success": True,
        "jobs": jobs
    })