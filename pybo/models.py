from django.db import models
from django.contrib.auth.models import User

#makemigrations, migrate 명령은 모델의 속성이 추가되거나 변경된 경우에 실행 

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    #Answer와 연결되어있으므로 answer(연결모델)_set 으로 연결된 답변 찾을 수 있음 
# -------------------------------------- [edit] ------------------------------------------
    def __str__(self):
        return self.subject
# -------------------------------------- [edit] ------------------------------------------
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content
# -------------------------------------- [edit] ------------------------------------------
