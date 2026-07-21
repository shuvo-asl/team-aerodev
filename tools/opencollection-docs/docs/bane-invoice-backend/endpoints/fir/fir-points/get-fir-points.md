# GET fir points

**GET** `{{url}}/api/fir-point/?page=1&limit=10&is_active=true`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `page` | `1` | query |
| `limit` | `10` | query |
| `is_active` | `true` | query |

## Examples

### GET fir points

**Request:** `GET` `{{url}}/api/fir-point/`

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "FIR Point Successfully Fetched",
  "data": {
    "result": [
      {
        "id": 1,
        "name": "firstpoint",
        "latitude": 2.856,
        "longitude": -3.45,
        "is_active": false
      }
    ]
  }
}
```

### get paginated fir points

**Request:** `GET` `{{url}}/api/fir-point/?page=1&limit=10`

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "FIR Point Successfully Fetched",
  "data": {
    "next": null,
    "previous": null,
    "current_page": 1,
    "total_object": 1,
    "total_page": 1,
    "result": [
      {
        "id": 1,
        "name": "firstpoint",
        "latitude": 2.856,
        "longitude": -3.45,
        "is_active": false
      }
    ]
  }
}
```

### filter fir points by active status

**Request:** `GET` `{{url}}/api/fir-point/?page=1&limit=10&is_active=true`

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "FIR Point Successfully Fetched",
  "data": {
    "next": null,
    "previous": null,
    "current_page": 1,
    "total_object": 1,
    "total_page": 1,
    "result": [
      {
        "id": 3,
        "name": "poi",
        "latitude": 82.856,
        "longitude": -134.45,
        "is_active": true
      }
    ]
  }
}
```
