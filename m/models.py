from distutils.command.upload import upload
from operator import mod
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
#from django_markdown.models import MarkdownField


# Create your models here.

class Skill(models.Model):
    skil= models.CharField(max_length=100,)
    desc = models.TextField(max_length=1000)
    def __str__(self):
        return self.skil

class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField( max_length=254)
    profile_img=CloudinaryField('image')
    def __str__(self):
        return self.name
class Testimonial(models.Model):
    client= models.ForeignKey(Client,related_name='clients', on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    project = models.CharField( max_length=50 ,null=True,blank=True)
    def __str__(self):
        return f'{self.project}-{self.client}'

class Profile(models.Model):
    user= models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    About = RichTextField(blank=True,null=True)
    title = models.CharField(max_length=300)
    picture=models.ImageField(upload_to='photos/users')
    cv = CloudinaryField('file')
    def __str__(self):
        return f'{self.user}_profile'

class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True,)
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Categorie'

class Album(models.Model):
    thumb = CloudinaryField('image')
    #post= models.OneToOneField(Post, related_name="album", on_delete=models.CASCADE)
    def __str__(self):
        return f'Album-{self.pk}'
    def thum(self):
        self.images.all().first()

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField(blank=True,null=True)
    slug=models.SlugField(unique=True)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    album = models.OneToOneField(Album, related_name=("album"), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(User, verbose_name="creator",related_name='posts', on_delete=models.CASCADE,null=True)
    views = models.IntegerField(default=0,)
    featured= models.BooleanField(default=False)
    def __str__(self):
        return f'Post-{self.pk}-{self.title}'
        
class ImageFile(models.Model):
    image =CloudinaryField('image')
    album = models.ForeignKey(Album,related_name='images',on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.album}-image'

class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User,related_name='comments', on_delete=models.CASCADE)
    comment = RichTextField(blank=True,null=True)
    created_at = models.DateTimeField( auto_now_add=True,blank=True,null=True)


    
class Stack(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'

class Case(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=10000,blank=True,null=True)
    category = models.ForeignKey(Category, related_name='cases' , on_delete=models.CASCADE)
    website =  models.CharField( max_length=50)
    used_stack = models.ManyToManyField(Stack,related_name="stacks" )
    album = models.OneToOneField(Album, related_name=("Album"), on_delete=models.CASCADE)
    def __str__(self):
        return f'Case-{self.pk}-{self.title}'


# class CaseAlbum(models.Model):
#     case = models.OneToOneField( Case,  related_name=("albom"), on_delete=models.CASCADE)
#     thumb = models.ImageField( upload_to='photos/cases',null=True)
#     def __str__(self):
#         return f'{self.case.title}-Album'

# class ImageFile2(models.Model):
#     image = models.ImageField( upload_to='photos/images')
#     album = models.ForeignKey(CaseAlbum,related_name='images',on_delete=models.CASCADE)
#     def __str__(self):
#         return f'{self.album}-image'

class Dgree(models.Model):
    source = models.CharField( max_length=50)
    start_date = models.DateField( auto_now=False, auto_now_add=False)
    end_date = models.DateField( auto_now=False, null=True, auto_now_add=False)
    course = models.CharField(max_length=50)
    note= models.TextField(max_length=300)
    def __str__(self):
        return f'{self.source}-{self.course}'

class Employment(models.Model):
    company = models.CharField( max_length=50)
    start_date = models.DateField( auto_now=False,  auto_now_add=False)
    end_date = models.DateField( auto_now=False, null=True, auto_now_add=False ,blank=True)
    title = models.CharField(max_length=50)
    note= models.TextField(max_length=300) 
    def __str__(self):
        return f'{self.company}-{self.title}'

class SocialAccount(models.Model):
    socialPlatform = models.CharField(max_length=50,)
    link= models.URLField()
    icon = CloudinaryField('file')
    
    def __str__(self):
        return self.socialPlatform
