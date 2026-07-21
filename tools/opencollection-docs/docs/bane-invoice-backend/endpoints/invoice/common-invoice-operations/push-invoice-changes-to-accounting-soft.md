# push invoice changes to accounting soft

**GET** `{{url}}/api/push-invoice-changes-to-accounting-software/568`

## Auth

Type: `bearer`

## Examples

### push changes to xero successfully

**Request:** `GET` `{{url}}/api/push-invoice-changes-to-accounting-software/568`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Changes are being pushed to the accounting software",
    "data": {
        "result": {
            "tracking_id_for_pushing_invoice_changes": "032e63e1-3316-4f11-b887-285a33c5729b"
        }
    }
}
```

### push invoice changes to accounting soft no changes detected

**Request:** `GET` `{{url}}/api/push-invoice-changes-to-accounting-software/576`

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Failed to push invoice changes",
    "error": "No changes detected",
    "errors": null
}
```
