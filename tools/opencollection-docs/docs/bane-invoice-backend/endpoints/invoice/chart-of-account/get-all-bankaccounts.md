# Get All BankAccounts

**GET** `{{url}}/api/account/?account_type=bank&object_name=bank`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `code` | `abc` | query |
| `is_active` | `true` | query |
| `limit` | `10` | query |
| `account_type` | `bank` | query |
| `object_name` | `bank` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |
| `` | `` |

## Examples

### Get All BankAccounts

**Request:** `GET` `{{url}}/api/account/?account_type=bank&object_name=bank`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Bank Account Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 92,
                "deleted_at": null,
                "created_at": "2024-11-05T13:49:21.654708+06:00",
                "updated_at": "2024-11-05T14:53:50.231054+06:00",
                "account_name": "yhrty2",
                "code": null,
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": "xero",
                "account_number": "632897998",
                "currency_code": "USD",
                "bank_account_type": "other",
                "bank_name": "yhrty2",
                "is_active": true
            },
            {
                "id": 93,
                "deleted_at": null,
                "created_at": "2024-11-05T13:49:21.679003+06:00",
                "updated_at": "2024-11-05T13:55:26.848420+06:00",
                "account_name": "yhrty",
                "code": null,
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": "xero",
                "account_number": "1212121212121",
                "currency_code": "BDT",
                "bank_account_type": "other",
                "bank_name": "yhrty",
                "is_active": true
            },
            {
                "id": 103,
                "deleted_at": null,
                "created_at": "2024-11-05T14:44:51.064078+06:00",
                "updated_at": null,
                "account_name": "test bank account30",
                "code": null,
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": null,
                "account_number": "6785",
                "currency_code": "BDT",
                "bank_account_type": "credit_card",
                "bank_name": "sonali bank",
                "is_active": true
            },
            {
                "id": 87,
                "deleted_at": null,
                "created_at": "2024-11-05T11:24:09.287642+06:00",
                "updated_at": null,
                "account_name": "test bank account2",
                "code": "",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": null,
                "account_number": "6785",
                "currency_code": "BDT",
                "bank_account_type": "credit_card",
                "bank_name": "sonali bank",
                "is_active": true
            },
            {
                "id": 65,
                "deleted_at": null,
                "created_at": "2024-10-08T15:51:19.277165+06:00",
                "updated_at": "2024-10-21T15:49:54.710236+06:00",
                "account_name": "Business Bank Account up",
                "code": "090",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": "xero",
                "account_number": "",
                "currency_code": "",
                "bank_account_type": "",
                "bank_name": "",
                "is_active": true
            },
            {
                "id": 66,
                "deleted_at": null,
                "created_at": "2024-10-08T15:51:19.333425+06:00",
                "updated_at": "2024-10-15T11:14:33.250058+06:00",
                "account_name": "Business Savings Account",
                "code": "091",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": "xero",
                "account_number": "",
                "currency_code": "",
                "bank_account_type": "",
                "bank_name": "",
                "is_active": true
            },
            {
                "id": 95,
                "deleted_at": null,
                "created_at": "2024-11-05T13:53:17.183736+06:00",
                "updated_at": "2024-11-05T13:55:26.871656+06:00",
                "account_name": "aaaaa",
                "code": "121",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": "xero",
                "account_number": "1212121212121",
                "currency_code": "BDT",
                "bank_account_type": "other",
                "bank_name": "aaaaa",
                "is_active": true
            },
            {
                "id": 97,
                "deleted_at": null,
                "created_at": "2024-11-05T13:55:06.400618+06:00",
                "updated_at": "2024-11-05T13:55:26.893771+06:00",
                "account_name": "fgfgftr",
                "code": "122",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": "xero",
                "account_number": "121212121212",
                "currency_code": "USD",
                "bank_account_type": "other",
                "bank_name": "fgfgftr",
                "is_active": true
            },
            {
                "id": 98,
                "deleted_at": null,
                "created_at": "2024-11-05T13:55:06.421219+06:00",
                "updated_at": "2024-11-05T13:55:26.913633+06:00",
                "account_name": "bbbb",
                "code": "123",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": "xero",
                "account_number": "1234",
                "currency_code": "BDT",
                "bank_account_type": "credit_card",
                "bank_name": "bbbb",
                "is_active": true
            },
            {
                "id": 99,
                "deleted_at": null,
                "created_at": "2024-11-05T13:55:06.446055+06:00",
                "updated_at": "2024-11-05T13:55:26.936085+06:00",
                "account_name": "bank account",
                "code": "8798890",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": "xero",
                "account_number": "455657677689",
                "currency_code": "BDT",
                "bank_account_type": "other",
                "bank_name": "bank account",
                "is_active": true
            },
            {
                "id": 100,
                "deleted_at": null,
                "created_at": "2024-11-05T13:55:06.480962+06:00",
                "updated_at": "2024-11-05T13:55:26.956527+06:00",
                "account_name": "Rupali Bank",
                "code": "BANK001",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": "xero",
                "account_number": "78389879",
                "currency_code": "USD",
                "bank_account_type": "other",
                "bank_name": "Rupali Bank",
                "is_active": true
            },
            {
                "id": 85,
                "deleted_at": null,
                "created_at": "2024-11-05T11:00:36.401380+06:00",
                "updated_at": null,
                "account_name": "test bank account",
                "code": "bank0079",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": null,
                "account_number": "6785",
                "currency_code": "BDT",
                "bank_account_type": "credit_card",
                "bank_name": "",
                "is_active": true
            },
            {
                "id": 88,
                "deleted_at": null,
                "created_at": "2024-11-05T11:26:07.752597+06:00",
                "updated_at": null,
                "account_name": "test bank account3",
                "code": "bank0090",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": null,
                "account_number": "6785",
                "currency_code": "BDT",
                "bank_account_type": "credit_card",
                "bank_name": "sonali bank",
                "is_active": true
            },
            {
                "id": 101,
                "deleted_at": null,
                "created_at": "2024-11-05T13:55:06.508156+06:00",
                "updated_at": "2024-11-05T13:55:26.975403+06:00",
                "account_name": "Sonali BANK",
                "code": "BANK123",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": "xero",
                "account_number": "12986387838",
                "currency_code": "USD",
                "bank_account_type": "other",
                "bank_name": "Sonali BANK",
                "is_active": true
            },
            {
                "id": 102,
                "deleted_at": null,
                "created_at": "2024-11-05T13:55:06.533656+06:00",
                "updated_at": "2024-11-05T13:55:26.995247+06:00",
                "account_name": "Sonali BANK2",
                "code": "BANK1234",
                "account_type": "BANK",
                "details": null,
                "transaction_type": "non_expense",
                "source": "xero",
                "account_number": "7838",
                "currency_code": "USD",
                "bank_account_type": "credit_card",
                "bank_name": "Sonali BANK2",
                "is_active": true
            }
        ]
    }
}
```
