# Update Email Template

**PATCH** `{{url}}/api/email_template/14/`

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
    "name": "test45",
    "subject": "demo",
    "body": "text"
}
```

## Examples

### Update Email Template

**Request:** `PATCH` `{{url}}/api/email_template/1/`

```json
{
    "name": "test45",
    "subject": "demo",
    "body": "text"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Email Template successfully updated",
    "data": {
        "result": {
            "id": 1,
            "deleted_at": null,
            "created_at": "2024-08-19T14:25:56.198280+06:00",
            "updated_at": "2024-11-12T16:13:48.585706+06:00",
            "name": "test45",
            "subject": "demo",
            "body": "text",
            "has_attachment": true,
            "is_active": true,
            "has_bank_details": false
        }
    }
}
```
