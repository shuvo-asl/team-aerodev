# Update A Bank Account

**PATCH** `{{url}}/api/account/92/?object_name=bank`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `object_name` | `bank` | query |

## Body

Type: `json`

```json
{
    "currency_code": "USD",
    "account_number": "632897998"
}
```

## Examples

### Update A Bank Account

**Request:** `PATCH` `{{url}}/api/account/92/?object_name=bank`

```json
{
    "currency_code": "USD",
    "account_number": "632897998"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Bank Account successfully updated",
    "data": {
        "result": {
            "id": 92,
            "account_name": "test bank",
            "code": "bank54",
            "deleted_at": null,
            "created_at": "2024-11-05T13:49:21.654708+06:00",
            "updated_at": "2024-11-12T11:45:12.093293+06:00",
            "account_type": "BANK",
            "details": null,
            "transaction_type": "non_expense",
            "source": "xero",
            "account_number": "632897998",
            "currency_code": "USD",
            "bank_account_type": "other",
            "bank_name": "sonali bank",
            "is_active": true
        }
    }
}
```
