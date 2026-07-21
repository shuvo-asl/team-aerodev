# project wide implemented gateway

**GET** `{{url}}/api/project-wide-implemented-gateway/`

## Auth

Type: `bearer`

## Examples

### New Request

**Request:** `GET` `{{url}}/api/project-wide-implemented-gateway/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Implemented Payment Gateway Successfully Fetched",
    "data": {
        "result": [
            {
                "name": "ebl",
                "is_active": true
            }
        ]
    }
}
```
