# warning message for invoice duplication

**POST** `{{url}}/api/warning-message-for-duplication/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "invoice": 726,
    "companies": [5]
}
```

## Examples

### New Request

**Request:** `POST` `{{url}}/api/warning-message-for-duplication/`

```json
{
    "invoice": 722,
    "companies": [2, 5]
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Warning messages for duplication",
    "data": {
        "result": {
            "2": [
                {
                    "tax_rate": {
                        "message": "Following Tax Rates are not mapped and will be kept empty if copied anyway",
                        "tax_rates": [
                            {
                                "id": 18,
                                "name": "yhrty"
                            }
                        ]
                    }
                },
                {
                    "coa": {
                        "message": "Following Chart of Accounts are not mapped and will be kept empty if copied anyway",
                        "coas": [
                            {
                                "id": 18,
                                "account_name": "Office Expenses"
                            }
                        ]
                    }
                },
                {
                    "pdf_template": {
                        "message": "PDF Template dup5 not found and will be created automatically"
                    }
                }
            ],
            "5": [
                {
                    "tax_rate": {
                        "message": "Following Tax Rates are not mapped and will be kept empty if copied anyway",
                        "tax_rates": [
                            {
                                "id": 18,
                                "name": "yhrty"
                            }
                        ]
                    }
                },
                {
                    "coa": {
                        "message": "Following Chart of Accounts are not mapped and will be kept empty if copied anyway",
                        "coas": [
                            {
                                "id": 18,
                                "account_name": "Office Expenses"
                            }
                        ]
                    }
                },
                {
                    "pdf_template": {
                        "message": "PDF Template dup5 not found and will be created automatically"
                    }
                },
                {
                    "currency": {
                        "message": "Currency Bangladeshi Taka not found and will be created automatically"
                    }
                }
            ]
        }
    }
}
```
