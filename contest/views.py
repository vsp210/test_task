from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic import CreateView


from .forms import ParticipantForm

from .models import Participant


# class ContestView(CreateView):
#     """Страница конкурса"""
#     template_name = 'contest/contest.html'
#     model = Participant
#     form_class = ParticipantForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         massege = ''
#         context['massege'] = massege
#         return context

#     def form_valid(self, form):
#         if form.is_valid():
#             massege = "Спасибо за участие!"
#             self.object = form.save()  # сохраняем модель в базе данных
#             return super().form_valid(form)
#         else:
#             print('sgdfdsg')
#             return super().form_invalid(form)

def ContestView(request):
    """Страница конкурса"""
    participant = Participant.objects.all()
    massege = ''
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            massege = 'Спасибо за участие!'
        else:
            massege = 'Ошибка'
    else:
        form = ParticipantForm()
    return render(request, 'contest/contest.html', {'form': form, 'massege': massege})
