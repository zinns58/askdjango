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


'''
언제 validators를 쓰고, 언제 clean을 쓸까요?
-> 가급적이면 모든 validators는 모델에 정의하고, ModelForm을 통해 모델의 validators 정보도 같이 가져오세요.

clean은 언쩨 쓰나요?
1) 특정 Form에서 1회성 유효성 검사 루틴이 필요할때
2) 다수 필드값을 묶어서, 유효성 검사가 필요할때
3) 필드값을 변경할 필요가 있을때 : validator를 통해서는 값을 변경할수 없음(단지 값의 조건만 체크할뿐임)
'''