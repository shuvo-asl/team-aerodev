# create schedule

**POST** `{{url}}/api/operator-performance-summary-schedule/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
  "title": "test schedule",
  "sent_day": 5,
  "to": ["kamrul@asl.aero"],
  "cc": ["afroza@asl.aero", "titas@asl.aero"],
  "bcc": [],
  "time": "13:09",
  "sent_day": 20
}
```

## Examples

### create schedule

**Request:** `POST` `{{url}}/api/operator-performance-summary-schedule/`

```json
{
  "title": "test schedule",
  "sent_day": 5,
  "to": ["kamrul@asl.aero"],
  "cc": ["afroza@asl.aero", "titas@asl.aero"],
  "bcc": [],
  "time": "13:09",
  "sent_day": 20
}
```

**Response:** `201 Created`

```json
{
  "status": "success",
  "message": "Operator Performance Summary Schedule successfully created",
  "data": {
    "result": {
      "id": 4,
      "title": "test schedule",
      "to": [
        "kamrul@asl.aero"
      ],
      "cc": [
        "afroza@asl.aero",
        "titas@asl.aero"
      ],
      "bcc": [],
      "time": "13:09:00",
      "previous_month": true,
      "start_day": null,
      "end_day": null,
      "sent_day": 20,
      "created_at": "2026-07-02T05:59:03.476316Z",
      "updated_at": null
    }
  }
}
```
