from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Testing, Attempts, Statistic


# def index(request):
#     return render(request, 'testing/testing_list.html')

class TestingListView(ListView):
    model = Testing

    def get_queryset(self):
        return Testing.objects.prefetch_related('statistic_set').all()


class TestingDetailView(DetailView):
    model = Testing


def get_question(pk, user):
    # if len(Attempts.objects.filter(user=user, testing_id=pk, answer=None)) == 0:
    #     return redirect('./statistic')
    # print('1111111')
    question = Attempts.objects.filter(answer=None).first().question
    # print('222222')
    return question


def creating_attempt(user, testing):
    for question in testing.questions.all():
        Attempts.objects.create(user_id=user.id, testing_id=testing.id, question_id=question.id)


def test(request, pk):
    context = {}
    testing = Testing.objects.prefetch_related('questions__variants').get(id=pk)
    if len(Attempts.objects.filter(user_id=request.user.id, testing_id=pk)) == 0:
        creating_attempt(request.user, testing)
    elif len(Attempts.objects.filter(user_id=request.user.id, testing_id=pk, answer=None)) == 0:
        return redirect('./statistic')
    question = get_question(pk, request.user)
    variants = question.variants.all()
    if request.POST:
        number_question = int(request.POST.get('number'))
        attempt = Attempts.objects.get(user_id=request.user.id, testing_id=pk, question_id=number_question)
        answer = [variant.id for variant in variants if request.POST.get(str(variant.id))]
        attempt.answer.add(*answer)
    if len(Attempts.objects.filter(user_id=request.user.id, testing_id=pk, answer=None)) == 0:
        return redirect('./statistic')
    question = get_question(pk, request.user)
    context['question'] = question
    context['answers'] = question.variants.all()
    return render(request, 'testing/passing.html', context=context)


def statistic(request, pk):
    try:
        statistic_obj = Statistic.objects.get(user=request.user, testing_id=pk)
        return render(request, 'testing/statistic.html', {'statistic': statistic_obj})
        # print('hello', statistic)
    except Statistic.DoesNotExist:
        attempt = Attempts.objects.filter(user=request.user, testing_id=pk)
        correct = [(a[0] == b[0]) for a, b in zip([i.answer.all() for i in attempt], [i.question.correct.all() for i in attempt])]
        # percent = (sum(correct) / len(correct)) * 100
        count = sum(correct)
        Statistic.objects.create(user=request.user, testing_id=pk, correct=count)
        statistic(request, pk)

