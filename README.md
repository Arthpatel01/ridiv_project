# Invoice and Invoice Detail Management API

----------------------
### 1: Create a virtual environment and activate it:
`python -m venv venv`

`venv\Scripts\activate`

### 2: Install the project dependencies:
`pip install -r requirements.txt`

### 3: Create & apply database migrations:
`python manage.py makemigrations`

`python manage.py migrate`

### 4: Create a superuser (admin) account:
`python manage.py createsuperuser`

### 5: Test all endpoints:
`python manage.py test invoices`

### 6: Start the development server:
`python manage.py runserver`

----------------------

## API Endpoints
### Create content format:
``url: /api/invoices/``
```
{
    "date": "2023-09-24",
    "customer_name": "Virat Kohli",
    "details": [
        {
            "description": "Product 1",
            "quantity": 10,
            "unit_price": "10.99",
            "price": "54.95"
        }
    ]
}
```


### Update content format:
``url: /api/invoices/``
```
{
    "pk": 9,
    "date": "2023-09-24",
    "customer_name": "MS Dhoni",
    "details": [
        {
            "pk":4,
            "description": "MRF Bat",
            "quantity": 10,
            "unit_price": "10.99",
            "price": "54.95"
        }
    ]
}
```

### Delete with pk as parameter:
``url: /api/invoices/<primary-key>``
```
1. http://127.0.0.1:9000/api/invoices/9
2. Then hit delete button

```
