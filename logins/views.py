from django.shortcuts import render,redirect
from signups.models import Signups
# Create your views here.
def login_view(request):
    errors = ''
    if request.method == 'POST':
        useremails = request.POST['useremail']
        userpassword = request.POST['userpassword']
        user = Signups.objects.filter(useremail = useremails).exists()
        if user:
            users = Signups.objects.get(useremail = useremails)
            if users.passwords == userpassword:
                response = redirect("/home/")
                response.set_cookie("logedin", useremails)
                return response
            else:
                errors = 'Wrong password please try again'
        else:
            errors = "user dont exist, please try gain"
    context = {
        'title':'vilastory | login',
        'errors':errors
    }
    return render(request, "login.html",context)

def login_meth(request):
   pass