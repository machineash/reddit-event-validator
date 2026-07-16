# Reddit Conversion Event Validator

A lightweight validator that checks Reddit conversion events **before** they're
sent to the Conversions API — catching common mistakes early so partners don't
silently lose conversion data.

## Why this exists
When advertisers send malformed conversion events, they often fail silently —
the data just doesn't match, and no one notices until conversions look wrong.
This tool catches those problems up front.

## What it checks
- **Attribution** — every event needs at least one identifier (a click ID or email); otherwise Reddit can't match it.
- **PII hashing** — flags raw (unhashed) emails, which shouldn't leave a partner's servers.
- **Required fields** — ensures the event name and conversion ID are present.

It collects *all* problems in one pass, so a partner sees everything to fix at once."

## Usage
```
python validator.py
```

## Example
```python
validate_event({"event_name": "Purchase", "conversion_id": "x1", "click_id": "abc"})
# → "VALID ✅"

validate_event({"email": "ashley@gmail.com"})
# → ['email is raw — must be hashed', 'missing event_name', 'missing conversion_id']
```

## Notes
Built as a focused example of the kind of validation that makes partner
integrations with Reddit's ad platform smoother and more reliable.