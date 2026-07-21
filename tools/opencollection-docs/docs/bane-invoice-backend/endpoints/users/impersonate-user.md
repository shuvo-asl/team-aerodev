# impersonate user

**GET** `{{url}}/api/impersonate/24/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### impersonate user

**Request:** `GET` `{{url}}/api/impersonate/24/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Successfully impersonated",
    "data": {
        "result": {
            "id": 24,
            "first_name": "",
            "last_name": "",
            "username": "ismail",
            "email": "ismail21123@asl.aero",
            "phone": "+8801668970410",
            "profile_image": "/media/10UtsEg9u8pWHrNQw4_KWANjzD8ytnrGC",
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2NjM1NzI3LCJpYXQiOjE3MjY2MzU2MDcsImp0aSI6IjE5M2ZiYWQ3YTFiZDQ0M2RiZGY0ODI3YjM4NjFiY2JmIiwidXNlcl9pZCI6MjQsImltcGVyc29uYXRlZF9ieSI6ImFkbWluIn0.RPe2noQedLnrroISekEWsv7evOMacM1X1nx3Cya_C2A"
        }
    }
}
```
