# delete internal notification

**DELETE** `{{url}}/api/notifications/1`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

```
[{'name': 'message', 'type': 'text', 'value': 'test notification'}, {'name': 'action_model', 'type': 'text', 'value': 'test', 'disabled': True}, {'name': 'action_object', 'type': 'text', 'value': '1', 'disabled': True}]
```
