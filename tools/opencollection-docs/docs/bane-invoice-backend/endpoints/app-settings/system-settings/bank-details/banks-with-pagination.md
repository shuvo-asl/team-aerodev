# banks with pagination

**GET** `{{url}}/api/system-settings/?type=bank_details&page=1&limit=3`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `type` | `bank_details` | query |
| `page` | `1` | query |
| `limit` | `3` | query |

## Examples

### banks with pagination

**Request:** `GET` `{{url}}/api/system-settings/?type=bank_details&page=1&limit=3`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "System Settings Successfully Fetched",
    "data": {
        "next": 2,
        "previous": null,
        "current_page": 1,
        "total_object": 7,
        "total_page": 3,
        "result": [
            {
                "id": 48,
                "deleted_at": null,
                "created_at": "2024-11-12T12:49:10.618132+06:00",
                "updated_at": null,
                "title": "imp bank info",
                "value_text": null,
                "value_file": null,
                "value_type": "",
                "type": "bank_details",
                "is_active": true,
                "logo": null,
                "bank_details": "example Bank deatils"
            },
            {
                "id": 47,
                "deleted_at": null,
                "created_at": "2024-11-11T11:11:52+06:00",
                "updated_at": "2024-11-11T11:22:21.814277+06:00",
                "title": "FinaceBankDetails",
                "value_text": null,
                "value_file": null,
                "value_type": "",
                "type": "bank_details",
                "is_active": true,
                "logo": null,
                "bank_details": "Beneficiary Name: Aerogon PTE Ltd\r\nBeneficiary Account Number: 288-903319-0\r\nSWIFT Code: DBSSSGSG\r\nBank NameDBS Bank Limited\r\nAddress:12 Marina Boulevard\r\nMarina Bay Financial Ccenter Tower 3\r\nSingapore 018982\r\nTel: +65 6878 8881, 6878 8882."
            },
            {
                "id": 38,
                "deleted_at": null,
                "created_at": "2024-11-04T11:45:59.739253+06:00",
                "updated_at": null,
                "title": "qwert",
                "value_text": null,
                "value_file": null,
                "value_type": "",
                "type": "bank_details",
                "is_active": true,
                "logo": null,
                "bank_details": "qwert"
            }
        ]
    }
}
```
