# send email

**POST** `{{url}}/api/send_email/`

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
    "users": [
        1,2,3
    ],
    "mail_subject": "Confirm Amit Malakar For the position of Junior Software Developer",
    "text": "Dear Ishtiak vai.please confirm amit malakar."
}
```

## Examples

### send email

**Request:** `POST` `{{url}}/api/send_email/`

```json
{
    "users": [
        1,2,3
    ],
    "mail_subject": "test",
    "text": "test"
}
```

**Response:** `200 OK`

```json
{
    "success": true
}
```
