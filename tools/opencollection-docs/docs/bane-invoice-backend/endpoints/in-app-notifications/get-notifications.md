# get notifications

**GET** `{{url}}/api/in-app-notifications?is_read=false`

Retrieve a list of in-app notifications for the authenticated user.

---

#### 🔹 Query Parameters

| Parameter | Type | Description | Required | Example |
| --- | --- | --- | --- | --- |
| `is_read` | boolean | Filter notifications by read status. | No | `true` or `false` |

#### 📥 Example Requests

- **Get all notifications:  
    **`GET {{url}}/api/in-app-notifications`
    
- Get only read notifications:  
    `GET {{url}}/api/in-app-notifications?is_read=true`
    
- **Get only unread notifications:  
    **`GET {{url}}/api/in-app-notifications?is_read=false`
    

``` json
✅ Successful Response
{
  "status": "success",
  "message": "In App Notification Successfully Fetched",
  "data": {
    "result": [
      {
        "id": 8,
        "notification_type": "new_comment",
        "message": "A new comment was added in Ticket TCK-00025",
        "object_id": 25,
        "is_read": true
      }
    ]
  }
}
 ```

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `is_read` | `false` | query |

## Examples

### get read notifications

**Request:** `GET` `{{url}}/api/in-app-notifications?is_read=true`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "In App Notification Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 8,
                "notification_type": "new_comment",
                "message": "A new comment was added in Ticket TCK-00025",
                "object_id": 25,
                "is_read": true
            }
        ]
    }
}
```

### get unread notifications

**Request:** `GET` `{{url}}/api/in-app-notifications?is_read=false`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "In App Notification Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 7,
                "notification_type": "new_comment",
                "message": "A new comment was added in Ticket TCK-00025",
                "object_id": 14,
                "is_read": false
            }
        ]
    }
}
```

### get all notifications

**Request:** `GET` `{{url}}/api/in-app-notifications`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "In App Notification Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 8,
                "notification_type": "new_comment",
                "message": "A new comment was added in Ticket TCK-00025",
                "object_id": 25,
                "is_read": true
            },
            {
                "id": 7,
                "notification_type": "new_comment",
                "message": "A new comment was added in Ticket TCK-00025",
                "object_id": 14,
                "is_read": false
            }
        ]
    }
}
```
