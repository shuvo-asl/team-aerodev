# GET paginated distance mappings

**GET** `{{url}}/api/fir-distance-mappings/?page=1&limit=10`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `page` | `1` | query |
| `limit` | `10` | query |

## Examples

### get paginated distance mapping

**Request:** `GET` `{{url}}/api/fir-distance-mappings/?page=1&limit=10`

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "FIR Distance Mapping Successfully Fetched",
  "data": {
    "next": 2,
    "previous": null,
    "current_page": 1,
    "total_object": 22,
    "total_page": 3,
    "result": [
      {
        "id": 13,
        "from_point": "ALMAM",
        "to_point": "HJJJ",
        "distance_nm": 534.56,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 14,
        "from_point": "AMATO",
        "to_point": "HJJJ",
        "distance_nm": 223.93,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 1,
        "from_point": "ANTAX",
        "to_point": "HJJJ",
        "distance_nm": 232.15,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 2,
        "from_point": "ATUGA",
        "to_point": "HJJJ",
        "distance_nm": 53.7,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 15,
        "from_point": "AVAGI",
        "to_point": "HJJJ",
        "distance_nm": 235.1,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 16,
        "from_point": "AVONO",
        "to_point": "HJJJ",
        "distance_nm": 306.22,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 17,
        "from_point": "DAGAP",
        "to_point": "HJJJ",
        "distance_nm": 180.58,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 18,
        "from_point": "DASTU",
        "to_point": "HJJJ",
        "distance_nm": 199.81,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 4,
        "from_point": "DEKUM",
        "to_point": "HJJJ",
        "distance_nm": 117.95,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 5,
        "from_point": "EPLAS",
        "to_point": "HJJJ",
        "distance_nm": 53.7,
        "is_active": true,
        "notes": ""
      }
    ]
  }
}
```
