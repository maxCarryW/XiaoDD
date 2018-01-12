from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from users.models import Area
from .forms import ContactRegisterForm, ContactLoginForm, ContactCheck
from base.views import ResponseResult
from contact.models import Contact
from base.views import BaseView


# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, "visit/login.html", {})

    def post(self, request):
        login_from = ContactLoginForm(request.POST)
        if login_from.is_valid():
            phone = request.POST.get('phone', '')
            password = request.POST.get('password', '')
            contact = authenticate(phone=phone, password=password)

            if contact is not None:
                if contact.is_active:
                    login(request, contact)
                    # return ResponseResult()
                    return HttpResponseRedirect(reverse('contact:'))
                else:
                    return ResponseResult(-1, 'fail', '用户未激活')
            else:
                return ResponseResult(-1, 'fail', '用户名或者密码错误')
        else:
            return ResponseResult(-1, 'fail', '用户名或者密码错误')


class RegisterView(View):
    def get(self, request):
        area = Area.objects.all().order_by("ordering")
        return render(request, "visit/register.html", {
            "area": area
        })

    def post(self, request):
        _from = ContactRegisterForm(request.POST)
        if _from.is_valid():
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            area = int(request.POST.get('area'))

            contact = Contact.objects.filter(phone=phone)
            if contact.count() > 0:
                return ResponseResult(-1, 'fail', "该号码已经注册")
            else:
                area_object = Area.objects.get(id=int(area))

                contact = Contact()
                contact.name = name
                contact.phone = phone
                contact.password = password
                contact.area = area_object
                contact.save()
                request.session['contact_id'] = contact.id
                return ResponseResult()

        else:
            return ResponseResult(-1, 'fail', "请求失败")


class R_stateView(View):
    def get(self, request):
        return render(request, "visit/Register_state.html", {})


class MyselfView(View):
    def get(self, request):
        return render(request, "visit/Myself.html", {})


class ForgetPasswordView(View):
    def get(self, request):
        return render(request, "visit/ForgetPassword.html", {})


# 后台管理模块
class ContactListView(BaseView):
    """联络员列表"""
    template_name = "404.html"


class ContactCheckView(View):
    def post(self, request):
        _form = ContactCheck(request.POST)
        if _form.is_valid():
            pk = request.POST.get("pk", "")
            checkState = request.POST.get("checkState", "")
            checkDescription = request.POST.get("checkDescription", "")

            contact = Contact.objects.get(id=pk)
            contact.checkState = checkState
            contact.checkDescription = checkDescription
            contact.save()
            return ResponseResult()
        else:
            return ResponseResult(-1, 'fail', "审核失败")


class DeleteView(View):
    def get(self, request, id):
        contact = Contact.objects.filter(id=int(id)).first()
        if contact:
            contact.delete()
