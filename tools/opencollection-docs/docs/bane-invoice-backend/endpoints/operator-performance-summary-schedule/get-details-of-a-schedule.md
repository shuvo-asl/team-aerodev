# get details of a schedule

**GET** `{{url}}/api/operator-performance-summary-schedule/3`

## Auth

Type: `bearer`

## Examples

### details of a schedule

**Request:** `GET` `{{url}}/api/operator-performance-summary-schedule/3`

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "Operator Performance Summary Schedule Fetched Successfully",
  "data": {
    "result": {
      "id": 3,
      "title": "test1",
      "to": [
        "oiewjfi@gmail.com"
      ],
      "cc": [],
      "bcc": [],
      "time": null,
      "previous_month": true,
      "start_day": null,
      "end_day": null,
      "sent_day": 5,
      "created_at": "2026-07-02T05:53:12.003979Z",
      "updated_at": null
    }
  }
}
```
