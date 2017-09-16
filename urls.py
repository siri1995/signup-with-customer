from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from sample3 import views as core_views
from . import views

urlpatterns = [
    url(r'^$', views.CustomerList.as_view(), name='customer-list'),
    url(r'customer/add/$', views.CustomerAddressCreate.as_view(), name='customer-add'),
    url(r'customer/(?P<pk>[0-9]+)/$', views.CustomerAddressUpdate.as_view(), name='customer-update'),
    url(r'customer/(?P<pk>[0-9]+)/delete/$', views.CustomerDelete.as_view(), name='customer-delete'),
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
]