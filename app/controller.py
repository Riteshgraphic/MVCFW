from .views import index, masters, login, registration, classes, subject,  sessions, exam, fees, assignsubject, assignclass, institute, sregistration, studentdetails
from fwfiles.protocols import request
from .models import User


def start(req):
    return index.index


def master(req):
    return masters.master


def loginpage(req):
    msg=""
    if req.method == "POST":
        username=req.POST.get("username")
        password=req.POST.get("password")
        if username and password:
            db=User(name=username,password=password,status=1)
            db.save()
            msg="data saved successfully"
        else:
            msg="data is not saved"
        
    data={"data":User.all(),
            "msg":msg}
    return login.login, data
    



def classmaster(req):
    return classes.Classes

def subjectmaster(req):
    return subject.subjects

def sessionmaster(req):
    return sessions.sessionss

def exammaster(req):
    return exam.exams

def feesmaster(req):
    return fees.feeses

def assignsub(req):
    return assignsubject.assignsubs

def assigncls(req):
    return assignclass.assignclasses

def institutemaster(req):
    return institute.registration

def seniorRegistration(req):
    return sregistration.registration

def register(req):
    return registration.registration
    
def Studentdetails(req):
    return studentdetails.dtl
    

