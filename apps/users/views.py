from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import JsonResponse

from .forms import LoginForm
from base.views import ResponseResult, BaseView

USER = get_user_model()


# Create your views here.


class CustomBackend(ModelBackend):
    """自定义django的认证"""

    def authenticate(self, username=None, password=None, **kwargs):
        """认证"""
        try:
            user = USER.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as ex:
            return None


class LoginView(View):
    """后台登录视图"""
    template_name = "404.html"

    def get(self, request):
        from users.adminx import GlobalSetting
        response = {}
        response['site'] = {
            'title': GlobalSetting.site_title,
            'footer': GlobalSetting.site_footer
        }
        return render(request, self.template_name, response)

    def post(self, request):
        login_from = LoginForm(request.POST)
        if login_from.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return ResponseResult()
                else:
                    return ResponseResult(-1, 'fail', '用户未激活')
            else:
                return ResponseResult(-1, 'fail', '用户名或者密码错误')
        else:
            return ResponseResult(-1, 'fail', '用户名或者密码错误')


class IndexView(BaseView):
    """后台主页视图"""
    template_name = "404.html"
