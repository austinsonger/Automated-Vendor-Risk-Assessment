import re

def extract_links(text: str) -> list:
    return re.findall(r'https?://\S+', text)

def format_response(raw_text: str) -> str:
    if not raw_text:
        return "⚠️ No output received from the AI model."

    cleaned = raw_text.strip()
    links = extract_links(cleaned)

    if links:
        link_section = "\n\n---\n🔗 **Quick Access Links**\n" + "\n".join(f"- {link}" for link in links)
        cleaned += link_section

    MAX_LENGTH = 15000
    return cleaned[:MAX_LENGTH] + ("\n\n⚠️ Output truncated." if len(cleaned) > MAX_LENGTH else "")
