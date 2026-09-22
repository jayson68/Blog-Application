from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView



urlpatterns = [
    path("", views.home, name="home"),
    path("profile/<str:username>/", views.profile_page, name="profile"),
    path("edit_profile/", views.edit_profile, name = "edit_profile"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("create/", views.create_post, name="create"),
    path("detail/<int:id>/", views.detail_post, name="detail"),
    path("update/<int:id>/", views.update_post, name="update"),
    path("delete/<int:id>/", views.delete_post, name="delete"),
    path("register/", views.register_view, name="register"),
    path("hello/", views.Getview.as_view(), name="getview"),
    path("hello/<int:pk>/", views.Getview.as_view(), name="post-detail"),

    path(
    "change-password/",PasswordChangeView.as_view(template_name="change_password.html"), name="change_password"),

    path(
        "change-password/done/",PasswordChangeDoneView.as_view(template_name="change_password_done.html"),name="password_change_done"),

    path('forgot_password/', PasswordResetView.as_view(template_name='forgot_password.html'), name="forgot_password"),
    path('forgot_password/done/', PasswordResetDoneView.as_view(template_name='forgot_password_done.html'), name="password_reset_done"),
    path('forgot_password/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='reset_password.html'), name="password_reset_confirm"),
    path('reset_password/done', PasswordResetCompleteView.as_view(template_name='reset_password_done.html'), name="password_reset_complete"),
]
