# top 5 paid invoice

**GET** `{{url}}/api/dashboard/top-five-invoices/?based_on=paid`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `based_on` | `paid` | query |

## Examples

### top 5 paid invoice

**Request:** `GET` `{{url}}/api/dashboard/top-five-invoices/?based_on=paid`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Top Five Invoicessuccessfully fetched",
    "data": {
        "result": [
            {
                "id": 1,
                "paid": 20,
                "percentage": 100,
                "client": {
                    "id": 3,
                    "name": "MD KAMRUL HASAN!!"
                }
            },
            {
                "id": 3,
                "paid": 0,
                "percentage": 0,
                "client": {
                    "id": 12,
                    "name": "test0"
                }
            },
            {
                "id": 5,
                "paid": 0,
                "percentage": 0,
                "client": {
                    "id": 3,
                    "name": "MD KAMRUL HASAN!!"
                }
            },
            {
                "id": 7,
                "paid": 0,
                "percentage": 0,
                "client": {
                    "id": 3,
                    "name": "MD KAMRUL HASAN!!"
                }
            },
            {
                "id": 8,
                "paid": 0,
                "percentage": 0,
                "client": {
                    "id": 3,
                    "name": "MD KAMRUL HASAN!!"
                }
            }
        ]
    }
}
```
