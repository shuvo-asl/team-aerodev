# aircraft of operator

**GET** `{{url}}/api/aircraft/`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `short_code` | `ETH` | query |

## Body

Type: `text`

## Examples

### aircraft of operator

**Request:** `GET` `{{url}}/api/aircraft/?short_code=ETH`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Aircraft of operator fetched successfully",
    "data": {
        "result": [
            {
                "aircraft_type": "B737",
                "mtow": 77564,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ALM",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AVB",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B789",
                "mtow": 249475,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AXK",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AZN",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BCE",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AUA",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B737",
                "mtow": 77564,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BAK",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BAO",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AWK",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AVE",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ATG",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B789",
                "mtow": 249475,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AYC",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "Boeing 737-760",
                "mtow": 70,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ETALM",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ANO",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BAM",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BAJ",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AOS",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AVQ",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ATR",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AUC",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AVC",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AZI",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BAI",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AVK",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AVD",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AWM",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B789",
                "mtow": 249475,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AUQ",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B789",
                "mtow": 249475,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AXT",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ANR",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B789",
                "mtow": 249475,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AYD",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ARF",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AXG",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AWI",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B738 ",
                "mtow": 79015,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AQO",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AVM",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AQL",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B738 ",
                "mtow": 79015,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AQQ",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AYN",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B763",
                "mtow": 186.9,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BBE",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ARI",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ARE",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AOU",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AYM",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ATK",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AUB",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AWP",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AWJ",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AWF",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AWG",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BAL",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B738 ",
                "mtow": 79015,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AQN",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B738 ",
                "mtow": 79015,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AYL",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AVT",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AOQ",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B737",
                "mtow": 77564,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ALN",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "Boeing 737 MAX 8",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AZO",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ANN",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ATI",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ATH",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B738 ",
                "mtow": 79015,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETAYL",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AVI",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B789",
                "mtow": 249475,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AXS",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B738 ",
                "mtow": 79015,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AZA",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B738 ",
                "mtow": 79015,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BAN",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ASG",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ATQ",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BAC",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B789",
                "mtow": 249475,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AUP",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AWH",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AOP",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ANQ",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AOR",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ASH",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-APU",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ASI",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A35K",
                "mtow": 308000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BAY",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BCD",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "Boeing 737-8JM(BBJ2)",
                "mtow": 79,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BBR",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B789",
                "mtow": 249475,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AUR",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AWN",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ANP",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AWO",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B789",
                "mtow": 249475,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AXL",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "Boeing 787-8 Dreamliner",
                "mtow": 228,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ETAOS",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "Boeing 737 MAX 8",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ETAZA",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "A35K",
                "mtow": 308000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BAZ",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "Boeing 777-F60",
                "mtow": 347,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ETARI",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "Boeing 737-860",
                "mtow": 79,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ETAQQ",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AOO",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "Airbus A350-941 ",
                "mtow": 283,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AYB",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "Boeing 787-8 ",
                "mtow": 228,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AOV",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "Airbus A350",
                "mtow": 275000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BAX",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "Boeing 737 MAX 8",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AVL",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "Boeing 787-8 ",
                "mtow": 228,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AOT",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AWE",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B738 ",
                "mtow": 79015,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ASJ",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "Boeing 787-9 Dreamliner",
                "mtow": 254,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ATJ",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-AVN",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ATY",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "Boeing 787-8 Dreamliner",
                "mtow": 228,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ETAOU",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "Boeing 737-760",
                "mtow": 70,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ETALN",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "Boeing 787-8 Dreamliner",
                "mtow": 228,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BCC",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "Airbus A350-941 ",
                "mtow": 283,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ETATR",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "Boeing 777-260(LR)",
                "mtow": 347.4,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ETANQ",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "Boeing 787-9 Dreamliner",
                "mtow": 254,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ETAXK",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "Boeing 777-260(LR)",
                "mtow": 347.4,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ETANR",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETARF",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETATY",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETAVE",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B789",
                "mtow": 249475,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETAXT",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B738 ",
                "mtow": 79015,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETAQN",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B788",
                "mtow": 227930,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETAOQ",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B789",
                "mtow": 249475,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETAXS",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETAVC",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A35K",
                "mtow": 308000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BAW",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETANN",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETAUB",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETAYM",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETAWM",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B737",
                "mtow": 77564,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETBAK",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETANP",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETAVD",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETAUC",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "Airbus A350-941 ",
                "mtow": 283,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ETAZN",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "A35K",
                "mtow": 308000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ETBAW",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "A359",
                "mtow": 268000,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET AVC",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "Boeing 737 MAX 8",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": " ET-AWJ",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BAP",
                "purpose_type": "",
                "wing_type": ""
            },
            {
                "aircraft_type": "B77L",
                "mtow": 347451,
                "mtow_unit": "kg",
                "operator_shortcode": "ETH",
                "registration_number": "ET-ARJ",
                "wing_type": "Fixed Wing",
                "purpose_type": ""
            },
            {
                "aircraft_type": "B38M",
                "mtow": 82,
                "mtow_unit": "ton",
                "operator_shortcode": "ETH",
                "registration_number": "ET-BBC",
                "purpose_type": "",
                "wing_type": ""
            }
        ]
    }
}
```
