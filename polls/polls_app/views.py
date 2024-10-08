from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

# Create your views here.
# def index(request):
#     all_questions = Question.objects.order_by("-pub_date")[:5]
#     output = ", ".join([q.question_text for q in all_questions])
#     template = loader.get_template("polls/index.html")
#     context = {"latest_question_list": all_questions}
#     # print(output) 
#     return HttpResponse(template.render(context, request))

def index(request):
    all_questions = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": all_questions}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        existing_question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": existing_question})

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
