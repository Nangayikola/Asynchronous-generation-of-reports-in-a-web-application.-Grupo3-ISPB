# tasks.py

from celery import shared_task
from time import sleep


@shared_task
def gerar_relatorio_async():
    # Simulação de geração de relatório (substitua com sua lógica real)
    sleep(10)  # Simula uma operação de longa duração
    # Código para gerar o relatório aqui

    return 'Relatório gerado com sucesso'
