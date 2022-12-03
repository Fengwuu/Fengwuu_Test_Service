from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_answer', 'display_correct_answer')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'collection', 'display_question')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Test, TestAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)



