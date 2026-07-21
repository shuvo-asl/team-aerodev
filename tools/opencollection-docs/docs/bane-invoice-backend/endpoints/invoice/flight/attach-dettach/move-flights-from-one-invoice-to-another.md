# move flights from one invoice to another

**POST** `{{url}}/api/move-flights/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
  "source_report_id": 445,
  "destination_report_id": 241,
  "flights": [35525]
}
```

## Examples

### at least one flight is required

**Request:** `POST` `{{url}}/api/move-flights/`

```json
{
  "source_report_id": 70,
  "destination_report_id": 79,
  "flights": []
}
```

**Response:** `400 Bad Request`

```json
{
  "status": "failed",
  "message": "Failed to move flights between reports",
  "error": null,
  "errors": {
    "flights": "Please select at least one flight."
  }
}
```

### source and destination report can not be same

**Request:** `POST` `{{url}}/api/move-flights/`

```json
{
  "source_report_id": 79,
  "destination_report_id": 79,
  "flights": [1]
}
```

**Response:** `400 Bad Request`

```json
{
  "status": "failed",
  "message": "Failed to move flights between reports",
  "error": "Source and destination reports must be different.",
  "errors": null
}
```

### moving flights wont work with void invoices

**Request:** `POST` `{{url}}/api/move-flights/`

```json
{
  "source_report_id": 323,
  "destination_report_id": 79,
  "flights": [1]
}
```

**Response:** `400 Bad Request`

```json
{
  "status": "failed",
  "message": "Failed to move flights between reports",
  "error": "Cannot move flights from a voided report.",
  "errors": null
}
```

### client of src and dest invoice must be same

**Request:** `POST` `{{url}}/api/move-flights/`

```json
{
  "source_report_id": 445,
  "destination_report_id": 442,
  "flights": [35525]
}
```

**Response:** `400 Bad Request`

```json
{
  "status": "failed",
  "message": "Failed to move flights between reports",
  "error": "Source and destination reports must belong to the same client.",
  "errors": null
}
```

### successful flight moving among reports

**Request:** `POST` `{{url}}/api/move-flights/`

```json
{
  "source_report_id": 445,
  "destination_report_id": 241,
  "flights": [35525]
}
```

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "Flights moved successfully.",
  "data": {
    "result": {
      "moved_count": 1,
      "source_report_id": 445,
      "destination_report_id": 241
    }
  }
}
```
