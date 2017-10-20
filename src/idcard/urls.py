from django.conf.urls import url

from src.idcard.views.generateidcard import generate
from src.idcard.views.idcardview import IdCardView

create = IdCardView.as_view({
    'get': 'list',
    'post': 'create'
})

update = IdCardView.as_view({
    'get': 'retrieve',
    'put': 'update'
})
urlpatterns = [

    url(r'^generate/(?P<id>\w+)/$', generate),
    url(r'^$', create),
    url(r'^(?P<id>\w+)/$', update),
    url(r'^redirect.php?url=34.233.78.6/view/(?P<id>\w+)/$', update)
]
