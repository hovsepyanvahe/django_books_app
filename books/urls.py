from django.urls import path
from .views import BooksView, SectionCreateView, SectionEditView, GrantAccessView

urlpatterns = [
    path('books/', BooksView.as_view(), name='books'),
    path('create-section/', SectionCreateView.as_view(), name='section-create'),
    path('edit-section/<int:pk>', SectionEditView.as_view(), name='section-edit'),
    path('grant-access/', GrantAccessView.as_view(), name='grant-access'),

]