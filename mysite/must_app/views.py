from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from .models import Question
import json

import redis


def data_pull():
    r = redis.Redis(
    host='redis-17905.c326.us-east-1-3.ec2.cloud.redislabs.com',
    port=17905,
    password='zHeoOL4uqpzaxTC7YgtuWvq4HRNSsoD0')

    AUDUSD = r.xrange("security:AUDUSD")

    AUDUSD_dict ={}

    for i in AUDUSD:
      unix = int(i[0].decode('utf-8').replace('-0', ''))
      data = {k.decode('utf-8'): v.decode('utf-8') for k, v in i[1].items()}
      AUDUSD_dict[unix] = data

    #print(AUDUSD_dict)
        
      

    

    return AUDUSD_dict



#import redis

'''
def redis_pull():
    r = redis.Redis(
    host='redis-17905.c326.us-east-1-3.ec2.cloud.redislabs.com',
    port=17905,
    password='zHeoOL4uqpzaxTC7YgtuWvq4HRNSsoD0')

    AUDUSD = r.xrange("security:AUDUSD")

    return AUDUSD
'''



def index(request):
    return HttpResponse("MUST_ai Landing Page.")

def signup(request):
    return HttpResponse("MUST_ai SignUp.")


def login(request):
    return HttpResponse("MUST_ai Login.")

def userhome(request):
    return HttpResponse("Must_ai User home page")

def paymentprocess(request):
    return HttpResponse("Must_ai Payment Process")


def securitiesdashboard(request):

    data_dict = data_pull()
    print(data_dict)

    return render(request, 'must_app/securitiesdashboard.html',{'data_dict':data_dict})
   # return HttpResponse("Must_ai Securities" % data )

def forexdashboard(request):
    return HttpResponse("Must_ai forex")

def metalsdashboard(request):
    return HttpResponse("Must_ai metals")

def energydashboard(request):
    return HttpResponse("Must_ai energy")

def securitydashboard(request):
    return HttpResponse("MUST AI security")





'''

def index(request):
    return HttpResponse("MUST_ai Landing Page.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
'''