from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test
from .models import Quiz, Answer, Result, ResultAnswers
from main.models import UserDocuments


def status_check(user):
    user_documents = UserDocuments.objects.get(user=user)
    status = False
    if user_documents.status == 'approved':
        status = True
    return status


class QuizListView(ListView):
    model = Quiz
    template_name = "exam/main-quiz.html"


def quiz_view(request, pk):
    if not status_check(request.user):
        return redirect('/home')
    quiz = Quiz.objects.get(pk=pk)
    context = {"quiz": quiz, "user": request.user.is_authenticated,}
    
    if request.method == 'POST':
        score = 0
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        for k, v in data_.items():
            question = quiz.questions.get(text=k)
            count = 0
            correct_answers = question.answers.filter(is_correct=True)
            if len(correct_answers) == len(v):
                for i in v:
                    for correct in correct_answers:
                        if question.answers.get(text=i) == correct:
                            count += 1
                if count == len(correct_answers):
                    score += question.score
            else:
                continue
        try:
            Result.objects.get(quiz=quiz, user=request.user)
            context['result_message_error'] = 'Вы уже проходили этот экзамен'
            return render(request, 'exam/quiz.html', context=context)
        except:
            result = Result.objects.create(course=quiz.course, quiz=quiz, user=request.user, status='completed', score=score)
            ResultAnswers.objects.create(result=result, answer_dict=data_)
            context['result'] = result
            context['result_message'] = 'Экзамен пройден. Вы можете посмотреть результаты'
            return render(request, 'exam/quiz.html', context=context)

    for question in quiz.questions.all():
        if question.correct_count != None:
            break
        question.correct_count = 0
        for answer in question.answers.all():
            if answer.is_correct:
                question.correct_count += 1
                question.save()
    try:
        context['result'] = quiz.results.get(user=request.user)
    except:
        context['result'] = None

    return render(request, 'exam/quiz.html', context=context)


def quiz_results(request, pk):
    if not status_check(request.user):
        return redirect('/home')
    quiz = Quiz.objects.get(pk=pk)
    result = Result.objects.get(quiz=quiz, user=request.user)
    result_answers = ResultAnswers.objects.get(result=result)
    max_score = 0
    for question in quiz.questions.all():
        max_score += question.score
    # ResultAnswers.objects.create(result=result, answer_dict={"1 + 1": "2", "2 + 2": "2", "x2 - 3x - 4 = 0": ["-4", "1", "8"]})
    # result_answers = ResultAnswers.objects.get(result=result, answer_dict={"1 + 1": "2", "2 + 2": "2", "x2 - 3x - 4 = 0": ["-4", "1", "8"]})
    return render(request, 'exam/quiz_results.html', {"quiz": quiz, "result": result, "result_answers": result_answers, "max_score": max_score, })


# def quiz_data_view(request, pk):
#     quiz = Quiz.objects.get(pk=pk)
#     questions = []
#     for q in quiz.get_questions():
#         answers = []
#         for a in q.get_answers():
#             answers.append(a.text)
#         questions.append({str(q): answers})
#     return JsonResponse({
#         'data': questions,
#         'time': quiz.time,
#     })


# def save_quiz_view(request, pk):
#     if request.headers.get('x-requested-with') == 'XMLHttpRequest':
#         quiz = Quiz.objects.get(pk=pk)
#         score = 0
#         data = request.POST
#         print(data)
        # for item in data:
        #     question = quiz.questions.get(item[''])
        #     answer = question.answers.get(text=answer)
        #     if answer.is_correct == True:
        #         score += question.score

        # data = request.POST
        # data_ = dict(data.lists())
        # data_.pop('csrfmiddlewaretoken')

        # quiz = Quiz.objects.get(pk=pk)
        # query_questions = list(quiz.get_questions())
        # questions = []
        # for question in query_questions:
        #     questions.append(question)

        # user = request.user
        # score = 0
        # multiplier = 100 / quiz.number_of_questions
        # results = []
        # correct_answer = None

        # for q in questions:
        #     a_selected = request.POST.get(q.text)

        #     if a_selected != "":
        #         question_answers = Answer.objects.filter(question=q)
        #         for a in question_answers:
        #             if a_selected == a.text:
        #                 if a.is_correct:
        #                     score += 1
        #                     correct_answer = a.text
        #             else:
        #                 if a.is_correct:
        #                     correct_answer = a.text
        #         results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
        #     else:
        #         results.append({str(q): 'not_answered'})

        # score_ = round(score * multiplier)
        # Result.objects.create(quiz=quiz, user=user, score=score_)

        # if score_ >= quiz.required_score_to_pass:
        #     return JsonResponse({'passed': True, 'score': score_, 'results': results})
        # else:
        #     return JsonResponse({'passed': False, 'score': score_, 'results': results})

