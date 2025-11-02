from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hour = datetime.now().hour
        if 0 <= hour < 6:
            greeting = "Доброй ночи"
        elif 6 <= hour < 12:
            greeting = "Доброе утро"
        elif 12 <= hour < 18:
            greeting = "Добрый день"
        else:
            greeting = "Добрый вечер"

        context["current_time"] = greeting
        return context
