# Insurance Policy Manager API (README made with AI)

A RESTful API built with Django for managing insurance policies. This API provides endpoints for creating, retrieving, updating, and deleting insurance policies.

## Features

- Create new insurance policies
- List all existing policies
- Retrieve specific policy details
- Update policy information
- Delete policies
- Data validation and integrity checks

## Requirements

- Python 3.8+
- Django 4.x
- Django REST Framework

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd insuranceManager
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure your database settings in `.env`

5. Apply migrations:
```bash
python manage.py migrate
```

6. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Create a New Policy
- **URL**: `/api/policies/`
- **Method**: `POST`
- **Data Parameters**:
  ```json
  {
    "customer_name": "Test",
    "policy_type": "auto",
    "expiry_date": "2024-12-31"
  }
  ```
- **Success Response**: `201 Created`

### List All Policies
- **URL**: `/api/policies/`
- **Method**: `GET`
- **Success Response**: `200 OK`

### Get Specific Policy
- **URL**: `/api/policies/<policy_id>/`
- **Method**: `GET`
- **Success Response**: `200 OK`

### Update Policy
- **URL**: `/api/policies/<policy_id>/`
- **Method**: `PUT`
- **Data Parameters**: Same as Create
- **Success Response**: `200 OK`

### Delete Policy
- **URL**: `/api/policies/<policy_id>/`
- **Method**: `DELETE`
- **Success Response**: `204 No Content`

## Data Validation

The API includes the following validations:
- Policy ID is auto-generated and unique
- Customer name is required
- Policy type must be one of the predefined types (e.g., "auto", "home")
- Expiry date must be a future date

## Error Handling

The API returns appropriate HTTP status codes and error messages:
- `400 Bad Request`: Invalid data provided
- `404 Not Found`: Policy not found
- `500 Internal Server Error`: Server-side errors

## Details
- Although the challenge instructed to do a policy_id and policy_type, I've chosen to add the database field as id and type and use the serializer to format to the required format.
- Didn't add more models, like the model for Customer, to not increase the complexity of the challenge. Also didn't add authentication due to the same reason.
- Although the challenge instructed to use Django ORM for validations, I tend to use the validations at the service layer and leave the ORM for the database operations.