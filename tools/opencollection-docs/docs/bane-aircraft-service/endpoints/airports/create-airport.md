# create airport

**POST** `{{url}}/airports`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "name": "Tabarka–Aïn Draham International Airport",
    "city_id": "6249",
    "iata": "TBJ",
    "icao": "DTKA2",
    "latitude": "36.98",
    "longitude": "8.876944",
    "altitude": "0",
    "timezone": "1",
    "dst": "E",
    "tzdbtz": "Africa\/Tunis",
    "color": "#11f22f",
    "is_visible": "1",
    "is_deleted": "0",
    "comment": "example comment"
}
```

## Examples

### New Request

**Request:** `POST` `{{url}}/airports`

```json
{
    "city_id": 1,
    "icao": "VGHS",
    "name": "test"
}
```

**Response:** `400 BAD REQUEST`

```json
{
    "error": "Airport Already Exists",
    "errors": null,
    "message": "Input data is invalid"
}
```

### create airport

**Request:** `POST` `{{url}}/airports`

```json
{
    "name": "Tabarka–Aïn Draham International Airport",
    "city_id": "6249",
    "iata": "TBJ",
    "icao": "DTKA2",
    "latitude": "36.98",
    "longitude": "8.876944",
    "altitude": "0",
    "timezone": "1",
    "dst": "E",
    "tzdbtz": "Africa\/Tunis",
    "color": "#11f22f",
    "is_visible": "1",
    "is_deleted": "0",
    "comment": "example comment"
}
```

**Response:** `200 OK`

```json
{
    "data": {
        "altitude": "0",
        "city_id": 6249,
        "color": "#11f22f",
        "comment": "example comment",
        "created_by": {
            "user_name": "admin"
        },
        "created_by_id": 1,
        "dst": "E",
        "iata": "TBJ",
        "icao": "DTKA2",
        "id": 6826,
        "is_deleted": false,
        "is_visible": true,
        "latitude": "36.98",
        "longitude": "8.876944",
        "name": "Tabarka–Aïn Draham International Airport",
        "timezone": "1",
        "tzdbtz": "Africa/Tunis",
        "updated_by": {
            "user_name": "admin"
        },
        "updated_by_id": 1
    },
    "error": null,
    "errors": null,
    "message": "successful"
}
```
