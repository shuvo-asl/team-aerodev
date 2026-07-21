# update company

**PATCH** `{{url}}/api/companies/11/`

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
    "country": "Bangladesh"
}
```

## Examples

### update company

**Request:** `PATCH` `{{url}}/api/companies/3/`

```json
{
    "name": "Bd_company",
    "country": "Bangladesh"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Company successfully updated",
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
