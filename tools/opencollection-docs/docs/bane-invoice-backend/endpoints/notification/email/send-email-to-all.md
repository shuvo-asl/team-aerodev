# send email to all

**POST** `{{url}}/api/send_email_all/`

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
    "mail_subject": "test",
    "text": "test"
}
```

## Examples

### send email to all

**Request:** `POST` `{{url}}/api/send_email_all/`

```json
{
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
