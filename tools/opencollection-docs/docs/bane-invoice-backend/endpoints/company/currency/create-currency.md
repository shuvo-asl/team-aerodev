# Create Currency

**POST** `{{url}}/api/currency/`

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
    "currency": 3,
    "is_default": true
}
```

## Examples

### Create Currency

**Request:** `POST` `{{url}}/api/currency/`

```json
{
    "currency": 3,
    "is_default": true
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Currency successfully created",
    "data": {
        "result": {
            "current_rate": 85.7098,
            "name": "Rupee",
            "prefix": "₹",
            "short_key": "INR",
            "id": 42,
            "is_default": false
        }
    }
}
```
