# update schedule email

**PUT** `{{url}}/api/email_schedule`

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
    "receiver": [
        1,2,3
    ],
    "schedule_month": "*",
    "schedule_day": "*",
    "schedule_hour": "*",
    "schedule_minute": "*",
    "mail_subject": "test",
    "text": "test sms"
}
```
