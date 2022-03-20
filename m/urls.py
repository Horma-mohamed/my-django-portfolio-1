from django.urls import path,include
from .views import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register('posts',Home,basename='posts')
router.register('comments',Comment,basename='comments')
router.register('projects',Cases,basename='projects')
router.register('testimonials',Testimonials,basename='testimonials')
router.register('employments',Employment,basename='employments')
router.register('degrees',Dgrees,basename='degrees')
router.register('skills',Skills,basename='skills')
router.register('categories',Category,basename='categories')
router.register('social-accounts',SocialAccount,basename='social-accounts')
urlpatterns = [
    path('sendmail',SendMail,name='home'),
    path('postscomments/<int:id>',getcomments,name='comments'),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]+router.urls


"""path('blog/',blog,name='blog'),
    path('blog/<str:post_slug>/',post,name='post'),
    path('projects/',projects,name='projects'),
    path('projects/<int:case_id>/',case,name='case'),"""