# create pdf templates

**POST** `{{url}}/api/pdf-template/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "design_id": 3,
    "has_bank_details": false,
    // "bank_details_id": 3,
    "has_chasing_details": true,
    "title": "Default PDF template for SSAAA Update",
    "terms_and_conditions": "abcd",
    "fields_of_interest": {
        "table_fields": ["serial", "name", "unit", "unit_price", "sub_total", "discount_rate", "tax_rate", "tax_amount", "total"],
        "summary_fields": ["amount", "tax_amount", "payable_amount"]
    },
    "is_default":true

}
```

## Examples

### create templates

**Request:** `POST` `{{url}}/api/pdf-template/`

```json
{
    "design_id": 1,
    "logo_id": 24,
    "has_bank_details": true,
    "bank_details_id": 25,
    "has_chasing_details": true,
    "title": "example title267"
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "PDF Template successfully created",
    "data": {
        "result": {
            "id": 29,
            "title": "example title267",
            "design_id": 1,
            "logo_id": 24,
            "has_bank_details": true,
            "bank_details_id": 25,
            "has_chasing_details": true,
            "logo_title": "test logo",
            "logo_file": "http://localhost:5011/api/media/images/system_settings/logo/2024/11/04/ASL_logo_Update_2024_by_ZM_FINAL.png",
            "bank_details_title": "test",
            "bank_details": "example bank",
            "design_template_name": "general inovoice template 1",
            "design_template_file_name": "general.html"
        }
    }
}
```
