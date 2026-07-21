# unlock field source

**POST** `{{url}}/api/flight/32702/field-source/unlock/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
  "fields": ["aircraft_registration_no"]
}
```

## Examples

### example

**Request:** `POST` `{{url}}/api/flight/32702/field-source/unlock/`

```json
{
  "fields": ["aircraft_registration_no"]
}
```

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "Field source unlocked successfully",
  "data": {
    "result": [
      {
        "field": "aircraft_registration_no",
        "label": "Registration",
        "current_value": "ET-BAL",
        "selected_source": "tfm",
        "locked": false,
        "pickable": true,
        "sources": [
          {
            "source": "bas",
            "at": "2026-06-25T10:14:45.217211+00:00",
            "value": "ET-BAL"
          },
          {
            "source": "tfm",
            "at": "2026-06-25T10:57:16.900099+00:00",
            "value": "ET-BAL"
          }
        ]
      }
    ]
  }
}
```
