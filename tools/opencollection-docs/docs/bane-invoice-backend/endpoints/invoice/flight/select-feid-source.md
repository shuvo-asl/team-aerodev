# Select feid source

**POST** `{{url}}/api/flight/32702/field-source/select/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
  "selections": [{"field":  "aircraft_registration_no", "source":  "tfm"}]
}
```

## Examples

### example

**Request:** `POST` `{{url}}/api/flight/32702/field-source/select/`

```json
{
  "selections": [{"field":  "aircraft_registration_no", "source":  "tfm"}]
}
```

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "Field source selected successfully",
  "data": {
    "result": [
      {
        "field": "aircraft_registration_no",
        "label": "Registration",
        "current_value": "ET-BAL",
        "selected_source": "tfm",
        "locked": true,
        "pickable": true,
        "sources": [
          {
            "source": "bas",
            "at": "2026-06-25T10:14:45.217211+00:00",
            "value": "ET-BAL"
          },
          {
            "source": "tfm",
            "value": "ET-BAL",
            "at": "2026-06-25T10:57:16.900099+00:00"
          }
        ]
      }
    ]
  }
}
```
