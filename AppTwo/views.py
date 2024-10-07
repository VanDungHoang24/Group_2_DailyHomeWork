from django.shortcuts import render

from django.http import HttpResponse

from AppTwo.models import AccessRecord,Topic,Webpage

# Create your views here.


def index(request):

   Webpage_list = AccessRecord.objects.order_by('date')
   date_dict={'access_records': Webpage_list}
   return render(request,'index.html', context=date_dict)



   # my_dic = {'insert_me': 'Hello BeDauCoder'}
   # return render(request, 'index.html',context=my_dic)
   # return HttpResponse("Hello World")

def about(request):
   return render(request, 'about.html')

def help(request):
   my_dic3 = {'help_page_tag': 'Help Page tags'}
   return render(request, 'help.html', context=my_dic3)


def home(request):
   return render(request, 'home.html')