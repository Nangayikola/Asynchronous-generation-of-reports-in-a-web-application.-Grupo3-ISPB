from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from django.shortcuts import render
from .tasks import gerar_relatorio_async

from feedback.forms import FeedbackForm


class FeedbackFormView(FormView):
    template_name = "feedback/feedback.html"
    form_class = FeedbackForm
    success_url = "/success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
    
    # views.py
def gerar_relatorio(request):
    if request.method == 'POST':
        # Iniciar a tarefa assíncrona
        task = gerar_relatorio_async.delay()
        context = {'task_id': task.id}
        return render(request, 'report.html', context)
    else:
        return render(request, 'index.html')


class SuccessView(TemplateView):
    template_name = "feedback/success.html"
    


