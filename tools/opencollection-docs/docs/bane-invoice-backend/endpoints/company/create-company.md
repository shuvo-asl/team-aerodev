# create company

**POST** `{{url}}/api/companies/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

```json
{
    "name": "Bd_company",
    "country": "Bangladesh",
    "company_currency_id": 1
}
```

## Examples

### create company

**Request:** `POST` `{{url}}/api/companies/`

```json
{
    "name": "Bd_company",
    "country": "Bangladesh"
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Company successfully created",
    "data": {
        "result": {
            "id": 3,
            "name": "Bd_company",
            "country": "Bangladesh",
            "is_primary": false
        }
    }
}
```
