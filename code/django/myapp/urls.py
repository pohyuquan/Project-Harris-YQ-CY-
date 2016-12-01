from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [

    # Stuff we need
    url(r'^$', views.index, name='index'),
    url(r'^data/$', views.data, name='data'),
    url(r'^team/$', views.team, name='team'),
    url(r'^code/$', views.code, name='code'),
    url(r'^contact/$', views.contact_us, name='contact_us'),
    url(r'^display_table/$', views.display_table, name='display_table'),
    url(r'^plottable/(?P<a>[A-Za-z0-9\-\'\,\% ]+)/(?P<b>[A-Za-z0-9\-\'\,\% ]+)/(?P<c>[A-Za-z0-9\-\'\,\% ]+)/(?P<d>[A-Za-z0-9\-\'\,\% ]+)$', views.plottable, name='plottable'),
    url(r'^display_pic/$', views.display_pic, name='display_pic'),
    url(r'^plotmath/(?P<c>[A-Za-z\-\ ]+)/$', views.plotmath, name='plotmath'),
    url(r'^plotreading/(?P<c>[A-Za-z\-\' ]+)/$', views.plotreading, name='plotreading'),
    url(r'^plotexpenditure/(?P<c>[A-Za-z\-\' ]+)/$', views.plotexpenditure, name='plotexpenditure'),
    url(r'^plotrelationmath/(?P<c>[A-Za-z\-\' ]+)/$', views.plotrelationmath, name='plotrelationmath'),
    url(r'^plotrelationreading/(?P<c>[A-Za-z\-\' ]+)/$', views.plotrelationreading, name='plotrelationreading'),
    url(r'^display_picrelation/$', views.display_picrelation, name='display_picrelation'),
    url(r'^variables/$', views.variables, name='variables'),
    url(r'^plotvariable/(?P<a>[A-Za-z0-9\-\'\,\% ]+)/(?P<b>[A-Za-z0-9\-\'\,\% ]+)/(?P<c>[A-Za-z0-9\-\'\,\% ]+)/(?P<d>[A-Za-z0-9\-\'\,\% ]+)$', views.plotvariable, name='plotvariable'),
    url(r'^final/$', views.final, name='final'),
    url(r'^finalplotmath/$', views.finalplotmath, name='finalplotmath'),
    url(r'^finalplotread/$', views.finalplotread, name='finalplotread'),
]
