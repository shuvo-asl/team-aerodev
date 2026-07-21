# company data mapping pairs

**GET** `{{url}}/api/company-data-mapping-pairs/tax-rate`

## Auth

Type: `bearer`

## Examples

### company data mapping pairs

**Request:** `GET` `{{url}}/api/company-data-mapping-pairs/tax-rate`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Company mapping pair Successfully Fetched",
    "data": {
        "result": [
            {
                "from_company": 1,
                "from_company_name": "ASL",
                "to_company": 2,
                "to_company_name": "Aerogon",
                "last_updated": "2025-09-02T15:48:16.839001+06:00"
            }
        ]
    }
}
```
