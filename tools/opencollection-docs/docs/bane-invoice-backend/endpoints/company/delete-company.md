# delete company

**DELETE** `{{url}}/api/companies/3/`

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

### delete company (failed)

**Request:** `DELETE` `{{url}}/api/companies/3/`

```json
{
    "name": "Bd_company",
    "country": "Bangladesh"
}
```

**Response:** `404 Not Found`

```json
{
    "status": "failed",
    "message": "Company Failed To Delete",
    "error": "Company Not Found",
    "errors": null
}
```

### Delete company (owner check)

**Request:** `DELETE` `{{url}}/api/companies/3/`

```json
{
    "name": "Bd_company",
    "country": "Bangladesh"
}
```

**Response:** `403 Forbidden`

```json
{
    "status": "failed",
    "message": "Access Denied",
    "error": "Only the owner can delete this company.",
    "errors": []
}
```
