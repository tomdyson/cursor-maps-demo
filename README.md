# NYC Accessible Shops & Restaurants App

This Django project provides a backend API for an application that helps users locate accessible shops and restaurants in New York City.

## Project Structure

- `nycmaps/`: Main project directory
  - `nycmaps/`: Project settings
    - `settings.py`: Django settings file
    - `urls.py`: Main URL configuration
  - `places/`: App directory
    - `models.py`: Defines `Place` and `AccessibilityFeature` models
    - `views.py`: Contains ViewSets for API endpoints
    - `serializers.py`: Serializers for converting model instances to JSON
    - `urls.py`: URL patterns for the places app
    - `admin.py`: Admin interface configuration

## Features

- REST API for accessible places and their features
- Django Admin interface for managing data
- Pagination support

## Local Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd nycmaps
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser for the admin interface:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Access the API at `http://127.0.0.1:8000/api/` and the admin interface at `http://127.0.0.1:8000/admin/`

## API Endpoints

- `/api/places/`: List and create places
- `/api/places/<id>/`: Retrieve, update, or delete a specific place
- `/api/accessibility-features/`: List and create accessibility features
- `/api/accessibility-features/<id>/`: Retrieve, update, or delete a specific accessibility feature

## Models

- `Place`: Represents a shop or restaurant with accessibility information
- `AccessibilityFeature`: Represents a specific accessibility feature that can be associated with places

## Next Steps

- Implement user authentication
- Add filtering and search functionality to the API
- Create frontend application to consume the API
- Implement data population strategy for shops and restaurants

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.