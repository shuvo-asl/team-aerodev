# get system settings

**GET** `{{url}}/api/system-settings`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `key` | `invoice_vat_rate` | query |
| `is_active` | `True` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

## Examples

### get system settings based on key param

**Request:** `GET` `{{url}}/api/system-settings?key=logo`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'System Settings' Successfully Fetched",
    "data": {
        "result": {
            "id": 5,
            "key": "logo",
            "value_text": null,
            "value_file": "/media/images/system_settings/2024/01/24/image-000.png",
            "type": "file",
            "created_at": "2024-01-24T12:34:57.846123+06:00",
            "updated_at": "2024-01-24T12:34:57.846229+06:00",
            "is_active": true
        }
    }
}
```

### get system settings based on is_active param

**Request:** `GET` `{{url}}/api/system-settings?is_active=True`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'System Settings' Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 5,
                "key": "logo",
                "value_text": null,
                "value_file": "/media/images/system_settings/2024/01/24/image-000.png",
                "type": "file",
                "created_at": "2024-01-24T12:34:57.846123+06:00",
                "updated_at": "2024-01-24T12:34:57.846229+06:00",
                "is_active": true
            },
            {
                "id": 4,
                "key": "invoice_chasing_and_reminder_minute",
                "value_text": "1",
                "value_file": null,
                "type": "text",
                "created_at": "2024-01-17T17:54:48.100965+06:00",
                "updated_at": "2024-01-17T17:54:48.101020+06:00",
                "is_active": true
            },
            {
                "id": 3,
                "key": "invoice_chasing_and_reminder_hour",
                "value_text": "8",
                "value_file": null,
                "type": "text",
                "created_at": "2024-01-17T06:00:26.164451+06:00",
                "updated_at": "2024-01-17T06:00:26.164508+06:00",
                "is_active": true
            },
            {
                "id": 2,
                "key": "days_to_due_date",
                "value_text": "7",
                "value_file": null,
                "type": "text",
                "created_at": "2024-01-08T08:58:19.047605+06:00",
                "updated_at": "2024-01-09T06:00:05.457920+06:00",
                "is_active": true
            },
            {
                "id": 1,
                "key": "invoice_vat_rate",
                "value_text": "15",
                "value_file": null,
                "type": "text",
                "created_at": "2024-01-08T08:57:38.169194+06:00",
                "updated_at": "2024-01-09T06:01:49.532306+06:00",
                "is_active": true
            }
        ]
    }
}
```

### get system settings

**Request:** `GET` `{{url}}/api/system-settings`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'System Settings' Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 4,
                "deleted_at": null,
                "key": "days_to_due_date",
                "value_text": "15",
                "value_file": null,
                "type": "text",
                "created_at": "2024-03-06T10:37:48.285032+06:00",
                "updated_at": "2024-03-06T10:37:48.285098+06:00"
            },
            {
                "id": 3,
                "deleted_at": null,
                "key": "invoice_chasing_and_reminder_hour_2",
                "value_text": "2",
                "value_file": null,
                "type": "text",
                "created_at": "2024-03-06T10:37:48.282396+06:00",
                "updated_at": "2024-08-27T16:05:10.781451+06:00"
            }
        ]
    }
}
```
