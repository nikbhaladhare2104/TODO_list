from .models import Question, Choice, Todo
from django.http import JsonResponse
from django.utils import timezone
from django.views import View
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class QuestionView(View):
    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:  # Check if 'id' is in the URL parameters
            try:
                question = Question.objects.get(id=kwargs['id'])
                choices = Choice.objects.filter(question_id=question.id)
                return JsonResponse({
                    'id': question.id,
                    'question_text': question.question_text,
                    'choices': list(choices.values())
                }, safe=False)
            except Question.DoesNotExist:
                return JsonResponse({'error': 'Question not found'}, status=404)
        #  Get all Questions with choices
        else:
            all_questions = Question.objects.all()
            full_list = []
            for question in all_questions:
                choices = Choice.objects.filter(question_id=question.id)
                full_list.append({'id': question.id, 'question_text': question.question_text, 'choices': list(choices.values()), 'published_date': question.pub_date})

            return JsonResponse(full_list, safe=False)


    def post(self, request):
        data = json.loads(request.body)  # Parse JSON body
        question = Question.objects.create(question_text=data['question_text'], pub_date=timezone.now())
        question.save()
        return JsonResponse({'id': question.id, 'question_text': question.question_text}, safe=False)


    def put(self, request):
        data = json.loads(request.body)  # Parse JSON body
        question = Question.objects.get(id=data['id'])
        question.question_text = data['question_text']
        question.save()
        return JsonResponse({'id': question.id, 'question_text': question.question_text}, safe=False)


    def delete(self, request):
        data = json.loads(request.body)  # Parse JSON body
        question = Question.objects.get(id=data['id'])
        question.delete()
        return JsonResponse({'id': question.id, 'question_text': question.question_text}, safe=False)



@method_decorator(csrf_exempt, name='dispatch')
class ChoiceView(View):
    def post(self, request):
        data = json.loads(request.body)  # Parse JSON body
        choice = Choice.objects.create(question_id=data['question_id'], choice_text=data['choice_text'], votes=data['votes'])
        choice.save()
        return JsonResponse({'id': choice.id, 'question_id': choice.question_id, 'choice_text': choice.choice_text}, safe=False)

    def put(self, request):
        data = json.loads(request.body)  # Parse JSON body
        choice = Choice.objects.get(id=data['id'])
        choice.choice_text = data['choice_text']
        choice.votes = data['votes']
        choice.save()
        return JsonResponse({'id': choice.id, 'question_id': choice.question_id, 'choice_text': choice.choice_text}, safe=False)


    def delete(self, request):
        data = json.loads(request.body)  # Parse JSON body
        choice = Choice.objects.get(id=data['id'])
        choice.delete()
        return JsonResponse({'id': choice.id, 'question_id': choice.question_id, 'choice_text': choice.choice_text}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class TodoView(View):