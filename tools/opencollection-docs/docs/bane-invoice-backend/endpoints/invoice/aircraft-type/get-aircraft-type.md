# get aircraft type

**GET** `{{url}}/api/bas/aircraft-type/1184/`

## Auth

Type: `bearer`

## Examples

### New Request

**Request:** `GET` `{{url}}/api/bas/aircraft-type/1/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Aircraft type fetched successfully",
    "data": {
        "result": {
            "name": "B-738",
            "mtow": 79000,
            "mtow_unit": "kg",
            "id": 1,
            "wing_type": "",
            "is_registration_fulfilled": false
        }
    }
}
```
