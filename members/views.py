from django.views import generic
from django.urls import reverse_lazy
from .models import Member

class IndexView(generic.ListView):
    template_name = 'members/index.html'
    context_object_name = 'member_list'

    def get_queryset(self):
      """Return all the members on the roster."""
      return Member.objects.all()

class CreateView(generic.edit.CreateView):
  template_name = 'members/create.html'
  model = Member
  fields = ['message']
  success_url = reverse_lazy('members:index')

class UpdateView(generic.edit.UpdateView):
    template_name = 'members/update.html'
    model = Member
    fields = ['message']
    success_url = reverse_lazy('members:index')

class DeleteView(generic.edit.DeleteView):
    template_name = 'members/delete.html'
    model = Member
    success_url = reverse_lazy('members:index')

