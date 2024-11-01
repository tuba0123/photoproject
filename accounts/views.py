from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    '''サインアップページのビュー
    
    '''
    # forms_class = CustomUserCreationForm
    form_class = CustomUserCreationForm
    # レンダリングするテンプレート
    template_name = 'signup.html'
    # サインアップ完了後のリダイレクト先のURLパターン
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self, form):
        '''CreateViewクラスのform_valud()オーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録を行う
        
        parameters:
            form(django.form.Form):
            form_classに格納されているCustomUserCreationFormオブジェクト
          Return:
            HttpResponseRedirectオブジェクト:
              スーパークラスのform_valid()の戻り値を返すことで、
              success_urlで設定されているURLにリダイレクトさせる
        '''
        # fromオブジェクトのフィールドの値をデータベースに保存
        user = form.save()
        self.object = user
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)
    
class SignUpSuccessView(TemplateView):
    '''サインアップ完了のページのビュー
    
    '''
    # レンダリングするテンプレート
    template_name = "signup_success.html"