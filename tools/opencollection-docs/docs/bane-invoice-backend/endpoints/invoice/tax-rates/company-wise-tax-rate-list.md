# company wise tax rate list

**GET** `{{url}}/api/tax-rates/company/1`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `is_active` | `true` | query |
| `default` | `true` | query |
| `source` | `Xero` | query |
| `limit` | `10` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |
| `` | `` |

## Examples

### New Request

**Request:** `GET` `{{url}}/api/tax-rates/company/1`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Tax Rate Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 20,
                "name": "rttttttte",
                "rate": 12,
                "source": "Custom",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 19,
                "name": "erter",
                "rate": 12,
                "source": "Custom",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 18,
                "name": "yhrty",
                "rate": 31,
                "source": "Custom",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 17,
                "name": "asfsa",
                "rate": 23,
                "source": "Custom",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": 4,
                "mapped_xero_tax_rate_name": "Exempt Sales"
            },
            {
                "id": 16,
                "name": "sdfs",
                "rate": 12,
                "source": "Custom",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": 9,
                "mapped_xero_tax_rate_name": "Tax on Consulting"
            },
            {
                "id": 15,
                "name": "fdgd",
                "rate": 5,
                "source": "Custom",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": 8,
                "mapped_xero_tax_rate_name": "Tax Exempt"
            },
            {
                "id": 14,
                "name": "dfsd",
                "rate": 3,
                "source": "Custom",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": 13,
                "mapped_xero_tax_rate_name": "Tax on Sales"
            },
            {
                "id": 13,
                "name": "Tax on Sales",
                "rate": 0,
                "source": "Xero",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 12,
                "name": "Sales Exempt",
                "rate": 34,
                "source": "Custom",
                "is_active": false,
                "default": false,
                "mapped_xero_tax_rate": 10,
                "mapped_xero_tax_rate_name": "Tax on Goods"
            },
            {
                "id": 11,
                "name": "Tax on Purchases",
                "rate": 0,
                "source": "Xero",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 10,
                "name": "Tax on Goods",
                "rate": 8.75,
                "source": "Xero",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 9,
                "name": "Tax on Consulting",
                "rate": 8.25,
                "source": "Xero",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 8,
                "name": "Tax Exempt",
                "rate": 0,
                "source": "Xero",
                "is_active": true,
                "default": true,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 7,
                "name": "Sales Tax on Imports",
                "rate": 0,
                "source": "Xero",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 6,
                "name": "MB - GST/RST on Sales",
                "rate": 12,
                "source": "Xero",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 5,
                "name": "MB - GST/RST on Purchases",
                "rate": 12,
                "source": "Xero",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 4,
                "name": "Exempt Sales",
                "rate": 0,
                "source": "Xero",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 3,
                "name": "Tax sales",
                "rate": 20,
                "source": "Custom",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": 11,
                "mapped_xero_tax_rate_name": "Tax on Purchases"
            },
            {
                "id": 2,
                "name": "Sales Exempt 3",
                "rate": 10,
                "source": "Custom",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 1,
                "name": "sales",
                "rate": 3.4,
                "source": "Custom",
                "is_active": true,
                "default": false,
                "mapped_xero_tax_rate": null
            }
        ]
    }
}
```
