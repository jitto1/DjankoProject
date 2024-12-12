from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Response, Survey
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Research Survey Tool!")


# View to list surveys
@login_required
def survey_list(request):
    surveys = Survey.objects.filter(user=request.user)  # Show surveys of the logged-in user
    return render(request, 'app/survey_list.html', {'surveys': surveys})

# View to create a new survey
@login_required
def survey_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Survey.objects.create(title=title, description=description, user=request.user)
        return redirect('survey_list')
    return render(request, 'app/survey_create.html')


from .models import Question

@login_required
def question_list(request, survey_id):
    survey = Survey.objects.get(id=survey_id, user=request.user)
    questions = Question.objects.filter(survey=survey)
    return render(request, 'app/question_list.html', {'survey': survey, 'questions': questions})


@login_required
def question_create(request, survey_id):
    survey = Survey.objects.get(id=survey_id, user=request.user)
    if request.method == 'POST':
        text = request.POST.get('text')
        Question.objects.create(text=text, survey=survey)
        return redirect('question_list', survey_id=survey.id)
    return render(request, 'app/question_create.html', {'survey': survey})


@login_required
def response_create(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    questions = Question.objects.filter(survey=survey)

    if request.method == 'POST':
        for question in questions:
            answer = request.POST.get(f'question_{question.id}')
            Response.objects.create(
                question=question, 
                user=request.user, 
                answer=answer
            )
        return redirect('survey_list')  # Redirect to survey list after submitting responses

    return render(request, 'app/response_create.html', {'survey': survey, 'questions': questions})


@login_required
def survey_results(request, survey_id):
    survey = Survey.objects.get(id=survey_id)
    questions = Question.objects.filter(survey=survey)
    results = []

    for question in questions:
        responses = Response.objects.filter(question=question)
        results.append({'question': question, 'responses': responses})

    return render(request, 'app/survey_results.html', {'survey': survey, 'results': results})


from django.contrib import messages

@login_required
def survey_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Survey.objects.create(title=title, description=description, user=request.user)
        messages.success(request, "Survey created successfully!")
        return redirect('survey_list')
    return render(request, 'app/survey_create.html')
