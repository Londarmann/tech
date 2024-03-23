from django.urls import path

from .views import CategoryListView, CategoryDetailView

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

]
