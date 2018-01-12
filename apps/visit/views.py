from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import ContactRegisterForm, ContactLoginForm, ContactCheck
from base.views import ResponseResult
from contact.models import Contact
from base.views import BaseView


# Create your views here.

class IndexView(View):
    def get(self, request):
        contact_id = request.session.get("contact_id", False)
        print(contact_id)
        if not contact_id:
            # 未登录
            return HttpResponseRedirect(reverse('contact:login'))
        else:
            # 已登录
            contact = Contact.objects.get(id=int(contact_id))
            if contact.checkState == 1:
                return render(request, "visit/index.html", {})
            else:
                return HttpResponseRedirect(reverse('contact:r_state'))


class InsertListView(View):
    def get(self, request):
        return render(request, "visit/InsertList.html", {})


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


class VisitListView(View):
    def get(self, request):
        return render(request, "visit/VisitList.html", {})
