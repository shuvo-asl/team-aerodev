# create schedule email

**POST** `{{url}}/api/email_schedule/`

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

## Examples

### create schedule email

**Request:** `POST` `{{url}}/api/email_schedule/`

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

**Response:** `201 Created`

```json
{
    "success": true,
    "data": {
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
}
```
