from django.conf.urls import include, url
from . import views

app_name="blog"
urlpatterns = [
  url(r'^$', views.v_post_list),
  url(r'^post/(?P<param_pk>[0-9]+)/$', views.v_post_detail, name='v_post_detail' ),
]
