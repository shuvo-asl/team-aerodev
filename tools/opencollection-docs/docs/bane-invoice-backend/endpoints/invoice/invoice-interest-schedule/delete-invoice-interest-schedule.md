# delete  Invoice Interest Schedule

**DELETE** `{{url}}/api/invoice-interest-schedule/2/?invoice_id=178`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `invoice_id` | `178` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

## Examples

### delete  Invoice Interest Schedule

**Request:** `DELETE` `{{url}}/api/invoice-interest-schedule/2/?invoice_id=178`

**Response:** `204 No Content`

```json
{
    "status": "success",
    "message": "Invoice Interest Schedule Successfully Deleted",
    "data": {
        "result": []
    }
}
```
