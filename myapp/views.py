from django.shortcuts import render
from django.views import generic
from .models import*
from hitcount.views import HitCountDetailView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from .forms import RapistForm
from django.urls import reverse_lazy
from .filters import SinppetFilter

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
class RapistDetail(HitCountDetailView):
    model = Rapiest
    context_object_name = 'post'
    template_name = "myapp/rapist_detail.html"
    count_hit = True

class PostLIst(ListView):
    model = Rapiest
    form_class = RapistForm
    template_name = "myapp/home.html"
    ordering = ['-id']
    paginate_by = 2
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = SinppetFilter(self.request.GET,queryset=self.get_queryset())
        return context
    



class AddRppist(CreateView):
    model = Rapiest 
    form_class = RapistForm
    template_name='myapp/add_rapist.html'
    success_url = reverse_lazy('home')
    

class UpdateRapist(UpdateView):
    model = Rapiest
    template_name = 'myapp/update.html'
    fields = '__all__'


class DeleteRapist(DetailView):
    model = Rapiest
    template_name = 'myapp/delete_rapist.html'
    success_url = reverse_lazy('home')




#User Register part

class UserRegister(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'myapp/register.html'
    success_url = reverse_lazy('login')




# def index(request):

#     rapist = Rapiest.objects.all()
#     rapist.views = rapist.views+1
#     rapist.save()
#     return render(request,'myapp/home.html',{'rapist':rapist})


