from django.shortcuts import render, redirect
from .models import Gym
from .forms import GymCreate
from django.http import HttpResponse
import os
from django.conf import settings
from django.http import HttpResponse, Http404

from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist