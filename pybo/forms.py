from django import forms
from pybo.models import Question, Answer


# -------------------------------------- [edit] ------------------------------------------
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
# 모델 폼 객체를 저장하면 연결된 모델의 데이터를 저장할 수 있음
# 장고 모델 폼은 내부 클래스로 Meta 클래스를 반드시 가져야 하며, Meta 클래스에는 모델 폼이 사용할 모델과
# 필드들을 적어야 함
# -------------------------------------- [edit] ------------------------------------------
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        #부트스트랩 적용 위해서 -> 불마도 가능? 
# -------------------------------------- [edit] ------------------------------------------
        labels = {
            'subject': '제목',
            'content': '내용',
        }
# -------------------------------------- [edit] ------------------------------------------
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }