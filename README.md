
# Django Rest Blog

This project is a simple Blog API built using Django and Django REST Framework. It allows users to create, update, delete, and view blog posts. The project includes essential CRUD (Create, Read, Update, Delete) functionalities for managing blog posts through RESTful APIs.

**P.S**: This project does not have any comments. It was for learning DRF and I did not write any comment for it. So please accept my apology.

## Features

- **User Authentication**: Uses Django's authentication system.
- **Blog Post Management**: Create, Read, Update, and Delete blog posts.
- **REST API**: All actions are exposed via API endpoints using Django REST Framework.
- **Pagination**: Blog posts are paginated for easier viewing of large data sets.
- **Background Tasks**: Manages background tasks using threads and celery.
- **Permissions**: Basic permission checks to ensure authenticated users can perform actions.

## Technologies Used

- **Django**: Web framework for the backend.
- **Django REST Framework**: Toolkit to build Web APIs.
- **SQLite**: Default database for development. (going to be changed to postgresql soon)
- **Celery**: Used to handle background tasks.
- **Docker** (optional): To run the project in a containerized environment.

## Requirements

- Python 3.x
- Django 3.x or higher
- Django REST Framework
- Docker (Optional, if you want to run using containers)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/PooyanGnb/Django-Rest-Blog.git
    cd Django-Rest-Blog
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the server:

    ```bash
    python manage.py runserver
    ```

The project will be available at `http://127.0.0.1:8000/`.

## API Endpoints

The following endpoints are available:

- `GET /api/posts/`: Retrieve a list of all blog posts.
- `GET /api/posts/<id>/`: Retrieve a single blog post by its ID.
- `POST /api/posts/`: Create a new blog post (authentication required).
- `PUT /api/posts/<id>/`: Update an existing blog post by its ID (authentication required).
- `DELETE /api/posts/<id>/`: Delete a blog post by its ID (authentication required).

## Authentication

Authentication is required for creating, updating, and deleting blog posts. The project uses Django's default authentication system with token-based authentication from Django REST Framework.

You can authenticate by passing a token in the request header:

```bash
Authorization: Token <your-token>
```

## Running with Docker

To run the project using Docker, follow these steps:

1. Build the Docker image:

    ```bash
    docker-compose build
    ```

2. Run the Docker containers:

    ```bash
    docker-compose up
    ```

The project will be accessible at `http://127.0.0.1:8000/`.

## Tests

To run the test suite:

```bash
python manage.py test
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Feel free to contribute by submitting a pull request. Please ensure all tests pass before submitting your PR.

---

### Author

This project is developed and maintained by [PooyanGnb](https://github.com/PooyanGnb).