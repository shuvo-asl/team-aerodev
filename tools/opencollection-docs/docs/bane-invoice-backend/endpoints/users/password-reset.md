# Password Reset

**POST** `{{url}}/api/password_reset/`

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
    "email":"coyoc50513@opposir.com"
}
```

## Examples

### Password Reset

**Request:** `POST` `{{url}}/api/password_reset/`

```json
{
    "email":"coyoc50513@opposir.com"
}
```

**Response:** `200 OK`

```json
{
    "status": "OK"
}
```
