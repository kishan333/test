from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Question

# Create your views here.

def detail(request):

	if request.method == 'GET':
		print("inside get detail method")
	question_id = 1

	return HttpResponse({'question_id' : question_id})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
# Leave the rest of the views (detail, results, vote) unchanged