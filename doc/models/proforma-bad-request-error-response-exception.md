
# Proforma Bad Request Error Response Exception

## Structure

`ProformaBadRequestErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`ProformaError`](../../doc/models/proforma-error.md) | Optional | - |

## Example (as JSON)

```json
{
  "errors": {
    "subscription": {
      "base": [
        "base3",
        "base4"
      ]
    }
  }
}
```

