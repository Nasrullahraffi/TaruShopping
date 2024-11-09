from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from app.forms import LoginForm, MyPassChangeForm, PassResetForm, PassResetDone
from django.contrib.auth.models import User



urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductdetailView.as_view(), name='product-detail'),
    path('showcart', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart, name="pluscart" ),
    path('removecart/', views.remove_cart ),
    path('minuscart/', views.minus_cart),
    path('add-to-cart', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('orders/', views.orders, name='orders'),
    path('accounts/password_change', auth_view.PasswordChangeView.as_view(template_name='app/changepassword.html', success_url='/passchangedone')
    , name='changepassword'),
    path('passchangedone', auth_view.PasswordChangeDoneView.as_view(template_name='app/passdone.html'), name='passchangedone'),
    path('password_reset', auth_view.PasswordResetView.as_view(template_name='app/passreset.html', form_class=PassResetForm,)
    ,name='password_reset'),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='app/passresetdone.html',),name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='app/passresetconfirm.html'),name='password_reset_confirm'),
    path('password_reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='app/passresetcomplete.html',),name='password_reset_complete'),
    path('mobile/', views.mobile, name='mobile'),
    path('topwear/', views.topwear, name='topwear'),
    path('shoes/', views.shoes, name='shoes'),
    path('bottomwear/', views.bottomwear, name='bottomwear'),

    path('accounts/login',auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    
    path('logout', views.logout_view, name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
