# CREATE fir points

**POST** `{{url}}/api/fir-point/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
  "name": " point3one2",
  "latitude": 2.856,
  "longitude": -3.45,
  "is_active": false
}
```

## Examples

### create fir point

**Request:** `POST` `{{url}}/api/fir-point/`

```json
{
  "name": "first point",
  "latitude": 2.856,
  "longitude": -3.45,
  "is_active": false
}
```

**Response:** `201 Created`

```json
{
  "status": "success",
  "message": "FIR Point successfully created",
  "data": {
    "result": {
      "id": 1,
      "name": "firstpoint",
      "latitude": 2.856,
      "longitude": -3.45,
      "is_active": false
    }
  }
}
```

### only alphabets are allowed for fir point name

**Request:** `POST` `{{url}}/api/fir-point/`

```json
{
  "name": " point3one2",
  "latitude": 2.856,
  "longitude": -3.45,
  "is_active": false
}
```

**Response:** `201 Created`

```json
{
  "status": "success",
  "message": "FIR Point successfully created",
  "data": {
    "result": {
      "id": 2,
      "name": "pointone",
      "latitude": 2.856,
      "longitude": -3.45,
      "is_active": false
    }
  }
}
```
