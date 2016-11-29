from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [

    # Stuff we need
    url(r'^$', views.index, name='index'),
    url(r'^data/$', views.data, name='data'),
    url(r'^display_table/$', views.display_table, name='display_table'),
    url(r'^plottable/(?P<a>[A-Za-z0-9\-\'\,\% ]+)/(?P<b>[A-Za-z0-9\-\'\,\% ]+)/(?P<c>[A-Za-z0-9\-\'\,\% ]+)/(?P<d>[A-Za-z0-9\-\'\,\% ]+)$', views.plottable, name='plottable'),
    url(r'^display_pic/$', views.display_pic, name='display_pic'),
    url(r'^plotmath/(?P<c>[A-Za-z\-\ ]+)/$', views.plotmath, name='plotmath'),
    url(r'^plotreading/(?P<c>[A-Za-z\-\' ]+)/$', views.plotreading, name='plotreading'),
    url(r'^plotexpenditure/(?P<c>[A-Za-z\-\' ]+)/$', views.plotexpenditure, name='plotexpenditure'),
    url(r'^plotrelation/(?P<c>[A-Za-z\-\' ]+)/$', views.plotrelation, name='plotrelation'),
    url(r'^display_picrelation/$', views.display_picrelation, name='display_picrelation'),
    url(r'^variables/$', views.variables, name='variables'),
    url(r'^plotvariable/(?P<a>[A-Za-z0-9\-\'\,\% ]+)/(?P<b>[A-Za-z0-9\-\'\,\% ]+)/(?P<c>[A-Za-z0-9\-\'\,\% ]+)/(?P<d>[A-Za-z0-9\-\'\,\% ]+)$', views.plotvariable, name='plotvariable'),

    # stuff just in case

    url(r'^formclass/$', views.FormClass.as_view(), name = "formclass"),
    url(r'^resp/$', views.resp_redirect, name = "resp_redirect"),
    url(r'^resp/(?P<state>[A-Z][A-Z])/$', views.resp, name = "resp"),
    url(r'^map/$', views.embedded_map, name = "map"),
]
