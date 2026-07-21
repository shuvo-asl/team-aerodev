# create bank details

**POST** `{{url}}/api/system-settings/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "bank_details": "example Bank deatils",
    "type": "bank_details",
    "title": "imp bank info"
}
```

## Examples

### New Request

**Request:** `POST` `{{url}}/api/system-settings/`

```json
{
    "bank_details": "example Bank deatils",
    "type": "bank_details",
    "title": "imp bank info"
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "System Settings successfully created",
    "data": {
        "result": {
            "id": 48,
            "deleted_at": null,
            "created_at": "2024-11-12T12:49:10.618132+06:00",
            "updated_at": null,
            "title": "imp bank info",
            "value_text": null,
            "value_file": null,
            "value_type": "",
            "type": "bank_details",
            "is_active": true,
            "logo": null,
            "bank_details": "example Bank deatils"
        }
    }
}
```
