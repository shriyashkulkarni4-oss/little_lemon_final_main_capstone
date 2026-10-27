Little Lemon API — peer review paths

The landing page is at: /

Public menu:
GET /restaurant/menu/
GET /restaurant/menu/{id}/

Authentication:
POST /api/register/       JSON: {"username":"guest1","email":"guest@example.com","password":"strong-pass-123"}
POST /api/token/          JSON: {"username":"guest1","password":"strong-pass-123"}
Send the returned token on protected requests as: Authorization: Token <token>

Table bookings (token required):
GET /restaurant/booking/tables/
POST /restaurant/booking/tables/  JSON: {"name":"Alex Morgan","no_of_guests":2,"booking_date":"2026-12-01","booking_time":"19:00"}
GET /restaurant/booking/tables/{id}/
PUT /restaurant/booking/tables/{id}/
PATCH /restaurant/booking/tables/{id}/
DELETE /restaurant/booking/tables/{id}/

Menu management (token required for POST, PUT, PATCH and DELETE):
POST /restaurant/menu/
PUT /restaurant/menu/{id}/
PATCH /restaurant/menu/{id}/
DELETE /restaurant/menu/{id}/

The Insomnia collection is in insomnia/Little-Lemon-API.json. Setup steps are in README.md.
