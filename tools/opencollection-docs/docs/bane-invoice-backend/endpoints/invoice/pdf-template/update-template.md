# update template

**PATCH** `{{url}}/api/pdf-template/2/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "is_default":true
}
```

## Examples

### update template

**Request:** `PATCH` `{{url}}/api/pdf-template/29/`

```json
{
    "logo_id": 24,
    "has_chasing_details": false
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "PDF Template successfully updated",
    "data": {
        "result": {
            "id": 29,
            "title": "example title267",
            "design_id": 1,
            "logo_id": 24,
            "has_bank_details": true,
            "bank_details_id": 25,
            "has_chasing_details": false,
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
