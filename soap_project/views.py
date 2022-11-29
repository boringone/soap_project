from django.views.generic import TemplateView
from django.shortcuts import render

class RecipiesView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {'context_variable': 'value'}


def my_view(request, path=''):
    return render(request=request, template_name='templates/index.html', context={'context_variable': 'value'})
