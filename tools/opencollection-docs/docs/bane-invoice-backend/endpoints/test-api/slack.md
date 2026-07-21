# Slack

**GET** `{{url}}/api/test/slack/`

## Auth

Type: `inherit`

## Examples

### Slack

**Request:** `POST` `{{url}}/api/test/slack/`

```json
{
    "log_level": "ERROR",
    "log": "Test log yfgruifgh"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Sent to slack",
    "data": {
        "result": {
            "log_level": "ERROR",
            "log": "Test log yfgruifgh"
        }
    }
}
```
