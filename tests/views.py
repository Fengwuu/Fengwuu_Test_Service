from django.contrib.auth.models import User
from django.core.cache import cache
from django.shortcuts import render
from django.views.generic import ListView
from .forms import *
from .models import *


def home(request):
    cache.clear()
    if request.user.is_authenticated:
        template = 'tests/home.html'
    else:
        template = 'tests/ask_for_login.html'  # User must be authenticated to be able to see tests

    context = {"questions": Question.objects.all(),
               'collections': Collection.objects.all(),
               'category': Category.objects.all()}

    return render(request, template, context, )


class TestsByCategory(ListView):
    model = Test
    template_name = 'tests/tests_by_category.html'
    context_object_name = 'test'

    def get_queryset(self):
        return Test.objects.filter(category_id=self.kwargs['category_id']).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def user_answer(request, question_number, test_id):
    form = TestUserAnswer()

    all_questions_in_test = Question.objects.all().filter(test_id=test_id)  # finding all questions in chosen test,
    # using ORM requests
    question_ids = list(all_questions_in_test.values_list('pk', flat=True))  # picking ids into one list to make test
    # completing process correctly

    question = Question.objects.get(pk=int(question_ids[question_number - 1]))

    finish = 0

    next_question = question_number + 1

    if question_number == 1:
        question_for_check_answers = Question.objects.get(pk=int(question_ids[question_number - 1]))
    else:
        question_for_check_answers = Question.objects.get(pk=int(question_ids[question_number - 2]))
        # fixing problem, where correct answer was picking for next question instead our

    correct_answer = list(question_for_check_answers.correct_answer.values_list('title'))
    correct_answer_list = list()

    for x in range(0, len(correct_answer)):
        correct_answer_list.append(correct_answer[x][0])
        # collecting all correct answers in 1 list, to make questions with multiple answers work correctly

    if int(question_ids[question_number - 1]) == question_ids[-1]:
        finish = 1

    answer_from_user = None
    if request.POST:
        answer_from_user = request.POST.getlist('choice')

    score = cache.get('score')

    last_question = Question.objects.get(pk=int(question_ids[-1]))  # Its need to make able to grade answer to last
    # question in test_result page, because after last question user is redirecting to results of the test

    if not score:
        score = 0

    if answer_from_user == correct_answer_list:
        score += 1
        cache.set('score', score, 60 * 30)
        # Calculating user score to make grade

    if finish == 1:  # preparing data to results of the test
        cache.set('score', score, 60 * 30)
        cache.set('test', Test.objects.get(pk=test_id), 60 * 30)
        cache.set('test_len', len(question_ids), 60 * 30)
        cache.set('answer_for_last_question', last_question.correct_answer.get(), 60 * 30)

    def get_queryset(self):
        return Test.objects.filter(question_pk=self.kwargs['question_pk']).select_related('question')

    return render(request, 'tests/testform.html', context={'form': form, 'question': question,
                                                           'next_question': next_question,
                                                           'finish': finish,
                                                           'test_id': test_id,
                                                           })


def test_result(request):
    score = cache.get('score')

    correct_answer = cache.get('answer_for_last_question')
    # back to 72 line about last question

    if request.POST:

        name = request.POST.getlist('choice')
        name = ''.join(name)

        if str(correct_answer) == name:
            score += 1
            # checking last question like previous

    test_len = int(cache.get('test_len'))
    percent = score / test_len * 100

    account = User.objects.get(username=request.user.username)
    if percent >= 60:
        test_title = cache.get('test')
        test = Test.objects.get(title=test_title.title)
        test_set = Test.objects.get(id=test.pk)

        account.userprofile.completed_tests.add(test_set.pk)
        account.save()

    context = {
        'score': score,
        'test': cache.get('test'),
        'percent': percent,
        'test_len': test_len,
    }

    return render(request, 'tests/test_result.html', context=context)
