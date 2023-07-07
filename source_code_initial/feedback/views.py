from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from django.shortcuts import render
from .tasks import gerar_relatorio_async

from django.http import JsonResponse

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
    
def long_polling_view(request):
    if request.method == 'POST':
        # Lógica para processar os dados recebidos na solicitação de long polling
        # Execute qualquer ação necessária e prepare a resposta
        
        # Exemplo de resposta
        data = {
            'status': 'success',
            'message': 'Dados recebidos e processados com sucesso.'
        }
        
        # Retorne a resposta em formato JSON
        return JsonResponse(data)


class SuccessView(TemplateView):
    template_name = "feedback/success.html"
    


