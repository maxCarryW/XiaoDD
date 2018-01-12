from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

def ResponseResult(code=1, state='success', message='操作成功', data={}):
    """用于序列化返回请求结果"""
    json = {}
    json["code"] = code
    json["state"] = state
    json["message"] = message
    json["data"] = data
    return JsonResponse(json, safe=False)


def page_not_found(request):
    """全局404页面定义"""
    from django.shortcuts import render_to_response
    responese = render_to_response('404.html', {})
    responese.status_code = 404
    return responese


class BaseView(View):
    """Class View 请求视图"""
    template_name = "404.html"
    from base.menu import MENU
    menu = MENU
    content = {}

    def get(self, request):
        if self.is_auth(request):
            response = {}
            response['menu'] = self.menu
            from users.adminx import GlobalSetting
            response['site'] = {
                'title': GlobalSetting.site_title,
                'footer': GlobalSetting.site_footer
            }
            response['content'] = self.content

            return render(request, self.template_name, response)
        else:
            return redirect('/admin/login')

    def is_auth(self, request):
        if request.user.is_authenticated():
            return True
        else:
            return False


class Pagination(View):
    """分页"""

    def get(self, request):
        from django.apps import apps
        import json
        get = request.GET
        app_label = get.get('app', '')
        model_name = get.get('model', '')
        page = get.get('page', '1')
        limit = get.get('limit', '20')

        # 动态配置查询条件，此处以and关键词查询
        q = Q()
        filters = {}
        for key in get:
            if key.startswith("and_"):
                new_key = key.replace("and_", "")
                q.add(Q(**{new_key: get[key]}), Q.AND)
            elif key.startswith("or_"):
                new_key = key.replace("or_", "")
                q.add(Q(**{new_key: get[key]}), Q.OR)
            else:
                pass

        # filters = {'checkState': 1, 'phone__contains': '183'}
        # for f in filters:
        #     q.add(Q(**{f: filters[f]}), Q.AND)

        model = apps.get_model(app_label, model_name)
        data = model.objects.filter(q)

        # pagination
        paginator = Paginator(data, int(limit))
        try:
            p = paginator.page(int(page))
        # 请求页数错误
        except PageNotAnInteger:
            p = paginator.page(1)
        except EmptyPage:
            p = paginator.page(paginator.num_pages)
        # 分页后的数据

        json_data = serializers.serialize("json", p)
        rows = json.loads(json_data)

        json = {}
        json["total"] = data.count()
        json["rows"] = rows
        return JsonResponse(json, safe=False)


