# Wolverine

## Requisitos da aplicação

### Atividade 1

- Implementar uma aplicação cliente com as seguintes características:

- [ ] Carregar a partir de um arquivo local um sinal de ultrassom;
- [x] Realizar o controle de ganho de sinal através do procedimento descrito abaixo;
- [ ] Enviar o sinal tratado para um servidor de reconstrução de imagens;
- [ ] Carregar a partir do servidor todas as imagens reconstruídas por um usuário.
- [ ] Selecionar uma ou mais imagens e salvar localmente.

- Cada imagem deverá conter no mínimo os seguintes dados:

- [ ] Identificação do usuário;
- [ ] Data e hora do início da reconstrução;
- [ ] Data e hora do término da reconstrução;
- [ ] Tamanho em pixels;
- [ ] O número de iterações executadas.


### Atividade 2

- Implementar um servidor para reconstrução de imagens:

- [ ] Receber os dados para reconstrução;
- [ ] Carregar o modelo de reconstrução de acordo com os parâmetros recebidos;
- [x] Executar o algoritmo de reconstrução;
- [x] Executar até que a norma L2 do resíduo (r) seja menor do que 1e10-4 .
- [ ] Salvar o resultado.


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
