# Get All Available Tax Rates For Mapping

**GET** `{{url}}/api/tax-rates/available-xero-for-mapping/?custom_tax_rate_id=11`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `custom_tax_rate_id` | `11` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |
| `` | `` |

## Examples

### available-xero-for-mapping

**Request:** `GET` `{{url}}/api/tax-rates/available-xero-for-mapping/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Available Xero tax rates for mapping retrieved successfully.",
    "data": {
        "result": [
            {
                "id": 20,
                "name": "Tax on Purchases",
                "rate": 8.25,
                "source": "Xero",
                "is_active": true,
                "others": {
                    "tax_type": "INPUT",
                    "tax_components": [
                        {
                            "Name": "State Tax",
                            "Rate": 4.25,
                            "IsCompound": false,
                            "IsNonRecoverable": false
                        },
                        {
                            "Name": "City Tax",
                            "Rate": 4,
                            "IsCompound": false,
                            "IsNonRecoverable": false
                        }
                    ]
                },
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 19,
                "name": "Tax on Goods",
                "rate": 8.75,
                "source": "Xero",
                "is_active": true,
                "others": {
                    "tax_type": "TAX001",
                    "tax_components": [
                        {
                            "Name": "State Tax",
                            "Rate": 4.5,
                            "IsCompound": false,
                            "IsNonRecoverable": false
                        },
                        {
                            "Name": "City Tax",
                            "Rate": 4.25,
                            "IsCompound": false,
                            "IsNonRecoverable": false
                        }
                    ]
                },
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 18,
                "name": "Tax on Consulting",
                "rate": 8.25,
                "source": "Xero",
                "is_active": true,
                "others": {
                    "tax_type": "OUTPUT",
                    "tax_components": [
                        {
                            "Name": "City Tax",
                            "Rate": 4,
                            "IsCompound": false,
                            "IsNonRecoverable": false
                        },
                        {
                            "Name": "State Tax",
                            "Rate": 4.25,
                            "IsCompound": false,
                            "IsNonRecoverable": false
                        }
                    ]
                },
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 17,
                "name": "Tax Exempt",
                "rate": 0,
                "source": "Xero",
                "is_active": true,
                "others": {
                    "tax_type": "NONE",
                    "tax_components": [
                        {
                            "Name": "No Tax",
                            "Rate": 0,
                            "IsCompound": false,
                            "IsNonRecoverable": false
                        }
                    ]
                },
                "default": true,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 16,
                "name": "Sales Tax on Imports",
                "rate": 0,
                "source": "Xero",
                "is_active": true,
                "others": {
                    "tax_type": "GSTONIMPORTS",
                    "tax_components": [
                        {
                            "Name": "TAX",
                            "Rate": 0,
                            "IsCompound": false,
                            "IsNonRecoverable": false
                        }
                    ]
                },
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 15,
                "name": "MB - GST/RST on Sales",
                "rate": 12,
                "source": "Xero",
                "is_active": true,
                "others": {
                    "tax_type": "CAN028",
                    "tax_components": [
                        {
                            "Name": "RST",
                            "Rate": 7,
                            "IsCompound": false,
                            "IsNonRecoverable": false
                        },
                        {
                            "Name": "GST",
                            "Rate": 5,
                            "IsCompound": false,
                            "IsNonRecoverable": false
                        }
                    ]
                },
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 14,
                "name": "MB - GST/RST on Purchases",
                "rate": 12,
                "source": "Xero",
                "is_active": true,
                "others": {
                    "tax_type": "CAN029",
                    "tax_components": [
                        {
                            "Name": "RST",
                            "Rate": 7,
                            "IsCompound": false,
                            "IsNonRecoverable": false
                        },
                        {
                            "Name": "GST",
                            "Rate": 5,
                            "IsCompound": false,
                            "IsNonRecoverable": false
                        }
                    ]
                },
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 13,
                "name": "Exempt Sales",
                "rate": 0,
                "source": "Xero",
                "is_active": true,
                "others": {
                    "tax_type": "CAN030",
                    "tax_components": [
                        {
                            "Name": "No Tax",
                            "Rate": 0,
                            "IsCompound": false,
                            "IsNonRecoverable": false
                        }
                    ]
                },
                "default": false,
                "mapped_xero_tax_rate": null
            }
        ]
    }
}
```

### Get All Available Tax Rates For Mapping

**Request:** `GET` `{{url}}/api/tax-rates/available-xero-for-mapping/?custom_tax_rate_id=11`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Available Xero tax rates for mapping retrieved successfully.",
    "data": {
        "result": [
            {
                "id": 20,
                "name": "Tax on Purchases",
                "rate": 8.25,
                "source": "Xero",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 18,
                "name": "Tax on Consulting",
                "rate": 8.25,
                "source": "Xero",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 16,
                "name": "Sales Tax on Imports",
                "rate": 0,
                "source": "Xero",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 15,
                "name": "MB - GST/RST on Sales",
                "rate": 12,
                "source": "Xero",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 14,
                "name": "MB - GST/RST on Purchases",
                "rate": 12,
                "source": "Xero",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 13,
                "name": "Exempt Sales",
                "rate": 0,
                "source": "Xero",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            }
        ]
    }
}
```
