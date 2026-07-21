# Create A Bank account

**POST** `{{url}}/api/account/?object_name=bank`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `object_name` | `bank` | query |

## Headers

| Name | Value |
|---|---|
| `object_name` | `bank` |

## Body

Type: `json`

```json
{
    "account_type": "BANK",
    "account_name": "test bank account3012",
    "transaction_type": "non_expense",
    "account_number": "4204",
    "bank_account_type": "credit_card",
    "currency_code": "USD",
    "bank_name": "sonali bank",
    "code": "bank-1212"
}
```

## Examples

### Create A Bank account

**Request:** `POST` `{{url}}/api/account/?object_name=bank`

```json
{
    "account_type": "BANK",
    "account_name": "test bank account3012",
    "transaction_type": "non_expense",
    "account_number": "4204",
    "bank_account_type": "credit_card",
    "currency_code": "USD",
    "bank_name": "sonali bank",
    "code": "bank-1212"
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Bank Account successfully created",
    "data": {
        "result": {
            "id": 118,
            "account_name": "test bank account3012",
            "code": "bank-1212",
            "deleted_at": null,
            "created_at": "2024-11-12T11:44:21.208265+06:00",
            "updated_at": null,
            "account_type": "BANK",
            "details": null,
            "transaction_type": "non_expense",
            "source": null,
            "account_number": "4204",
            "currency_code": "USD",
            "bank_account_type": "credit_card",
            "bank_name": "sonali bank",
            "is_active": true
        }
    }
}
```
