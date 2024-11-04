from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render
from MyApps1.models import Students
#from django.core.urlresolvers import reverse_Jazy #old-lib
from django.urls import reverse_lazy	#new-lib
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
# Create your views here.
class StudentsListView(ListView):
    model = Students

class StudentsDetailView(DetailView):
    model = Students

class StudentsCreateView(CreateView):
    model = Students
    #fields=('empno', 'ename','job', 'sal')
    fields = '__all__'

class StudentsUpdateView(UpdateView):
    model = Students
    fields = ('name', 'dept', 'marks')

class StudentsDeleteView(DeleteView):
    model = Students
    success_url = reverse_lazy('home')



