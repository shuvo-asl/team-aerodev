# aircrfat type create

**POST** `{{url}}/aircraft-types`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `page` | `2` | query |
| `item_count` | `10` | query |
| `all` | `true` | query |

## Body

Type: `json`

```json
{
    "name": "test_type4",
    "wing_type": "Helicopter",
    "mtow": 1400,
    "mtow_unit": "kg",
    "is_registration_fulfilled": true
}
```

## Examples

### New Request

**Request:** `POST` `{{url}}/aircraft-types`

```json
{
    "name": "test_type4",
    "wing_type": "Helicopter",
    "mtow": 1400,
    "mtow_unit": "kg",
    "is_registration_fulfilled": true
}
```

**Response:** `201 CREATED`

```json
{
    "data": {
        "id": 1106,
        "is_deleted": false,
        "is_registration_fulfilled": true,
        "mtow": 1400,
        "mtow_unit": "kg",
        "name": "test_type4",
        "wing_type": "Helicopter"
    },
    "error": null,
    "errors": null,
    "message": "successful"
}
```
