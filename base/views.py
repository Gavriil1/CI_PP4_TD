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

from .models import Task
from .forms import PostForm

# Login and Register Page
class CustomLoginView(LoginView):
    template_name = '/workspace/CI_PP4_TD/templates/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

# Register view page
class RegisterPage(FormView):
    template_name = '/workspace/CI_PP4_TD/templates/register.html'
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
    template_name = '/workspace/CI_PP4_TD/templates/task_form.html'
    # fields = ['title', 'description', 'complete']
    # fields = '__all__'
    form_class = PostForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = PostForm
    template_name = '/workspace/CI_PP4_TD/templates/task_form.html'
    # fields = '__all__'
    # fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = '/workspace/CI_PP4_TD/templates/task_confirm_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

# Pages : Homepage, Manual Page
@login_required
def homepage(request):
  mydata = Task.objects.filter(user=request.user)
  freq_count_d = Task.objects.filter(user=request.user, frequency="Daily").count()
  # freq_count_d = Task.objects.filter(frequency="Daily").count()
  freq_count_w = Task.objects.filter(user=request.user, frequency="Weekly").count()
  freq_count_m = Task.objects.filter(user=request.user, frequency="Monthly").count()
  freq_count_y = Task.objects.filter(user=request.user, frequency="Yearly").count()
  template = loader.get_template('/workspace/CI_PP4_TD/templates/homepage.html')
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
  template = loader.get_template('/workspace/CI_PP4_TD/templates/manual.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))


# class TaskList(LoginRequiredMixin, ListView):
#     model = Task
#     context_object_name = 'tasks'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tasks'] = context['tasks'].filter(user=self.request.user)
#         context['count'] = context['tasks'].filter(complete=False).count()

#         search_input = self.request.GET.get('search-area') or ''
#         if search_input:
#             context['tasks'] = context['tasks'].filter(title__icontains=search_input)

#         context['search_input'] = search_input
#         return context

# 404 page for django
def custom_404(request, exception):
    return render(request, '/workspace/CI_PP4_TD/templates/404.html', status=404)


def test(request):
  mydata = Task.objects.filter(user=request.user)
  freq_count_d = Task.objects.filter(frequency="Daily").count()
  freq_count_w = Task.objects.filter(frequency="Weekly").count()
  freq_count_m = Task.objects.filter(frequency="Monthly").count()
  freq_count_y = Task.objects.filter(frequency="Yearly").count()
  template = loader.get_template('/workspace/CI_PP4_TD/templates/test.html')
  context = {
    'mymembers': mydata,
    'freq_count_d': freq_count_d,
    'freq_count_w': freq_count_w,
    'freq_count_m': freq_count_m,
    'freq_count_y': freq_count_y,
  }
  return HttpResponse(template.render(context, request))
