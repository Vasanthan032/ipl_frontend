from django.views.generic import TemplateView, ListView
# from django.contrib.auth.mixins import LoginRequiredMixin
from analysis import models

class HomePage(ListView):
    template_name = "index.html"
    model = models.Stadium

class TestPage(TemplateView):
    template_name = "test.html"

class ThanksPage(TemplateView):
    template_name = "thanks.html"
