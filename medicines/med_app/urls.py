from django.urls import path
from med_app import views

app_name = 'med_app'

urlpatterns = [
    path('', views.main_view, name='index'),
    # path('contact/', views.contacts, name='contact'),
    path('find_drug/', views.find_drug, name='find_drug'),
    path('thanks/', views.thanks, name='thanks'),
    path('comments_view/', views.CommentsViews.as_view(), name='comments_view'),
    path('comments_detail/<int:pk>/', views.CommentsDetail.as_view(), name='comments_detail'),
    path('comments_create/', views.CommentsCreate.as_view(), name='comments_create'),
    path('comments_update/<int:pk>/', views.CommentsUpdate.as_view(), name='comments_update'),
    path('comments_delete/<int:pk>/', views.CommentsDelete.as_view(), name='comments_delete'),
]