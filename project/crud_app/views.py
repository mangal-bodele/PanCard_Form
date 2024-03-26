from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PanCardForm
from .models import PanCard

@login_required(login_url='login_url')
def create_pan(request):
    template_name = 'crud_app/create.html'
    form = PanCardForm()
    if request.method == "POST":
        form = PanCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)
@login_required(login_url='login_url')
def show_pan(request):
    template_name = 'crud_app/show.html'
    pancards = PanCard.objects.all()
    context = {'pancards': pancards}
    return render(request, template_name, context)


def update_pan(request,pk):
    template_name = 'crud_app/create.html'
    obj=PanCard.objects.get(id=pk)
    form = PanCardForm(instance=obj)
    if request.method == "POST":
        form = PanCardForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def delete_pan(request,pk):
    template_name = 'crud_app/confirm.html'
    obj = PanCard.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
    return render(request, template_name)

