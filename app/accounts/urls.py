from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('', views.home, name='home'),

    path('customers_list', views.customers_list, name='customers_list'),
    path('create_customer', views.create_customer, name='create_customer'),
    path('edit_customer/<int:customer_id>/', views.edit_customer, name='edit_customer'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout_view, name='logout'),
    # path('companies/<int:customer_id>/', views.companies_list, name='customer_companies'),

    # path('error-500/', views.error_500, name='error_500'),
    # path('pace/', views.pace, name='pace'),
    # path('blank-page/', views.blank_page, name='blank_page'),
    # path('starter-page/', views.starter_page, name='starter_page'),
    # # Authentication
    # path('accounts/register/', views.register, name='register'),
    # path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    # path('accounts/logout/', views.user_logout_view, name='logout'),
    # path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    # path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
    #     template_name='accounts/password_change_done.html'
    # ), name="password_change_done"),
    # path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    # path('accounts/password-reset-confirm/<uidb64>/<token>/',
    #      views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
    #     template_name='accounts/password_reset_done.html'
    # ), name='password_reset_done'),
    # path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
    #     template_name='accounts/password_reset_complete.html'
    # ), name='password_reset_complete'),
]
