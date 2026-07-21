# create new company settins

**POST** `{{url}}/api/company-settings/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "type": "bank_details",
    "title": "comapany_bank",
    "bank_details": "quifheru"
}
```

## Examples

### bank details create

**Request:** `POST` `{{url}}/api/company-settings/`

```json
{
    "type": "bank_details",
    "title": "comapany_bank",
    "bank_details": "quifheru"
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Company Settings successfully created",
    "data": {
        "result": {
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
    }
}
```
