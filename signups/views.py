from django.shortcuts import render

# Create your views here.
def signup_view(request):
    context = {
        'title':'vilastory | signup',
    }
    return render(request, "signup.html",context)

def signup_meth(request):
    if request.method == 'POST':
        pass