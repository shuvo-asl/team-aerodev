# update notification subscribe

**PATCH** `{{url}}/api/notification_subscribe/2/`

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
    "send_to_all": false
}
```

## Examples

### create notification subscribe

**Request:** `POST` `{{url}}/api/notification_subscribe/`

```json
{
    "receiver": [
        1,2,3
    ],
    "name": "app"
}
```

**Response:** `200 OK`

```json
{
    "success": true,
    "data": {
        "id": 2,
        "name": "app",
        "send_to_all": false,
        "created_at": "2023-03-27T10:52:19.502570+06:00",
        "updated_at": "2023-03-27T10:52:19.502582+06:00",
        "created_by": 1,
        "updated_by": null,
        "receiver": [
            1,
            2,
            3
        ]
    }
}
```

### update notification subscribe

**Request:** `PATCH` `{{url}}/api/notification_subscribe/2/`

```json
{
    "send_to_all": true
}
```

**Response:** `200 OK`

```json
{
    "success": true,
    "data": {
        "id": 2,
        "name": "app",
        "send_to_all": true,
        "created_at": "2023-03-27T10:52:19.502570+06:00",
        "updated_at": "2023-03-27T10:52:19.502582+06:00",
        "created_by": 1,
        "updated_by": 1,
        "receiver": [
            1,
            2,
            3
        ]
    }
}
```
