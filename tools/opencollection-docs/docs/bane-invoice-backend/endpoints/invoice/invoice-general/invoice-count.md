# invoice count

**GET** ``

## Auth

Type: `inherit`

## Examples

### invoice count

**Request:** `GET` `{{url}}/api/invoice-count/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice count successfully fetched",
    "data": {
        "result": {
            "draft": 6,
            "approved": 0,
            "awaiting_payment": 122
        }
    }
}
```
