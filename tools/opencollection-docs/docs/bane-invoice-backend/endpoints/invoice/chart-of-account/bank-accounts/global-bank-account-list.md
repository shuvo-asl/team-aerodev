# global bank account list

**GET** `{{url}}/api/global-bank-account-list/`

## Auth

Type: `bearer`

## Body

Type: `text`

## Examples

### global list of bank accounts

**Request:** `GET` `{{url}}/api/global-bank-account-list/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Bank Accounts Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 66,
                "bank_name": "bank account usd",
                "banks_company_name": "ASL"
            },
            {
                "id": 64,
                "bank_name": "City Bank PLC",
                "banks_company_name": "Aerogon"
            },
            {
                "id": 57,
                "bank_name": "city afg",
                "banks_company_name": "ASL"
            },
            {
                "id": 56,
                "bank_name": "CITY BDT",
                "banks_company_name": "ASL"
            },
            {
                "id": 55,
                "bank_name": "CITY USD",
                "banks_company_name": "ASL"
            }
        ]
    }
}
```
