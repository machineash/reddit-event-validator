from validator import validate_event, has_attribution, email_looks_raw

def test_valid_event_passes():
    event = {"event_name": "Purchase", "conversion_id": "x1", "click_id": "abc"}
    assert validate_event(event) == "VALID ✅"

def test_missing_fields_are_caught():
    result = validate_event({"email": "ashley@gmail.com"})
    assert "missing event_name" in result
    assert "missing conversion_id" in result

def test_raw_email_is_flagged():
    result = validate_event({"email": "ashley@gmail.com"})
    assert "email is raw — must be hashed" in result

def test_click_id_alone_is_valid_attribution():
    assert has_attribution({"click_id": "abc"}) == True

def test_no_signal_fails_attribution():
    assert has_attribution({"value": 25}) == False