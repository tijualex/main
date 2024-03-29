# user/urls.py
from django.urls import include, path
from user import views
from user.views import create_design
from .views import myorders

from django.contrib.auth import views as auth_views

urlpatterns = [
    # general
    path('accounts/', include('allauth.urls')),
    path('login_view/', views.login_view, name='login_view'),   # URL for login
    path('signup', views.signup, name='signup'),  # URL for signup
    path('', views.index, name='index'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('design/', views.design, name='design'),
    
    
    path('check-username-exists/', views.check_username_exists, name='check-username-exists'),
    
    #forgot password
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    #profile
    path('profile', views.profile, name='profile'),
  
    #google
    path('accounts/', include('allauth.urls')),
    
    
    
    # design
    
    path('dress_detail/<str:dress_type>/', views.dress_detail, name='dress_detail'),
    path('pattern_details/<int:pattern_id>/<str:pattern_type>/', views.pattern_details, name='pattern_details'),
    path('confirm_design', views.confirm_design, name='confirm_design'),
    path('display_selected_patterns/<str:selected_patterns>/<str:selected_pattern_id>/<str:total_price>/', views.display_selected_patterns, name='display_selected_patterns'),
    path('create_design/', views.create_design, name='create_design'),    
    # mesurement
    path('measurement/<int:design_id>/', views.measurement_view, name='measurement_view'),
    
    
    #order
    path('order_confirmation_view/<int:design_id>', views.order_confirmation_view, name='order_confirmation_view'),
    path('create_order/', views.create_order, name='create_order'),
    path('add_address/',views.add_address, name='add_address'),
    



    # payment
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('payment_confirm/<int:order_id>',views.payment_confirm, name='payment_confirm'),
    
    
    #myorders
    path('myorders/', views.myorders, name='myorders'),
    path('export_order_details_pdf/<int:order_id>/', views.export_order_details_pdf, name='export_order_details_pdf'),

    #mydesigns
    path('my_designs/', views.my_designs, name='my_designs'),
    path('design/<int:design_id>/', views.view_design, name='view_design'),
    
    
    
    path('community/', views.community, name='community'),
    path('send_message/', views.send_message, name='send_message'),
    
]
