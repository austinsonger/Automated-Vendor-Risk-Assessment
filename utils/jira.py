import os
import requests

JIRA_API_TOKEN = os.environ["JIRA_API_TOKEN"]
JIRA_SITE = os.environ["JIRA_SITE"]

def post_comment(issue_key: str, comment_text: str):
    """
    Posts a comment to a Jira issue using the Atlassian Cloud REST API (ADF format).
    """
    url = f"{JIRA_SITE}/rest/api/3/issue/{issue_key}/comment"
    headers = {
        "Authorization": f"Bearer {JIRA_API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "body": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": comment_text}]
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code >= 300:
        raise Exception(f"Jira API Error: {response.status_code} - {response.text}")

    return response.json()

