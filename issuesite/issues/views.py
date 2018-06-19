from django.shortcuts import render
from .models import Issue
# Create your views here.


def issues(request):
    issues = Issue.objects.order_by('created_at')

    return render(request, 'issues.html', {'issues': issues})
