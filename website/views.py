from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import signupform ,AddRecordForm
from .models import Record

def home(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'you have been loged in')
            return redirect('home')
        else:
            messages.success(request,'there was an error please try again')
            return redirect('home')
    else:
        record=Record.objects.all()
        ctx={'records':record}
        return render(request,'home.html',ctx)
def logout_user(request):
    logout(request)
    messages.success(request, 'you have been loged out')
    return redirect('home')
from django.shortcuts import render, redirect
from .forms import signupform


def register_user(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
        else:
            ctx = {'form': form}
            return render(request, 'register.html', ctx)
    else:
        form = signupform()         # empty form when user visits the page
        ctx = {'form': form}
        return render(request, 'register.html', ctx)
@login_required(login_url='/login')   
def record(request,pk):
    record=get_object_or_404(Record,id=pk)
    ctx={'record':record}
    return render(request,'record.html',ctx)


@login_required(login_url='/login')   
def delete_record(request,pk):
    record=get_object_or_404(Record,id=pk)
    record.delete()
    return redirect('home')


@login_required(login_url='/login')   
def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return render(request,'add_record.html',{'form':form})

@login_required(login_url='/login')   
def update_record(request, pk):
    record = get_object_or_404(Record, id=pk)

    if request.method == 'POST':
        form = AddRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddRecordForm(instance=record)

    return render(request, 'update_record.html', {'form': form})



    

