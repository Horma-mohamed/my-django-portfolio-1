
from tkinter import E
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import *
from django.core.mail import send_mail,BadHeaderError
from django.template import RequestContext, loader

# Create your views here.
categories = Category.objects.all()
I = User.objects.get(username='AA')
posts= Post.objects.all()
degrees = Dgree.objects.all()
employments = Employment.objects.all()
def home(req):
    skils = Skills.objects.all()
    testimonials = Testimonial.objects.all()
    lastest_posts = Post.objects.all().order_by('-created_at')[0:3]
    lastest_cases = Case.objects.all()[0:3]
    msgs = False
    if req.method == 'POST':
        subject = req.POST['subject']
        message = req.POST['message']
        contacter_email = req.POST['email']
        send_to =  'horma495@gmail.com'
        email_from = settings.EMAIL_HOST_USER
        html_msg = loader.render_to_string(
            'email/contact_me_msg.html',
            {
                'client':contacter_email,
                'msg':message,
            }
        )
        try :
            send_mail( subject, message, email_from, [send_to,] ,fail_silently=False, html_message=html_msg)
            #starttime= datetime.now().second
            #msgs = 'email is Sended successfuly !!'
            #return redirect('contact')
        except BadHeaderError :
            msgs = False
    
    return JsonResponse(data)
    #return render(req,'pages/home.html',cont)
def blog(req):
    posts= Post.objects.all()
    search = None
    category =None
    if req.method=='GET':
        search = req.GET.get('search')
        category = req.GET.get('category')
        if search is not None :
            posts = Post.objects.filter(title__contains=search)
            
        elif category is not None :
            posts = Post.objects.filter(category__name__contains=category)
    c = {
        'posts': posts,
        'search':search,
        'categories':categories,
        'I':I,
        
    }
    
    return render(req,'pages/blog.html',c)

def post(req,post_slug ):
    post = get_object_or_404(Post,slug=post_slug)
    album = Album.objects.get(post=post)
    session_key =f'post-{post.pk}'
    
    if not req.session.get(session_key,False):
        post.views += 1
        post.save()
        req.session[session_key] = True
    c = {
        'post': post,
        'album':album,
        'I':I,
    }
    if req.method == 'POST' :
        if req.user.is_authenticated :
            """user = req.POST['user']
            email = req.POST['email']"""
            comment = req.POST['comment']
            user = req.user
            Comment.objects.create(author=user,post=post,comment=comment)
        else:
            return redirect('home')
    return render(req,'pages/post.html',c)


def projects(req):
    projects= Case.objects.all()
    filterkey =None
    filterkey = req.GET.get('category')
    if filterkey is not None :
        projects = Case.objects.filter(category__name=filterkey)
            
        
    c = {
        'projects': projects,
        'category':filterkey,
        'categories':categories,
        'I':I,
        
    }
    return render(req,'pages/projects.html',c)

def case(req, case_id):
    case = get_object_or_404(Case,pk=case_id)
    c = {
        'case':case,
    }
    return render(req,'pages/case.html',c)


def handler404(req, *arg, **kwargs):
    response =render(req, 'e404.html',{}, context_instance = RequestContext(req))
    response.status_code = 400
    return response