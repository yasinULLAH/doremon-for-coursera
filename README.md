Here’s the `README.md` content for your GitHub repository. This file provides an overview of the Little Lemon API, setup instructions, and endpoint information.

```markdown
# Little Lemon API

This is a Django REST API project for the Little Lemon restaurant. The API manages menu items and table bookings, allowing for CRUD operations. This project uses Django, Django REST Framework, and connects to a MySQL database.

## Features

- **Menu API**: Handles menu items with options to list, create, update, and delete.
- **Table Booking API**: Manages table bookings, including reservations with CRUD operations.
- **User Authentication**: Basic authentication and user management setup.

## API Endpoints

Here are the main API endpoints you can test:

### Menu API
- **List all menu items**: `GET /api/menu/`
- **Retrieve a specific menu item**: `GET /api/menu/<id>/`
- **Create a new menu item**: `POST /api/menu/`
- **Update an existing menu item**: `PUT /api/menu/<id>/`
- **Delete a menu item**: `DELETE /api/menu/<id>/`

### Table Booking API
- **List all table bookings**: `GET /api/bookings/`
- **Retrieve a specific booking**: `GET /api/bookings/<id>/`
- **Create a new booking**: `POST /api/bookings/`
- **Update an existing booking**: `PUT /api/bookings/<id>/`
- **Delete a booking**: `DELETE /api/bookings/<id>/`

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd little_lemon
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the MySQL database**:
   - Update your database credentials in `little_lemon/settings.py` under `DATABASES`.

4. **Apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the server**:
   ```bash
   python manage.py runserver
   ```

## Testing the API

The API endpoints can be tested using tools like **Insomnia** or **Postman**. Additionally, unit tests are available and can be run using:
```bash
python manage.py test restaurant_api
```

## Project Structure

```
little_lemon/
├── restaurant_api/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── little_lemon/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
└── manage.py
```

## Notes

- Ensure that the MySQL server is running and accessible with the credentials provided.
- Use Django’s admin panel to manage database entries at `/admin/`.
- Modify and expand functionality as required by project specifications.
```

This file provides a comprehensive overview and helps others understand how to set up and use your API project. Let me know if you need additional details.
