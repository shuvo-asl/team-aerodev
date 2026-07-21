# Create A Tax Rate

**POST** `{{url}}/api/tax-rates/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "name": "Sales Exempt mapped",
    "rate": 0.0,
    "source": "Custom",
    "is_active": true,
    "default": false,
    "mapped_xero_tax_rate": 2
}
```

## Examples

### Create A Tax Rates

**Request:** `POST` `{{url}}/api/tax-rates/`

```json
{
    "company": 1,
    "name": "Sales Exempt mapped",
    "rate": 0.0,
    "source": "Bane",
    "is_active": true,
    "others": {},
    "default": false,
    "mapped_xero_tax_rate": 2
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Tax Rate successfully created",
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
