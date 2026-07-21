# signup

**POST** `{{url}}/api/signup/`

## Auth

Type: `inherit`

## Body

Type: `json`

```json
{
  "first_name": "Jane",
  "last_name": "Doe",
  "email": "kamrul@asl.aero",
  "phone": "+8801684806728",
  "password": "kamrul123",
  "confirm_password": "kamrul123",
  "company_name": "kamrul",
  "company_country": "Bangladesh",
  "company_currency_id": 1
}
```

## Examples

### signup

**Request:** `POST` `{{url}}/api/signup/`

```json
{
  "first_name": "Jane",
  "last_name": "Doe",
  "email": "kamrul2@asl.aero",
  "phone": "+8801684806728",
  "password": "kamrul123",
  "confirm_password": "kamrul123",
  "company_name": "kamrul",
  "company_country": "Bangladesh",
  "company_currency_id": 1
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Signup Successful",
    "data": {
        "result": {}
    }
}
```

### signup , email taken error

**Request:** `POST` `{{url}}/api/signup/`

```json
{
  "first_name": "Jane",
  "last_name": "Doe",
  "email": "kamrul2@asl.aero",
  "phone": "+8801684806728",
  "password": "kamrul123",
  "confirm_password": "kamrul123",
  "company_name": "kamrul",
  "company_country": "Bangladesh",
  "company_currency_id": 1
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Sign Up Failed To Create",
    "error": null,
    "errors": {
        "email": "This email is already taken."
    }
}
```
