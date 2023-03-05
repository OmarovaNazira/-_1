from django.urls import path
from todo_app import views

urlpatterns = [
    path('', views.home_page),
    path('categories/<int:pk>', views.category_page),
    path('about', views.about_page),
    path('todo_app/categories', views.categories_handler),
    path('todo_app/categories/<int:pk>', views.category_handler),
    path('todo_app/categories/<int:pk>/products', views.category_products_handler),
    path('todo_app/products', views.products_handler),
    path('todo_app/products/<int:pk>', views.product_handler)
]
