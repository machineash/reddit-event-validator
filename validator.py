def has_attribution(event):
    """True if the event has at least one identifier Reddit can match on."""
    if event.get("click_id"):
        return True
    if event.get("email"):        
        return True
    return False

def email_looks_raw(event):
    """True if an email is present but not hashed (still contains '@')."""
    email = event.get("email")
    if email and "@" in email:
        return True
    return False

def check_required_fields(event):
    """Return a list of any missing required fields (event_name, conversion_id)."""
    problems = []
    if not event.get("event_name"):
        problems.append("missing event_name")
    if not event.get("conversion_id"):
        problems.append("missing conversion_id")
    return problems

def validate_event(event):
    """Run all checks and return 'VALID ✅' or a list of problems."""
    problems = []

    # check 1: attribution
    if not has_attribution(event):
        problems.append("no attribution signal (needs click_id or email)")

    # check 2: raw email
    if email_looks_raw(event):
        problems.append("email is raw — must be hashed")

    # check 3: required fields + combine lists
    problems = problems + check_required_fields(event)  

    # final verdict
    if len(problems) == 0:
        return "VALID ✅"
    else:
        return problems


if __name__ == "__main__":
    print(validate_event({"event_name": "Purchase", "conversion_id": "x1", "click_id": "abc"}))
    print(validate_event({"email": "  ashleykafoo@gmail.COM  "}))