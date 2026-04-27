def validate_answer(answer: str) -> tuple[bool, list[str]]:
    errors = []

    if not answer.strip():
        errors.append("empty_answer")

    if len(answer.strip()) < 20:
        errors.append("too_short")

    if "I don't know" in answer and len(answer.strip()) < 80:
        errors.append("weak_answer")

    return len(errors) == 0, errors
