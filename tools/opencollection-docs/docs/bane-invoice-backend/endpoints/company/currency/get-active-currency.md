# Get active currency

**GET** `{{url}}/api/current-currency/`

## Auth

Type: `bearer`

## Examples

### Get active currency

**Request:** `GET` `{{url}}/api/current-currency/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Active Currency Fetched Successfully",
    "data": {
        "result": {
            "id": 1,
            "prefix": "$",
            "short_key": "BDT",
            "current_rate": 1,
            "default": true
        }
    }
}
```
