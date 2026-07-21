# top 5 due invoices

**GET** `{{url}}/api/dashboard/top-five-invoices/?based_on=due`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `based_on` | `due` | query |

## Examples

### top 5 due invoices

**Request:** `GET` `{{url}}/api/dashboard/top-five-invoices/?based_on=due`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Top Five Invoicessuccessfully fetched",
    "data": {
        "result": [
            {
                "id": 8,
                "due": 500,
                "percentage": 47.64,
                "client": {
                    "id": 3,
                    "name": "MD KAMRUL HASAN!!"
                }
            },
            {
                "id": 11,
                "due": 489.6,
                "percentage": 46.65,
                "client": {
                    "id": 15,
                    "name": "SRD Aviation"
                }
            },
            {
                "id": 3,
                "due": 20,
                "percentage": 1.91,
                "client": {
                    "id": 12,
                    "name": "test0"
                }
            },
            {
                "id": 5,
                "due": 20,
                "percentage": 1.91,
                "client": {
                    "id": 3,
                    "name": "MD KAMRUL HASAN!!"
                }
            },
            {
                "id": 12,
                "due": 20,
                "percentage": 1.91,
                "client": {
                    "id": 3,
                    "name": "MD KAMRUL HASAN!!"
                }
            }
        ]
    }
}
```
