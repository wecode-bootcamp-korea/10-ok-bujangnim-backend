import json
import jwt
import bcrypt
from django.shortcuts import render
from .models import User
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.db import IntegrityError
from aesop_project.settings import SECRET_KEY
#from django.core.exceptions import ObjectDoesNotExist
class SignUpView(View):
    def post(self,request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({'message' : 'Existing-Account'}, status = 401)
            if('@' in data['email']) and( len(data['password']) >= 5 and):
                hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt())
                User(
                    email = data['email'],
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                    password = hashed_password.decode('utf-8')
                   # password = data['password']
                ).save()
                return JsonResponse({'message' : 'success'}, status = 200)
            return JsonResponse({'message' : 'Wrong_ERROR'}, status = 401)
        except KeyError:
            return JsonResponse({'message' :'KEY_ERROR'},status = 400)

# def login_decorator(func):
#     def wrapper(self, request, *args, **kwargs):
#         if "Authorization" not in request.headers:
#             return JsonResponse({'error_code' : 'Invalid_Login'}, status = 401)
#         encode_token = request.headers["Authorization"]

#         try:
#             data = jwt.decode(encode_token, SECRET_KEY, algorithm = 'HS256')
#             user = User.objects.get(id=data['id'])
#             request.user = user
#         except jwt.DecodeError:
#             return JsonResponse({'message' : "Invalid Token"}, status = 401)
#         except User.DoesNotExist:
#             return JsonResponse({'message' : "Not Exist User"},status = 401)
#         return func(self, request, *args, **kwargs)
#     return wrapper

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(email = data['email']).exists():
                user = User.objects.get(email = data['email'])
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    token = jwt.encode({'email':data['email']},SECRET_KEY , algorithm  = 'HS256')
                    token = token.decode('utf-8')
                    return JsonResponse({'token' : token}, status = 200)
                return JsonResponse({'message': ' 허락안함'},status = 401)
        except KeyError:
            return JsonResponse({'message' :'오타'}, status = 400)

class TokenCheckView(View):
    def post(self,request):
        data = json.loads(request.body)
        data_token_info = jwt.decode(data['token'], SECRET_KEY, algorithm = 'HS256')
        if User.objects.filter(email=data_token_info['user']).exists():
            return HttpResponse(status = 200)
        return HttpResponse(status=403)


