# ticket events

**GET** `{{url}}/api/ticket-event-stream/TCK-00001?last_event_id=1`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `last_event_id` | `1` | query |

## Examples

### ticket events without pagination

**Request:** `GET` `{{url}}/api/ticket-event-stream/TCK-00001?last_event_id=1`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Ticket Event Stream Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 6,
                "event_type": "comment_created",
                "payload": {
                    "text": "example text",
                    "user_id": 1,
                    "attachments": [
                        {
                            "id": 7,
                            "url": "http://localhost:5011/api/media/comment_attachments/bdflag_DgwRRhn.jpg"
                        }
                    ]
                },
                "created_at": "2026-01-07T13:08:10.818985+06:00"
            },
            {
                "id": 5,
                "event_type": "comment_created",
                "payload": {
                    "text": "example text",
                    "user_id": 1,
                    "attachments": [
                        {
                            "id": 6,
                            "url": "http://localhost:5011/api/media/comment_attachments/bdflag_VnJEINj.jpg"
                        }
                    ]
                },
                "created_at": "2026-01-07T13:07:20.356919+06:00"
            },
            {
                "id": 4,
                "event_type": "comment_created",
                "payload": {
                    "text": "example text",
                    "user_id": 1,
                    "attachments": [
                        {
                            "id": 5,
                            "url": "http://localhost:5011/api/media/comment_attachments/bdflag_oFl3Ujv.jpg"
                        }
                    ]
                },
                "created_at": "2026-01-07T13:07:02.190854+06:00"
            },
            {
                "id": 3,
                "event_type": "comment_created",
                "payload": {
                    "text": "example text",
                    "user_id": 1,
                    "attachments": [
                        {
                            "id": 4,
                            "url": "http://localhost:5011/api/media/comment_attachments/bdflag_4C2RFn8.jpg"
                        }
                    ]
                },
                "created_at": "2026-01-07T13:06:25.884009+06:00"
            },
            {
                "id": 2,
                "event_type": "comment_created",
                "payload": {
                    "text": "example text",
                    "user_id": 1,
                    "attachments": [
                        {
                            "id": 3,
                            "url": "http://localhost:5011/api/media/comment_attachments/bdflag_jQvHPDK.jpg"
                        }
                    ]
                },
                "created_at": "2026-01-07T13:05:25.087679+06:00"
            }
        ]
    }
}
```

### ticket events pagination

**Request:** `GET` `{{url}}/api/ticket-event-stream/TCK-00001?last_event_id=1&limit=2`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Ticket Event Stream Successfully Fetched",
    "data": {
        "next": 2,
        "previous": null,
        "current_page": 1,
        "total_object": 5,
        "total_page": 3,
        "result": [
            {
                "id": 6,
                "event_type": "comment_created",
                "payload": {
                    "text": "example text",
                    "user_id": 1,
                    "attachments": [
                        {
                            "id": 7,
                            "url": "http://localhost:5011/api/media/comment_attachments/bdflag_DgwRRhn.jpg"
                        }
                    ]
                },
                "created_at": "2026-01-07T13:08:10.818985+06:00"
            },
            {
                "id": 5,
                "event_type": "comment_created",
                "payload": {
                    "text": "example text",
                    "user_id": 1,
                    "attachments": [
                        {
                            "id": 6,
                            "url": "http://localhost:5011/api/media/comment_attachments/bdflag_VnJEINj.jpg"
                        }
                    ]
                },
                "created_at": "2026-01-07T13:07:20.356919+06:00"
            }
        ]
    }
}
```

### all ticket events

**Request:** `GET` `{{url}}/api/ticket-event-stream/TCK-00001`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Ticket Event Stream Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 6,
                "event_type": "comment_created",
                "payload": {
                    "text": "example text",
                    "user_id": 1,
                    "attachments": [
                        {
                            "id": 7,
                            "url": "http://localhost:5011/api/media/comment_attachments/bdflag_DgwRRhn.jpg"
                        }
                    ]
                },
                "created_at": "2026-01-07T13:08:10.818985+06:00"
            },
            {
                "id": 5,
                "event_type": "comment_created",
                "payload": {
                    "text": "example text",
                    "user_id": 1,
                    "attachments": [
                        {
                            "id": 6,
                            "url": "http://localhost:5011/api/media/comment_attachments/bdflag_VnJEINj.jpg"
                        }
                    ]
                },
                "created_at": "2026-01-07T13:07:20.356919+06:00"
            },
            {
                "id": 4,
                "event_type": "comment_created",
                "payload": {
                    "text": "example text",
                    "user_id": 1,
                    "attachments": [
                        {
                            "id": 5,
                            "url": "http://localhost:5011/api/media/comment_attachments/bdflag_oFl3Ujv.jpg"
                        }
                    ]
                },
                "created_at": "2026-01-07T13:07:02.190854+06:00"
            },
            {
                "id": 3,
                "event_type": "comment_created",
                "payload": {
                    "text": "example text",
                    "user_id": 1,
                    "attachments": [
                        {
                            "id": 4,
                            "url": "http://localhost:5011/api/media/comment_attachments/bdflag_4C2RFn8.jpg"
                        }
                    ]
                },
                "created_at": "2026-01-07T13:06:25.884009+06:00"
            },
            {
                "id": 2,
                "event_type": "comment_created",
                "payload": {
                    "text": "example text",
                    "user_id": 1,
                    "attachments": [
                        {
                            "id": 3,
                            "url": "http://localhost:5011/api/media/comment_attachments/bdflag_jQvHPDK.jpg"
                        }
                    ]
                },
                "created_at": "2026-01-07T13:05:25.087679+06:00"
            },
            {
                "id": 1,
                "event_type": "comment_created",
                "payload": {
                    "text": "example text",
                    "user_id": 1,
                    "attachments": [
                        {
                            "id": 2,
                            "url": "http://localhost:5011/api/media/comment_attachments/bdflag_7zOYFOb.jpg"
                        }
                    ]
                },
                "created_at": "2026-01-07T13:04:31.492629+06:00"
            }
        ]
    }
}
```
