# company gateways

**GET** `{{url}}/api/implemented-company-gateway/11/200/`

## Auth

Type: `inherit`

## Examples

### company gateways

**Request:** `GET` `{{url}}/api/implemented-company-gateway/11/200/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Successfully Fetched Enabled Payment Gateways",
    "data": {
        "result": {
            "enabled_gateways": [
                "ebl"
            ]
        }
    }
}
```
