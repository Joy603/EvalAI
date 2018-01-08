from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^challenge_host_team/(?P<challenge_host_team_pk>[0-9]+)/notebook$', views.notebook_list,
        name='get_notebook_list'),
]