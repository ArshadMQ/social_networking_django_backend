# Social Networking API

This project is a Django-based social networking API. The API includes functionalities for user authentication, searching users, sending/accepting/rejecting friend requests, listing friends, and viewing pending friend requests.

## Getting Started

Follow these steps to set up and run the project.

### Prerequisites

Ensure you have the following installed:
- Python 3.9+
- Docker
- Docker Compose

### Installation

1. **Clone the repository**

    ```sh
    git clone https://github.com/ArshadQ118/social_networking_django_backend.git
    ```

2. **Navigate to the project directory**

    ```sh
    cd social_networking_django_backend
    ```

3. **Create a virtual environment**

    ```sh
    python -m venv venv
    ```

4. **Activate the virtual environment**

    ```sh
    source venv/bin/activate
    ```

5. **Install the required dependencies**

    ```sh
    pip install -r requirements.txt
    ```

6. **Migrate the database**

    ```sh
    python manage.py migrate
    ```

7. **Build and start the Docker containers**

    ```sh
    docker-compose up --build
    ```

### Testing the API

To test the API endpoints, use the provided Postman collection. Import the collection into Postman and execute the requests.

### Notes

- The default database used is SQLite.
- The Django development server will be running on port 8000. Access it at `http://localhost:8000`.
- The API endpoints require authentication for most operations. Use the authentication endpoints to obtain tokens and include them in your requests.

### Postman Collection

To simplify testing, a Postman collection is included. Import the `Social_Networking_API.postman_collection.json` file into Postman to access predefined requests for all the API endpoints.

### API Endpoints

- **User Login/Signup**
  - `POST /api/users/register/` - Sign up a new user.
  - `POST /api/users/login/` - Log in an existing user.
  
- **User Search**
  - `GET /api/users/search/?qsearch=<keyword>` - Search for users by email or name (pagination supported).

- **Friend Requests**
  - `PATCH /api/users/friend-request/<int:request_id>` Access/Reject a friend request.

- **Pending Requests**
  - `GET /api/users/pending-requests/<int:request_id>` To List friends requests
  
- **Friends List**
  - `GET /api/friends/` - List friends.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Docker](https://www.docker.com/)
- [Postman](https://www.postman.com/)

