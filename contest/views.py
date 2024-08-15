from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic import CreateView


from .forms import ParticipantForm

from .models import Participant


def ContestView(request):
    """Страница конкурса"""
    participants = Participant.objects.all().order_by('-created_at')  # <--- Add this line
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
    return render(request, 'contest/contest.html', {'form': form, 'massege': massege, 'participants': participants})
