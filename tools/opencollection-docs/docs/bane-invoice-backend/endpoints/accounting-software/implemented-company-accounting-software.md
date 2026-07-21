# implemented company accounting software

**GET** `{{url}}/api/implemented-company-accounting-software/2/`

## Auth

Type: `inherit`

## Examples

### New Request

**Request:** `GET` `{{url}}/api/implemented-company-accounting-software/2/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Successfully Fetched Enabled Accounting Software",
    "data": {
        "result": {
            "enabled_software": [
                "xero"
            ]
        }
    }
}
```
