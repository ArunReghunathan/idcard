# from django.views.decorators.csrf import csrf_exempt

from django.conf.urls import url

from src.users.views.userview import UserView, UserSignin

user = UserView.as_view({
    'get': 'list',
    'post': 'create'
})

single_user = UserView.as_view({
    'get': 'retrieve',
    'put': 'update'
})

urlpatterns = [

    url(r'^$',  user),
    url(r'^signin/$', UserSignin),
    url(r'^(?P<id>\w+)/$', single_user),
]
