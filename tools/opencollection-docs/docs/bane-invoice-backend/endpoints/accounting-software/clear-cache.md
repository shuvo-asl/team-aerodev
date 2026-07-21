# clear cache

**POST** `{{url}}/api/clear-cache-by-key/`

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
    "keyword": "xero"
}
```

## Examples

### clear cache

**Request:** `POST` `{{url}}/api/clear-cache-by-key/`

```json
{
    "keyword": "xero"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Cleared 3 cache keys containing the keyword \"xero\".",
    "data": {
        "result": [
            "xero_tax_rates",
            "xero_contact_ismail@asl.aero",
            "xero_items"
        ]
    }
}
```
