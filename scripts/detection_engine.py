def matches_rule(event, rule):
    query = rule.get("query", {})
    identity = event.get("userIdentity", {})
    response = event.get("responseElements") or {}

    checks = {
        "event_source": event.get("eventSource"),
        "event_name": event.get("eventName"),
        "user_type": identity.get("type"),
        "response_elements": response,
    }

    return all(checks.get(key) == value for key, value in query.items())
