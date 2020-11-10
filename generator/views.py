from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):
    password = ''
    characters = []
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('lowercase'):
        characters.extend('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('digit'):
        characters.extend('1234567890')
    if request.GET.get('special'):
        characters.extend('!@#$%^&*~')
    
    for x in range(int(request.GET.get('length'))):
        password+=random.choice(characters)
        
    return render(request,'generator/password.html',{'password':password})