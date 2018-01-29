from django.contrib import admin
from .models import Question
from .models import Choice


# C:\Users\13925\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\django\contrib\admin\templates\admin
# Register your models here.

class ChoiceInline(admin.TabularInline):  # StackedInline(堆放) TabularInline(表格)
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']  # 改变表单顺序
    fieldsets = [  # 字段集
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text', 'pub_date', ]  # 'was_published_recently'
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
