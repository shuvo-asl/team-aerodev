# get company settings

**GET** `{{url}}/api/company-settings/`

## Auth

Type: `bearer`

## Examples

### all company settings

**Request:** `GET` `{{url}}/api/company-settings/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Company Settings Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 1,
                "title": "comapany_bank",
                "bank_details": "quifheru",
                "deleted_at": null,
                "created_at": "2024-12-04T17:24:27.854570+06:00",
                "updated_at": null,
                "value_text": null,
                "value_file": null,
                "value_type": "",
                "type": "bank_details",
                "is_active": true,
                "logo": null,
                "company": 2
            }
        ]
    }
}
```
