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
    # print(pk)
    # print(request.user)
    # attempt = Attempts()
    testing = Testing.objects.prefetch_related('questions__variants').get(id=pk)
    # print(test, test.__dict__)
    # print(test.questions.first().variants.all())
    question = testing.questions.first()
    variants = question.variants.all()
    context['question'] = question
    context['answers'] = variants
    if request.POST:
        number_question = int(request.POST.get('number'))
        print(number_question)
        attempt = Attempts.objects.create(user_id=request.user.id, testing_id=pk, question_id=number_question)
        answer = [variant.id for variant in variants if request.POST.get(str(variant.id))]
        attempt.answer.add(*answer)
        # print(answer)
    return render(request, 'testing/passing.html', context=context)
