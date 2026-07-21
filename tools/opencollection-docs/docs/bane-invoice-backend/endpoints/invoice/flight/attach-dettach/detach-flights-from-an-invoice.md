# Detach flights from an invoice

**POST** `{{url}}/api/detach-multiple-flights/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
  "report_id": 69,
  "flights": [12243]
}
```

## Examples

### at least one flight is required

**Request:** `POST` `{{url}}/api/detach-multiple-flights/`

```json
{
  "report_id": 69,
  "flights": []
}
```

**Response:** `400 Bad Request`

```json
{
  "status": "failed",
  "message": "Failed to detach flights from report",
  "error": null,
  "errors": {
    "flights": "Please select at least one flight."
  }
}
```

### provided flights must belong to the given report/invoice

**Request:** `POST` `{{url}}/api/detach-multiple-flights/`

```json
{
  "report_id": 69,
  "flights": [34038]
}
```

**Response:** `400 Bad Request`

```json
{
  "status": "failed",
  "message": "Failed to detach flights from report",
  "error": "Some of the provided flights are not attached to this report.",
  "errors": {
    "flights": "Some of the provided flights are not attached to this report.",
    "invalid_flight_ids": [
      34038
    ]
  }
}
```

### detaching flight from voided invoice does not work

**Request:** `POST` `{{url}}/api/detach-multiple-flights/`

```json
{
  "report_id": 323,
  "flights": [34038]
}
```

**Response:** `400 Bad Request`

```json
{
  "status": "failed",
  "message": "Failed to detach flights from report",
  "error": "Cannot detach flights from a voided report.",
  "errors": null
}
```

### successful detach operation

**Request:** `POST` `{{url}}/api/detach-multiple-flights/`

```json
{
  "report_id": 69,
  "flights": [12243]
}
```

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "Flights detached successfully.",
  "data": {
    "result": {
      "detached_count": 1,
      "report_id": 69
    }
  }
}
```
