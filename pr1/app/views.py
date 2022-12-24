from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm, AuthUserForm, RegisterUserForm
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

def sign_up(request):
    return render(request, 'sign_up.html', {'title': 'Главная страница'})

def index(request):
    return render(request, 'index.html', {'title': 'Инструкция'})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'details.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'create.html'

    form_class = ArticlesForm

class NewsDeletelView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'delete.html'

class MyprojectLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthUserForm
    success_url = '/home/'
    def get_success_url(self):
        return self.success_url
    
class RegisterUserView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm
    success_url = '/home/'

class MyProjectLogout(LogoutView):
    template_name = 'sign_up.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Ошибка'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', data)
    
def news_home(request):
    app = Articles.objects.order_by('-date')
    return render(request, 'news_home.html', {'app': app})
