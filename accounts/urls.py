from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from accounts.views import add_remove_frm2fav, LogOutUser

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.UserModelView.as_view(), name='signup'),

    url(r'^login/$', views.login_user, name='login'),

    url(r'^logout/$', LogOutUser.as_view(), name='logout'),

    url(r'^passwordchange/$', views.ChangePassword.as_view(), name='password-change'),

    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset/password_reset_form.html"), name='password_reset'),

    url(r'^password_reset/complete/$', auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset/password_reset_complete.html"),
        name='password_reset_complete'),

    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset/password_reset_done.html"),
        name='password_reset_done'),

    url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset/password_reset_confirm.html"), name='password_reset_confirm'),

    url(r'^myprofile/(?P<pk>[\w-]+)/',
        views.UserModelDetailView.as_view(), name='myprofile'),

    url(r"^updateprofile/(?P<pk>[\w-]+)/",
        views.UserModelView.as_view(), name='update-profile'),

    path("fav-articles/<slug>/", add_remove_frm2fav, name='add-remove-fav'),


]
