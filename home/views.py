from django.shortcuts import render
from home.models import users
from django.http import HttpResponse
from django.shortcuts import render_to_response

def homePageView(request):
    return render(request,'base.html')

def registerPageView(request):
    return render(request,'RegisterLoginTemplates/Register.html')

def loginView(request):
    return render(request,'RegisterLoginTemplates/login.html')

def register(request):
    iserror = False
    userdata = {}
    if request.method == "POST":
        for key,value in request.POST.items():
            value.strip()
            if value in "invalidalreadypresentRequired":
                iserror = True
                userdata[key] = 'restricted' 
            if value != "":
                if key == 'mobileno':
                    if len(value) < 10 or len(value)>10 or value.isdecimal() == False:
                        iserror = True
                        userdata[key] = 'invalid'                        
                    else:
                        temp = users.objects.filter(mobileno = value)
                        if len(temp) > 0:
                            iserror = True
                            userdata[key] = 'alreadypresent'
                        else:
                            userdata[key] = value
                elif key == 'email':
                    temp = users.objects.filter(email = value)
                    if len(temp) > 0:
                        iserror = True
                        userdata[key] = 'alreadypresent'
                    else:
                        userdata[key] = value
                else:
                    userdata[key] = value
            else:
                iserror = True
                temp = {key :f'Required'}
                userdata.update(temp)
        if userdata['password'] != userdata['repassword']:
            iserror = True
            temp = {'repassword':'invalid'}
            userdata.update(temp)
        if iserror:
            print(userdata)
            return render(request,'RegisterLoginTemplates/Register.html',userdata)
        else:
            obj = users(name = userdata['fname'].title(),gender = userdata['gender'],mobileno = userdata['mobileno'],email = userdata['email'],password = userdata['password'])
            obj.save()
            return render(request,'RegisterLoginTemplates/login.html',{"status":"saveuser","email":userdata['email']})
    else:
        return render(request,'RegisterLoginTemplates/login.html')

def loginprocess(request):
    iserror = False
    userdata = {}
    usr = None
    if request.method == "POST":
        for key,value in request.POST.items():
            value.strip()
            if value != "":
                userdata[key] = value
            else:
                iserror = True
                temp = {key :f'Required'}
                userdata.update(temp)
        if userdata['userid'] != 'Required' and userdata['password'] != 'Required':
            temp = users.objects.filter(email = userdata['userid'],password = userdata['password'] )
            if len(temp) > 0:
                userdata['msg'] = 'valid'
            else:
                temp = users.objects.filter(mobileno = userdata['userid'],password = userdata['password'] )
                if len(temp)>0:
                    userdata['msg'] = 'valid'
                else:
                    iserror = True
                    userdata['msg'] = "invalid"
        if iserror:
            print(userdata)
            return render(request,'RegisterLoginTemplates/login.html',userdata)
        else:
            return render(request,'dashboard/dashboard.html')
    else:
        return render(request,'RegisterLoginTemplates/login.html')


        

