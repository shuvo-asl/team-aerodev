# add system settings

**POST** `{{url}}/api/system-settings/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "title": "test_settings769",
    "type": "general",
    "value_type": "text",
    "value_text": "fci",
    "bank_details": "fhgewifu"
}
```

## Examples

### add system settings

**Request:** `POST` `{{url}}/api/system-settings/`

```json
{
    "title": "test_settings769",
    "type": "general",
    "value_type": "text",
    "value_text": "fci",
    "bank_details": "fhgewifu"
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "System Settings successfully created",
    "data": {
        "result": {
            "id": 50,
            "deleted_at": null,
            "created_at": "2024-11-12T16:20:01.040553+06:00",
            "updated_at": null,
            "title": "test_settings769",
            "value_text": "fci",
            "value_file": null,
            "value_type": "text",
            "type": "general",
            "is_active": true,
            "logo": null,
            "bank_details": ""
        }
    }
}
```
