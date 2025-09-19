# Teste de Backend - CodeLeap Network API

API RESTful desenvolvida em Django e Django REST Framework como parte do processo seletivo da CodeLeap. A API implementa as funcionalidades de CRUD para posts em uma rede social.

## Pré-requisitos

- Python 3.9+
- Git

## Como Executar o Projeto

1.  **Clone o repositório:**
    ```sh
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd SEU_REPOSITORIO
    ```

2.  **Crie e ative um ambiente virtual:**
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Aplique as migrações do banco de dados:**
    ```sh
    python manage.py migrate
    ```

5.  **Inicie o servidor:**
    ```sh
    python manage.py runserver
    ```
A API estará disponível em `http://127.0.0.1:8000/careers/`.

## Endpoints da API

| Método | URL                  | Ação                | Corpo (JSON) de Exemplo                                 |
|--------|----------------------|---------------------|---------------------------------------------------------|
| `GET`  | `/careers/`          | Listar todos os posts | N/A                                                     |
| `POST` | `/careers/`          | Criar um novo post  | `{ "username": "john", "title": "t", "content": "c" }` |
| `PATCH`| `/careers/{id}/`     | Atualizar um post     | `{ "title": "novo título", "content": "novo conteúdo" }`  |
| `DELETE`| `/careers/{id}/`     | Deletar um post       | N/A                                                     |