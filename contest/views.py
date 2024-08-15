from django.views import View
from django.shortcuts import render
from .forms import ParticipantForm
from .models import Participant

class ContestView(View):
    """Страница конкурса"""
    template_name = 'contest/contest.html'
    message = ''

    def get(self, request):
        participants = Participant.objects.all().order_by('-created_at')
        form = ParticipantForm()
        return render(request, self.template_name, {'form': form, 'participants': participants, 'message': self.message})

    def post(self, request):
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            self.message = 'Спасибо за участие!'
        else:
            self.message = 'Ошибка'
        participants = Participant.objects.all().order_by('-created_at')
        return render(request, self.template_name, {'form': form, 'message': self.message, 'participants': participants})
