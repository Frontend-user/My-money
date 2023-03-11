from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('false/', views.false, name='false'),
    path('categories/', views.categories_show, name='categories_show'),
    # path('statistics/', views.statistics_show, name='statistics_show'),
    path('categories/add/', views.categories_add, name='categories_add'),
    path('categories/delete/<int:category_id>/', views.categories_delete, name='categories_delete'),
    path('categories/categories_open/<int:category_id>/', views.categories_open, name='categories_open'),
    path('categories/categories_open/expense_add/<int:category_id>/', views.expense_add, name='expense_add'),
    path('categories/categories_open/expense_delete/<int:expense_id>/', views.expense_delete, name='expense_delete'),

]
