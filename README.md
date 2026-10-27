# Little Lemon API Capstone

A Django and Django REST Framework API for a small restaurant. It serves a static HTML landing page, stores menu items and table bookings in MySQL, and uses token authentication for protected operations.

## Requirements

- Python 3.10 or newer
- Docker Desktop (for the included MySQL service), or a MySQL 8 compatible database

## Run locally on Windows

1. Copy `.env.example` to `.env`. The sample values are for local development only.
2. Start the database with `docker compose up -d db`.
3. Create a virtual environment and install dependencies:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   py -m pip install -r requirements.txt
   ```

4. Apply database migrations and create an admin user:

   ```powershell
   py manage.py migrate
   py manage.py loaddata restaurant/fixtures/menu_items.json
   py manage.py createsuperuser
   py manage.py runserver
   ```

5. Visit http://127.0.0.1:8000/ for the landing page and http://127.0.0.1:8000/admin/ for Django admin.

The default database engine is MySQL. To use SQLite for a quick local exercise, set `DB_ENGINE=sqlite` in `.env`.

## API paths

The peer review path list is in [Readme.txt](Readme.txt). The browsable menu is public. Register at `/api/register/`, then get an API token from `/api/token/`. Pass it in the `Authorization` header as `Token <token>` for booking operations and menu changes.

| Purpose | Path | Access |
| --- | --- | --- |
| Menu list and create | `/restaurant/menu/` | GET public; POST authenticated |
| Menu item detail | `/restaurant/menu/{id}/` | GET public; changes authenticated |
| Booking list and create | `/restaurant/booking/tables/` | Authenticated |
| Booking detail | `/restaurant/booking/tables/{id}/` | Authenticated |
| Register account | `/api/register/` | Public |
| Obtain token | `/api/token/` | Public |

## Insomnia

Import `insomnia/Little-Lemon-API.json`. Set the collection's `base_url` environment value to `http://127.0.0.1:8000`. Register an account, obtain a token, then paste the token into the `token` environment value before trying protected requests. The collection includes examples for menu, registration, token login, and table bookings.

## Tests

The project includes API tests for public menu access, protected changes, account registration, and booking creation. Select SQLite before running them:

```powershell
$env:DB_ENGINE = "sqlite"
py manage.py test
```

## GitHub

Commit `Readme.txt` with the project and push it to the repository you submit for peer review. Never commit `.env` or real database credentials.
