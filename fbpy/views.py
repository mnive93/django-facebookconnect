from pyfb import Pyfb
from django.http import HttpResponse, HttpResponseRedirect
from settings import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET, FACEBOOK_REDIRECT_URL
from django.shortcuts import render_to_response

def index(request):
   return render_to_response("index.html", {"FACEBOOK_APP_ID": FACEBOOK_APP_ID})



def facebook_login(request):
    facebook = Pyfb(FACEBOOK_APP_ID)
    return HttpResponseRedirect(facebook.get_auth_code_url(redirect_uri=FACEBOOK_REDIRECT_URL))

def facebook_login_success(request):
    code = request.GET.get('code')    
    facebook = Pyfb(FACEBOOK_APP_ID)
    facebook.get_access_token(FACEBOOK_APP_SECRET, code, redirect_uri=FACEBOOK_REDIRECT_URL)
    me = facebook.get_myself()

    welcome = "Welcome %s. Your Facebook login has been completed successfully! Is this your email address? %s"
    return HttpResponse(welcome % (me.name, me.email))


