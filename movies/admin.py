from email import message
from django import forms
from django.contrib import admin
from django.utils.html import mark_safe

from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    trailer = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewInLine(admin.StackedInline):
    model = Review
    extra = 0
    readonly_fields = ('name', 'email')


class FoorageInLine(admin.TabularInline):
    model = Footage
    extra = 0
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="60"')

    get_img.short_description = "Footage"



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name', 'url')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name', 'url')
    list_filter = ('name', 'year')
    form = MovieAdminForm
    search_fields = ('name', 'category__name', 'actors', 'director')
    readonly_fields = ('get_img',)
    inlines = [FoorageInLine, ReviewInLine]
    fieldsets = (
        (None, {
            'fields': ('name', 'url', 'trailer', 'description', ('poster', 'get_img')),
        }),
        (None, {
            'fields': ('year', 'contry', 'director', 'actors', 'category', 'genres', 'premiere', 'budget', 'box_office'),
        })
    )

    def get_img(self,obj):
        return mark_safe(f'<img src={obj.poster.url} width="60" height="90"')

    get_img.short_description = "Image"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie')
    readonly_fields = ('name', 'email')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'age', 'get_img')

    def get_img(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="45" height="60"')

    get_img.short_description = "Image"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(Footage)
class FootageAdmin(admin.ModelAdmin):
    list_display = ('movie', 'get_img')

    def get_img(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="60"')

    get_img.short_description = "Footage"

@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'star', 'ip')


admin.site.site_title = 'EnjoyMovie'
admin.site.site_header = 'EnjoyMovie'
