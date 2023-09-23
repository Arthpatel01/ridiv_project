# Invoice and Invoice Detail Management API

---------------------
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
### Invoices

1. GET /api/invoices/: List all invoices.
2. POST /api/invoices/: Create a new invoice. 
3. GET /api/invoices/{id}/: Retrieve details of a specific invoice. 
4. PUT /api/invoices/{id}/: Update a specific invoice. 
5. DELETE /api/invoices/{id}/: Delete a specific invoice.


### Invoice Details
1. GET /api/invoice-details/: List all invoice details.
2. POST /api/invoice-details/: Create a new invoice detail. 
3. GET /api/invoice-details/{id}/: Retrieve details of a specific invoice detail. 
4. PUT /api/invoice-details/{id}/: Update a specific invoice detail. 
5. DELETE /api/invoice-details/{id}/: Delete a specific invoice detail.
