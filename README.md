# API de Posts - Teste Técnico CodeLeap

![Status](https://img.shields.io/badge/status-concluído-brightgreen)

API RESTful desenvolvida como parte do desafio técnico para a vaga de Backend na CodeLeap. O projeto implementa um CRUD completo para gerenciar posts de uma rede social, seguindo as especificações fornecidas.

## 🚀 Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias:

- **Python**
- **Django**
- **Django REST Framework**

## ✨ Funcionalidades

A API oferece a funcionalidade de um CRUD (Create, Read, Update, Delete) para posts, permitindo:

-   ✅ Criar um novo post.
-   ✅ Listar todos os posts existentes, ordenados do mais recente para o mais antigo.
-   ✅ Visualizar os detalhes de um post específico.
-   ✅ Atualizar parcialmente as informações de um post (título e conteúdo).
-   ✅ Deletar um post.

## ⚙️ Como Executar o Projeto

Para rodar este projeto localmente, siga os passos abaixo.

### **Pré-requisitos**

-   [Python 3.9+](https://www.python.org/downloads/)
-   [Git](https://git-scm.com/)

### **Instalação**

1.  **Clone o repositório:**
    ```sh
    git clone [https://github.com/franciscomaath/api_posts_codeleap.git](https://github.com/franciscomaath/api_posts_codeleap.git)
    cd api_posts_codeleap
    ```

2.  **Crie e ative um ambiente virtual:**
    ```sh
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
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

5.  **Inicie o servidor de desenvolvimento:**
    ```sh
    python manage.py runserver
    ```

A API estará disponível para testes no endereço: `http://127.0.0.1:8000/careers/`

## Endpoints da API

A URL base para todos os endpoints é `/careers/`.

| Método | Endpoint         | Ação                | Exemplo de Corpo (JSON)                                |
| :----- | :--------------- | :------------------ | :----------------------------------------------------- |
| `GET`  | `/`              | Listar todos os posts | N/A                                                    |
| `POST` | `/`              | Criar um novo post  | `{ "username": "string", "title": "string", "content": "string" }` |
| `GET`  | `/<int:id>/`     | Obter um post específico | N/A                                                    |
| `PATCH`| `/<int:id>/`     | Atualizar um post     | `{ "title": "string", "content": "string" }`           |
| `DELETE`| `/<int:id>/`     | Deletar um post       | N/A                                                    |

## Autor

Feito por **Francisco Maath**.

[![GitHub](https://img.shields.io/badge/GitHub-franciscomaath-blue?logo=github)](https://github.com/franciscomaath)
