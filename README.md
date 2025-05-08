# 🤖 Automated Vendor Risk Assessment (OpenAI + Jira + AWS Lambda)

This project automates vendor risk assessments by using OpenAI Deep Research Model to analyze structured vendor data submitted through Jira Service Management. Upon receiving a webhook from Jira, it builds a custom AI prompt, runs the assessment, and posts the results back to the Jira ticket.

---

## 📦 Features

- ✅ Triggered by Jira Service Management issue submission  
- ✅ Builds structured prompts with up to 11 risk domains  
- ✅ Uses OpenAI Deep Research Model to generate security, compliance, legal, and financial risk insights  
- ✅ Posts structured results as a comment on the Jira issue  
- ✅ Deployable as an AWS Lambda function with optional AWS Secrets Manager integration  

---

## 🚀 Deployment (AWS SAM)

### 1. Install prerequisites

```bash
brew install awscli
brew install sam
pip install --upgrade pip
```

### 2. Clone the repository

```bash
git clone https://github.com/your-org/vendor-risk-analyzer.git
cd vendor-risk-analyzer
```

### 3. Build the Lambda package

```bash
sam build
```

### 4. Deploy the stack

```bash
sam deploy --guided
```

Follow the prompts and note the API Gateway URL.

---

## 🔗 Jira Setup

In **Jira Project Settings > Automation**:

- **Trigger:** Issue Created  
- **Condition:** Request Type = "Vendor Risk Assessment"  
- **Action:** Send Web Request  
  - Method: `POST`  
  - URL: `https://<api-id>.execute-api.<region>.amazonaws.com/Prod/api/vendor-risk-analyzer`  
  - Content-Type: `application/json`  
  - Body:

```json
{
  "issue_id": "{{issue.key}}",
  "vendor_name": "{{issue.fields.customfield_10000}}",
  "vendor_service_type": "{{issue.fields.customfield_10001}}",
  "data_sensitivity": "{{issue.fields.customfield_10002}}"
  // Add more fields as needed
}
```

> Replace `customfield_10000` with your actual Jira custom field IDs.

---

## 📁 Project Structure

```
vendor-risk-analyzer/
├── lambda_function.py           # AWS Lambda entry point
├── prompt_builder.py            # Builds structured GPT-4 prompt
├── format_response.py           # Optional output cleanup
├── requirements.txt             # Dependencies
├── .env.example                 # Sample environment config
├── template.yaml                # AWS SAM deployment template
├── event.json                   # Sample local test payload
├── utils/
│   ├── jira.py                  # Posts comments to Jira
│   └── secrets.py               # Secrets from env or Secrets Manager
└── tests/
    └── test_prompt_builder.py   # Unit tests
```

---

## 🧪 Local Testing

### Test your prompt locally:
```bash
python -m lambda_function
```

### Or use AWS SAM:
```bash
sam local invoke "VendorRiskAnalyzerFunction" -e event.json
```

---

## 🔐 Secrets Configuration

You can store secrets in **AWS Secrets Manager** or a `.env` file:

- `OPENAI_API_KEY`
- `JIRA_API_TOKEN`
- `JIRA_SITE`

> Example `.env` file:
```env
OPENAI_API_KEY=sk-...
JIRA_API_TOKEN=your-token
JIRA_SITE=https://yourcompany.atlassian.net
```
---


## ✅ Vendor Example





## ✅ To-Do / Future Enhancements

- [ ] Auto-classify vendors into buckets (Low / Medium / High)  
- [ ] Add contract document analysis using file attachments  
---

## 👨‍💻 Author

Created by Austin Songer
Contact: austin@songer.me
License: MIT
