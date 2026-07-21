# get all schedule email

**GET** `{{url}}/api/email_schedule`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

## Examples

### get all schedule email

**Request:** `GET` `{{url}}/api/email_schedule`

**Response:** `200 OK`

```json
{
    "success": true,
    "data": [
        {
            "id": 1,
            "schedule_month": "*",
            "schedule_day": "*",
            "schedule_hour": "*",
            "schedule_minute": "*",
            "mail_subject": "test",
            "text": "test sms",
            "send_to_all": false,
            "active": true,
            "receiver": [
                1,
                2,
                3
            ]
        }
    ]
}
```
