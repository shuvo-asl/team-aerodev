# Password Reset Confirm

**POST** `{{url}}/api/password_reset/confirm/`

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
    "token":"e245b7f7adfdb4eae497eee4",
    "password":"admin12345"
}
```

## Examples

### Password Reset Confirm

**Request:** `POST` `{{url}}/api/password_reset/confirm/`

```json
{
    "token":"e245b7f7adfdb4eae497eee4",
    "password":"admin12345"
}
```

**Response:** `200 OK`

```json
{
    "status": "OK"
}
```
