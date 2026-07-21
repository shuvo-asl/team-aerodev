# Update Invoice

**PATCH** `{{url}}/api/invoice/5/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

```json
{
    "operator": 1,
    "billing_flight": 2, 
    "currency": 1,
    "status": "approve",
    "charges": {
        "embarkation_fees":{
            "parameter_value": 50
        },
        "landing":{
            "parameter_value": 26,
            "sub_charges":{
                "off_time_landing_takeoff": true,
                "training_purpose_discount": true,
                "test_flight_discount": true,
                "security_others_international": true,
                "security_others_local": true,
                "parking_charge": true,
                "hanger_charge": true
            }
        },
        "navigation_charge":{
        },
        "boarding_bridge_charge":{
            "parameter_value": 70,
            "sub_charges":{
                "boarding_bridge_above_2hour_charge": true,
                "discount_charge_frequent_boarding_bridge": true
            }
        }
    }
}
```
