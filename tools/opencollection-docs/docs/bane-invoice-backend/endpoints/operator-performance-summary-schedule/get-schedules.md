# get schedules

**GET** `{{url}}/api/operator-performance-summary-schedule`

## Auth

Type: `bearer`

## Examples

### list of schedules

**Request:** `GET` `{{url}}/api/operator-performance-summary-schedule`

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "Operator Performance Summary Schedule Successfully Fetched",
  "data": {
    "result": [
      {
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
    ]
  }
}
```
