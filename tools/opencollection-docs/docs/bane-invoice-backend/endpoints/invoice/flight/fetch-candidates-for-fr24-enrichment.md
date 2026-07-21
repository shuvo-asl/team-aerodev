# fetch candidates for fr24 enrichment

**GET** `{{url}}/api/flight/32729/fr24-candidates/`

## Auth

Type: `bearer`

## Examples

### example

**Request:** `GET` `{{url}}/api/flight/32729/fr24-candidates/`

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "FR24 candidates fetched successfully",
  "data": {
    "result": [
      {
        "fr24_id": "4039adb8",
        "flight": null,
        "callsign": "5YBRE",
        "operating_as": null,
        "painted_as": null,
        "type": "C208",
        "reg": "5Y-BRE",
        "orig_icao": "HJJJ",
        "datetime_takeoff": "2026-06-17T06:01:46Z",
        "dest_icao": null,
        "dest_icao_actual": null,
        "datetime_landed": "2026-06-17T07:40:56Z",
        "hex": "04C17F",
        "first_seen": "2026-06-17T05:05:19Z",
        "last_seen": "2026-06-17T07:30:52Z",
        "flight_ended": true,
        "_score": 25,
        "_match_type": "callsign"
      },
      {
        "fr24_id": "403a0f81",
        "flight": null,
        "callsign": "5YBRE",
        "operating_as": null,
        "painted_as": null,
        "type": "C208",
        "reg": "5Y-BRE",
        "orig_icao": null,
        "datetime_takeoff": null,
        "dest_icao": "HJJJ",
        "dest_icao_actual": "HJJJ",
        "datetime_landed": "2026-06-17T09:17:35Z",
        "hex": "04C17F",
        "first_seen": "2026-06-17T07:53:33Z",
        "last_seen": "2026-06-17T09:17:35Z",
        "flight_ended": true,
        "_score": 15,
        "_match_type": "callsign"
      }
    ]
  }
}
```
