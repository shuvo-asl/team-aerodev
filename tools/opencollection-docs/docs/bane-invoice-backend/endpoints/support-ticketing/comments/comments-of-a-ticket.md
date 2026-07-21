# comments of a ticket

**GET** `{{url}}/api/comments/?ticket_id=TCK-00014`

## 📘 GET `/api/comments/`

Retrieve comments for a specific ticket.

### ⚠️ Access Control

- Users with `can_assign_tickets` permission can access **all comments**.
    
- Other users can only access comments for tickets:
    
    - Where they are the **client**, or
        
    - Where they are the **assigned agent**.
        
- In those cases, the `ticket_id` query parameter is **required**.
    

### 🧾 Query Parameters

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ticket_id` | str |  | ID of the ticket to fetch comments for |

✅ Sample Response

``` json
{
  "status": "success",
  "message": "Comment Successfully Fetched",
  "data": {
    "result": [
      {
        "ticket": 14,
        "text": "example text",
        "id": 12,
        "created_at": "2025-05-08T13:28:52.282128+06:00",
        "attachments": [
          {
            "id": 23,
            "file": "http://localhost:5011/api/media/ticket_attachments/example.jpg"
          }
        ]
      }
    ]
  }
}

 ```

### ❌ Error Responses

| Status | Message | Condition |
| --- | --- | --- |
| 400 | `"Ticket ID is required"` | `ticket_id` is missing and user is not admin |
| 403 | `"You must change your password first."` | User flagged to change password |
| 403 | `"Permission denied"` |  |

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `ticket_id` | `TCK-00014` | query |

## Examples

### comments of a ticket

**Request:** `GET` `{{url}}/api/comments/?ticket_id=TCK-00014`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Message Successfully Fetched",
    "data": {
        "result": [
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 37,
                "created_at": "2025-05-19T11:42:18.787421+06:00",
                "user": {
                    "id": 1,
                    "name": "Admin Admin",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 36,
                "created_at": "2025-05-19T11:35:19.980441+06:00",
                "user": {
                    "id": 1,
                    "name": "Admin Admin",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 25,
                "created_at": "2025-05-15T11:49:27.315087+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": [
                    {
                        "id": 9,
                        "file": "http://localhost:5011/api/media/comment_attachments/bdflag_Woee0d1.jpg"
                    }
                ]
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 18,
                "created_at": "2025-05-14T14:53:08.202377+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 17,
                "created_at": "2025-05-14T14:48:29.130373+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 12,
                "created_at": "2025-05-08T13:28:52.282128+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 11,
                "created_at": "2025-05-05T16:06:59.686602+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 10,
                "created_at": "2025-05-05T15:27:53.929800+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 9,
                "created_at": "2025-05-05T15:03:58.064381+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 8,
                "created_at": "2025-05-05T15:02:03.974425+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 7,
                "created_at": "2025-05-05T15:00:19.913954+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 6,
                "created_at": "2025-05-05T14:59:39.740735+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 5,
                "created_at": "2025-05-05T14:58:13.834398+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 4,
                "created_at": "2025-05-05T12:50:04.556502+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 3,
                "created_at": "2025-05-05T12:48:36.498580+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 2,
                "created_at": "2025-05-05T12:48:01.249773+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": []
            },
            {
                "ticket": "TCK-00014",
                "text": "example text",
                "id": 1,
                "created_at": "2025-05-05T12:46:22.034478+06:00",
                "user": {
                    "id": 4,
                    "name": "admin1 admin1",
                    "profile_image": null
                },
                "attachments": []
            }
        ]
    }
}
```
