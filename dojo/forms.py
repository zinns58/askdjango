# dojo/forms.py
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


'''
class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)

    # ModelForm.save 인터페이스를 흉내내어 구현
    def save(self, commit=True):
        self.instance = Post(**self.cleaned_data)
        if commit:
            self.instance.save()
        return self.instance
'''


'''
Form에서 제공하는 2가지 유효성 검사
1) validator 함수를 통한 유효성 검사
 - 값이 원하는 조건에 맞지 않을때, ValidationError 예외를 발생
 - 리턴값을 쓰지 않음
2) Form 클래스내 clean 맴버함수를 통한 유효성 검사 및 값 변경
 - 값이 원하는 조건에 맞지 않을때, ValidationError예외를 발생
 - 리턴값을 통해 값 변경
결론) 프론트앤드에서 입력받은 데이터를 검사하고, 값을 변경하여 사용하므로, views 내에서 끝까지 cleaned_data의 값을 사용해야함.

예시)
class CommentForm(forms.Form):
    def clean_message(self):
        return self.cleaned_data.get('message', '').strip() # 좌우 공백 제거
'''