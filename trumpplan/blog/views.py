from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response, get_object_or_404
# Create your views here.
#from .models import Blog, Category

from django.http import HttpResponse

from collections import OrderedDict
from . import posts

pages = OrderedDict([
    ("Clean up DC",{
        "full": 'Measures to clean up the corruption and special interest collusion in Washington, DC',
     'pages':[
        "Term Limits",
        "Hiring Freeze",
        "Federal Regulations",
        "Lobbying",
        "Foreign Lobbyists"
    ]}),
    ("American Workers", {
        "full": 'Protect American workers',
     'pages':[
        "NAFTA",
        "TPP",
        "China",
        "Trade Abuse",
        "Energy",
        "Infrastructure",
        "Climate Change"
    ]}),
    ("Security & Law", {
        "full": 'Actions to restore security and the constitutional rule of law',
     'pages':['Executive Actions',
              'Supreme Court',
              'Sanctuary Cities',
              'Immigrant Deportation',
              'Immigration Suspension'

    ]}),
    ('Legislation',{
     'full': "Next, I will work with Congress to introduce the following Legislative measures",
    'pages':["Middle Class Tax Relief",
             'End Offshoring Act',
             'American Energy & Infrastructure Act',
             'School Choice and Opportunity Act',
             'Repeal & Replace Obamacare Act',
             'Affordable Childcare and Eldercare Act',
             'End Illegal Immigration Act ("The Wall")',
             'Restoring Community Safety Act',
             'Restoring National Security Act',
             'Clean up Corruption in Washington Act']})
])

def my_redirect(request):
    return HttpResponsePermanentRedirect(reverse('section_loader'))

def create_menu():
    pass

def index_flash(request,value_link=None):
    return render(request, 'flash.html')

def load_section(request, key):
    print('LOADING SECTION')
    key = key.replace('/', '')
    data = pages[key]
    return render_to_response('sections.html', {'data':data, 'category':key,
                                                'pages':pages})

def load_article(request, key, val):

    post_text = posts.get_post(val)

    if not post_text:
        return render_to_response('coming_soon.html', {'data':val,
                                                       'pages':pages})
    else:
        return render_to_response('article.html',{'data':val,
                                                  'pages':pages})


def index(request):
    return render_to_response('homepage.html', {'pages':pages})

def load_post(key):
    directory = os

