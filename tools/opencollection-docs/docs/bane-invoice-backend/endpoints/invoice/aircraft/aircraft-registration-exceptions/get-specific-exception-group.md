# get specific exception group

**GET** `{{url}}/api/aircraft-registration-exception/1/`

## Auth

Type: `bearer`

## Body

Type: `text`

```
{
    "email": "devs@aerogon.aero",
    "password": "devs@2026",
    "user_type": "asl"
}
```

## Examples

### get specific exception group

**Request:** `GET` `{{url}}/api/aircraft-registration-exception/1/`

```json
{
    "email": "devs@aerogon.aero",
    "password": "devs@2026",
    "user_type": "asl"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Registration Exception Group Fetched Successfully",
    "data": {
        "result": {
            "id": 1,
            "note": "These aircrafts are VIP",
            "created_at": "2026-03-08T06:23:13.102879Z",
            "updated_at": null,
            "registrations": [
                "TEST02",
                "TEST01"
            ]
        }
    }
}
```
