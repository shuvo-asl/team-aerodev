# Update A Chart of Account

**PATCH** `{{url}}/api/account/2/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "account_type": "savings"
}
```

## Examples

### Update A Chart of Account

**Request:** `PATCH` `{{url}}/api/account/2/`

```json
{
    "account_type": "savings"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Chart Of Account successfully updated",
    "data": {
        "result": {
            "id": 2,
            "deleted_at": null,
            "created_at": "2024-09-01T22:43:44.613725+06:00",
            "updated_at": "2024-09-01T22:44:00.873647+06:00",
            "account_name": "Regan",
            "code": "regan",
            "account_type": "savings",
            "details": "na",
            "transaction_type": "expense"
        }
    }
}
```
