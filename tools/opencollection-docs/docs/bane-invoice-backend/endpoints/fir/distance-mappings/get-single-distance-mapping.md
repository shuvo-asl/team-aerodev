# GET single distance mapping

**GET** `{{url}}/api/fir-distance-mappings/1`

## Auth

Type: `bearer`

## Examples

### get single distance mapping

**Request:** `GET` `{{url}}/api/fir-distance-mappings/1`

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "FIR Distance Mapping Fetched Successfully",
  "data": {
    "result": {
      "id": 1,
      "from_point": "ANTAX",
      "to_point": "HJJJ",
      "distance_nm": 232.15,
      "is_active": true,
      "notes": ""
    }
  }
}
```
