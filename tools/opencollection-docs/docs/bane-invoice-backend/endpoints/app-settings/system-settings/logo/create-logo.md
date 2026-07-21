# create logo

**POST** `{{url}}/api/system-settings/`

## Auth

Type: `bearer`

## Body

Type: `multipart-form`

```
[{'name': 'title', 'type': 'text', 'value': 'logo for testing'}, {'name': 'type', 'type': 'text', 'value': 'logo'}, {'name': 'logo', 'type': 'file', 'value': ['postman-cloud:///1ef7eff2-7e20-49a0-aa44-c41b878eb3de']}]
```

## Examples

### New Request

**Request:** `POST` `{{url}}/api/system-settings/`

```json
[{'name': 'title', 'type': 'text', 'value': 'logo for testing'}, {'name': 'type', 'type': 'text', 'value': 'logo'}, {'name': 'logo', 'type': 'file', 'value': ['postman-cloud:///1ef7eff2-7e20-49a0-aa44-c41b878eb3de']}]
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "System Settings successfully created",
    "data": {
        "result": {
            "id": 49,
            "deleted_at": null,
            "created_at": "2024-11-12T12:52:34.177770+06:00",
            "updated_at": null,
            "title": "logo for testing",
            "value_text": null,
            "value_file": null,
            "value_type": "",
            "type": "logo",
            "is_active": false,
            "logo": "http://localhost:5011/api/media/images/system_settings/logo/2024/11/12/bdflag.jpg",
            "bank_details": ""
        }
    }
}
```
