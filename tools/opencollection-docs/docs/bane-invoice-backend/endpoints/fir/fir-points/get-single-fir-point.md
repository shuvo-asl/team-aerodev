# GET single fir point

**GET** `{{url}}/api/fir-point/1`

## Auth

Type: `bearer`

## Examples

### get single fir point

**Request:** `GET` `{{url}}/api/fir-point/1`

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "FIR Point Fetched Successfully",
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
