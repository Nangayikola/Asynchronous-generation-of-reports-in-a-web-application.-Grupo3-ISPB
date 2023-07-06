# Aplicativo de Geração Assíncrona de Relatórios

Este é um aplicativo web que permite aos usuários gerar relatórios a partir dos dados fornecidos por eles. A geração dos relatórios é realizada de forma assíncrona em segundo plano, utilizando o framework Django e a biblioteca Celery. Além disso, o long polling é utilizado para fornecer um link quando o relatório estiver pronto.

## Funcionalidades

- Os usuários podem solicitar a geração de um relatório, fornecendo os dados necessários.
- O relatório é gerado de forma assíncrona em segundo plano, para não congelar o aplicativo web durante o processo.
- O long polling é utilizado para verificar periodicamente o status do relatório.
- O Celery é utilizado como sistema de fila para executar as tarefas assíncronas de geração de relatórios.
- O Redis é utilizado como backend de filas para o Celery.

## Requisitos do Sistema

- Python 3.x
- Django
- Celery
- Redis

## Instalação

1. Clone o repositório:

```
git clone https://github.com/Nangayikola/Asynchronous-generation-of-reports-in-a-web-application.-Grupo3-ISPB.git
```

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Configure o ambiente:

Certifique-se de ter o Redis instalado e em execução em sua máquina. Atualize as configurações do Celery no arquivo `settings.py` com as informações corretas do seu ambiente.

4. Execute as migrações do banco de dados:

```
python manage.py migrate
```

5. Inicie o Celery:

```
celery -A nome_do_projeto worker --loglevel=info
```

6. Inicie o servidor de desenvolvimento do Django:

```
python manage.py runserver
```

7. Acesse o aplicativo no navegador:

```
http://127.0.0.1/:8000
```

## Uso

1. Na página inicial do aplicativo, preencha o formulário com os dados necessários para a geração do relatório.
2. Clique no botão "Gerar Relatório".
3. Uma mensagem será exibida informando que o relatório está sendo gerado.
4. O long polling verificará periodicamente o status do relatório.
5. Quando o relatório estiver pronto, um link de download será fornecido para o usuário.
6. O usuário pode clicar no link para baixar o relatório gerado.

## Contribuição

As contribuições são bem-vindas! Se você encontrar algum problema ou tiver alguma sugestão de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.
