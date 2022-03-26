from django.contrib import admin
from .models import * 
# Register your models here.
from django_markdown.admin import MarkdownModelAdmin
class InlineImages(admin.StackedInline):
    model = ImageFile
    extra = 1
# class InlineAlbum(admin.StackedInline):
#     model = Album
# class InlineAlbum2(admin.StackedInline):
#     model = CaseAlbum
class AlbumClass(admin.ModelAdmin):
    inlines = [InlineImages,]

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    # inlines = [InlineAlbum,]
# class CasesAdmin(admin.ModelAdmin):
#     inlines = [InlineAlbum2,]
admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(Testimonial)
admin.site.register(Client)
admin.site.register(Profile)
admin.site.register(Album,AlbumClass)
admin.site.register(ImageFile)
admin.site.register(Post,ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Dgree)
admin.site.register(Employment)
admin.site.register(Case,MarkdownModelAdmin)
admin.site.register(Stack)
admin.site.register(SocialAccount)

