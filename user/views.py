from django.shortcuts import render
from user.models import User
from django.views import View
from django.http import JsonResponse
# Create your views here.

class SignUpView(models.Model):
    def post(self,request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({'message' : 'Existing-Account'}, status = 401)
            if('@' in data['email']) and( len(data['password']) >= 5):
               User(
                   first_name = data['first_name'],
                   last_name = data['last_name'],
                   password = data['password']
               ).save()
               return JsonResponse({'message' : 'success'}, status = 200)
            return JsonResponse({'message' : 'Wrong_ERROR'}, status = 401)
        except KeyError:
            return JsonResponse({'message' :'KEY_ERROR'},status = 400)

class SignInView(models.Model):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email = data['email']).exists():
                user = User.objects.get(email = data['email'])
            if user.password == data['password']:
                return JsonResponse({'message' : 'success'}, status = 200)
            return JsonResponse({'message': ' 허락안함'},status = 401)
        except KeyError:
            return JsonResponse({'message' :'오타'}, status = 400)

