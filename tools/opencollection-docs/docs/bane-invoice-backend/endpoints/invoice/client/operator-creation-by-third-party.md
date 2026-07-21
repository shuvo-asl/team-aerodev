# operator creation by third party

**POST** `{{url}}/api/third-party/create-operator/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "name": "postman_op",
    "short_code": "PMO2",
    "email": "postman_op2@gmail.com",
    "phone": "+8801558250667",
    "billing_address": "Dhaka",
    "days_to_due_date": 20
}
```

## Examples

### operator creation without days to due date

**Request:** `POST` `{{url}}/api/third-party/create-operator/`

```json
{
    "name": "postman_op",
    "short_code": "PMO1",
    "email": "postman_op1@gmail.com",
    "phone": "+8801558250667",
    "billing_address": "Dhaka"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Operators created successfully",
    "data": {
        "result": {
            "id": 100,
            "name": "postman_op",
            "short_code": "PMO1",
            "email": "postman_op1@gmail.com",
            "phone": "+8801558250667",
            "billing_address": "Dhaka",
            "days_to_due_date": 15,
            "client_type": "operator",
            "preferred_currency": null,
            "status": "active",
            "chasing_rule": [],
            "interest_rule": []
        }
    }
}
```

### operator creation

**Request:** `POST` `{{url}}/api/third-party/create-operator/`

```json
{
    "name": "postman_op",
    "short_code": "PMO2",
    "email": "postman_op2@gmail.com",
    "phone": "+8801558250667",
    "billing_address": "Dhaka",
    "days_to_due_date": 20
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Operators created successfully",
    "data": {
        "result": {
            "id": 101,
            "name": "postman_op",
            "short_code": "PMO2",
            "email": "postman_op2@gmail.com",
            "phone": "+8801558250667",
            "billing_address": "Dhaka",
            "days_to_due_date": 20,
            "client_type": "operator",
            "preferred_currency": null,
            "status": "active",
            "chasing_rule": [],
            "interest_rule": []
        }
    }
}
```

### failed validation for required fields

**Request:** `POST` `{{url}}/api/third-party/create-operator/`

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Failed to create operator",
    "error": null,
    "errors": {
        "name": "This field is required.",
        "short_code": "This field is required.",
        "email": "This field is required.",
        "phone": "This field is required.",
        "billing_address": "This field is required."
    }
}
```
