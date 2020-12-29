from django.shortcuts import render,HttpResponse,redirect
from django.http import *
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from onlineapp.models import addp
# Create your views here.
def index(request):
    logout(request)
    usernames = "student"
    passwords = "student"
    usernamet = "teacher"
    passwordt = "teacher"
    if request.POST:
        username = request.POST['name']
        password = request.POST['psww']
        position = request.POST['torst']
        if(position == "Student" and usernames==username and passwords==password):
            return redirect('mains')
        elif(position=='Teacher' and usernamet==username and passwordt==password):
            return redirect('maint')
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request,'login.html')
    #return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('home')

def mains(request):
    tests= addp.objects.all()
    context={"b":[]}
    for i in tests:
        context["b"].append(i.subject)
    return render(request, 'mains.html',context)

def maint(request):
    tests= addp.objects.all()
    context={"b":[]}
    for i in tests:
        context["b"].append(i.subject)
    print(context)
    return render(request, 'maint.html',context)

def addpapers(request):
    print("hiiii")
    if request.method == "POST":
        #print("hiiiiiiiiiiiii")
        subject = request.POST.get('SUBJECT NAME')
        #print(subject)
        q1=request.POST.get('Q1')
        q1op1=request.POST.get('Q1OP1')
        q1op2=request.POST.get('Q1OP2')
        q1op3=request.POST.get('Q1OP3')
        q1op4=request.POST.get('Q1OP4')
        q1correctoption=int(request.POST.get('Q1 CORRECT OPTION'))

        q2=request.POST.get('Q2')
        q2op1=request.POST.get('Q2OP1')
        q2op2=request.POST.get('Q2OP2')
        q2op3=request.POST.get('Q2OP3')
        q2op4=request.POST.get('Q2OP4')
        q2correctoption=int(request.POST.get('Q2 CORRECT OPTION'))
        
        q3=request.POST.get('Q3')
        q3op1=request.POST.get('Q3OP1')
        q3op2=request.POST.get('Q3OP2')
        q3op3=request.POST.get('Q3OP3')
        q3op4=request.POST.get('Q3OP4')
        q3correctoption=int(request.POST.get('Q3 CORRECT OPTION'))
        
        q4=request.POST.get('Q4')
        q4op1=request.POST.get('Q4OP1')
        q4op2=request.POST.get('Q4OP2')
        q4op3=request.POST.get('Q4OP3')
        q4op4=request.POST.get('Q4OP4')
        q4correctoption=int(request.POST.get('Q4 CORRECT OPTION'))

        q5=request.POST.get('Q5')
        q5op1=request.POST.get('Q5OP1')
        q5op2=request.POST.get('Q5OP2')
        q5op3=request.POST.get('Q5OP3')
        q5op4=request.POST.get('Q5OP4')
        q5correctoption=int(request.POST.get('Q5 CORRECT OPTION'))

        q6=request.POST.get('Q6')
        q6op1=request.POST.get('Q6OP1')
        q6op2=request.POST.get('Q6OP2')
        q6op3=request.POST.get('Q6OP3')
        q6op4=request.POST.get('Q6OP4')
        q6correctoption=int(request.POST.get('Q6 CORRECT OPTION'))

        q7=request.POST.get('Q7')
        q7op1=request.POST.get('Q7OP1')
        q7op2=request.POST.get('Q7OP2')
        q7op3=request.POST.get('Q7OP3')
        q7op4=request.POST.get('Q7OP4')
        q7correctoption=int(request.POST.get('Q7 CORRECT OPTION'))

        q8=request.POST.get('Q8')
        q8op1=request.POST.get('Q8OP1')
        q8op2=request.POST.get('Q8OP2')
        q8op3=request.POST.get('Q8OP3')
        q8op4=request.POST.get('Q8OP4')
        q8correctoption=int(request.POST.get('Q8 CORRECT OPTION'))

        q9=request.POST.get('Q9')
        q9op1=request.POST.get('Q9OP1')
        q9op2=request.POST.get('Q9OP2')
        q9op3=request.POST.get('Q9OP3')
        q9op4=request.POST.get('Q9OP4')
        q9correctoption=int(request.POST.get('Q9 CORRECT OPTION'))

        q10=request.POST.get('Q10')
        q0op1=request.POST.get('Q10OP1')
        q10op2=request.POST.get('Q10OP2')
        q10op3=request.POST.get('Q10OP3')
        q10op4=request.POST.get('Q10OP4')
        q10correctoption=int(request.POST.get('Q10 CORRECT OPTION'))

        Addp = addp(subject=subject,q1=q1,q1op1=q1op1,q1op2=q1op2,q1op3=q1op3,q1op4=q1op4,q1correctoption=q1correctoption,q2=q2,q2op1=q2op1,q2op2=q2op2,q2op3=q2op3,q2op4=q2op4,q2correctoption=q2correctoption,q3=q3,q3op1=q3op1,q3op2=q3op2,q3op3=q3op3,q3op4=q3op4,q3correctoption=q3correctoption,q4=q4,q4op1=q4op1,q4op2=q4op2,q4op3=q4op3,q4op4=q4op4,q4correctoption=q4correctoption,q5=q5,q5op1=q5op1,q5op2=q5op2,q5op3=q5op3,q5op4=q5op4,q5correctoption=q5correctoption,q6=q6,q6op1=q6op1,q6op2=q6op2,q6op3=q6op3,q6op4=q6op4,q6correctoption=q6correctoption,q7=q7,q7op1=q7op1,q7op2=q7op2,q7op3=q7op3,q7op4=q7op4,q7correctoption=q7correctoption,q8=q8,q8op1=q8op1,q8op2=q8op2,q8op3=q8op3,q8op4=q8op4,q8correctoption=q8correctoption,q9=q9,q9op1=q9op1,q9op2=q9op2,q9op3=q9op3,q9op4=q9op4,q9correctoption=q9correctoption,q10=q10,q0op1=q0op1,q10op2=q10op2,q10op3=q10op3,q10op4=q10op4,q10correctoption=q10correctoption)
        Addp.save()
        messages.info(request, 'Paper added successfully!')
    return render(request,'addp.html')  

def checkmark(request):
    return render(request,'checkm.html')


area=""
    

def taketest(request):
    test=request.POST.get('test')
    global area
    area=test
    #print(area)
    tests= addp.objects.all()
    #print(tests)
    context={"l1":[]}
    for i in tests:
        print(i.subject)
        if(test==i.subject):
            context["l1"].append(i.q1)
            context["l1"].append(i.q1op1)
            context["l1"].append(i.q1op2)
            context["l1"].append(i.q1op3)
            context["l1"].append(i.q1op4)
            context["l1"].append(i.q1correctoption)
        print(context)
        #print(context)
    return render(request,'taketest.html',context)


def question2(request):
    global area
    test=area
    print(test)
    tests= addp.objects.all()
    context={"l2":[]}
    for i in tests:
        if(test==i.subject):
            context["l2"].append(i.q2)
            context["l2"].append(i.q2op1)
            context["l2"].append(i.q2op2)
            context["l2"].append(i.q2op3)
            context["l2"].append(i.q2op4)
            context["l2"].append(i.q2correctoption)
    #print(context,test)
    return render(request,'question2.html',context) 


def question3(request):
    global area
    test=area
    print(test)
    tests= addp.objects.all()
    context={"l3":[]}
    for i in tests:
        if(test==i.subject):
            context["l3"].append(i.q3)
            context["l3"].append(i.q3op1)
            context["l3"].append(i.q3op2)
            context["l3"].append(i.q3op3)
            context["l3"].append(i.q3op4)
            context["l3"].append(i.q3correctoption)
    #print(context,test)
    return render(request,'question3.html',context) 

def question4(request):
    global area
    test=area
    print(test)
    tests= addp.objects.all()
    context={"l4":[]}
    for i in tests:
        if(test==i.subject):
            context["l4"].append(i.q4)
            context["l4"].append(i.q4op1)
            context["l4"].append(i.q4op2)
            context["l4"].append(i.q4op3)
            context["l4"].append(i.q4op4)
            context["l4"].append(i.q4correctoption)
    #print(context,test)
    return render(request,'question4.html',context) 

def question5(request):
    global area
    test=area
    print(test)
    tests= addp.objects.all()
    context={"l5":[]}
    for i in tests:
        if(test==i.subject):
            context["l5"].append(i.q5)
            context["l5"].append(i.q5op1)
            context["l5"].append(i.q5op2)
            context["l5"].append(i.q5op3)
            context["l5"].append(i.q5op4)
            context["l5"].append(i.q5correctoption)
    #print(context,test)
    return render(request,'question5.html',context) 


def question6(request):
    global area
    test=area
    print(test)
    tests= addp.objects.all()
    context={"l6":[]}
    for i in tests:
        if(test==i.subject):
            context["l6"].append(i.q6)
            context["l6"].append(i.q6op1)
            context["l6"].append(i.q6op2)
            context["l6"].append(i.q6op3)
            context["l6"].append(i.q6op4)
            context["l6"].append(i.q6correctoption)
    #print(context,test)
    return render(request,'question6.html',context) 


def question7(request):
    global area
    test=area
    print(test)
    tests= addp.objects.all()
    context={"l7":[]}
    for i in tests:
        if(test==i.subject):
            context["l7"].append(i.q7)
            context["l7"].append(i.q7op1)
            context["l7"].append(i.q7op2)
            context["l7"].append(i.q7op3)
            context["l7"].append(i.q7op4)
            context["l7"].append(i.q7correctoption)
    #print(context,test)
    return render(request,'question7.html',context) 


def question8(request):
    global area
    test=area
    print(test)
    tests= addp.objects.all()
    context={"l8":[]}
    for i in tests:
        if(test==i.subject):
            context["l8"].append(i.q8)
            context["l8"].append(i.q8op1)
            context["l8"].append(i.q8op2)
            context["l8"].append(i.q8op3)
            context["l8"].append(i.q8op4)
            context["l8"].append(i.q8correctoption)
    #print(context,test)
    return render(request,'question8.html',context) 


def question9(request):
    global area
    test=area
    print(test)
    tests= addp.objects.all()
    context={"l9":[]}
    for i in tests:
        if(test==i.subject):
            context["l9"].append(i.q9)
            context["l9"].append(i.q9op1)
            context["l9"].append(i.q9op2)
            context["l9"].append(i.q9op3)
            context["l9"].append(i.q9op4)
            context["l9"].append(i.q9correctoption)
    #print(context,test)
    return render(request,'question9.html',context) 


def question10(request):
    global area
    test=area
    print(test)
    tests= addp.objects.all()
    context={"l10":[]}
    for i in tests:
        if(test==i.subject):
            context["l10"].append(i.q10)
            context["l10"].append(i.q0op1)
            context["l10"].append(i.q10op2)
            context["l10"].append(i.q10op3)
            context["l10"].append(i.q10op4)
            context["l10"].append(i.q10correctoption)
    #print(context,test)
    return render(request,'question10.html',context) 


def finalscore(request):
    global area
    test=area
    print(test)
    context={}
    context["sub"]=area
    print(context)
    return render(request,'finalscore.html',context)

