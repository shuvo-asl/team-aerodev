# Password Reset With Token

**POST** `{{url}}/api/password_reset/?token=e245b7f7adfdb4eae497eee4 `

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `token` | `e245b7f7adfdb4eae497eee4 ` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

```json
{
    "email":"ismail@asl.aero"
}
```

## Examples

### Password Reset With Token

**Request:** `POST` `{{url}}/api/password_reset/?token=e245b7f7adfdb4eae497eee4 `

```json
{
    "email":"ismail@asl.aero"
}
```

**Response:** `200 OK`

```json
{
    "status": "OK"
}
```
