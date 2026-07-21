# update registration exception group

**PATCH** `{{url}}/api/aircraft-registration-exception/1/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "note": "These aircrafts are VIP(updated)",
    "registrations": ["TEST02", "TEST01"]

}
```

## Examples

### update registration exception group

**Request:** `PATCH` `{{url}}/api/aircraft-registration-exception/1/`

```json
{
    "note": "These aircrafts are VIP(updated)",
    "registrations": ["TEST02", "TEST01", "TEST05"]

}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Registration Exception Group successfully updated",
    "data": {
        "result": {
            "id": 1,
            "note": "These aircrafts are VIP(updated)",
            "created_at": "2026-03-08T06:23:13.102879Z",
            "updated_at": "2026-03-08T06:31:32.208102Z",
            "registrations": [
                "TEST05",
                "TEST02",
                "TEST01"
            ]
        }
    }
}
```
