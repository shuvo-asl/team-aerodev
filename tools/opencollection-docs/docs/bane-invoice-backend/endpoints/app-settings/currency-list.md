# currency list

**GET** `{{url}}/api/currency-list/`

## Examples

### currency list

**Request:** `GET` `{{url}}/api/currency-list/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Currency Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 5,
                "prefix": "€",
                "short_key": "EUR",
                "current_rate": 0.9472,
                "default": null,
                "name": "Euro",
                "flag": "http://localhost:5011/api/media/Flag_of_Europe.svg.png",
                "is_active": false
            },
            {
                "id": 4,
                "prefix": "£",
                "short_key": "GBP",
                "current_rate": 0.7873,
                "default": null,
                "name": "Pound Sterling",
                "flag": "http://localhost:5011/api/media/Flag_of_the_United_Kingdom_1-2.svg.png",
                "is_active": false
            },
            {
                "id": 3,
                "prefix": "₹",
                "short_key": "INR",
                "current_rate": 84.6255,
                "default": null,
                "name": "Rupee",
                "flag": "http://localhost:5011/api/media/Flag_of_India.svg.png",
                "is_active": true
            },
            {
                "id": 2,
                "prefix": "৳",
                "short_key": "BDT",
                "current_rate": 119.4888,
                "default": null,
                "name": "Taka",
                "flag": "http://localhost:5011/api/media/download.jpeg",
                "is_active": true
            },
            {
                "id": 1,
                "prefix": "$",
                "short_key": "USD",
                "current_rate": 1,
                "default": true,
                "name": "Dollar",
                "flag": "http://localhost:5011/api/media/download.png",
                "is_active": true
            }
        ]
    }
}
```
