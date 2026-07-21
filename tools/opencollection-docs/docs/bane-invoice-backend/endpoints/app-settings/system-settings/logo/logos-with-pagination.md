# logos with pagination

**GET** `{{url}}/api/system-settings/?type=logo&page=1&limit=3`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `type` | `logo` | query |
| `page` | `1` | query |
| `limit` | `3` | query |

## Examples

### logos with pagination

**Request:** `GET` `{{url}}/api/system-settings/?type=logo&page=1&limit=3`

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
                "id": 49,
                "deleted_at": null,
                "created_at": "2024-11-12T12:52:34.177770+06:00",
                "updated_at": null,
                "title": "logo for testing",
                "value_text": null,
                "value_file": null,
                "value_type": "",
                "type": "logo",
                "is_active": false,
                "logo": "http://localhost:5011/api/media/images/system_settings/logo/2024/11/12/bdflag.jpg",
                "bank_details": ""
            },
            {
                "id": 32,
                "deleted_at": null,
                "created_at": "2024-11-04T11:08:32.703479+06:00",
                "updated_at": null,
                "title": "sgdfs",
                "value_text": null,
                "value_file": null,
                "value_type": "",
                "type": "logo",
                "is_active": false,
                "logo": "http://localhost:5011/api/media/images/system_settings/logo/2024/11/04/Screenshot_from_2024-09-23_17-52-36_rTlMj01.png",
                "bank_details": ""
            },
            {
                "id": 31,
                "deleted_at": null,
                "created_at": "2024-11-04T11:07:04.363042+06:00",
                "updated_at": null,
                "title": "hello",
                "value_text": null,
                "value_file": null,
                "value_type": "",
                "type": "logo",
                "is_active": false,
                "logo": "http://localhost:5011/api/media/images/system_settings/logo/2024/11/04/AFRMS_logo_final_zMXBj2U.png",
                "bank_details": ""
            }
        ]
    }
}
```
