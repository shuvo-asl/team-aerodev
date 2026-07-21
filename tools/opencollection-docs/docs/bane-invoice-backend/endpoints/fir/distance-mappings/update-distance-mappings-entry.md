# UPDATE distance mappings entry

**PATCH** `{{url}}/api/fir-distance-mappings/24/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
        "to_point": "ALMAM",
        "from_point": "HJJJ",
        "distance_nm": 540.56,
        "is_active": false,
        "notes": "sample note"
}
```

## Examples

### update fir distance mapping

**Request:** `PATCH` `{{url}}/api/fir-distance-mappings/24/`

```json
{
        "to_point": "ALMAM",
        "from_point": "HJJJ",
        "distance_nm": 540.56,
        "is_active": false,
        "notes": "sample note"
}
```

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "FIR Distance Mapping successfully updated",
  "data": {
    "result": {
      "id": 24,
      "from_point": "HJJJ",
      "to_point": "ALMAM",
      "distance_nm": 540.56,
      "is_active": false,
      "notes": "sample note"
    }
  }
}
```
