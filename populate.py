import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE','StudentCRUDCBVProject.settings')
import django
django.setup()

from MyApps1.models import *
from faker import Faker
from random import *
faker=Faker()
departments = [
    "Mechanical Engineering (ME)",
    "Civil Engineering (CE)",
    "Electrical Engineering (EE)",
    "Computer Engineering (CSE)",
    "Chemical Engineering (CHE)",
    "Biomedical Engineering (BME)",
    "Aerospace Engineering (AE)",
    "Environmental Engineering (EnvE)",
    "Industrial Engineering (IE)",
    "Materials Science and Engineering (MSE)",
    "Automotive Engineering (AutoE)",
    "Petroleum Engineering (PE)",
    "Mechatronics Engineering (MTE)",
    "Software Engineering (SE)",
    "Telecommunications Engineering (TE)",
    "Structural Engineering (StrE)",
    "Marine Engineering (MarE)",
    "Robotics Engineering (RobE)",
    "Mining Engineering (MinE)",
    "Nuclear Engineering (NE)"
]

def populate(n):
    for i in range(n):
        frollno=randint(1000,1999)
        fname=faker.name()
        fdept=faker.random.choice(departments)
        fmarks=randint(35,99)

        stud_record=Students.objects.get_or_create(rollno=frollno,name=fname,dept=fdept,marks=fmarks)
        print(stud_record)
populate(10)
