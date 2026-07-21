# delete a issue type

**DELETE** `{{url}}/api/issue-types/3/`

**Description:**  
  
Deletes the specified issue type **only if it is not already used in any ticket**.

**Behavior:**

- If the issue type is linked to one or more tickets, deletion is blocked with a validation error.
    
- On successful deletion, the response has HTTP status code `204 No Content` with a success message.
    

**Success Response:**

- **Status Code:** `204 No Content`
    
- **Body:**
    

{}

**Failure Response (In Use):**

- **Status Code:** `400 Bad Request`
    
- **Body:**
    

``` json
{
  "status": "failed",
  "message": "Issue Type Failed To Delete",
  "error": "This issue type is already used in a ticket",
  "errors": null
}
 ```

## Auth

Type: `bearer`

## Body

Type: `text`

```
{
    "name": "server error"
}
```

## Examples

### New Request

**Request:** `DELETE` `{{url}}/api/issue-types/1/`

```json
{
    "name": "server error"
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Issue Type Failed To Delete",
    "error": "This issue type is already used in a ticket",
    "errors": null
}
```

### delete a issue type

**Request:** `DELETE` `{{url}}/api/issue-types/2/`

```json
{
    "name": "server error"
}
```

**Response:** `204 No Content`
