# from django.http import HttpResponse
# from django.shortcuts import render

# def aboutUS(request):
#     data={
#         'title':'About Ankit',
#         'ankit':'Ankit is a web developer',
#         'bdata': 'This is about page',
#         'clist': ['Ankit','Rahul','Rohit','Rajesh'],
#         'number':[],
#         'student_details':[
#             {'name':'Ankit', 'roll':101, 'branch':'CSE'},
#             {'name':'Rahul', 'roll':102, 'branch':'CSE'},
#             {'name':'Rohit', 'roll':103, 'branch':'CSE'},
#             {'name':'Rajesh','roll':104, 'branch':'CSE',}]
#         }
#      return render(request, "home.html")

# def blog(request, courseid):
#     return HttpResponse(f"Blog page for course ID: {courseid}")

# def article(request, slug):
#     return HttpResponse(f"Article page for slug: {slug}")

# def user_profile(request, username):
#     return HttpResponse(f"User profile page for username: {username}")


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contactus(request):
    return render(request, 'contactus.html')






