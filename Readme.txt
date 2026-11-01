================================================================================
Little Lemon Restaurant - Back-End Developer Capstone Project
================================================================================

Welcome to the Little Lemon API capstone project submission.
This project is built using Django and Django REST Framework (DRF), connects to a MySQL database, serves static HTML content, implements full authentication with token support, and includes comprehensive unit tests.

Base URL: http://127.0.0.1:8000/

--------------------------------------------------------------------------------
1. STATIC HTML CONTENT
--------------------------------------------------------------------------------
- GET /
  Description: Displays the Little Lemon home page with static HTML, CSS, and images.

- GET /restaurant/
  Description: Serves the Little Lemon restaurant front-end template and static assets.


--------------------------------------------------------------------------------
2. USER REGISTRATION & AUTHENTICATION ENDPOINTS (DJOSER & TOKEN AUTH)
--------------------------------------------------------------------------------
- POST /auth/users/
  Description: Register a new user account.
  Payload (JSON):
  {
    "username": "peer_reviewer",
    "password": "StrongPassword123!",
    "email": "reviewer@example.com"
  }

- POST /auth/token/login/
  Description: Log in with credentials to receive a token.
  Payload (JSON):
  {
    "username": "peer_reviewer",
    "password": "StrongPassword123!"
  }
  Response:
  {
    "auth_token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
  }

- POST /api-token-auth/
  Description: Alternative direct DRF token retrieval endpoint.
  Payload (JSON):
  {
    "username": "peer_reviewer",
    "password": "StrongPassword123!"
  }

- POST /auth/token/logout/
  Description: Log out and invalidate the auth token.
  Header: Authorization: Token <your_token_here>


--------------------------------------------------------------------------------
3. MENU ITEMS API ENDPOINTS
--------------------------------------------------------------------------------
- GET /restaurant/menu/  (or /api/menu/ or /api/menu-items/)
  Description: List all menu items.
  Method: GET
  Headers: None required

- POST /restaurant/menu/ (or /api/menu/ or /api/menu-items/)
  Description: Add a new menu item.
  Method: POST
  Headers: Content-Type: application/json
  Payload (JSON):
  {
    "title": "Greek Salad",
    "price": "12.99",
    "inventory": 25
  }

- GET /restaurant/menu/<id> (or /restaurant/menu-items/<id>)
  Description: Retrieve details of a single menu item by ID.
  Method: GET
  Example: GET /restaurant/menu/1

- PUT /restaurant/menu/<id>
  Description: Update a menu item by ID.
  Method: PUT
  Payload (JSON):
  {
    "title": "Greek Salad Special",
    "price": "14.99",
    "inventory": 20
  }

- DELETE /restaurant/menu/<id>
  Description: Delete a menu item by ID.
  Method: DELETE


--------------------------------------------------------------------------------
4. TABLE BOOKING API ENDPOINTS (AUTHENTICATION PROTECTED)
--------------------------------------------------------------------------------
Note: These endpoints require an authenticated user.
Include the header:
  Authorization: Token <your_token_here>

- GET /restaurant/booking/tables/ (or /api/booking/tables/)
  Description: List all table reservations.
  Method: GET
  Header: Authorization: Token <your_token_here>

- POST /restaurant/booking/tables/ (or /api/booking/tables/)
  Description: Book a new table reservation.
  Method: POST
  Header:
    Authorization: Token <your_token_here>
    Content-Type: application/json
  Payload (JSON):
  {
    "name": "Alex Smith",
    "no_of_guests": 4,
    "booking_date": "2026-11-05T19:00:00Z"
  }

- GET /restaurant/booking/tables/<id>/
  Description: Retrieve a specific table booking.
  Method: GET
  Header: Authorization: Token <your_token_here>

- PUT /restaurant/booking/tables/<id>/
  Description: Update an existing table booking.
  Method: PUT
  Header: Authorization: Token <your_token_here>
  Payload (JSON):
  {
    "name": "Alex Smith",
    "no_of_guests": 6,
    "booking_date": "2026-11-05T20:00:00Z"
  }

- DELETE /restaurant/booking/tables/<id>/
  Description: Cancel a table booking.
  Method: DELETE
  Header: Authorization: Token <your_token_here>


--------------------------------------------------------------------------------
5. HOW TO RUN UNIT TESTS
--------------------------------------------------------------------------------
Run the automated test suite in the project terminal:
  python manage.py test
or:
  python manage.py test restaurant
or:
  python manage.py test tests/

Unit tests include:
- MenuItemTest (tests/test_models.py): Tests model string representations and values.
- MenuViewTest (tests/test_views.py): Tests GET requests and serialization for menu items using DRF APIClient.
