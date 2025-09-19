# API de Posts - Teste Técnico CodeLeap

![Status](https://img.shields.io/badge/status-concluído-brightgreen)

API RESTful desenvolvida como parte do desafio técnico para a vaga de Backend na CodeLeap. O projeto implementa um CRUD completo para gerenciar posts, com funcionalidades avançadas como comentários, likes, autenticação por token, paginação, filtros e documentação automática Swagger.

## 🚀 Tecnologias Utilizadas

- **Python**
- **Django**
- **Django REST Framework**
- **drf-spectacular** (para geração de documentação OpenAPI/Swagger)

## ✨ Funcionalidades

-   ✅ **Autenticação Completa:** Sistema seguro de autenticação por Token.
-   ✅ **CRUD de Posts:** Operações completas de Criação, Leitura, Atualização e Deleção para posts.
-   ✅ **Sistema de Comentários:** Endpoint para adicionar comentários a um post específico.
-   ✅ **Sistema de Likes:** Endpoint para curtir e descurtir posts (toggle).
-   ✅ **Paginação:** Respostas de listagem são paginadas para melhor performance.
-   ✅ **Busca e Ordenação:** A lista de posts pode ser dinamicamente buscada por texto (`?search=`) e ordenada por diferentes campos (`?ordering=`).
-   ✅ **Documentação Automática:** Geração automática de uma documentação interativa com Swagger UI.

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

5.  **Crie um superusuário:** Como a API é protegida, você precisará de um usuário para se autenticar e testar.
    ```sh
    python manage.py createsuperuser
    ```
    (siga os prompts para criar seu usuário e senha)

6.  **Inicie o servidor:**
    ```sh
    python manage.py runserver
    ```

## 🔑 Como Usar a API (Autenticação)

Todos os endpoints (exceto o de login) são protegidos. Para usá-los, você primeiro precisa obter um token de autenticação.

1.  **Obtenha seu Token:**
    Faça uma requisição `POST` para `http://127.0.0.1:8000/api-token-auth/` com seu usuário e senha no corpo:
    ```json
    {
        "username": "seu_usuario",
        "password": "sua_senha"
    }
    ```
    A resposta conterá seu token.

2.  **Use o Token:**
    Em todas as outras requisições, adicione um Header chamado `Authorization` com o valor `Token seu_token_copiado_aqui`.

## 📖 Documentação da API (Swagger)

Uma documentação completa e interativa da API está disponível. Com o servidor rodando, acesse em seu navegador:

**`http://127.0.0.1:8000/api/docs/`**

Nesta página, você pode visualizar e testar todos os endpoints. Para testar os endpoints protegidos, clique no botão "Authorize" e insira seu token no formato `Token <seu_token>`.

## Endpoints da API

A URL base para os recursos principais é `/careers/`.

| Método | Endpoint                    | Ação                                                              | Corpo (JSON) de Exemplo                              |
| :----- | :-------------------------- | :---------------------------------------------------------------- | :--------------------------------------------------- |
| `POST` | `/api-token-auth/`          | Obter token de autenticação                                       | `{ "username": "...", "password": "..." }`           |
| `GET`  | `/careers/`                 | Lista posts (paginado). Aceita `?search=` e `?ordering=`.          | N/A                                                  |
| `POST` | `/careers/`                 | Cria um novo post                                                 | `{ "title": "string", "content": "string" }`         |
| `GET`  | `/careers/{id}/`            | Obtém um post e seus comentários/likes                            | N/A                                                  |
| `PATCH`| `/careers/{id}/`            | Atualiza parcialmente um post                                     | `{ "title": "string", "content": "string" }`         |
| `DELETE`| `/careers/{id}/`            | Deleta um post                                                    | N/A                                                  |
| `POST` | `/careers/{id}/like/`       | Curte ou descurte um post (toggle)                                | N/A                                                  |
| `POST` | `/careers/{post_pk}/comments/`| Adiciona um comentário a um post                                  | `{ "content": "string" }`                            |


## Autor

Feito por **Francisco Maath**.

[![GitHub](https://img.shields.io/badge/GitHub-franciscomaath-blue?logo=github)](https://github.com/franciscomaath)