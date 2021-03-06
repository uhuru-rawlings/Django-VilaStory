from django.shortcuts import render, redirect
from profiles.models import Posts,Profiles
from signups.models import Signups
from posts.models import ImportantInfo

# Create your views here.
def post_view(request):
    try:
        user = request.COOKIES['logedin']
    except:
        return redirect("/")
    users = Signups.objects.filter(useremail = user).first()
    try:
        details = ImportantInfo.objects.filter(village=users.village)
    except:
        details = 'nodetails'
    try:
        get_posts = Posts.objects.filter(post_village = users.village)
    except:
        get_posts = "noposts"
    context = {
        'title':'vilastory | posts',
        'get_posts':get_posts,
        'details':details
    }
    return render(request, "posts.html",context)

def addinfo_view(request):
    if request.method == 'POST':
        try:
            user = request.COOKIES['logedin']
        except:
            return redirect("/home/")
        users = Signups.objects.filter(useremail = user).first()
        nearhosp = request.POST['nearhosp']
        nearpolice = request.POST['nearpolice']
        shopingcent = request.POST['shopingcent']
        getdetails = ImportantInfo(village = users.village, hospital = nearhosp, policestation = nearpolice,market = shopingcent)
        getdetails.save()
    return redirect("/home/")