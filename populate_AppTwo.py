import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Group_2.settings')
import django
django.setup()

#FAKER POP SCRIP

import random
from AppTwo.models import AccessRecord,Topic,Webpage
from faker import Faker

Fakegen= Faker()
topics = ['Search','Social','Maketplace','News','Gane']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the toppic for the entry
        top=add_topic()
        
        # create the fake data for that entry
        fake_url = Fakegen.url()
        fake_date = Fakegen.date()
        fake_name = Fakegen.name()

        # create the new webpage entry
        # webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        webpg = Webpage.objects.get_or_create(category=top, url=fake_url, name=fake_name)[0]


        #create a fake access record for that webpage 
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__=="__main__":
    print("population script!")
    populate(20)
    print("population complete!")



