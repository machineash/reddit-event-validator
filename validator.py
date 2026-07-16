def has_attribution(event):
    # if there's a click_id, we're good → return True
    if event.get("click_id"):
        return True
    # if there's an email, we're good → return True
    if event.get("email"):        # ← you: check for email (copy the pattern above)
        return True
    # if we got here, there's NEITHER → return False
    return False                   # ← you: what do we return?

def email_looks_raw(event):
    email = event.get("email")
    if email and "@" in email:
        return True
    return False

def check_required_fields(event):
    problems = []
    if not event.get("event_name"):
        problems.append("missing event_name")
    if not event.get("conversion_id"):
        problems.append("missing conversion_id")
    return problems

def validate_event(event):
    problems = []

    # check 1: attribution
    if not has_attribution(event):
        problems.append("no attribution signal (needs click_id or email)")

    # check 2: raw email
    if email_looks_raw(event):
        problems.append("email is raw — must be hashed")

    # check 3: required fields — this ALREADY returns a list of problems
    problems = problems + check_required_fields(event)   # combine the lists

    # final verdict
    if len(problems) == 0:
        return "VALID ✅"
    else:
        return problems
