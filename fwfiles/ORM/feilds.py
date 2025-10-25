from sqlalchemy import Column, Integer, String, Float, Boolean, Text, Date, DateTime, Time
from sqlalchemy.dialects.mysql import LONGTEXT
from datetime import datetime


def IntegerField(primary_key=False, null=False, increment=False):
    return Column(Integer, primary_key=primary_key, nullable=null,autoincrement=increment)

def CharField(max_length=255, null=False):
    return Column(String(max_length), nullable=null)

def FloatField(null=False):
    return Column(Float, nullable=null)

def BooleanField(default=False, null=False):
    return Column(Boolean, default=default, nullable=null)

def TextField(long=False, null=False):
    return Column(LONGTEXT if long else Text, nullable=null)

def FileField(max_length=255, null=False): 
    return Column(String(max_length), nullable=null)

def DateField(auto_now=False, auto_now_add=False, null=False):
    default = None
    if auto_now or auto_now_add:
        default = datetime.utcnow().date
    return Column(Date, default=default, nullable=null)

def DateTimeField(auto_now=False, auto_now_add=False, null=False):
    default = None
    if auto_now or auto_now_add:
        default = datetime.utcnow
    return Column(DateTime, default=default, nullable=null)

def TimeField(auto_now=False, auto_now_add=False, null=False):
    default = None
    if auto_now or auto_now_add:
        default = datetime.utcnow().time
    return Column(Time, default=default, nullable=null)
