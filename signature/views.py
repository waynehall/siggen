from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignatureForm
from .models import EmployeeInfo


def index(request):
    return HttpResponse ("Hi this is the gen page")

# Create your views here.
def create(request):
    if request.method =='POST':
        form = SignatureForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return redirect('SigView', pk=instance.pk)
    else:
        form = SignatureForm
    return render(request, 'signature/create.html', {'form':form})


def SigView(request, pk):
    employee = get_object_or_404(EmployeeInfo, pk=pk)
    return render (request, 'signature/detail.html', {'employee': employee})