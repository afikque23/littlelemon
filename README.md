# Little Lemon - Meta Back-End Developer Capstone Project

This repository contains the complete implementation for the **Little Lemon Restaurant API** capstone project, fulfilling all grading criteria for the **Meta Back-End Developer Professional Certificate**.

---

## 📋 Evaluation Checklist & Peer Review Criteria

| # | Peer Review Criterion | Implementation Status | Notes |
|---|---|---|---|
| 1 | **Does the web application use Django to serve static HTML content?** | ✅ **Yes** | Static HTML, CSS, and JS served at `GET /restaurant/` and root `GET /` using Django templates and static files. |
| 2 | **Has the learner committed the project to a Git repository?** | ✅ **Yes** | Project is version-controlled via Git and hosted on GitHub. |
| 3 | **Does the application connect the backend to a MySQL database?** | ✅ **Yes** | Configured in `littlelemon/settings.py` (`NAME: littlelemon`, `USER: root`, `ENGINE: django.db.backends.mysql`). |
| 4 | **Are the menu and table booking APIs implemented?** | ✅ **Yes** | CRUD endpoints for Menu items (`/restaurant/menu/`) and Table Bookings (`/restaurant/booking/tables/`). |
| 5 | **Is the application set up with user registration and authentication?** | ✅ **Yes** | Configured with Djoser (`/auth/users/`, `/auth/token/login/`) and DRF Token Authentication (`/api-token-auth/`). |
| 6 | **Does the application contain unit tests?** | ✅ **Yes** | Located in `tests/` and `restaurant/tests/` testing both models (`test_models.py`) and API views (`test_views.py`). |
| 7 | **Can the API be tested with the Insomnia REST client?** | ✅ **Yes** | All endpoints return standard JSON responses with full HTTP method support (GET, POST, PUT, DELETE). |
| 8 | **Is a `Readme.txt` file present with testable API paths?** | ✅ **Yes** | `Readme.txt` is located in the repository root detailing all endpoints and sample payloads. |

---

## 🚀 API Endpoints Overview

### 1. Static Web Content
* `GET /` or `GET /restaurant/`: Serves the static Little Lemon home page.

### 2. User Authentication (Djoser & Token)
* `POST /auth/users/`: Register a new user.
* `POST /auth/token/login/`: Obtain an authentication token.
* `POST /auth/token/logout/`: Invalidate authentication token.
* `POST /api-token-auth/`: Alternative DRF token acquisition endpoint.

### 3. Menu API
* `GET /restaurant/menu/`: Retrieve all menu items.
* `POST /restaurant/menu/`: Create a new menu item.
* `GET /restaurant/menu/<int:pk>`: Retrieve a single menu item.
* `PUT /restaurant/menu/<int:pk>`: Update a menu item.
* `DELETE /restaurant/menu/<int:pk>`: Delete a menu item.

### 4. Table Booking API (Protected via Token)
* `GET /restaurant/booking/tables/`: List all table reservations.
* `POST /restaurant/booking/tables/`: Book a new reservation table.
* `GET /restaurant/booking/tables/<int:pk>/`: Retrieve specific booking.
* `PUT /restaurant/booking/tables/<int:pk>/`: Update booking details.
* `DELETE /restaurant/booking/tables/<int:pk>/`: Cancel a reservation.

---

## 🧪 Running Unit Tests

Run the following command in the project root:

```bash
python manage.py test
```

This executes:
1. `MenuItemTest` (`tests/test_models.py`): Validates model fields and string representation (`"IceCream : 80"`).
2. `MenuViewTest` (`tests/test_views.py`): Validates APIClient GET requests and JSON serialization equality.
