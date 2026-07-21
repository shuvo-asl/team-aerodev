# Update A Tax Rate

**PATCH** `{{url}}/api/tax-rates/11/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "name": "Sales Exempt 3",
    "rate": 0,
    "source": "Custom",
    "is_active": true,
    "default": false,
    "mapped_xero_tax_rate": 13
}
```

## Examples

### Update A Tax Rate

**Request:** `PATCH` `{{url}}/api/tax-rates/7/`

```json
{
    "company": 1,
    "name": "Sales Exempt mapped",
    "rate": 0,
    "source": "Bane",
    "is_active": true,
    "others": {},
    "default": false,
    "mapped_xero_tax_rate": 2
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Tax Rate successfully updated",
    "data": {
        "result": {
            "id": 7,
            "company": 1,
            "name": "Sales Exempt mapped",
            "rate": 0,
            "source": "Bane",
            "is_active": true,
            "others": {},
            "default": false,
            "mapped_xero_tax_rate": 2
        }
    }
}
```
