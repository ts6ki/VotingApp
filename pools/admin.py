from django.contrib import admin

from .models import Question, Choice

class ChoiceInlineAdmin(admin.StackedInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text", "pub_date"]
    search_fields = ["question_text"]
    date_hierarchy = "pub_date"
    inlines = [ChoiceInlineAdmin]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["choice_text", "votes"]
    search_fields = ["choice_text"]
    list_filter = ["question"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
