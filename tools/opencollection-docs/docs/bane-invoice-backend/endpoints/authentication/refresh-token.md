# Refresh Token

**POST** `{{url}}/api/token/refresh/`

## Auth

Type: `inherit`

## Body

Type: `json`

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTQzNTkyOSwiaWF0IjoxNzMxNDA3MTI5LCJqdGkiOiJjZDYzMTQwYjgyNTU0MDIyOWZiMjgzMmFjOTc3YzVhNSIsInVzZXJfaWQiOjN9.2E6odFuKi9nFhMWI2uy9WDa5ZXmAwh59AyJLmMpCgyw"
}
```

## Examples

### Refresh Token

**Request:** `POST` `{{url}}/api/token/refresh/`

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTQzNTkyOSwiaWF0IjoxNzMxNDA3MTI5LCJqdGkiOiJjZDYzMTQwYjgyNTU0MDIyOWZiMjgzMmFjOTc3YzVhNSIsInVzZXJfaWQiOjN9.2E6odFuKi9nFhMWI2uy9WDa5ZXmAwh59AyJLmMpCgyw"
}
```

**Response:** `200 OK`

```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNDM1OTQ3LCJpYXQiOjE3MzE0MDcxMjksImp0aSI6IjBkMDgyZmYwMGQ2NzRjZDBiNjNjODU0ZDNkOGEwMDYxIiwidXNlcl9pZCI6M30.QiY61DjJgjtPgU0CGgSTjqRcxG5hYgGt9T2v-V652Nc"
}
```
