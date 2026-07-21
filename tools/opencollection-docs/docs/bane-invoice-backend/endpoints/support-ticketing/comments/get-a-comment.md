# get a comment

**GET** `{{url}}/api/comments/12/`

## Auth

Type: `bearer`

## Examples

### get a comment

**Request:** `GET` `{{url}}/api/comments/12/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Comment Fetched Successfully",
    "data": {
        "result": {
            "ticket": 14,
            "text": "example text",
            "id": 12,
            "created_at": "2025-05-08T13:28:52.282128+06:00",
            "attachments": [
                {
                    "id": 23,
                    "file": "http://localhost:5011/api/media/ticket_attachments/bdflag_leeHYpC.jpg"
                }
            ]
        }
    }
}
```
