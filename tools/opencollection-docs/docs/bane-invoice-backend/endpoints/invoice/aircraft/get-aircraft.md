# get aircraft

**GET** `{{url}}/api/bas/aircraft/1/`

## Auth

Type: `bearer`

## Headers

| Name | Value |
|---|---|
| `` | `` |

## Examples

### New Request

**Request:** `GET` `{{url}}/api/bas/aircraft/1/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Aircraft fetched successfully",
    "data": {
        "result": {
            "id": 1,
            "registration_number": "A7CFD",
            "aircraft_type_id": 2,
            "aircraft_type_name": "GL5T",
            "icao24": "",
            "operator_id": 0,
            "operator_name": ""
        }
    }
}
```
