from django.conf.urls import url

from src.users.views.userview import UserView

user = UserView.as_view({
    'get': 'list',
    'post': 'create'
})

single_user = UserView.as_view({
    'get': 'retrieve',
    'put': 'update'
})

urlpatterns = [

    url(r'^$', user),
    url(r'^(?P<id>\w+)/$', single_user)
]
