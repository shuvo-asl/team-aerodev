# implemented accounting software

**GET** `{{url}}/api/project-wide-implemented-accounting-software/`

## Auth

Type: `bearer`

## Examples

### New Request

**Request:** `GET` `{{url}}/api/project-wide-implemented-accounting-software/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Implemented Accounting Software Successfully Fetched",
    "data": {
        "result": [
            {
                "name": "xero",
                "is_active": true
            }
        ]
    }
}
```
