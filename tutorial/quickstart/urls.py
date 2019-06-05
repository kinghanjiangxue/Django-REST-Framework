# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from .views import api_root, SnippetViewSet, UserViewSet
# from rest_framework import renderers

# urlpatterns = [
#     url('^quickstart/$', SnippetList.as_view()),
#     url('^quickstart/(?P<pk>[0-9]+)/$', SnippetDetail.as_view()),
#     url('^users/$',UserList.as_view()),
#     url('users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
#
#     url('^$', api_root),
#     url('^snippets/(?P<pk>[0-9]+)/highlight/$',SnippetHighlight.as_view()),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)


# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
#
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })
#
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderers_class=[renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
#
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
#
# urlpatterns = format_suffix_patterns([
#     url('^api-auth/', include('rest_framework.urls')),
#     url('^$',api_root),
#     url('snippets/$', snippet_list, name='snippet-list'),
#     url('^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#     url('^snippets/(?P<pk>[0-9])/highlight/$', snippet_highlight, name='snippet-highlight'),
#     url('^users/$', user_list, name='user-list'),
#     url('^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
# ])


from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from quickstart import views
from rest_framework.schemas import get_schema_view

# 创建路由器并注册我们的视图。
router = DefaultRouter()
router.register('snippets', views.SnippetViewSet)
router.register('users', views.UserViewSet)


schema_view = get_schema_view(title='Pastebin API')

# API url 现在有路由器自动确定
urlpatterns = [
    url('^schema/$', schema_view),
    url('^', include(router.urls))
]