# charges

**GET** `{{url}}/api/charges/`

## Auth

Type: `bearer`

## Body

Type: `text`

```
{
    "email": "admin@gmail.com",
    "password": "admin@123",
    "user_type": "asl"
}
```

## Examples

### charges

**Request:** `GET` `{{url}}/api/charges/`

```json
{
    "email": "admin@gmail.com",
    "password": "admin@123",
    "user_type": "asl"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Charges Fetched Successfully",
    "data": {
        "result": [
            {
                "id": 16,
                "name": "Overfly Permit Charge",
                "parent": null,
                "charges": "195.0 $ / 1 Permit",
                "has_button": false
            },
            {
                "id": 15,
                "name": "Security & Others For Local",
                "parent": "Landing",
                "charges": "375.00 % on Landing",
                "has_button": false
            },
            {
                "id": 14,
                "name": "Security & Others For International",
                "parent": "Landing",
                "charges": "200.00 % on Landing",
                "has_button": false
            },
            {
                "id": 13,
                "name": "Discount Charge for the frequent users of Boarding Bridges",
                "parent": "Boarding Bridge Charge",
                "charges": "",
                "has_button": true
            },
            {
                "id": 12,
                "name": "Boarding Bridge Above 2 Hour Charge",
                "parent": "Boarding Bridge Charge",
                "charges": "",
                "has_button": true
            },
            {
                "id": 11,
                "name": "Boarding Bridge Charge",
                "parent": null,
                "charges": "",
                "has_button": true
            },
            {
                "id": 10,
                "name": "Navigation Charge",
                "parent": null,
                "charges": "",
                "has_button": true
            },
            {
                "id": 9,
                "name": "Hanger Charge",
                "parent": "Parking Charge",
                "charges": "50.00 % on Parking Charge",
                "has_button": false
            },
            {
                "id": 8,
                "name": "Parking Charge",
                "parent": "Landing",
                "charges": "25.00 % on Landing",
                "has_button": false
            },
            {
                "id": 5,
                "name": "Test Fly Discount",
                "parent": "Landing",
                "charges": "75.00 % discount on Landing",
                "has_button": false
            },
            {
                "id": 4,
                "name": "Training Purpose Discount",
                "parent": "Landing",
                "charges": "50.00 % discount on Landing",
                "has_button": false
            },
            {
                "id": 3,
                "name": "Landing or take off after sunset and before sunrise.",
                "parent": "Landing",
                "charges": "10.00 % surcharge on Landing",
                "has_button": false
            },
            {
                "id": 2,
                "name": "Landing",
                "parent": null,
                "charges": "",
                "has_button": true
            },
            {
                "id": 1,
                "name": "Embarkation Fees",
                "parent": null,
                "charges": "Local: 25.0 ৳ / 1 Passenger International: 25.0 ৳ / 1 Passenger",
                "has_button": false
            }
        ]
    }
}
```
