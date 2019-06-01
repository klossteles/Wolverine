# Wolverine

## Requisitos da aplicação

### Atividade 1

- Implementar uma aplicação cliente com as seguintes características:

1. Carregar a partir de um arquivo local um sinal de ultrassom;
2. Realizar o controle de ganho de sinal através do procedimento descrito abaixo;
3. Enviar o sinal tratado para um servidor de reconstrução de imagens;
4. Carregar a partir do servidor todas as imagens reconstruídas por um usuário.
5. Selecionar uma ou mais imagens e salvar localmente.

- Cada imagem deverá conter no mínimo os seguintes dados:

1. Identificação do usuário;
2. Data e hora do início da reconstrução;
3. Data e hora do término da reconstrução;
4. Tamanho em pixels;
5. O número de iterações executadas.


### Atividade 2

- Implementar um servidor para reconstrução de imagens:

1. Receber os dados para reconstrução;
2. Carregar o modelo de reconstrução de acordo com os parâmetros recebidos;
3. Executar o algoritmo de reconstrução;
4. Executar até que a norma L2 do resíduo (r) seja menor do que 1e10-4 .
5. Salvar o resultado.


## Running

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
celery -A worker.wolverine_workers flower
```

### Django Development Server
```
python manage.py runserver
```