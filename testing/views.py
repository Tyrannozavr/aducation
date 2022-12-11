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


def test(request, pk):
    context = {}
    testing = Testing.objects.prefetch_related('questions__variants').get(id=pk)
    question_id = Attempts.objects.filter(answer=None).first().question_id
    # question = testing.questions.first()
    question = testing.questions.get(id=question_id)
    variants = question.variants.all()
    context['question'] = question
    context['answers'] = variants
    if len(Attempts.objects.filter(user_id=request.user.id, testing_id=pk)) == 0:
        for question in testing.questions.all():
            Attempts.objects.create(user_id=request.user.id, testing_id=pk, question_id=question.id)
    if request.POST:
        number_question = int(request.POST.get('number'))
        # attempt = Attempts.objects.create(user_id=request.user.id, testing_id=pk, question_id=number_question)
        # print(number_question)
        attempt = Attempts.objects.get(user_id=request.user.id, testing_id=pk, question_id=number_question)
        # print(Attempts.objects.filter(answer=None))

        answer = [variant.id for variant in variants if request.POST.get(str(variant.id))]
        attempt.answer.add(*answer)
    return render(request, 'testing/passing.html', context=context)
