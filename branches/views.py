from django.shortcuts import render
from .models import Branch

def branches_list(request):
    branches = Branch.objects.all()
    return render(request, 'branches/branches_list.html', {'branches': branches})


