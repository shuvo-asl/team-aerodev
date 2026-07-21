# update fir point

**PATCH** `{{url}}/api/fir-point/1/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
  "name": "first point updated",
  "latitude": 2.857,
  "longitude": -3.456,
  "is_active": true
}
```

## Examples

### update fir point

**Request:** `PATCH` `{{url}}/api/fir-point/1/`

```json
{
  "name": "first point updated",
  "latitude": 2.857,
  "longitude": -3.456,
  "is_active": true
}
```

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "FIR Point successfully updated",
  "data": {
    "result": {
      "id": 1,
      "name": "firstpointupdated",
      "latitude": 2.857,
      "longitude": -3.456,
      "is_active": true
    }
  }
}
```
