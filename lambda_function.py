import json
import os
import openai
import requests
from prompt_builder import build_prompt

# Load OpenAI Key
openai.api_key = os.environ["OPENAI_API_KEY"]
JIRA_API_TOKEN = os.environ["JIRA_API_TOKEN"]
JIRA_SITE = os.environ["JIRA_SITE"]  # e.g., https://yourcompany.atlassian.net

def lambda_handler(event, context):
    try:
        # Parse incoming JSON body
        body = json.loads(event["body"])

        issue_id = body.get("issue_id")
        prompt = build_prompt(body)

        # Call OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        output = response["choices"][0]["message"]["content"]

        # Post comment to Jira
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
    r = requests.post(url, headers=headers, json=payload)
    if r.status_code >= 300:
        raise Exception(f"Jira API Error: {r.text}")
