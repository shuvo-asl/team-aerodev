# get exception registration group list

**GET** `{{url}}/api/aircraft-registration-exception?registration_number=4`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `page` | `2` | query |
| `limit` | `1` | query |
| `registration_number` | `4` | query |

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

### get exception registration group list

**Request:** `GET` `{{url}}/api/aircraft-registration-exception`

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
    "message": "Registration Exception Group Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 1,
                "note": "These aircrafts are VIP",
                "created_at": "2026-03-08T06:23:13.102879Z",
                "updated_at": null,
                "registrations": [
                    "TEST02",
                    "TEST01"
                ]
            },
            {
                "id": 2,
                "note": "These aircrafts are VIP",
                "created_at": "2026-03-08T06:27:38.501367Z",
                "updated_at": null,
                "registrations": [
                    "TEST04",
                    "TEST03"
                ]
            }
        ]
    }
}
```
