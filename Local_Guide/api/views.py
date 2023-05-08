from django.http import HttpResponse
from rest_framework import generics
from django.shortcuts import render
from . models import *
from rest_framework.response import Response
from . serializer import *
from rest_framework.decorators import api_view
from .models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.shortcuts import render, redirect
import random


# Create your views here
glob_username = ''

def index(request):
    response = {}
    if request.method == 'POST':
        username = str(request.POST.get('username'))
        password = str(request.POST.get('password'))
        print(username, password)
        global glob_username 
        glob_username = username
        try:
            user = User.objects.get(username=username,password=password)
            #user = User.objects.filter(username=username1, password=password1)
            print('lets print database info',user)
            return render(request, 'city.html')
            #return render( request, 'index.html', {'response':'match kar gaya'})
        except User.DoesNotExist:
            a = 'pansu'
            response = {'response':'Invalid UserID or Password', 'pansu_response':a}
            return render(request, 'index.html',response)

        # If the student exists, render a success message
        
    return render(request, 'index.html', response)


# @api_view(['POST'])
# def Search_Route(request):


# 	return render(request, 'city.html',{'response':'User Logged In'})


def sign_up(request):
    response = {}
    if request.method == 'POST':
        # Get the user details from the request body
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        name = request.POST.get('name')
        print('hello')
        a_list = [username,city,password,name,phone]
        print(a_list)
        user = User.objects.create(
            username=username,
            phone=phone,
            city=city,
            password=password,
            name=name,
        )
        user.save()

        a = "You are Registered"
        response = {'response':a}
    else:
        Response = None
    return render(request, 'signup.html',response)



string_from = ''
string_to = ''

@api_view(['POST'])
def Search_Route(request):
    from1 = str(request.data.get('from'))
    to1 = str(request.data.get('to'))
    global string_from
    global string_to
    string1 = from1.strip().upper()
    string2 = to1.strip().upper()
    string_from = string1
    string_to = string2
    print(string1, string2)
    print('global var',glob_username)
    if glob_username != '':
        try:
            graph = {
        'RAMBAG' : ['RAMBAG','TEDI','BELAN','WATER'],
        'BHAGWAN' : ['RAMBAG','WATER','SULTAN','BHAGWAN','SANJAY','HARI'],
        'WATER' : ['RAMBAG','SULTAN', 'BHAGWAN','KHANDARI','SIKANDRA'],
        }
            def find_shortest_path(graph, start, end, path=[]):
                path = path + [start]
                if start == end:
                    return path
                if start not in graph:
                    return None
                shortest = None
                for node in graph[start]:
                    if node not in path:
                        newpath = find_shortest_path(graph, node, end, path)
                        if newpath:
                            if not shortest or len(newpath) < len(shortest):
                                shortest = newpath
                return shortest
            result = find_shortest_path(graph=graph, start=string1,end=string2)
            # result = find_shortest_path()
            print(result)
            response = {'response':result}
            return render(request, 'city.html', response)
            # return Response({'result': result})
            #return render(request, 'city.html')    

        except ValueError:
            return Response({'error': 'Invalid input. Both inputs must be strings.'})
    else:
        print('it do not work without login')
        return render(request, 'index.html')



def logout(request):
    return render(request,'index.html')


def profile(request):

    print('This is a global variable inside from profile fn ', glob_username)
    
    # user = User.objects.select_related('name','username','phone','city').get(username=glob_username)
    user = User.objects.filter(username=glob_username).values('name','username','phone','city')
    print(user)
    return render(request, 'profile.html', {'user':user})


def delete(request):
    user = User.objects.get(username=glob_username)
    print('is it working')
    print(user)
    user.delete()
    print('i think it is deleted')
    return render(request, 'delete.html', {'ifdeleted':'User Account Permanently Deleted'})

def cab(request):
    rnum = random.randint(1,10)
    booking_id = random.randint(1000,9999)
    user = User.objects.filter(username=glob_username).values('name','username','phone','city')
    driver = Driver.objects.filter(id=rnum).values('dname','dphone',)
    print(user,'/n',driver,booking_id, rnum)
    return render(request, 'cab.html', {'user':user, 'driver':driver, 'booking_id':booking_id, 'from':string_from, 'to':string_to})




class ReactView(generics.CreateAPIView):
	serializer_class = ReactSerializer
	queryset = React.objects.all()
	
	def get(self, request):
		detail = [ {"name": detail.name,"detail": detail.detail}
		for detail in React.objects.all()]
		return Response(detail)

	def post(self, request):
		serializer = ReactSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)


def ram_ram(request):
    return render(request, 'testing.html')

def hal_chal(request):
    return HttpResponse('<h1>kese ho bhai </h1>')
