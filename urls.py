from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('orderplaced/',views.orderplaced),
    path('restaurant/',views.restuarent,name='restuarant'),
    path('register/user/',views.customerRegister,name='register'),
    path('login/user/',views.customerLogin,name='login'),
    path('login/restaurant/',views.restLogin,name='rlogin'),
    path('register/restaurant/',views.restRegister,name='rregister'),
    path('profile/restaurant/',views.restaurantProfile,name='rprofile'),
    path('profile/user/',views.customerProfile,name='profile'),
    path('user/create/',views.createCustomer,name='ccreate'),
    path('user/update/<int:id>/',views.updateCustomer,name='cupdate'),
    path('restaurant/create/',views.createRestaurant,name='rcreate'),
    path('restaurant/update/<int:id>/',views.updateRestaurant,name='rupdate'),
    path('restaurant/orderlist/',views.orderlist,name='orderlist'),
    path('restaurant/menu/',views.menuManipulation,name='mmenu'),
    path('logout/',views.Logout,name='logout'),
    path('restaurant/<int:pk>/',views.restuarantMenu,name='menu'),
    path('checkout/',views.checkout,name='checkout'),
    path('myorders/',views.myorders,name='myorders'),
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    