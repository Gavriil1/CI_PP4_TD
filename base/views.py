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
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'base/register.html'
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
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)

        # Filter by selected importance
        selected_importance = self.request.GET.get('importance', '')
        if selected_importance:
            context['tasks'] = context['tasks'].filter(importance=selected_importance)
            context['selected_importance'] = selected_importance
        else:
            context['selected_importance'] = ''

        context['search_input'] = search_input

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # fields = ['title', 'description', 'complete']
    fields = '__all__'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    # fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


# def testing(request):
#   template = loader.get_template('base/template.html')
#   context = {
#     'fruits': ['Apple', 'Banana', 'Cherry'],   
#   }
#   return HttpResponse(template.render(context, request))
def testing(request):
  mydata = Task.objects.all()
  freq_count_d = Task.objects.filter(frequency="Daily").count()
  freq_count_w = Task.objects.filter(frequency="Weekly").count()
  freq_count_m = Task.objects.filter(frequency="Monthly").count()
  freq_count_y = Task.objects.filter(frequency="Yearly").count()
  template = loader.get_template('base/homepage.html')
  context = {
    'mymembers': mydata,
    'freq_count_d': freq_count_d,
    'freq_count_w': freq_count_w,
    'freq_count_m': freq_count_m,
    'freq_count_y': freq_count_y,
  }
  return HttpResponse(template.render(context, request))


def daily(request):
  mydata = Task.objects.all()
  freq_count_d = Task.objects.filter(frequency="Daily").count()
  template_daily = loader.get_template('base/daily.html')
  context = {
    'mymembers': mydata,
    'freq_count_d': freq_count_d,
  }
  return HttpResponse(template_daily.render(context, request))

def weekly(request):
  mydata = Task.objects.all()
  freq_count_w = Task.objects.filter(frequency="Weekly").count()
  template_weekly = loader.get_template('base/weekly.html')
  context = {
    'mymembers': mydata,
    'freq_count_w': freq_count_w,
  }
  return HttpResponse(template_weekly.render(context, request))


def monthly(request):
  mydata = Task.objects.all()
  freq_count_m = Task.objects.filter(frequency="Monthly").count()
  template_monthly = loader.get_template('base/monthly.html')
  context = {
    'mymembers': mydata,
    'freq_count_m': freq_count_m,
  }
  return HttpResponse(template_monthly.render(context, request))


def yearly(request):
  mydata = Task.objects.all()
  freq_count_y = Task.objects.filter(frequency="Yearly").count()
  template_yearly = loader.get_template('base/yearly.html')
  context = {
    'mymembers': mydata,
    'freq_count_y': freq_count_y,
  }
  return HttpResponse(template_yearly.render(context, request))
