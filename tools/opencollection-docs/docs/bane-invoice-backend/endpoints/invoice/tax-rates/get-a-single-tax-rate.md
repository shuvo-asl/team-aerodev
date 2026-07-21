# Get A Single Tax Rate

**GET** `{{url}}/api/tax-rates/1/`

## Auth

Type: `bearer`

## Examples

### Get A Single Chart of Account

**Request:** `GET` `{{url}}/api/account/1/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Chart Of Account Fetched Successfully",
    "data": {
        "result": {
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
    }
}
```
