# Update Flights State

**GET** `{{url}}/api/test-update-flight-state/`

## Auth

Type: `bearer`

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
