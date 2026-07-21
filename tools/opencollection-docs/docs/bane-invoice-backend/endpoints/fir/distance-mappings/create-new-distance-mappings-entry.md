# CREATE new distance mappings entry

**POST** `{{url}}/api/fir-distance-mappings/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
        "to_point": "b",
        "from_point": "a",
        "distance_nm": 534.56,
        "is_active": true,
        "notes": ""
}
```

## Examples

### create new fir distance mapping

**Request:** `POST` `{{url}}/api/fir-distance-mappings/`

```json
{
        "to_point": "ALMAM",
        "from_point": "HJJJ",
        "distance_nm": 534.56,
        "is_active": true,
        "notes": ""
}
```

**Response:** `201 Created`

```json
{
  "status": "success",
  "message": "FIR Distance Mapping successfully created",
  "data": {
    "result": {
      "id": 24,
      "from_point": "HJJJ",
      "to_point": "ALMAM",
      "distance_nm": 534.56,
      "is_active": true,
      "notes": ""
    }
  }
}
```

### only unique pairs are eligible for mapping creation

**Request:** `POST` `{{url}}/api/fir-distance-mappings/`

```json
{
        "to_point": "b",
        "from_point": "a",
        "distance_nm": 534.56,
        "is_active": true,
        "notes": ""
}
```

**Response:** `400 Bad Request`

```json
{
  "status": "failed",
  "message": "FIR Distance Mapping Failed To Create",
  "error": null,
  "errors": {
    "from_point": "A mapping already exists for these given points",
    "to_point": "A mapping already exists for these given points"
  }
}
```
