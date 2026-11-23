def validate_booking(destination, departure_date, travelers):

    if not destination:
        return "Destination is required"

    if not departure_date:
        return "Departure date is required"

    if travelers <= 0:
        return "Invalid traveler count"

    return "Booking details validated"


def check_sensitive_information(user_input):

    sensitive_terms = [
        "password",
        "api_key",
        "secret"
    ]

    for term in sensitive_terms:
        if term in user_input.lower():
            return "Sensitive information detected"

    return "Input validation passed"


if __name__ == "__main__":
    result = validate_booking(
        "Chicago",
        "2026-12-15",
        2
    )

    print(result)
