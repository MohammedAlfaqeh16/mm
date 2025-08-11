from django.shortcuts import render,HttpResponse
from . import models
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
   num_book= models.Book.objects.all().count()
   authers = models.Author.objects.all().count()
   num_book_instanc =models.BookInstance.objects.all().count()
   num_book_instanc_av =models.BookInstance.objects.filter(status__exact='a').count
   context={
      'num_book':num_book,
      'num_book_instanc':num_book_instanc,
      'num_book_instanc_av':num_book_instanc_av
      ,'authers':authers
   }
   
   return render(request , 'index.html',context)


class BookCreate(LoginRequiredMixin,generic.CreateView):
   model =models.Book
   fields='__all__'
   
   success_url='/library/list-book'
   template_name='create.html'

class register(generic.CreateView):
   form_class = UserCreationForm
   success_url='/accounts/login'
   template_name='registration/register.html'
   
   
   

class BookListView(generic.ListView):
    model =models.Book
    template_name = "list.html"
    context_object_name ='books'

class BookDetail(generic.DetailView):
    model = models.Book
    template_name = "detail.html"
    context_object_name ='books'

