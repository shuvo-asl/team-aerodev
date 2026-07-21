# Create Aircraft

**POST** `{{url}}/api/bas/aircraft/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "icao24": "773907",
    "registration_number": "SH-ABC ",
    "operator_id": 2934,
    "aircraft_type_id": 10
}
```

## Examples

### Create Aircraft - Success

**Request:** `POST` `{{url}}/api/bas/aircraft/`

```json
{
    "icao24": "773907",
    "registration_number": "SH-ABC ",
    "operator_id": 2934,
    "aircraft_type_id": 10
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Aircraft created successfully",
    "data": {
        "result": {
            "id": 4820,
            "icao24": "773907",
            "registration_number": "SH-ABC",
            "operator_id": 2934,
            "operator_name": "Air Antilles",
            "aircraft_type_id": 10,
            "aircraft_type_name": "BD700-1A10"
        }
    }
}
```
