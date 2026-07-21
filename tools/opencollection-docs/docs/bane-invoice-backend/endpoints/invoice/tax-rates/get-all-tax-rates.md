# Get All Tax Rates

**GET** `{{url}}/api/tax-rates/?search=tax`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `is_active` | `true` | query |
| `default` | `true` | query |
| `source` | `Xero` | query |
| `limit` | `10` | query |
| `search` | `tax` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |
| `` | `` |

## Examples

### Get All Tax Rates

**Request:** `GET` `{{url}}/api/tax-rates/?limit=10`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Tax Rate Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 4,
        "total_page": 1,
        "result": [
            {
                "id": 7,
                "company": 1,
                "name": "Sales Exempt mapped",
                "rate": 0,
                "source": "Bane",
                "is_active": true,
                "others": {},
                "default": false,
                "mapped_xero_tax_rate": 2
            },
            {
                "id": 3,
                "company": 1,
                "name": "Sales Exempt 2",
                "rate": 0,
                "source": "Bane",
                "is_active": true,
                "others": {},
                "default": false,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 2,
                "company": 1,
                "name": "Sales Exempt",
                "rate": 0,
                "source": "Xero",
                "is_active": true,
                "others": {},
                "default": true,
                "mapped_xero_tax_rate": null
            },
            {
                "id": 1,
                "company": 1,
                "name": "Sales Exempt",
                "rate": 0,
                "source": "Bane",
                "is_active": true,
                "others": {},
                "default": true,
                "mapped_xero_tax_rate": null
            }
        ]
    }
}
```
