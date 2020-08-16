from django.urls import path
from . import views 

urlpatterns = [ 
    path('', views.store, name="store"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user"),
    path('footer/', views.footerPage, name="footer"),

    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('product/<str:pk_test>/', views.product, name="product"),
	path('create_product/', views.createProduct, name="create_product"),


]