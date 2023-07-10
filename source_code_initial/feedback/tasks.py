# tasks.py

from celery import shared_task
from time import sleep
from .models import Report


@shared_task
def gerar_relatorio_async(report_id):
    report = Report.objects.get(id=report_id)
    # Lógica para gerar o relatório
    # Salvar o arquivo do relatório no caminho correto
    report.file_path = '/path/to/generated_report.pdf'
    report.status = 'completed'
    report.save()

