from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from .forms import *
from . import models
# Create your views here.
def home(request):
    form=RegistrationForm()
    if request.method=="POST":
         form=RegistrationForm(request.POST)
         if(form.is_valid()):
            name=request.POST['username']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            password=request.POST['password']
            myuser=User.objects.create_user(name,email,password)
            myuser.first_name= first_name
            myuser.last_name= last_name
            myuser.save()
            # mob_no=7000405307
            profileuser=Profile.objects.create(name=myuser)
            profileuser.save() 
            print(name,first_name,last_name,email,password)
            return redirect(signin)

    return render(request,"home.html",{'form':form})
def signin(request):
    form=LoginForm()
    if request.method=="POST":
            form=LoginForm(request.POST)
            name=request.POST['username']
            password=request.POST['password']
            print(name,password)
            user=User.objects.all()
            i=0
            for usr in user:
                if(str(usr)==str(name)):
                  valid_user= authenticate(username=name,password=password)  
                  if valid_user is not None:
                    login(request,valid_user)
                    fname=valid_user.first_name
                    c_user=str(request.user)
                    print(c_user)
                    return redirect(f'messenger/{c_user}')
            else:
             return render(request,'signin.html',{'form':form,'error':"Invalid credentials"})
    return render(request,'signin.html',{'form':form})
def messenger(request,username):
    users=User.objects.all()
    freind=Freinds.objects.filter(sender=request.user)
    # print(freind)
    receivers=[]
    for i in freind:
        receivers.append(i.receiver)
    a=[]
    for i in receivers:
        if i!=str(request.user):
         user1=User.objects.filter(username=i)
         a.append(user1)
    # print(username)
    # msgs=Message.objects.all()
    # print(msgs)
    # print(str(request.user),username)
    # print(username)
    msgs=Message.objects.filter(sender=str(request.user), receiver=username)|Message.objects.filter(sender=username,receiver=str(request.user))
    # print(msgs)
    return render(request,"messenger.html",{'a':a,'receiver':username,'display':msgs,'c_user':str(request.user)})
def signout(request):
    logout(request)
    return redirect(signin)
def profile(request):
    user=request.user
    user_p=Profile.objects.get(name=user)
    if request.method=="POST":
        mob=request.POST['mobile']
        status=request.POST['status']
        print(mob,status)
        user_p.mobile_no=mob
        user_p.status=status
    return render(request,"profile.html",{'user_p':user_p})
def requests(request):
    receive=request.user
    requests=Request.objects.filter(receiver=str(receive))
    return render(request,"requests.html",{'requests':requests})
def send(request,receiver):
    if request.method=="POST":
        msg=request.POST['message']
        usr=request.user
        if msg!='':
         msg1=Message.objects.create(msg=msg,sender=str(usr),receiver=receiver)
         msg1.save()
    return redirect(f"/messenger/{receiver}")
def accept(request,sender):
    user=User.objects.get(username=sender)
    requesst=Request.objects.get(sender=user,receiver=str(request.user))
    requesst.delete()
    Freinds.objects.create(sender=user,receiver=str(request.user)).save()
    Freinds.objects.create(sender=request.user,receiver=sender).save()
    return redirect(requests)
def makefreinds(request):
    sent_request=Request.objects.filter(sender=request.user)
    print(sent_request)
    list=[]
    for receivers in sent_request:
         list.append(receivers.receiver)
    print(list)
    users1=User.objects.filter(~Q(username=str(request.user)))
    list1=[]
    for i in users1:
        k=0
        for j in list:
            if str(i)==str(j):
                k=1
        if k==0:
          list1.append(i)
    print(list1)
    return render(request,"send_request.html",{'users':list1})
def send_request(request,receiver):
    make_request=Request.objects.create(sender=request.user,receiver=str(receiver))
    make_request.save()
    return redirect(makefreinds)