# Create registration exception group

**POST** `{{url}}/api/aircraft-registration-exception/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "note": "These aircrafts are VIP",
    "registrations": ["TEST01", "TEST02"]
}
```

## Examples

### Create registration exception group

**Request:** `POST` `{{url}}/api/aircraft-registration-exception/`

```json
{
    "note": "These aircrafts are VIP",
    "registrations": ["TEST03", "TEST04"]
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Registration Exception Group successfully created",
    "data": {
        "result": {
            "id": 2,
            "note": "These aircrafts are VIP",
            "created_at": "2026-03-08T06:27:38.501367Z",
            "updated_at": null,
            "registrations": [
                "TEST04",
                "TEST03"
            ]
        }
    }
}
```

### Create registration exception group registration list can not be empty

**Request:** `POST` `{{url}}/api/aircraft-registration-exception/`

```json
{
    "note": "These aircrafts are VIP",
    "registrations": []
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Registration Exception Group Failed To Create",
    "error": null,
    "errors": {
        "registrations": "This list may not be empty."
    }
}
```
