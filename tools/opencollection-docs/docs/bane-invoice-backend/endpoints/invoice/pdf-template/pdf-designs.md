# pdf designs

**GET** `{{url}}/api/pdf-design/`

## Auth

Type: `bearer`

## Examples

### pdf designs

**Request:** `GET` `{{url}}/api/pdf-design/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "PDF Design Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 1,
                "template_name": "general inovoice template 1",
                "template_file_name": "general.html"
            },
            {
                "id": 2,
                "template_name": "Finance",
                "template_file_name": "finance_invoice.html"
            }
        ]
    }
}
```
