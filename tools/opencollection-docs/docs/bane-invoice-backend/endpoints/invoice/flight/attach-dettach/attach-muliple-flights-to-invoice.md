# attach muliple flights to invoice

**POST** `{{url}}/api/attach-multiple-flights/`

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

### atleast one flight is required flight list for attach

**Request:** `POST` `{{url}}/api/attach-multiple-flights/`

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
  "message": "Failed to attach flights to report",
  "error": null,
  "errors": {
    "flights": "Please select at least one flight."
  }
}
```

### can't attach a flight to voided invoice

**Request:** `POST` `{{url}}/api/attach-multiple-flights/`

```json
{
  "report_id": 325,
  "flights": [1]
}
```

**Response:** `400 Bad Request`

```json
{
  "status": "failed",
  "message": "Failed to attach flights to report",
  "error": "Cannot attach flights to a voided report.",
  "errors": null
}
```

### flights must be in ready to bill status for attach operation

**Request:** `POST` `{{url}}/api/attach-multiple-flights/`

```json
{
  "report_id": 69,
  "flights": [37210]
}
```

**Response:** `400 Bad Request`

```json
{
  "status": "failed",
  "message": "Failed to attach flights to report",
  "error": "Some of the selected flights are not in Ready to Bill status.",
  "errors": {
    "invalid_flight_ids": [
      37210
    ]
  }
}
```

### flight and invoice client must match

**Request:** `POST` `{{url}}/api/attach-multiple-flights/`

```json
{
  "report_id": 69,
  "flights": [37170]
}
```

**Response:** `400 Bad Request`

```json
{
  "status": "failed",
  "message": "Failed to attach flights to report",
  "error": "Some of the selected flights do not belong to the same client as the report.",
  "errors": {
    "invalid_flight_ids": [
      37170
    ]
  }
}
```

### successful attachment

**Request:** `POST` `{{url}}/api/attach-multiple-flights/`

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
  "message": "Flights attached successfully.",
  "data": {
    "result": {
      "attached_count": 1,
      "report_id": 69
    }
  }
}
```
