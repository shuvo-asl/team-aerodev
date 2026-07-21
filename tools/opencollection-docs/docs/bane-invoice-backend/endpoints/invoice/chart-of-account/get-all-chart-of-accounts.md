# Get All Chart of Accounts

**GET** `{{url}}/api/account/?limit=10`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `code` | `abc` | query |
| `is_active` | `true` | query |
| `limit` | `10` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |
| `` | `` |

## Examples

### Get All Chart of Accounts

**Request:** `GET` `{{url}}/api/account/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Chart Of Account Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 1,
                "deleted_at": null,
                "created_at": "2024-08-25T11:20:08.256311+06:00",
                "updated_at": null,
                "account_name": "Regan",
                "code": "reg",
                "account_type": "current",
                "details": "na",
                "transaction_type": "expense"
            }
        ]
    }
}
```

### Get All Chart of Accounts

**Request:** `GET` `{{url}}/api/account/?limit=10`

**Response:** `401 Unauthorized`

```json
{
    "status": "failed",
    "message": "Authentication Failed",
    "error": "Invalid Token Or Token Was Not Provided",
    "errors": []
}
```
