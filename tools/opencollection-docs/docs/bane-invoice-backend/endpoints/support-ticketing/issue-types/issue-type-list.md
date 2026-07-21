# issue type list

**GET** `{{url}}/api/issue-types/`

## Auth

Type: `bearer`

## Examples

### New Request

**Request:** `GET` `{{url}}/api/issue-types/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Issue Type Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 1,
                "name": "Payment"
            },
            {
                "id": 2,
                "name": "Currency Issue"
            },
            {
                "id": 3,
                "name": "Need Human Assistance"
            }
        ]
    }
}
```
