from django.http import Http404
from django.views.generic.base import TemplateView

from .models import Participant


class ContestView(TemplateView):
    """Страница конкурса"""

    template_name = 'contest/contest.html'
