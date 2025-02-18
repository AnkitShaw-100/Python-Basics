from django.http import HttpResponse
from django.shortcuts import render

def aboutUS(request):
    return render(request, "index.html")

def blog(request, courseid):
    return HttpResponse(f"Blog page for course ID: {courseid}")

def article(request, slug):
    return HttpResponse(f"Article page for slug: {slug}")

def user_profile(request, username):
    return HttpResponse(f"User profile page for username: {username}")