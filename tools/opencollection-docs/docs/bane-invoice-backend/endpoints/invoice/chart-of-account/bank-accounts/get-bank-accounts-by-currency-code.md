# get bank accounts by currency code

**GET** `{{url}}/api/account/?account_type=BANK&object_name=bank&currency_code=INR`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `account_type` | `BANK` | query |
| `object_name` | `bank` | query |
| `currency_code` | `INR` | query |

## Examples

### get bank accounts by currency code

**Request:** `GET` `{{url}}/api/account/?account_type=BANK&object_name=bank&currency_code=INR`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Bank Account Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 117,
                "account_name": "dvdxvx",
                "code": "01",
                "deleted_at": null,
                "created_at": "2024-11-11T11:21:58.710793+06:00",
                "updated_at": "2024-11-11T11:22:13.057732+06:00",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "expense",
                "source": null,
                "account_number": "22334456789",
                "currency_code": "INR",
                "bank_account_type": "other",
                "bank_name": "city bank",
                "is_active": true
            }
        ]
    }
}
```
