# void a flight

**PATCH** `{{url}}/api/flight/void/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
  "flight_ids": [8,80,14],
  "notes": "Reason for voiding this/these flight(s)"
}
```

## Examples

### Validation with No Flight

**Request:** `PATCH` `{{url}}/api/flight/void/`

```json
{
  "flight_ids": [],
  "notes": "Reason for voiding this/these flight(s)"
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Flight status failed to void",
    "error": null,
    "errors": {
        "flight_ids": [
            "At least one flight ID must be provided."
        ]
    }
}
```

### Validation with flight already billing

**Request:** `PATCH` `{{url}}/api/flight/void/`

```json
{
  "flight_ids": [1,15,80],
  "notes": "Reason for voiding this/these flight(s)"
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Flight status failed to void",
    "error": "[ErrorDetail(string='Flights [1, 15] cannot be voided due to status: billing', code='invalid')]",
    "errors": null
}
```

### Successfully voided incomplete and ready to bill flights

**Request:** `PATCH` `{{url}}/api/flight/void/`

```json
{
  "flight_ids": [8,80,14],
  "notes": "Reason for voiding this/these flight(s)"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Flight(s) voided successfully",
    "data": {
        "result": {
            "updated_count": 3,
            "flight_ids": [
                80,
                14,
                8
            ],
            "notes": "Reason for voiding this/these flight(s)"
        }
    }
}
```
