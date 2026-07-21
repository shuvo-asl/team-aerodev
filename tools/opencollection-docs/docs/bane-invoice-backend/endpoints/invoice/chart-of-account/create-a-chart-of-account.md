# Create A Chart of Account

**POST** `{{url}}/api/account/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "account_name": "Regan",
    "code": "regan",
    "account_type": "current",
    "details": "na",
    "transaction_type": "expense"
}
```

## Examples

### Create A Chart of Account

**Request:** `POST` `{{url}}/api/account/`

```json
{
    "account_name": "Regan",
    "code": "regan",
    "account_type": "current",
    "details": "na",
    "transaction_type": "expense"
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Chart Of Account successfully created",
    "data": {
        "result": {
            "id": 2,
            "deleted_at": null,
            "created_at": "2024-09-01T22:43:44.613725+06:00",
            "updated_at": null,
            "account_name": "Regan",
            "code": "regan",
            "account_type": "current",
            "details": "na",
            "transaction_type": "expense"
        }
    }
}
```
