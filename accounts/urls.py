from django.urls import path
from . import views
from .views import redirect_view, redirect_plannets, redirect_corps, redirect_lumin, redirect_varsta, redirect_gravity,redirect_contact, SearchResultsView


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('jolie/', redirect_view, name ="redirect"),
    path('planets/', redirect_plannets, name ="plannets"),
    path('corps/', redirect_corps, name ="corps"),
    path('lumin/', redirect_lumin, name ="lumin"),
    path('viteze/', redirect_gravity, name ="viteze"),
    path('varsta/', redirect_varsta, name ="varsta"),
    path('contact/', redirect_contact, name="contact"),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('contributor/<str:pk_test>/', views.contributor, name="contributor"),
    path('object/', views.object, name="object"),
    path('articles/', views.article, name="articles"),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('add_object', views.addObject, name="add_object"),
    path('add_contributor', views.addContributor, name="add_contributor"),
    path('add_article', views.addArticle, name="add_article"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    

]