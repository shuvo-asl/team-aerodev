# get all notification subscription

**GET** `{{url}}/api/notification_subscribe`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

## Examples

### get all notification subscription

**Request:** `GET` `{{url}}/api/notification_subscribe`

**Response:** `200 OK`

```json
{
    "results": [
        {
            "id": 1,
            "name": "test",
            "send_to_all": false,
            "created_at": "2023-03-16T11:35:52.525655+06:00",
            "updated_at": "2023-03-16T11:35:52.525675+06:00",
            "created_by": 1,
            "updated_by": null,
            "receiver": [
                1
            ]
        }
    ]
}
```
