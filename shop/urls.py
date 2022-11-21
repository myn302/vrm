from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path ("", views.index, name = 'MyShop'),
    path ("productpage/<int:id>", views.singleProductPage, name = 'singleProductPage'),
    path ("search/", views.search, name = 'search'),
    path ("refundRequest/", views.refundRequest, name = 'refundRequest'),
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handleLogin, name="handleLogin"),
    path('logout/', views.handleLogout, name="handleLogout"),
    path ("checkout/", views.checkout, name = 'checkout'),
    path ("ordersuccess/", views.orderSuccess, name = 'orderSuccess')

]
