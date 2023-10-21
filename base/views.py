from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.urls import path
from . import views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


from .models import Task
from .forms import PostForm
#import here messages for django  https://www.youtube.com/watch?v=8kBo91L8JTY
from django.contrib import messages

# Login and Register Page
class CustomLoginView(LoginView):
    template_name = 'login-register/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

# Register view page
class RegisterPage(FormView):
    template_name = 'login-register/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


# Tasks DetailView,CreateView, Task Update, Delete View

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'todoapp-create-update-delete/task_form.html'
    form_class = PostForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Task was created successfully")
        return super(TaskCreate, self).form_valid(form)




class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = PostForm
    template_name = 'todoapp-create-update-delete/task_form.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, "Task updated successfully")
        return super(TaskUpdate, self).form_valid(form)




class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'todoapp-create-update-delete/task_confirm_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Todo list updated sucesfully")
        return super().delete(request, *args, **kwargs)


# Pages : Homepage, Manual Page
@login_required
def homepage(request):
  mydata = Task.objects.filter(user=request.user)
  freq_count_d = Task.objects.filter(user=request.user, frequency="Daily").count()
  freq_count_w = Task.objects.filter(user=request.user, frequency="Weekly").count()
  freq_count_m = Task.objects.filter(user=request.user, frequency="Monthly").count()
  freq_count_y = Task.objects.filter(user=request.user, frequency="Yearly").count()
  template = loader.get_template('todoapp-create-update-delete/homepage.html')
  context = {
    'mymembers': mydata,
    'freq_count_d': freq_count_d,
    'freq_count_w': freq_count_w,
    'freq_count_m': freq_count_m,
    'freq_count_y': freq_count_y,
  }
  return HttpResponse(template.render(context, request))

@login_required
def manual(request):
  mydata = Task.objects.all()
  template = loader.get_template('todoapp-create-update-delete/manual.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))



def custom_404(request, exception):
    return render(request, '404.html', status=404)


def test(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'test.html', context)



def test(request):
  mydata = Task.objects.filter(user=request.user)
  freq_count_d = Task.objects.filter(user=request.user, frequency="Daily").count()
  freq_count_w = Task.objects.filter(user=request.user, frequency="Weekly").count()
  freq_count_m = Task.objects.filter(user=request.user, frequency="Monthly").count()
  freq_count_y = Task.objects.filter(user=request.user, frequency="Yearly").count()
  template = loader.get_template('test.html')
  context = {
    'mymembers': mydata,
    'freq_count_d': freq_count_d,
    'freq_count_w': freq_count_w,
    'freq_count_m': freq_count_m,
    'freq_count_y': freq_count_y,
  }
  return HttpResponse(template.render(context, request))