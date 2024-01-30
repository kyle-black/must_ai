from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from .models import Question



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


def securitiesdashboard(request, data):
    return HttpResponse("Must_ai Securities" % data )

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