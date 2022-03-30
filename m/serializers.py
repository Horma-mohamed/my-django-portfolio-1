from dataclasses import field, fields
from rest_framework import serializers
from .models import * 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('name',)
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFile
        fields = ('image',)
class UserSerializer(serializers.ModelSerializer):
    #post = serializers.CharField(source='post.title',required=False)
    class Meta:
        model = User
        fields = ('username',)
class AlbumSerializer(serializers.ModelSerializer):
    images= ImageSerializer(many=True)
    post = serializers.CharField(source='post.title',required=False)
    class Meta:
        model = Album
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    post = serializers.CharField(source='post.title',required=False)
    author = UserSerializer(many=False)
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    #created_by = serializers.CharField(source='create_by.username',required=False)
    #slug_ = serializers.CharField(source=getslug, required=False)
    category = CategorySerializer(many=False)
    comments = CommentSerializer(many=True)
    create_by = UserSerializer(many=False)
    album = AlbumSerializer(many=False)
    thumb = serializers.ImageField(source='album.thumb')
    class Meta:
        model = Post
        fields = '__all__'
        #fields = ('title','category','conten','create_by')



class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = '__all__'
# class ImageSerializer2(serializers.ModelSerializer):
#     class Meta:
#         model = ImageFile2
# class CaseAlbumSerializer(serializers.ModelSerializer):
#     images = ImageSerializer2(many=True)
#     class Meta:
#         model = CaseAlbum
#         fields='__all__'
class CaseSerializer(serializers.ModelSerializer):
    #usedstacks = StackSerializer(many=True,read_only=True)
    category= CategorySerializer(many=False)
    album= AlbumSerializer(many=False)
    thumb = serializers.ImageField(source='album.thumb')
    class Meta:
        model = Case
        fields = '__all__'

class DgreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dgree
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.name',required=False)
    class Meta:
        model = Testimonial
        fields = '__all__'
class EmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields = '__all__'

class SocialAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
