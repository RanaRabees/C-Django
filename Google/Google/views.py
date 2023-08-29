

from os import remove
from django.http import HttpResponse
from django.shortcuts import render
from sympy import N
from instagram.models import CNIC
from . import views


def home(request):
   return render(request,'home.html')
    
 

def book(request):
    b=''
    if request.method == 'POST':
        name          = request.POST.get('name')
        father_name   = request.POST.get('father_name')
        gender        = request.POST.get('gender')
        country       = request.POST.get('country')
        date_birth    = request.POST.get('date_birth')
        data = CNIC( name=name,father_name=father_name, gender=gender, country=country ,date_birth=date_birth)
        data.save()
        b='your data has been sent sir you can go and check'
    return render(request,'book.html',{'b':b})

       



def about(request):    
    return render(request,'about.html') 
        
    
def text(request):
    Atext=request.POST.get('text','default')
    rpu=request.POST.get('rpu','off')
    upper=request.POST.get('upper','off')
    nl=request.POST.get('nl','off')  
    # print(rpu)
    # print(Atext)
    if rpu == "on" :
        # analyzed=Atext    
        punctuations = ''' ? ` , : , @  ; ,% ^ <<,,,>>>..!!!| “ ”, _ - ( ), { },[ ] ,  ,*, \\\::"""'  ~ , / , , #,$, &  ''' 
        analyzed=""
        for i in Atext:
            if i not in punctuations:
               analyzed=analyzed+i 
        data={'rpu': rpu , 'btext': analyzed }         
        return render(request,'text.html', data)
    elif(upper == "on") :
        punctuations = '''?`,:,@;,%^<<,,,>>>{..!!!|“”,_-(),,[],,*,\\\}::"""'~,/,,#,$,&''' 
        analyzed=""
        for i in Atext:
            if i not in punctuations:
               analyzed=analyzed + i.upper()                        
            data={'rpu': rpu , 'btext': analyzed }         
        return render(request,'text.html', data)
    
    elif(nl == "on") :               
        analyzed=""
        for i in Atext:
            if i != '\n' and i != '\r':
               analyzed=analyzed + i.upper() 
            #    analyzed=analyzed                       
            data={'rpu': rpu , 'btext': analyzed }         
        return render(request,'text.html', data)     
            
              
    else:
        return HttpResponse(" !!! oooo MENTAL MELTAL BHIA APP NE SUB KUCH KUTTAM KAR DIYA HE  HA HA HA HI HI HI !!! ")
                    
       



def index(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')



def base(request):
    return render(request,'base.html')

def harry(request):    
    return render(request,'harry.html') 
