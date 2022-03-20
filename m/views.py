
from tkinter import E
from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import *
from django.core.mail import send_mail,BadHeaderError
from django.template import RequestContext, loader
from rest_framework.views import APIView , status
from rest_framework.response import Response
from .serializers import *
from rest_framework import  viewsets,generics
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination



class PostPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size=6
    def get_paginated_response(self, data):
        return Response({
            
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data,
            'current':self.page.number,
            'pages':self.page.paginator.num_pages
            
        })
    

class Home(viewsets.ModelViewSet):
    posts=Post.objects.all().order_by('-created_at')
    # paginator = Paginator(posts,1)
    pagination_class = PostPagination
    queryset = posts
    serializer_class =PostSerializer

class Comment(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class =CommentSerializer
    #permission_classes = [IsAuthenticated]

class Skills(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class =SkillSerializer

class Category(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class =CategorySerializer

class Cases(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class =CaseSerializer

class Testimonials(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class =TestimonialSerializer

class Dgrees(viewsets.ModelViewSet):
    queryset = Dgree.objects.all()
    serializer_class =DgreeSerializer

class Employment(viewsets.ModelViewSet):
    queryset = Employment.objects.all()
    serializer_class =EmploymentSerializer

class SocialAccount(viewsets.ModelViewSet):
    queryset = SocialAccount.objects.all()
    serializer_class =SocialAccountSerializer

def SendMail(req):
    subject=req.GET.get('subject')
    message = req.GET.get('message')
    email = req.GET.get('email')
    email_from = settings.EMAIL_HOST_USER
    try:
        send_mail(subject,message,email_from,['horma496@gmail.com'])
        return HttpResponse('message_sended_successefuly')
    except BadHeaderError:
        return HttpResponse('there is an error message is not send ')


def getcomments(req,id):
    comments = ''
    data = CommentSerializer(comments,many=True)
    return Response(data)
            #send_mail(subject=subject,message=message,from_email='horma400@gmail.com',recipient_list=['horma496@gmail.com'])
        
            #return HttpResponse('404')
"""class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = int
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'"""

"""class Home(APIView):
        def get(self,request):
            skills = Skills.objects.all()
            posts = Post.objects.all()
            cases = Case.objects.all()
            dgrees = Dgree.objects.all()
            Testimonials = Testimonial.objects.all()
            data =[ PostSerializer(posts,many=True).data, SkillsSerializer(skills,many=True).data,CaseSerializer(cases,many=True).data,DgreeSerializer(dgrees,many=True).data,TestimonialSerializer(Testimonials,many=True).data,]
            return Response(data)
        def post(self,req):
            serializer = PostSerializer(data=req.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            """

    


