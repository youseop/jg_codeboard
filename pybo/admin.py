from django.contrib import admin

# -------------------------------------- [edit] ------------------------------------------
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
# -------------------------------------- [edit] ------------------------------------------
# -------------------------------------- [edit] ------------------------------------------