from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
import datetime
from models import Package, Recipient
from django.template import Context, loader
from django.core import serializers

def home(request):
    packages = Package.objects.all() #serializers.serialize( "python", Package.objects.all() ) #
    t = 'alternate/index.html'
    c = Context({'packages': packages })
                              # TemplateFile, context_instance, MIME type
    return render_to_response(t, c, context_instance=RequestContext(request))

def worker(request):
    packages = Package.objects.all() #serializers.serialize( "python", Package.objects.all() ) #
    t = 'alternate/worker.html'
    c = Context({'packages': packages })
                              # TemplateFile, context_instance, MIME type
    return render_to_response(t, c, context_instance=RequestContext(request))

def add_new_pkg(request):
    recipients = Recipient.objects.all()
    t = 'alternate/worker_create_new_pkg.html'
    c = Context({'recipients':recipients })
    return render_to_response(t,c, context_instance=RequestContext(request))
# data = serializers.serialize( "python", Package.objects.all() )

def add_new_recipient(request):
    recipients = Recipient.objects.all()
    t = 'alternate/worker_create_new_recipient.html'
    c = Context({'recipients':recipients })
    return render_to_response(t,c, context_instance=RequestContext(request))
# data = serializers.serialize( "python", Package.objects.all() )

def logout(request):
    recipients = Recipient.objects.all()
    t = 'alternate/logout_screen.html'
    c = Context({'recipients':recipients })
    return render_to_response(t,c, context_instance=RequestContext(request))
# data = serializers.serialize( "python", Package.objects.all() )
