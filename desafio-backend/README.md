# University API

### Instalando as dependềncias
---

Para instalar as dependências com o pip basta executar:

```bash
$ pip install -r requirements.txt 
```

### Criando o banco de dados
---

Para criar o banco de dados, é necessário apenas executar o script **`create_database.py`** e o banco será automaticamente criado baseado nos arquivos SQL encontrados na pasta **`database`**. O comando utilizado é:

```bash
$ python create_database.py
```

### Executando a API
---

Para executar a API basta rodar o comando:

```bash
$ uvicorn main:app
```

Assim a aplicação vai estar no endereço `http://localhost:8000`.

### Testando a API
---

Em relação aos testes, eles podem ser feitos utilizando a interface do Swagger, presente por padrão no FastAPI. Para acessar essa interface basta entrar no endereço `http://localhost:8000/docs`.

