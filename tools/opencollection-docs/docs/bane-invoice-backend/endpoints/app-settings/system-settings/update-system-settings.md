# update system settings

**PATCH** `{{url}}/api/system-settings/4/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

```json
  {
    "key": "days_to_due_date",
    "value_text": "20",
    "type": "text"
}
```

## Examples

### update system settings

**Request:** `PATCH` `{{url}}/api/system-settings/4/`

```json
  {
    "key": "days_to_due_date",
    "value_text": "20",
    "type": "text"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'System Settings' Updated Successfully.",
    "data": {
        "result": {
            "id": 4,
            "deleted_at": null,
            "key": "days_to_due_date",
            "value_text": "20",
            "value_file": null,
            "type": "text",
            "created_at": "2024-03-20T09:53:41.315766+06:00",
            "updated_at": "2024-09-01T23:01:59.621409+06:00"
        }
    }
}
```
