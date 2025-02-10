from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('<int:product_id>/<int:review_id>/feedback/<int:choice>/',
         views.review_feedback, name='review_feedback'),
    path('<int:product_id>/<int:review_id>/delete/',
         views.delete_review, name='delete_review'),
    path('my-products/', views.my_products, name='my_products'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
