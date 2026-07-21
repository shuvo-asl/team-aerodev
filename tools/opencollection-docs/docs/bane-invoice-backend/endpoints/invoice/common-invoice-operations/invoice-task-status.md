# invoice task status

**GET** `{{url}}/api/task-status/?email_tracking_id=4fc537cd-1917-46fe-9bd9-b29cacab5d&accounting_software_tracking_id=714f6c6e-3777-4a96-a413-ee9ba97a7aa5`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `email_tracking_id` | `4fc537cd-1917-46fe-9bd9-b29cacab5d` | query |
| `accounting_software_tracking_id` | `714f6c6e-3777-4a96-a413-ee9ba97a7aa5` | query |

## Examples

### invoice task status

**Request:** `GET` `{{url}}/api/task-status/?email_tracking_id=c13310c4-885f-4189-a793-001d72c70df9&accounting_software_tracking_id=e493ad77-cbff-4a97-a3fd-f10bf4d81aad`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Email status fetched and Accounting software status fetched successfully",
    "data": {
        "result": {
            "email_tracking": {
                "task_id": "c13310c4-885f-4189-a793-001d72c70df9",
                "status": "SUCCESS",
                "result": null
            },
            "accounting_software_tracking": {
                "task_id": "e493ad77-cbff-4a97-a3fd-f10bf4d81aad",
                "status": "SUCCESS",
                "result": null
            },
            "message": "Email status fetched and Accounting software status fetched successfully"
        }
    }
}
```
