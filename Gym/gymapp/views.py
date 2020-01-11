from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Gym
from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist



# View Function for Search
# Search Funcanality

def search_function_hai(request):
    if request.method =='GET':
        freddie = request.GET['hacker']
        if freddie:
            matchstore = Gym.objects.filter(Q(workoutname__icontains=freddie))                             
            if matchstore:                
                return render(request,'gymapp/upload_form.htm', {'sac':matchstore})
            else:
                messages.error(request, "The word, You type did  not Exist")
                # return HttpResponse("The word, You type was not Exist")
        else:
            return HttpResponseRedict('gymapp/premium.htm')  
    return render(request, 'gymapp/premium.htm')         
