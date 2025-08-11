from django.urls import path
from . import views
from django.contrib.auth import views as v

urlpatterns = [
    path('',views.index ,name='index'),
    path('/create-book',views.BookCreate.as_view() ,name='create_book'),
    path('/detail-book/<int:pk>',views.BookDetail.as_view() ,name='book_detail'),
    path('/list-book',views.BookListView.as_view() ,name='list_book'),
    
    path('accounts/register',views.register.as_view() ,name='register'),
    path('accounts/pass-change',v.PasswordChangeView.as_view(template_name='registration/change-pass.html',success_url='/'),name='pass-change')
    

]
