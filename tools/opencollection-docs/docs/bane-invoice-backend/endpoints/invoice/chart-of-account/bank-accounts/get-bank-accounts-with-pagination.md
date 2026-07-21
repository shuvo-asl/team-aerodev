# get bank accounts with pagination

**GET** `{{url}}/api/account/?account_type=BANK&object_name=bank&page=1&limit=2`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `account_type` | `BANK` | query |
| `object_name` | `bank` | query |
| `page` | `1` | query |
| `limit` | `2` | query |

## Examples

### get bank accounts Copy

**Request:** `GET` `{{url}}/api/account/?account_type=BANK&object_name=bank&page=1&limit=2`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Bank Account Successfully Fetched",
    "data": {
        "next": 2,
        "previous": null,
        "current_page": 1,
        "total_object": 17,
        "total_page": 9,
        "result": [
            {
                "id": 93,
                "account_name": "yhrty",
                "code": null,
                "deleted_at": null,
                "created_at": "2024-11-05T13:49:21.679003+06:00",
                "updated_at": "2024-11-11T11:21:32.683550+06:00",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": "xero",
                "account_number": "1212121212121",
                "currency_code": "USD",
                "bank_account_type": "other",
                "bank_name": "yhrty",
                "is_active": true
            },
            {
                "id": 113,
                "account_name": "nggh",
                "code": null,
                "deleted_at": null,
                "created_at": "2024-11-07T10:30:28.013866+06:00",
                "updated_at": "2024-11-07T10:39:44.455817+06:00",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": null,
                "account_number": "",
                "currency_code": "BDT",
                "bank_account_type": "other",
                "bank_name": "city bank",
                "is_active": true
            }
        ]
    }
}
```
