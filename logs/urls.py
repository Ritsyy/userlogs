from django.conf.urls import url

from .views import WeavedinLogsView

urlpatterns = [
    url(r'^user/(?P<user_id>\d+)/$', WeavedinLogsView.as_view(), name='logs_user'),
    url(r'^logs/$', WeavedinLogsView.as_view(), name='logs'),
]
