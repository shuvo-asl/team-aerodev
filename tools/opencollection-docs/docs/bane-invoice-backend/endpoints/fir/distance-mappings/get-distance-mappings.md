# GET distance mappings

**GET** `{{url}}/api/fir-distance-mappings/?is_active=false`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `is_active` | `false` | query |

## Examples

### get distance mappings

**Request:** `GET` `{{url}}/api/fir-distance-mappings/`

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "FIR Distance Mapping Successfully Fetched",
  "data": {
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
      },
      {
        "id": 19,
        "from_point": "EPSIX",
        "to_point": "HJJJ",
        "distance_nm": 211.51,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 6,
        "from_point": "GINPU",
        "to_point": "HJJJ",
        "distance_nm": 349.0,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 7,
        "from_point": "ITOXA",
        "to_point": "HJJJ",
        "distance_nm": 332.33,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 8,
        "from_point": "KABLA",
        "to_point": "HJJJ",
        "distance_nm": 66.79,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 20,
        "from_point": "KAFIA",
        "to_point": "HJJJ",
        "distance_nm": 534.56,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 9,
        "from_point": "MALAKAL",
        "to_point": "HJJJ",
        "distance_nm": 281.0,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 10,
        "from_point": "OVELA",
        "to_point": "HJJJ",
        "distance_nm": 56.65,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 21,
        "from_point": "RABAK",
        "to_point": "HJJJ",
        "distance_nm": 490.08,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 22,
        "from_point": "RADAG",
        "to_point": "HJJJ",
        "distance_nm": 460.92,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 11,
        "from_point": "SAGBU",
        "to_point": "HJJJ",
        "distance_nm": 89.89,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 23,
        "from_point": "TAPOS",
        "to_point": "HJJJ",
        "distance_nm": 120.58,
        "is_active": true,
        "notes": ""
      },
      {
        "id": 12,
        "from_point": "WAU",
        "to_point": "HJJJ",
        "distance_nm": 276.0,
        "is_active": true,
        "notes": ""
      }
    ]
  }
}
```

### filter distance mapping by active status

**Request:** `GET` `{{url}}/api/fir-distance-mappings/?is_active=false`

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "FIR Distance Mapping Successfully Fetched",
  "data": {
    "result": [
      {
        "id": 13,
        "from_point": "ALMAM",
        "to_point": "HJJJ",
        "distance_nm": 534.56,
        "is_active": false,
        "notes": ""
      }
    ]
  }
}
```
