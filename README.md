# Wolverine

## Requisitos da aplicação

### Atividade 1

#### Implementar uma aplicação cliente com as seguintes características:

- [x] Carregar a partir de um arquivo local um sinal de ultrassom;
- [x] Realizar o controle de ganho de sinal através do procedimento descrito abaixo;
- [x] Enviar o sinal tratado para um servidor de reconstrução de imagens;
- [x] Carregar a partir do servidor todas as imagens reconstruídas por um usuário.
- [x] Selecionar uma ou mais imagens e salvar localmente.

#### Cada imagem deverá conter no mínimo os seguintes dados:

- [x] Identificação do usuário;
- [x] Data e hora do início da reconstrução;
- [x] Data e hora do término da reconstrução;
- [x] Tamanho em pixels;
- [x] O número de iterações executadas.


### Atividade 2

#### Implementar um servidor para reconstrução de imagens:

- [x] Receber os dados para reconstrução;
- [x] Carregar o modelo de reconstrução de acordo com os parâmetros recebidos;
- [x] Executar o algoritmo de reconstrução;
- [x] Executar até que a norma L2 do resíduo (r) seja menor do que 1e10-4 .
- [x] Salvar o resultado.


### Requisitos Não-funcionais

- [x] Bootstrap 4
- [x] Registro de usuários
- [x] Salvar e carregar arquivos de diretório específico (ENV)
- [x] Carregar arquivo do modelo de diretório específico (ENV)
- [ ] Fluxos de exceção nas telas
- [x] Redirect e flash nos formulários


## Rodando o Projeto

### Redis
```
docker run --rm --name wolverine -p 6379:6379 redis
```

### Celery
```
celery worker -A worker.wolverine_workers
```

### Flower
```
celery worker -A worker.wolverine_workers --concurrency=1
```

### Django Development Server
```
python manage.py runserver
```
