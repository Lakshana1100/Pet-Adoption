from django.shortcuts import render
from django.http import HttpResponse

from pet.models import daycareInsert
from pet.models import adoptInsert
from pet.models import fosterInsert
from pet.models import contactInsert
from django.contrib import messages

from pet.models import dogs


#from django.db import connection

from pet.models import daycareDisplay
import pyodbc as db

# Create your views here.

def one(request):
    return render(request,"onefile.html")

def two(request):
    return render(request,"twofile.html")

#def mainp(request):
    #return render(request,"home.html")

def steps(request):
    return render(request,"stepsToAdopt.html")

def lucy(request):
    result=dogs.objects.raw('select * from dogs where id=2')
    return render(request,'Lucy.html',{'dogs':result})

def mia(request):
    result=dogs.objects.raw('select * from dogs where id=3')
    return render(request,'Mia.html',{'dogs':result})

def lola(request):
    result=dogs.objects.raw('select * from dogs where id=4')
    return render(request,'Lola.html',{'dogs':result})

def harley(request):
    result=dogs.objects.raw('select * from dogs where id=5')
    return render(request,'Harley.html',{'dogs':result})

def snow(request):
    result=dogs.objects.raw('select * from dogs where id=6')
    return render(request,'Snow.html',{'dogs':result})

def newlitter(request):
    result=dogs.objects.raw('select * from dogs where id=7')
    return render(request,'NewLitter.html',{'dogs':result})

def buddy(request):
    result=dogs.objects.raw('select * from dogs where id=8')
    return render(request,'Buddy.html',{'dogs':result})

def sunny(request):
    result=dogs.objects.raw('select * from dogs where id=9')
    return render(request,'Sunny.html',{'dogs':result})

def bear(request):
    result=dogs.objects.raw('select * from dogs where id=10')
    return render(request,'Bear.html',{'dogs':result})

def PYH(request):
    return render(request,"PrepareYourHome.html")

def donate(request):
    return render(request,"Donate.html")

def newvolunteer(request):
    return render(request,"NewVolunteer.html")

def fosterawareness(request):
    return render(request,"FosterAwareness.html")

def daycare(request):
    return render(request,"DayCare.html")

def release(request):
    return render(request,"ReleaseOfOwn.html")

def why(request):
    return render(request,"WhyDogs&Life.html")

#def contactus(request):
    #return render(request,"ContactUs.html")

def formadopt(request):
    return render(request,"AppFormAdopt.html")

def formfoster(request):
    return render(request,"AppFormFoster.html")

def daycareslot(request):
    return render(request,"DaycareSlots.html")

#def formdaycare(request):
    #return render(request,"AppFormDaycare.html")

def insertDaycare(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('age') and request.POST.get('address') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('datedd')  and request.POST.get('datedd2'):
            saverecord=daycareInsert()
            saverecord.name=request.POST.get('name')
            saverecord.age=request.POST.get('age')
            saverecord.address=request.POST.get('address')
            saverecord.phone=request.POST.get('phone')
            saverecord.email=request.POST.get('email')
            saverecord.datedd=request.POST.get('datedd')
            saverecord.datedd2=request.POST.get('datedd2')
            saverecord.save()
            messages.success(request,'Record saved successfully.')
            return render(request,'AppFormDaycare.html')
    else:
            return render(request,'AppFormDaycare.html')

def displayDaycare(request):
    conn_str = (
        r'DRIVER={MySQL ODBC 8.0 ANSI Driver};'
        r'SERVER=localhost;'
        r'DATABASE=pet;'
        r'User =root;'
        r'Password=admin;'
        r'Trusted_Connection=yes;'
        )
    conn=db.connect(conn_str)
    cursor=conn.cursor()
    cursor.execute("select name,address,phone,email,datedd,datedd2 from daycare")
    result=cursor.fetchall()
    return render(request,'DaycareSlots.html',{'daycareDisplay':result})

def insertAdopt(request):
    if request.method=='POST':
        print(request.POST)
        if request.POST.get('name') and request.POST.get('age') and request.POST.get('address') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('selectdog'):
            saverecord=adoptInsert()
            saverecord.name=request.POST.get('name')
            saverecord.age=request.POST.get('age')
            saverecord.address=request.POST.get('address')
            saverecord.phone=request.POST.get('phone')
            saverecord.email=request.POST.get('email')
            saverecord.selectdog=request.POST.get('selectdog')
            saverecord.save()
            messages.success(request,'Record saved successfully.')
            return render(request,'AppFormAdopt.html')
    else:
            return render(request,'AppFormAdopt.html')


def insertFoster(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('age') and request.POST.get('address') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('selectdog'):
            saverecord=fosterInsert()
            saverecord.name=request.POST.get('name')
            saverecord.age=request.POST.get('age')
            saverecord.address=request.POST.get('address')
            saverecord.phone=request.POST.get('phone')
            saverecord.email=request.POST.get('email')
            saverecord.selectdog=request.POST.get('selectdog')
            saverecord.save()
            messages.success(request,'Record saved successfully.')
            return render(request,'AppFormFoster.html')
    else:
            return render(request,'AppFormFoster.html')

def insertContact(request):
    if request.method=='POST':
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('email') and request.POST.get('textbox'):
            saverecord=contactInsert()
            saverecord.fname=request.POST.get('fname')
            saverecord.lname=request.POST.get('lname')
            saverecord.email=request.POST.get('email')
            saverecord.textbox=request.POST.get('textbox')
            saverecord.save()
            messages.success(request,'Query sent.')
            return render(request,'ContactUs.html')
    else:
            return render(request,'ContactUs.html')


def adminDogs(request):
    result=dogs.objects.all()
    return render(request,'adminDogs.html',{'dogs':result})


def mainp(request):
    resultdisplay=dogs.objects.all()
    return render(request,'home.html',{'dogs':resultdisplay})








'''
cnxn = db.connect(conn_str)
cursor = cnxn.cursor()

cursor.execute("SELECT * FROM employees")
row = cursor.fetchone()
while row:
    print (row)
    row = cursor.fetchone()
'''
#cnxn = pyodbc.connect('DRIVER={ODBC Driver for MySQL};User ID=myuserid;Password=mypassword;Server=myserver;Database=mydatabase;Port=myport;String Types=Unicode')
#Server=LakshPC;Trusted_Connection=yes;
#conn=pyodbc.connect('Driver={ mysqlodbc };user=root;password=admin; Database=pet;')
'''
dbhost = "localhost" #'192.168.0.116:3306'
un = 'root'
up = 'admin'
dbname = 'pet'
port ='3306'
'''


