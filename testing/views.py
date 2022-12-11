from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Testing, Attempts


# def index(request):
#     return render(request, 'testing/testing_list.html')

class TestingListView(ListView):
    model = Testing

    def get_queryset(self):
        return Testing.objects.prefetch_related('statistic_set').all()


class TestingDetailView(DetailView):
    model = Testing


def get_question(pk, user):
    question = Attempts.objects.filter(answer=None).first().question
    return question


def creating_attempt(user, testing):
    for question in testing.questions.all():
        Attempts.objects.create(user_id=user.id, testing_id=testing.id, question_id=question.id)


def test(request, pk):
    context = {}
    testing = Testing.objects.prefetch_related('questions__variants').get(id=pk)
    if len(Attempts.objects.filter(user_id=request.user.id, testing_id=pk)) == 0:
        creating_attempt(request.user, testing)
    question = get_question(pk, request.user)
    variants = question.variants.all()
    if request.POST:
        number_question = int(request.POST.get('number'))
        attempt = Attempts.objects.get(user_id=request.user.id, testing_id=pk, question_id=number_question)
        answer = [variant.id for variant in variants if request.POST.get(str(variant.id))]
        attempt.answer.add(*answer)

    # question_id = Attempts.objects.filter(answer=None).first().question_id
    # question = testing.questions.get(id=question_id)

    # print(question == get_question(pk, request.user))
    question = get_question(pk, request.user)
    context['question'] = question
    context['answers'] = question.variants.all()

    return render(request, 'testing/passing.html', context=context)
#
# def test(request, pk):
#     context = {}
#     testing = Testing.objects.prefetch_related('questions__variants').get(id=pk)
#     if len(Attempts.objects.filter(user_id=request.user.id, testing_id=pk)) == 0:
#         creating_attempt(request.user, testing)
#     if request.POST:
#         number_question = int(request.POST.get('number'))
#         attempt = Attempts.objects.get(user_id=request.user.id, testing_id=pk, question_id=number_question)
#         answer = [variant.id for variant in variants if request.POST.get(str(variant.id))]
#         attempt.answer.add(*answer)
#     question = get_question(pk, request.user)
#     variants = question.variants.all()
#     # question_id = Attempts.objects.filter(answer=None).first().question_id
#     # question = testing.questions.get(id=question_id)
#
#     # print(question == get_question(pk, request.user))
#     context['question'] = question
#     context['answers'] = variants
#
#     return render(request, 'testing/passing.html', context=context)
