from django.conf.urls import url
from radarcxapp import views

urlpatterns = [
    url('^$', views.coins, name='home'),
    url('coins', views.coins, name='coins'),
    url('conditions', views.conditions, name='conditions'),
    url('new_cond', views.new_cond.as_view(), name='new_cond'),
    url('add_coin', views.add_coin.as_view(), name='add_coin'),
    url('delete_coin', views.delete_coin.as_view(), name='delete_coin'),
    url('manifest.json', views.manifest, name='manifest'),
    url('najva-messaging-sw.js', views.sw, name='sw'),
    url('najva-token', views.najva_token, name='najva_token'),
    url('chk', views.chk, name='chk'),
    url('signals', views.signals, name='signals'),
    # url('log', views.log, name='log'),
]
