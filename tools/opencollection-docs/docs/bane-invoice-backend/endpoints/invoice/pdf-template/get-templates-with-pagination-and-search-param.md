# get templates with pagination and search param

**GET** `{{url}}/api/pdf-template/?page=1&limit=2&search=general`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `page` | `1` | query |
| `limit` | `2` | query |
| `search` | `general` | query |

## Examples

### get templates with pagination and search param

**Request:** `GET` `{{url}}/api/pdf-template/?page=1&limit=2&search=general`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "PDF Template Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 1,
        "total_page": 1,
        "result": [
            {
                "id": 26,
                "title": "Finance General Invoice",
                "design_id": 2,
                "logo_id": 5,
                "has_bank_details": true,
                "bank_details_id": 47,
                "has_chasing_details": false,
                "logo_title": "asl_logo",
                "logo_file": null,
                "bank_details_title": "FinaceBankDetails",
                "bank_details": "Beneficiary Name: Aerogon PTE Ltd\r\nBeneficiary Account Number: 288-903319-0\r\nSWIFT Code: DBSSSGSG\r\nBank NameDBS Bank Limited\r\nAddress:12 Marina Boulevard\r\nMarina Bay Financial Ccenter Tower 3\r\nSingapore 018982\r\nTel: +65 6878 8881, 6878 8882.",
                "design_template_name": "Finance",
                "design_template_file_name": "finance_invoice.html"
            }
        ]
    }
}
```
