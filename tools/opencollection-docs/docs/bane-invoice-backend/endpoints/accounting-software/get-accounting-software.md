# get accounting software

**GET** `{{url}}/api/accounting-software/13/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### get accounting soft

**Request:** `GET` `{{url}}/api/accounting-software/4`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Accounting Software Fetched Successfully",
    "data": {
        "result": {
            "id": 4,
            "name": "xero",
            "credentials": {
                "client_id": "gAAAAABm1W2684UEdMOJRZPRELUaLVu97vAhQZmlW_Lo7CIAhKMOk0E1kq4xMlE15a5RNnW-xwsRoCEr2KBoFYWnsN96wHqVIQ=="
            }
        }
    }
}
```

### get accounting software

**Request:** `GET` `{{url}}/api/accounting-software/7`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Accounting Software Fetched Successfully",
    "data": {
        "result": {
            "id": 7,
            "name": "flow",
            "credentials": {
                "api_secret": "very secret key"
            }
        }
    }
}
```
