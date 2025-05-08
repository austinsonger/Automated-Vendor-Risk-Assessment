import json
import os
import openai
import requests
from prompt_builder import build_prompt

# Load API keys from environment
openai.api_key = os.environ["OPENAI_API_KEY"]
JIRA_API_TOKEN = os.environ["JIRA_API_TOKEN"]
JIRA_SITE = os.environ["JIRA_SITE"]  # e.g., "https://yourcompany.atlassian.net"

def lambda_handler(event, context):
    try:
        # Parse JSON body from API Gateway
        body = json.loads(event["body"])
        issue_id = body.get("issue_id")

        # Build the structured AI prompt
        prompt = build_prompt(body)

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        output = response["choices"][0]["message"]["content"]

        # Post the AI-generated output as a comment to the Jira issue
        post_comment_to_jira(issue_id, output)

        return {
            "statusCode": 200,
            "body": json.dumps({"status": "posted", "issue_id": issue_id})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

def post_comment_to_jira(issue_key, comment_text):
    """Send a formatted comment to the specified Jira issue."""
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
