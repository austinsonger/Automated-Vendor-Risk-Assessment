def format_response(raw_text: str) -> str:
    """
    Clean and optionally stylize the OpenAI response before posting to Jira.

    - Strips leading/trailing whitespace.
    - Ensures it's safe to insert into Jira's comment body.
    - You can extend this to add markdown formatting, truncation, etc.
    """
    if not raw_text:
        return "⚠️ No output received from the AI model."

    # Optional: Trim overly long output (Jira comment limits = ~32KB)
    MAX_LENGTH = 15000
    cleaned = raw_text.strip()

    if len(cleaned) > MAX_LENGTH:
        return cleaned[:MAX_LENGTH] + "\n\n⚠️ Output truncated due to length."

    return cleaned
