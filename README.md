# 🤖 Automated Vendor Risk Assessment 
> (OpenAI + Jira + AWS Lambda)

This project automates vendor risk assessments by using OpenAI Deep Research Model to analyze structured vendor data submitted through Jira Service Management. Upon receiving a webhook from Jira, it builds a custom AI prompt, runs the assessment, and posts the results back to the Jira ticket.


## Example Output

[Vendor Example - Google Workspace](#-vendor-example)


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
├── template.yaml                # AWS SAM deployment template
├── utils/
    ├── jira.py                  # Posts comments to Jira
    └── secrets.py               # Secrets from env or Secrets Manager
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

### Google Workspace Vendor Risk Assessment

#### 1. Vendor Profile Information

- **Vendor Name:** Google Workspace (Google Cloud / Google LLC)
- **Legal Business Name:** Google LLC (a wholly-owned subsidiary of Alphabet Inc.)
- **Website:** workspace.google.com
- **Primary Contact(s):** *Insufficient information available.* (Typically via Google sales/support channels; specific contacts to be identified through account management.)
- **Type of Service:** Cloud-based productivity and collaboration suite (SaaS), including email, storage, documents, etc.
- **Geographic Locations (Ops/Data Centers):** Global infrastructure – Google owns and operates data centers in North America, Europe, Asia-Pacific, and other regions. Customers can optionally choose to keep certain data in specific regions (e.g., U.S. or EU data residency) for compliance.
- **Length and Terms of Relationship:** *Insufficient information available.* (To be filled in with the start date and contract term if this assessment is for an existing customer relationship.)

*No risk score applicable for profile information.*





#### 2. Due Diligence and Background Checks

- **Business Credit Report Summary:** Alphabet Inc. (Google’s parent company) is financially robust with excellent credit ratings (Moody’s *Aa2* and S&P *AA+*, stable outlook). The company has **no known issues with creditworthiness**; it maintains enormous cash reserves (~$95 billion cash on hand) and low debt, reflecting very low financial default risk.

- **Litigation or Legal History:** Google/Alphabet faces ongoing regulatory and legal scrutiny due to its size and market influence. Notably, the EU has levied multibillion-euro antitrust fines (e.g., a record €4.3 billion fine related to Android in 2018), and Google is contesting or appealing some of these decisions. In the U.S., the Department of Justice and state AGs have active antitrust lawsuits regarding Google’s advertising and search business. **Importantly, none of these lawsuits directly implicate Google’s ability to deliver Google Workspace services** – they are mostly antitrust/competition matters. There have been no known court judgments threatening Google’s core cloud services. However, regulatory pressures (antitrust, privacy) are an ongoing business risk.

- **Ownership & Parent Companies:** Google Workspace is provided by Google LLC, which is a wholly-owned subsidiary of Alphabet Inc. (NASDAQ: GOOGL). Alphabet is one of the world’s largest tech companies, ensuring strong backing and stability for Google Workspace operations.

- **Watchlist / Sanctions Screening:** **No records found** of Google LLC or Alphabet being on any international sanctions or watchlists. Google is a U.S.-based entity in good standing. (Standard checks of OFAC, EU sanctions, etc., return no hits on Google/Alphabet; *next step:* maintain periodic screening, but low risk here.)

- **Media & Reputation Summary:** Google has a strong global brand and is generally seen as a leader in technology and security. Media coverage is largely positive regarding Google’s innovation and reliability, though the company does receive criticism in press for privacy issues and monopolistic practices. For instance, privacy advocates have scrutinized Google’s data collection policies, and Google+ had a high-profile data leak in 2018 (prompting its shutdown). Overall, **no significant negative events have been reported about Google Workspace’s security or service delivery**. The vendor enjoys a good reputation for enterprise service uptime and security, reinforced by its top-tier security team and transparency reports.

- **Risk Score:** **3/10 (Low-Moderate).**
 *Justification:* Google’s extremely strong financial position and stable ownership reduce business continuity risk. While ongoing legal/regulatory cases pose some reputation and regulatory risk, these have not impacted Google’s ability to serve customers. The risk of vendor failure or sanction is very low. Continued monitoring of antitrust outcomes is advised, but overall due diligence risk remains low.



#### 3. Information Security Controls

- **Data Encryption Practices:** Google Workspace encrypts all customer data at rest and in transit by default, using strong cryptographic algorithms (AES-256 or AES-128) and secure transport (TLS). This means emails, documents, and files are encrypted on Google’s servers and while moving between data centers or to the user. For additional protection, Google offers **client-side encryption** (CSE) for certain Workspace apps, letting customers control their own encryption keys for an extra layer of security. *Encryption risk is minimal* – data is protected against unauthorized access both in storage and transit.

- **Network Security (Firewalls, IDS/IPS):** Google’s infrastructure is protected by multiple layers of network security. They use custom-designed firewalls and routing controls at their data centers, and isolate the Google Workspace environment on Google’s private global network for traffic between facilities. Google has built-in **intrusion detection systems**: internal network traffic is continuously inspected for suspicious patterns (e.g., botnet traffic) and anomalies. A proprietary correlation system analyzes network and system logs to flag potential threats in real time. These measures, combined with DDoS protections and network redundancy, provide a robust defense against network-based attacks.

- **Endpoint Protection & Access Control:** Google implements strict endpoint and identity security for its own operations. All Google employees are required to use hardware security keys for 2-step verification, which has **eliminated successful phishing attacks on Google’s workforce** since its implementation. Internally, Google follows a zero-trust model (“BeyondCorp”), treating both internal and external networks as untrusted and enforcing context-aware access to resources. Role-based access control (RBAC) and least privilege principles are in place: employees have only minimal default access, and additional access to production systems or customer data requires formal approval and is logged and monitored. Multi-factor authentication is also available and recommended for Google Workspace admin and user accounts, with options like Google Authenticator and security keys. These controls greatly reduce the risk of unauthorized access.

- **Logging/Monitoring Practices:** Google has comprehensive logging and monitoring across its infrastructure. Administrator and system actions in Google Workspace are logged (and available to customers via admin audit logs). Internally, Google’s security team monitors internal systems 24/7: internal network traffic, system logs, and employee actions are analyzed for unusual behavior. Automated systems generate alerts on anomalies (e.g., an admin accessing an unusual amount of customer data), which are then investigated by security engineers. Google’s dedicated Security Operations Center and incident response teams have eyes on potential issues around the clock. These monitoring controls ensure that any suspicious activity is quickly detected and addressed.

- **Secure SDLC / DevSecOps Maturity:** Security is deeply ingrained in Google’s software development lifecycle. Google employs secure coding practices and extensive security reviews for Google Workspace code. Its **vulnerability management program** uses both automated scanning and manual penetration testing to find and fix vulnerabilities proactively. All identified issues are tracked to resolution with priority given based on severity. Google also engages with the external security research community (e.g., through bug bounty programs and Project Zero team) to catch vulnerabilities in Google Workspace and underlying open-source components. This mature DevSecOps approach – combined with regular **third-party audits** and certifications – indicates a very high level of security assurance in the product development and deployment process.

- *Risk Score:** **2/10 (Low).**
 *Justification:* Google Workspace’s security controls meet or exceed industry best practices. Strong encryption, network defenses, rigorous access controls (with universal MFA), continuous monitoring, and a robust security culture all significantly mitigate risk. The residual information security risk is low. (Notably, Google’s own use of advanced security like hardware 2FA and zero-trust networking sets a high bar for protection of customer data.) Regular independent audits (SOC 2, ISO 27001) further validate these controls.



#### 4. Data Handling and Privacy

- **Data Classification & Segregation:** Google Workspace is a multi-tenant cloud service – customer data is logically separated and access is restricted by design. Google treats all customer content as confidential by default. Internally, **very few employees can access customer data**, and those who can are subject to strict controls and monitoring. Google’s systems are engineered so that each customer’s data is isolated and only accessible with the customer’s credentials or by Google staff with explicit authorization (for support or maintenance, and even then actions are logged via Access Transparency). *Customer administrators can implement data labeling and DLP rules within Workspace to classify and protect sensitive information on their end.* Overall, the risk of cross-tenant data leakage is extremely low given Google’s architecture and auditing of data access.

- **Data Residency / Jurisdiction:** By default, Google may process and store Workspace data in any of its global data centers to ensure performance and reliability. However, Google offers **data region controls** for Workspace: administrators can choose to locate covered data (e.g., Drive, Gmail content) in the **United States or European Union** data centers to meet sovereignty requirements. Google’s Cloud infrastructure is certified under EU data protection frameworks, and Standard Contractual Clauses are in place for international data transfers. *If specific residency beyond US/EU is required, that may not be guaranteed without additional services.* For most customers, the current data region options and legal safeguards (e.g. EU SCCs) are sufficient to address jurisdictional risks. Next steps if needed: consider **Google Workspace Assured Controls** or hold your own encryption keys to further limit data movement.

- **Data Retention & Destruction Policy:** Google Workspace allows configurable data retention through admin policies (e.g., Vault for e-discovery and retention). Google’s default is to retain user-deleted content for a limited period (trash retention, etc.) and permanently delete it thereafter. **Upon contract termination**, Google’s Data Processing Addendum commits that customer data will be deleted from Google systems within a fixed time frame (typically 180 days or less for complete deletion from backups) – though some residual copies might persist briefly in backups before automated deletion. Google has detailed procedures for secure data destruction of disks when they are retired from data centers (such drives are physically destroyed or wiped). *Public documentation confirms that Google’s disk destruction and data deletion processes meet or exceed industry standards.* If needed, the customer should ensure Vault/Takeout is used to export data before termination. **Risk is low**; Google’s practices minimize lingering data, but explicit retention requirements should be addressed via configuration and contract if necessary.

- **Privacy Compliance (GDPR, CCPA, HIPAA, etc.):** Google Workspace is fully **GDPR-compliant** as a data processor. Google offers a comprehensive Cloud Data Processing Addendum (CDPA/DPA) which incorporates the EU Standard Contractual Clauses for lawful cross-border data transfer and outlines Google’s privacy commitments. Under this DPA, Google contractually commits to key GDPR requirements (processing data only per instructions, assisting with data subject requests, breach notifications within 72 hours, etc.). For **CCPA**, Google is categorized as a Service Provider and refrains from selling personal data. Google also signs **HIPAA Business Associate Agreements (BAA)** for Workspace (for eligible editions) to support HIPAA compliance for healthcare data. Additionally, Google Workspace has achieved **ISO 27701 (Privacy Information Management)** certification, indicating its privacy program is audited against international standards. *In summary, Google has strong privacy controls and contractual terms:* the risk of non-compliance is low. Next steps for full assurance: review the signed DPA/BAA and ensure all required configurations (like retention settings, consent for additional services) are in place on the customer side.

- **Use of Subcontractors / 4th Parties:** Google performs the vast majority of Google Workspace data processing with its own infrastructure and personnel. It does engage a limited number of **subprocessors** for specific support and ancillary services (for example, for global customer support, infrastructure maintenance, etc.). All Google Workspace subprocessors are subject to Google’s vendor security assessment and are bound by stringent security & privacy agreements. Google publishes a list of subprocessors for Workspace (available on their Trust Center) and provides notice to customers of any significant changes. There is **no indication of high-risk fourth parties** in the Workspace supply chain – Google’s tight control over its infrastructure limits third-party exposure. *Risk is low*, but customers should periodically review the Google Workspace subprocessor list (and Google will update the DPA if new critical subprocessors are added).

- **Risk Score:** **2/10 (Low).**
 *Justification:* Google demonstrates strong data handling practices with respect to isolation, residency options, retention, and privacy law compliance. The presence of robust data protection terms (GDPR DPA, SCCs, HIPAA BAA) and Google’s limited reliance on third-party processors mitigate most privacy risks. While data residency is global by default, Google provides mechanisms to address sovereignty concerns. Residual risk around data privacy is minimal, provided the customer also configures the product in line with their compliance needs.



#### 5. Compliance and Certifications

- **SOC Reports:** Google Workspace undergoes regular independent audits. Google publishes **SOC 2 and SOC 3** reports annually for Google Cloud/Workspace services. The **most recent SOC 2 Type II** report can be requested through Google’s compliance portal or sales team (usually under NDA). These SOC reports cover security, availability, confidentiality, and privacy controls, providing assurance that controls are suitably designed and operating effectively. *(Link: Google Cloud Compliance Reports repository – customers can access the SOC 2 report via Google’s trust center or upon request.)*

- **ISO Certifications:** Google Workspace is certified under **ISO/IEC 27001** (Information Security Management), as well as **ISO/IEC 27017** (cloud security controls) and **ISO/IEC 27018** (cloud privacy protections for PII). Google has also added **ISO/IEC 27701** certification for its privacy information management system. These certifications are audited by third-party certifying bodies yearly. *(The ISO certificates and statements of applicability are available on Google’s Compliance Resource Center – e.g., an ISO 27001 certificate covering Google Cloud Platform and Google Workspace.)*

- **FedRAMP / NIST Alignment:** Google Workspace has achieved **FedRAMP High authorization** for its services used by U.S. federal agencies. This means Google Workspace meets the stringent NIST 800-53 controls required for high-impact federal systems. Federal customers can leverage Google’s FedRAMP package (available via the FedRAMP PMO) to satisfy their compliance. Google also aligns with **NIST CSF** and **NIST 800-171** (per CMMC requirements) as part of its security program. In addition, Google participates in other government frameworks (e.g., BSI C5 in Germany, MTCS in Singapore). *This broad compliance suggests a strong control environment mapped to NIST and other standards.*

- **Other Frameworks (PCI-DSS, HIPAA, HITRUST):** While Google Workspace is not meant for processing credit card transactions, the underlying Google infrastructure has **PCI DSS compliance** for relevant services. (Google Cloud Platform is PCI DSS certified, and by inheritance some Workspace components may qualify, but *storing cardholder data in Workspace is generally not a typical use case*.) For healthcare, as mentioned, Workspace can be used in a HIPAA-regulated environment with a BAA. Google doesn’t list HITRUST certification for Workspace, but many of the controls overlap with its existing audits. Google’s compliance documentation often provides **mapping documents** to regulations like GDPR, CCPA, GLBA, etc., to help customers. Overall, no major compliance gaps are known – **Workspace meets or exceeds requirements in most industries** (education, government, finance, healthcare) when configured properly.

- **External Pen Tests / Vulnerability Scans:** Google engages independent third parties to perform penetration testing on Google Cloud and Workspace services as part of certain compliance audits (e.g., FedRAMP requires regular 3PAO pen tests). The results are not publicly shared in detail, but customers under NDA can request a summary of penetration test reports. Additionally, Google’s Vulnerability Reward Program (bug bounty) invites security researchers worldwide to test Workspace for vulnerabilities, adding another layer of external scrutiny. There have been **no known significant unresolved vulnerabilities** reported publicly for Google Workspace in recent years. The combination of internal and external testing means any serious issue is likely to be caught and remediated quickly.

- **Risk Score:** **1/10 (Very Low).**
 *Justification:* Google Workspace maintains an extensive set of up-to-date compliance certifications and third-party attestations. These certifications (SOC 2, ISO 27001 series, FedRAMP High, etc.) have been independently validated, greatly reducing compliance risk. Customers in regulated industries can rely on these reports to satisfy oversight requirements. The risk of Google lacking a needed certification is very low — they are continuously expanding compliance coverage. (Remaining tasks are mostly on the customer side to ensure they leverage Google’s compliance capabilities properly.) 





#### 6. Incident Management

- **Breach History:** **No major data breaches of Google Workspace** have been publicly reported to date. Google has a strong track record of security; notably, since moving to security key MFA, they’ve had zero known incidents of employee account compromise. One historical incident outside of Workspace was the Google+ API data exposure in 2018 (affecting Google+ social network profiles), but that did not impact Google Workspace services or customer enterprise data. Google is very transparent via its Security Incident Impact Reports and would notify customers of any breach involving their data. To date, **Workspace’s breach history is clean**, indicating a low likelihood of undetected security failures. (Any minor incidents have been quickly contained with no noteworthy customer impact reported publicly.)

- **Incident Response Plan Status:** Google has a rigorous, formal **incident response plan** for security and privacy incidents affecting customer data. Dedicated incident response teams (part of Google’s global Security team) are in place. In the event of an incident, Google’s process includes defined steps for triage, investigation, containment, and recovery. Specialized roles (incident commander, forensics, legal, communications, etc.) are assigned to handle various aspects. Google’s incident playbooks cover scenarios from system outages to data breaches. This plan is regularly tested and refined through drills and post-mortems. *As a customer, you can have confidence that Google is prepared to respond swiftly to any Workspace security incidents.*

- **Detection/Containment Metrics:** Specific metrics (like mean time to detect/respond) are not publicly disclosed by Google. However, given their capabilities (24/7 monitoring, automated detection systems, and a large security team), one can infer very short detection times – potentially **minutes to hours** for critical incidents. Google has stated that it actively monitors and often catches issues before they impact customers. Containment and remediation also benefit from Google’s automation (e.g., isolating affected systems) and enormous engineering resources. For example, Google’s rapid response to zero-day vulnerabilities (such as patching server or browser issues across its fleet) is well-regarded in the industry. *Overall, Google’s incident detection/response speed is among the best in class.* (For more concrete metrics, a security questionnaire response from Google might be needed – next step: request Google’s SIG or CAIQ response which might include more details on IR timing.)

- **Notification & Escalation Protocols:** Per Google’s Customer Agreements and the Cloud DPA, Google **commits to notify customers without undue delay** (and within 72 hours as required under GDPR) if any security breach occurs that affects customer data. They have support personnel dedicated to customer communications during incidents. In practice, if a significant Workspace incident happens (e.g., a widespread outage or data issue), Google posts public status updates on the Workspace Status Dashboard and sends notifications to admins. For any data breach, Google would use established channels (likely email to registered security contacts or admin console alerts) to inform customers, provide remediation guidance, and follow up with a post-incident report. Escalation internally at Google is very fast – incidents are treated with the highest priority, involving senior leadership when needed. *There is low risk of Google failing to notify; the protocols are clearly defined.* One area to verify: ensure your organization’s contact information is up-to-date in the Google Admin Console for emergency communications.

- **Risk Score:** **2/10 (Low).**
 *Justification:* Google’s incident management maturity – reflected by a lack of serious breaches, a dedicated global IR team, and clear notification commitments – means the likelihood and impact of an unmanaged incident are low. They have demonstrated the ability to contain and resolve issues quickly. The score is not 1 only because no system is immune to incidents; however, Google’s capabilities drastically limit potential damage. The residual risk mainly lies in extremely sophisticated attacks or unforeseen vulnerabilities, but even then Google’s responsiveness would mitigate impact on customers.



#### 7. Business Continuity & Disaster Recovery

- **BCP/DRP Documentation:** Google has robust **Business Continuity and Disaster Recovery plans** for Google Workspace, though the detailed documentation is internal. The architecture of Workspace itself provides inherent disaster tolerance – data is redundantly stored across multiple data centers and Google can shift workloads as needed. Google’s continuity planning is regularly tested; they design for failure at the component, server, and data center levels. While proprietary, Google’s BC/DR plans have been examined as part of compliance audits (e.g., ISO 27001, SOC 2) and found to be comprehensive. *Next steps:* If required for audit, a summary of Google’s BCP/DR approach for Workspace can be requested via their compliance team. It likely covers emergency response, recovery procedures, and organizational resilience (Google has geographically dispersed operations centers to manage continuity).

- **RTO & RPO:** Google does not publicly publish specific RTO/RPO values for Google Workspace, but given their redundancy, the **Recovery Time Objective is near zero** for most single-component failures (services fail over automatically). In scenarios of major outage, Google’s goal is to restore service in minutes, not hours – evidenced by the rare downtime incidents which are usually resolved quickly. The **Recovery Point Objective** (data loss tolerance) is effectively **zero or near-zero** for in-region failures because data is synchronously replicated. Even in catastrophic regional failures, Google Workspace is architected to switch to backup systems with minimal data loss (possibly a few seconds of recent data might be in transit). In practice, Gmail and Drive have extremely high durability (11 nines for Google Cloud Storage). *Overall, RTO/RPO are very aggressive (low), meaning customers are unlikely to lose data or experience prolonged downtime.* Google’s SLA of 99.9% uptime supports that outages per month should be less than ~43 minutes.

- **DR/BCP Testing Frequency:** Google conducts continuous testing of its infrastructure resilience. This includes drills like data center failovers, chaos engineering experiments, and simulating large-scale outages to ensure systems respond as expected. They haven’t disclosed a specific interval (e.g., quarterly or annually) for full BCP drills, but given their engineering culture, **automated failover is tested regularly**. Google’s services also have frequent **disaster simulations** – for example, they might intentionally take a data center offline to verify traffic routes to another. Additionally, Google’s incident post-mortems feed into BCP improvements. *This continual testing regime reduces the risk of any unforeseen failure during a real disaster.*

- **Geo-Redundancy Capabilities:** Google Workspace data is geographically distributed. For instance, an email in Gmail is stored in multiple data centers in different locations by default for redundancy. If one site goes down (due to natural disaster or other issue), user data is still accessible from another site. Google’s network can automatically re-route user connections to the nearest active region. All core Workspace services (Gmail, Drive, etc.) are built on active-active replication across data centers. Furthermore, Google takes backups on separate media, and even these backups are encrypted and protected. The system is also highly scalable to handle failover load. **Geo-redundancy is a key strength for Google** – it significantly lowers the risk of data loss or prolonged outage due to any single-location event.

- **Risk Score:** **1/10 (Very Low).**
 *Justification:* Google’s BC/DR posture for Workspace is extremely strong. The company’s massive, distributed infrastructure and proven redundancy mean that even in the event of disasters, operations can continue with minimal disruption. Past performance (Workspace historically has had few global outages and no significant data losses) backs this up. The risk of extended downtime or irrecoverable data loss is negligible. (The only caveat is dependent on an internet connection – as with any cloud service, customer-side continuity plans should ensure internet access and backup mail solutions if needed for extreme cases.)



#### 8. Human Resources and Training

- **Background Checks on Employees:** Google has strict hiring standards and performs thorough **employee background checks** for personnel in sensitive positions. Before hiring, Google verifies education, previous employment, and references, and for roles with access to customer data or facilities, they also conduct identity and criminal checks as allowed by law. These checks help ensure that those with potential access to systems are vetted for trustworthiness. The company’s global workforce screening lowers the insider risk from the outset.

- **Security Awareness Training:** **All Google employees receive security and privacy training** from day one and repeatedly during their tenure. New hires must complete security orientation and sign the Code of Conduct (emphasizing data protection). Ongoing, Google runs regular security refresher courses, phishing tests, and a security newsletter to keep staff aware of emerging threats. Engineers get additional secure coding training and are kept up-to-date on best practices. There are also internal campaigns like “Privacy Week” to reinforce the culture of security. This pervasive training regimen greatly reduces the likelihood of human error leading to security incidents.

- **Insider Threat Mitigation Strategies:** Google employs multiple controls to mitigate insider threats (malicious or accidental). These include the least-privilege access model – employees are given access only to what they need, and access is tightly monitored. High-risk actions (like accessing customer accounts or data) require justification and are logged via Access Transparency for customer visibility. Google also has internal monitoring to detect unusual employee activity on systems. For example, if an employee tried to download large amounts of customer data, it would trigger alerts. The dedicated security team does behavioral analytics to spot insider anomalies. Additionally, Google fosters a culture where employees are encouraged to report suspicious activities or potential security issues (with anonymity options). Overall, these measures, along with background checks and training, create a strong defense against insider risks.

- **Role-Based Access Control (RBAC):** Google’s internal systems and the administration of Google Workspace use robust RBAC. Access to production environments and customer data is limited to a small group of authorized engineers. Google uses an automated system to grant and revoke access rights based on role changes or termination – when an employee leaves or changes role, access is promptly removed. Administrative access requires approvals and is logged, and privileges are segregated (for instance, support engineers might be able to see metadata but not content unless escalated). On the customer side, Google Workspace allows administrators to implement RBAC for their IT admins (with predefined admin roles and the ability to create custom roles with least privilege). *The enforcement of RBAC internally ensures no single employee can unilaterally access or compromise the system without oversight.* Google’s zero-trust approach also means that even within the network, services authenticate and authorize each call, further implementing RBAC at a service-to-service level.

- **Risk Score:** **2/10 (Low).**
 *Justification:* Google’s HR and security training practices significantly lower personnel-related risks. With comprehensive background checks, continuous training, and strong internal controls on access, the likelihood of an insider-caused incident or negligence is very low. The only residual risk comes from the human factor that no program can 100% eliminate (e.g., a highly sophisticated social engineering of an employee or a rogue insider at the highest privilege). However, given Google’s multiple overlapping controls (technical and cultural), the insider threat risk is well-managed.



#### 9. Financial Risk and Stability

- **Balance Sheet / Income Statement Insights:** Alphabet Inc. (Google’s parent) is one of the financially strongest companies in the world. In 2024, Alphabet reported **annual revenues of $350 billion** with a net income of over **$100 billion**. The company has a huge asset base and minimal long-term debt (debt-to-equity is only ~8%). Alphabet maintains a cash reserve around **$95 billion** as of the most recent reports, providing ample liquidity. These figures show that Google can easily invest in and support Google Workspace operations; **financial failure or sudden bankruptcy risk is essentially zero** for a company of this scale and profitability.

- **Profitability & Cash Flow:** Google’s core businesses (including Google Workspace within Google Cloud segment) are profitable. Google Cloud (which includes Workspace) is growing rapidly; while historically Google Cloud segment operated at a loss, it turned profitable in 2023. Alphabet overall is a cash flow machine, generating over $70 billion in free cash flow in 2024. Such strong cash flow means Google can cover operational costs, R&D, and any unforeseen expenses (like legal fines or incident costs) without impacting service delivery. The profit margins are high and trends are stable or improving. There’s no indication of financial stress. *This financial stability means continuity of the service and future investment in improvements are assured.*

- **Insurance Coverage (Cyber, Liability):** Google/Alphabet carries extensive insurance, though exact policies are confidential. It is common for a company of Alphabet’s size to have cyber liability insurance, errors & omissions coverage, and general liability insurance in place with high coverage limits (often in the hundreds of millions). In addition, Alphabet’s balance sheet effectively self-insures many risks (they could absorb the cost of an incident). *Due to insufficient public info, we cannot quantify their insurance, but it’s reasonable to assume robust coverage.* Next steps if needed: Google may provide a certificate of insurance under NDA if required by a customer contract. However, **practical risk of financial loss to customers from Google’s insolvency is nil**. The insurance aspect mainly ensures Google can respond to legal liabilities or claims; given their financial muscle, this is a minor concern.

- **Risk Score:** **1/10 (Very Low).**
 *Justification:* Alphabet’s financial strength virtually eliminates traditional vendor financial risks (like bankruptcy, going concern issues, or inability to invest in security). The company’s revenues and cash buffers are massive, and it has top-tier credit ratings indicating confidence in its stability. There is no significant risk that Google will be unable to fulfill its obligations due to financial problems. (Even large fines or market downturns have historically barely dented their operations.) Thus, financial risk to the customer is negligible.



#### 10. Legal and Contractual Risk

- **MSA / DPA Review Notes:** Google’s standard **Master Services Agreement (MSA)** and Data Processing Addendum (DPA, now called the Cloud Data Processing Addendum - CDPA) for Google Workspace are publicly available and have been vetted by thousands of organizations. Key points: The DPA meets GDPR requirements, including Google’s role as a Processor and Model Contractual Clauses for data transfers. Google also contractually commits to security measures in the DPA (Annex with technical and organizational measures) and breach notification obligations. The **MSA** (Terms of Service) covers liability limits, use of service, customer data ownership (customer retains all rights to their data), and acceptable use. No unusual clauses have been noted – they are fairly standard for a cloud provider. One item: Google’s terms include that they do not use Workspace customer data for advertising purposes or sell it, which is explicitly stated and important for privacy. *If this assessment is internal, ensure Legal has reviewed the MSA/DPA versions signed; no red flags from a public review standpoint.*

- **Termination / Liability Clauses:** Google’s liability clause in the Workspace agreement typically caps liability to the amount paid by the customer in the last 12 months (and often excludes indirect/consequential damages). This is a **standard limitation of liability** for SaaS providers. It means if Google fails in some way, their financial responsibility is limited. While this is common, it does present residual risk: in a hypothetical severe incident causing large losses, Google’s contractual payout is capped. The termination provisions usually allow either party to terminate for cause (e.g., material breach) and allow the customer to retrieve data (data export) upon termination. There’s also usually a clause that if services are terminated, Google will delete customer data per the DPA. No lock-in penalties beyond possibly remaining contract fees. *The contractual risk here is moderate only because of the typical liability cap.* To mitigate, some customers negotiate higher caps for data breach events – it’s worth evaluating if that’s needed for your risk appetite.

- **SLA Terms:** Google Workspace provides a Service Level Agreement guaranteeing **99.9% uptime** for core services. If availability falls below this, customers can claim service credits (scaled by downtime, up to 50% of monthly fee for severe outages). The SLA excludes outages caused by factors outside Google’s control or scheduled maintenance (which is minimal, Google rarely has downtime windows). Historically, Google has met or exceeded its SLA most of the time – Google publishes uptime reports (Workspace had ~99.98% uptime in past years). The SLA is in line with industry norms. *Risk:* Low – the SLA provides some recourse for downtime, though credits may not cover the full business impact of an outage. Ensure you understand the credit claiming process (must file within 30 days of incident). No SLA for performance aside from uptime, but performance issues are rare given Google’s infrastructure.

- **Audit Rights:** Under Google’s standard contract and DPA, **customers have limited audit rights**. Google generally does not permit on-site audits by each customer due to security and scalability, but the DPA Section 7.5 provides that customers can either review Google’s audit reports (SOC/ISO certifications) or commission an independent audit in certain circumstances. If a customer requires it (and regulatory requirements demand it), Google will allow an audit by an accredited third-party auditor on the customer’s behalf, subject to conditions (e.g., auditor can’t be a Google competitor, and reasonable advance notice). Google may charge for such audits. In practice, almost all customers rely on the provided **third-party attestations** instead of conducting their own audit. This approach is common in cloud contracts, but it means direct audit rights are somewhat restricted. *Risk:* For most, low – because the available documentation is comprehensive. However, if your organization requires direct audits, this could be a negotiation point.

- **Risk Score:** **4/10 (Moderate).**
 *Justification:* Legally, Google’s contracts are standard and fair for a large provider, but from the customer perspective, the **limitations of liability and limited direct auditability introduce some risk**. The moderate score reflects that in a worst-case scenario (e.g., a major data breach), the customer’s ability to recover losses from Google is contractually limited. That said, Google’s strong performance and compliance reduce the likelihood of ever needing to invoke these clauses. The recommendation is to accept Google’s standard terms for most points (since they are an industry norm), while ensuring internal strategies (insurance, backups, etc.) account for the residual contractual limitations. No showstoppers in the contract were identified.



#### 11. Risk Scoring and Tiering

- **Inherent Risk Score:** **9/10 (High)**
   *Justification:* Google Workspace has access to a wide range of the organization’s data (email, documents, calendars) and is deeply integrated into daily operations. Inherently, a failure or breach of this vendor could have **critical impact** on confidentiality and availability of our information. The broad scope and criticality of the service make the raw risk high before considering controls (particularly in areas of data sensitivity and business dependence).
- **Residual Risk Score:** **2/10 (Low)**
   *Justification:* After evaluating Google’s strong controls, compliance posture, and reliability, the risk remaining is very low. Google’s security measures, resilience, and financial stability dramatically mitigate the inherent risks. For example, encryption and access controls protect data, and geo-redundancy protects availability. The gap between inherent and residual risk is large, showing Google’s controls are highly effective. The **2/10** residual rating indicates only a minimal likelihood of a significant adverse event affecting us via Google Workspace (though not zero – e.g., a black swan event could still occur).
- **Tier Recommendation:** **Critical (Tier 1)** vendor
   *Justification:* Google Workspace should be classified as a **Critical** supplier given its importance. This service underpins email communication, document storage, and collaboration for the organization – an outage or compromise would be immediately felt enterprise-wide. The vendor handles **sensitive data** and a high volume of business processes. Tiering it as Critical ensures the highest level of ongoing oversight (e.g. annual risk reviews, executive visibility). Despite the low residual risk, the impact of a worst-case scenario warrants a top-tier classification.
- **Overall Justification Summary:** In summary, **Google Workspace is a high-inherent-risk vendor that is managed to a low residual risk through excellent controls and assurances**. Google’s dominance in technology, massive investment in security, and plethora of compliance certifications give confidence in the service. We should maintain this vendor as a strategic partner, with periodic due diligence refresh (especially watching for any regulatory changes or reported incidents). The recommendation is to continue usage with standard monitoring. Areas with “Insufficient information” (like specific contacts or insurance details) can be addressed by engaging Google directly if needed. No immediate remediation actions are required from a vendor risk standpoint, other than ensuring our own configurations and contingency plans are in place in alignment with this assessment.



## ✅ To-Do / Future Enhancements

- [ ] Auto-classify vendors into buckets (Low / Medium / High)  
- [ ] Add contract document analysis using file attachments  
---

## 👨‍💻 Author

Created by Austin Songer
Contact: austin@songer.me
License: MIT


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
├── utils/
    ├── jira.py                  # Posts comments to Jira
    └── secrets.py               # Secrets from env or Secrets Manager
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

### Google Workspace Vendor Risk Assessment

#### 1. Vendor Profile Information

- **Vendor Name:** Google Workspace (Google Cloud / Google LLC)
- **Legal Business Name:** Google LLC (a wholly-owned subsidiary of Alphabet Inc.)
- **Website:** workspace.google.com
- **Primary Contact(s):** *Insufficient information available.* (Typically via Google sales/support channels; specific contacts to be identified through account management.)
- **Type of Service:** Cloud-based productivity and collaboration suite (SaaS), including email, storage, documents, etc.
- **Geographic Locations (Ops/Data Centers):** Global infrastructure – Google owns and operates data centers in North America, Europe, Asia-Pacific, and other regions. Customers can optionally choose to keep certain data in specific regions (e.g., U.S. or EU data residency) for compliance.
- **Length and Terms of Relationship:** *Insufficient information available.* (To be filled in with the start date and contract term if this assessment is for an existing customer relationship.)

*No risk score applicable for profile information.*





#### 2. Due Diligence and Background Checks

**Business Credit Report Summary:** Alphabet Inc. (Google’s parent company) is financially robust with excellent credit ratings (Moody’s *Aa2* and S&P *AA+*, stable outlook). The company has **no known issues with creditworthiness**; it maintains enormous cash reserves (~$95 billion cash on hand) and low debt, reflecting very low financial default risk.

**Litigation or Legal History:** Google/Alphabet faces ongoing regulatory and legal scrutiny due to its size and market influence. Notably, the EU has levied multibillion-euro antitrust fines (e.g., a record €4.3 billion fine related to Android in 2018), and Google is contesting or appealing some of these decisions. In the U.S., the Department of Justice and state AGs have active antitrust lawsuits regarding Google’s advertising and search business. **Importantly, none of these lawsuits directly implicate Google’s ability to deliver Google Workspace services** – they are mostly antitrust/competition matters. There have been no known court judgments threatening Google’s core cloud services. However, regulatory pressures (antitrust, privacy) are an ongoing business risk.

**Ownership & Parent Companies:** Google Workspace is provided by Google LLC, which is a wholly-owned subsidiary of Alphabet Inc. (NASDAQ: GOOGL). Alphabet is one of the world’s largest tech companies, ensuring strong backing and stability for Google Workspace operations.

**Watchlist / Sanctions Screening:** **No records found** of Google LLC or Alphabet being on any international sanctions or watchlists. Google is a U.S.-based entity in good standing. (Standard checks of OFAC, EU sanctions, etc., return no hits on Google/Alphabet; *next step:* maintain periodic screening, but low risk here.)

**Media & Reputation Summary:** Google has a strong global brand and is generally seen as a leader in technology and security. Media coverage is largely positive regarding Google’s innovation and reliability, though the company does receive criticism in press for privacy issues and monopolistic practices. For instance, privacy advocates have scrutinized Google’s data collection policies, and Google+ had a high-profile data leak in 2018 (prompting its shutdown). Overall, **no significant negative events have been reported about Google Workspace’s security or service delivery**. The vendor enjoys a good reputation for enterprise service uptime and security, reinforced by its top-tier security team and transparency reports.

**Risk Score:** **3/10 (Low-Moderate).**
 *Justification:* Google’s extremely strong financial position and stable ownership reduce business continuity risk. While ongoing legal/regulatory cases pose some reputation and regulatory risk, these have not impacted Google’s ability to serve customers. The risk of vendor failure or sanction is very low. Continued monitoring of antitrust outcomes is advised, but overall due diligence risk remains low.



#### 3. Information Security Controls

**Data Encryption Practices:** Google Workspace encrypts all customer data at rest and in transit by default, using strong cryptographic algorithms (AES-256 or AES-128) and secure transport (TLS). This means emails, documents, and files are encrypted on Google’s servers and while moving between data centers or to the user. For additional protection, Google offers **client-side encryption** (CSE) for certain Workspace apps, letting customers control their own encryption keys for an extra layer of security. *Encryption risk is minimal* – data is protected against unauthorized access both in storage and transit.

**Network Security (Firewalls, IDS/IPS):** Google’s infrastructure is protected by multiple layers of network security. They use custom-designed firewalls and routing controls at their data centers, and isolate the Google Workspace environment on Google’s private global network for traffic between facilities. Google has built-in **intrusion detection systems**: internal network traffic is continuously inspected for suspicious patterns (e.g., botnet traffic) and anomalies. A proprietary correlation system analyzes network and system logs to flag potential threats in real time. These measures, combined with DDoS protections and network redundancy, provide a robust defense against network-based attacks.

**Endpoint Protection & Access Control:** Google implements strict endpoint and identity security for its own operations. All Google employees are required to use hardware security keys for 2-step verification, which has **eliminated successful phishing attacks on Google’s workforce** since its implementation. Internally, Google follows a zero-trust model (“BeyondCorp”), treating both internal and external networks as untrusted and enforcing context-aware access to resources. Role-based access control (RBAC) and least privilege principles are in place: employees have only minimal default access, and additional access to production systems or customer data requires formal approval and is logged and monitored. Multi-factor authentication is also available and recommended for Google Workspace admin and user accounts, with options like Google Authenticator and security keys. These controls greatly reduce the risk of unauthorized access.

**Logging/Monitoring Practices:** Google has comprehensive logging and monitoring across its infrastructure. Administrator and system actions in Google Workspace are logged (and available to customers via admin audit logs). Internally, Google’s security team monitors internal systems 24/7: internal network traffic, system logs, and employee actions are analyzed for unusual behavior. Automated systems generate alerts on anomalies (e.g., an admin accessing an unusual amount of customer data), which are then investigated by security engineers. Google’s dedicated Security Operations Center and incident response teams have eyes on potential issues around the clock. These monitoring controls ensure that any suspicious activity is quickly detected and addressed.

**Secure SDLC / DevSecOps Maturity:** Security is deeply ingrained in Google’s software development lifecycle. Google employs secure coding practices and extensive security reviews for Google Workspace code. Its **vulnerability management program** uses both automated scanning and manual penetration testing to find and fix vulnerabilities proactively. All identified issues are tracked to resolution with priority given based on severity. Google also engages with the external security research community (e.g., through bug bounty programs and Project Zero team) to catch vulnerabilities in Google Workspace and underlying open-source components. This mature DevSecOps approach – combined with regular **third-party audits** and certifications – indicates a very high level of security assurance in the product development and deployment process.

**Risk Score:** **2/10 (Low).**
 *Justification:* Google Workspace’s security controls meet or exceed industry best practices. Strong encryption, network defenses, rigorous access controls (with universal MFA), continuous monitoring, and a robust security culture all significantly mitigate risk. The residual information security risk is low. (Notably, Google’s own use of advanced security like hardware 2FA and zero-trust networking sets a high bar for protection of customer data.) Regular independent audits (SOC 2, ISO 27001) further validate these controls.



#### 4. Data Handling and Privacy

**Data Classification & Segregation:** Google Workspace is a multi-tenant cloud service – customer data is logically separated and access is restricted by design. Google treats all customer content as confidential by default. Internally, **very few employees can access customer data**, and those who can are subject to strict controls and monitoring. Google’s systems are engineered so that each customer’s data is isolated and only accessible with the customer’s credentials or by Google staff with explicit authorization (for support or maintenance, and even then actions are logged via Access Transparency). *Customer administrators can implement data labeling and DLP rules within Workspace to classify and protect sensitive information on their end.* Overall, the risk of cross-tenant data leakage is extremely low given Google’s architecture and auditing of data access.

**Data Residency / Jurisdiction:** By default, Google may process and store Workspace data in any of its global data centers to ensure performance and reliability. However, Google offers **data region controls** for Workspace: administrators can choose to locate covered data (e.g., Drive, Gmail content) in the **United States or European Union** data centers to meet sovereignty requirements. Google’s Cloud infrastructure is certified under EU data protection frameworks, and Standard Contractual Clauses are in place for international data transfers. *If specific residency beyond US/EU is required, that may not be guaranteed without additional services.* For most customers, the current data region options and legal safeguards (e.g. EU SCCs) are sufficient to address jurisdictional risks. Next steps if needed: consider **Google Workspace Assured Controls** or hold your own encryption keys to further limit data movement.

**Data Retention & Destruction Policy:** Google Workspace allows configurable data retention through admin policies (e.g., Vault for e-discovery and retention). Google’s default is to retain user-deleted content for a limited period (trash retention, etc.) and permanently delete it thereafter. **Upon contract termination**, Google’s Data Processing Addendum commits that customer data will be deleted from Google systems within a fixed time frame (typically 180 days or less for complete deletion from backups) – though some residual copies might persist briefly in backups before automated deletion. Google has detailed procedures for secure data destruction of disks when they are retired from data centers (such drives are physically destroyed or wiped). *Public documentation confirms that Google’s disk destruction and data deletion processes meet or exceed industry standards.* If needed, the customer should ensure Vault/Takeout is used to export data before termination. **Risk is low**; Google’s practices minimize lingering data, but explicit retention requirements should be addressed via configuration and contract if necessary.

**Privacy Compliance (GDPR, CCPA, HIPAA, etc.):** Google Workspace is fully **GDPR-compliant** as a data processor. Google offers a comprehensive Cloud Data Processing Addendum (CDPA/DPA) which incorporates the EU Standard Contractual Clauses for lawful cross-border data transfer and outlines Google’s privacy commitments. Under this DPA, Google contractually commits to key GDPR requirements (processing data only per instructions, assisting with data subject requests, breach notifications within 72 hours, etc.). For **CCPA**, Google is categorized as a Service Provider and refrains from selling personal data. Google also signs **HIPAA Business Associate Agreements (BAA)** for Workspace (for eligible editions) to support HIPAA compliance for healthcare data. Additionally, Google Workspace has achieved **ISO 27701 (Privacy Information Management)** certification, indicating its privacy program is audited against international standards. *In summary, Google has strong privacy controls and contractual terms:* the risk of non-compliance is low. Next steps for full assurance: review the signed DPA/BAA and ensure all required configurations (like retention settings, consent for additional services) are in place on the customer side.

**Use of Subcontractors / 4th Parties:** Google performs the vast majority of Google Workspace data processing with its own infrastructure and personnel. It does engage a limited number of **subprocessors** for specific support and ancillary services (for example, for global customer support, infrastructure maintenance, etc.). All Google Workspace subprocessors are subject to Google’s vendor security assessment and are bound by stringent security & privacy agreements. Google publishes a list of subprocessors for Workspace (available on their Trust Center) and provides notice to customers of any significant changes. There is **no indication of high-risk fourth parties** in the Workspace supply chain – Google’s tight control over its infrastructure limits third-party exposure. *Risk is low*, but customers should periodically review the Google Workspace subprocessor list (and Google will update the DPA if new critical subprocessors are added).

**Risk Score:** **2/10 (Low).**
 *Justification:* Google demonstrates strong data handling practices with respect to isolation, residency options, retention, and privacy law compliance. The presence of robust data protection terms (GDPR DPA, SCCs, HIPAA BAA) and Google’s limited reliance on third-party processors mitigate most privacy risks. While data residency is global by default, Google provides mechanisms to address sovereignty concerns. Residual risk around data privacy is minimal, provided the customer also configures the product in line with their compliance needs.



#### 5. Compliance and Certifications

**SOC Reports:** Google Workspace undergoes regular independent audits. Google publishes **SOC 2 and SOC 3** reports annually for Google Cloud/Workspace services. The **most recent SOC 2 Type II** report can be requested through Google’s compliance portal or sales team (usually under NDA). These SOC reports cover security, availability, confidentiality, and privacy controls, providing assurance that controls are suitably designed and operating effectively. *(Link: Google Cloud Compliance Reports repository – customers can access the SOC 2 report via Google’s trust center or upon request.)*

**ISO Certifications:** Google Workspace is certified under **ISO/IEC 27001** (Information Security Management), as well as **ISO/IEC 27017** (cloud security controls) and **ISO/IEC 27018** (cloud privacy protections for PII). Google has also added **ISO/IEC 27701** certification for its privacy information management system. These certifications are audited by third-party certifying bodies yearly. *(The ISO certificates and statements of applicability are available on Google’s Compliance Resource Center – e.g., an ISO 27001 certificate covering Google Cloud Platform and Google Workspace.)*

**FedRAMP / NIST Alignment:** Google Workspace has achieved **FedRAMP High authorization** for its services used by U.S. federal agencies. This means Google Workspace meets the stringent NIST 800-53 controls required for high-impact federal systems. Federal customers can leverage Google’s FedRAMP package (available via the FedRAMP PMO) to satisfy their compliance. Google also aligns with **NIST CSF** and **NIST 800-171** (per CMMC requirements) as part of its security program. In addition, Google participates in other government frameworks (e.g., BSI C5 in Germany, MTCS in Singapore). *This broad compliance suggests a strong control environment mapped to NIST and other standards.*

**Other Frameworks (PCI-DSS, HIPAA, HITRUST):** While Google Workspace is not meant for processing credit card transactions, the underlying Google infrastructure has **PCI DSS compliance** for relevant services. (Google Cloud Platform is PCI DSS certified, and by inheritance some Workspace components may qualify, but *storing cardholder data in Workspace is generally not a typical use case*.) For healthcare, as mentioned, Workspace can be used in a HIPAA-regulated environment with a BAA. Google doesn’t list HITRUST certification for Workspace, but many of the controls overlap with its existing audits. Google’s compliance documentation often provides **mapping documents** to regulations like GDPR, CCPA, GLBA, etc., to help customers. Overall, no major compliance gaps are known – **Workspace meets or exceeds requirements in most industries** (education, government, finance, healthcare) when configured properly.

**External Pen Tests / Vulnerability Scans:** Google engages independent third parties to perform penetration testing on Google Cloud and Workspace services as part of certain compliance audits (e.g., FedRAMP requires regular 3PAO pen tests). The results are not publicly shared in detail, but customers under NDA can request a summary of penetration test reports. Additionally, Google’s Vulnerability Reward Program (bug bounty) invites security researchers worldwide to test Workspace for vulnerabilities, adding another layer of external scrutiny. There have been **no known significant unresolved vulnerabilities** reported publicly for Google Workspace in recent years. The combination of internal and external testing means any serious issue is likely to be caught and remediated quickly.

**Risk Score:** **1/10 (Very Low).**
 *Justification:* Google Workspace maintains an extensive set of up-to-date compliance certifications and third-party attestations. These certifications (SOC 2, ISO 27001 series, FedRAMP High, etc.) have been independently validated, greatly reducing compliance risk. Customers in regulated industries can rely on these reports to satisfy oversight requirements. The risk of Google lacking a needed certification is very low — they are continuously expanding compliance coverage. (Remaining tasks are mostly on the customer side to ensure they leverage Google’s compliance capabilities properly.) 





#### 6. Incident Management

**Breach History:** **No major data breaches of Google Workspace** have been publicly reported to date. Google has a strong track record of security; notably, since moving to security key MFA, they’ve had zero known incidents of employee account compromise. One historical incident outside of Workspace was the Google+ API data exposure in 2018 (affecting Google+ social network profiles), but that did not impact Google Workspace services or customer enterprise data. Google is very transparent via its Security Incident Impact Reports and would notify customers of any breach involving their data. To date, **Workspace’s breach history is clean**, indicating a low likelihood of undetected security failures. (Any minor incidents have been quickly contained with no noteworthy customer impact reported publicly.)

**Incident Response Plan Status:** Google has a rigorous, formal **incident response plan** for security and privacy incidents affecting customer data. Dedicated incident response teams (part of Google’s global Security team) are in place. In the event of an incident, Google’s process includes defined steps for triage, investigation, containment, and recovery. Specialized roles (incident commander, forensics, legal, communications, etc.) are assigned to handle various aspects. Google’s incident playbooks cover scenarios from system outages to data breaches. This plan is regularly tested and refined through drills and post-mortems. *As a customer, you can have confidence that Google is prepared to respond swiftly to any Workspace security incidents.*

**Detection/Containment Metrics:** Specific metrics (like mean time to detect/respond) are not publicly disclosed by Google. However, given their capabilities (24/7 monitoring, automated detection systems, and a large security team), one can infer very short detection times – potentially **minutes to hours** for critical incidents. Google has stated that it actively monitors and often catches issues before they impact customers. Containment and remediation also benefit from Google’s automation (e.g., isolating affected systems) and enormous engineering resources. For example, Google’s rapid response to zero-day vulnerabilities (such as patching server or browser issues across its fleet) is well-regarded in the industry. *Overall, Google’s incident detection/response speed is among the best in class.* (For more concrete metrics, a security questionnaire response from Google might be needed – next step: request Google’s SIG or CAIQ response which might include more details on IR timing.)

**Notification & Escalation Protocols:** Per Google’s Customer Agreements and the Cloud DPA, Google **commits to notify customers without undue delay** (and within 72 hours as required under GDPR) if any security breach occurs that affects customer data. They have support personnel dedicated to customer communications during incidents. In practice, if a significant Workspace incident happens (e.g., a widespread outage or data issue), Google posts public status updates on the Workspace Status Dashboard and sends notifications to admins. For any data breach, Google would use established channels (likely email to registered security contacts or admin console alerts) to inform customers, provide remediation guidance, and follow up with a post-incident report. Escalation internally at Google is very fast – incidents are treated with the highest priority, involving senior leadership when needed. *There is low risk of Google failing to notify; the protocols are clearly defined.* One area to verify: ensure your organization’s contact information is up-to-date in the Google Admin Console for emergency communications.

**Risk Score:** **2/10 (Low).**
 *Justification:* Google’s incident management maturity – reflected by a lack of serious breaches, a dedicated global IR team, and clear notification commitments – means the likelihood and impact of an unmanaged incident are low. They have demonstrated the ability to contain and resolve issues quickly. The score is not 1 only because no system is immune to incidents; however, Google’s capabilities drastically limit potential damage. The residual risk mainly lies in extremely sophisticated attacks or unforeseen vulnerabilities, but even then Google’s responsiveness would mitigate impact on customers.



#### 7. Business Continuity & Disaster Recovery

**BCP/DRP Documentation:** Google has robust **Business Continuity and Disaster Recovery plans** for Google Workspace, though the detailed documentation is internal. The architecture of Workspace itself provides inherent disaster tolerance – data is redundantly stored across multiple data centers and Google can shift workloads as needed. Google’s continuity planning is regularly tested; they design for failure at the component, server, and data center levels. While proprietary, Google’s BC/DR plans have been examined as part of compliance audits (e.g., ISO 27001, SOC 2) and found to be comprehensive. *Next steps:* If required for audit, a summary of Google’s BCP/DR approach for Workspace can be requested via their compliance team. It likely covers emergency response, recovery procedures, and organizational resilience (Google has geographically dispersed operations centers to manage continuity).

**RTO & RPO:** Google does not publicly publish specific RTO/RPO values for Google Workspace, but given their redundancy, the **Recovery Time Objective is near zero** for most single-component failures (services fail over automatically). In scenarios of major outage, Google’s goal is to restore service in minutes, not hours – evidenced by the rare downtime incidents which are usually resolved quickly. The **Recovery Point Objective** (data loss tolerance) is effectively **zero or near-zero** for in-region failures because data is synchronously replicated. Even in catastrophic regional failures, Google Workspace is architected to switch to backup systems with minimal data loss (possibly a few seconds of recent data might be in transit). In practice, Gmail and Drive have extremely high durability (11 nines for Google Cloud Storage). *Overall, RTO/RPO are very aggressive (low), meaning customers are unlikely to lose data or experience prolonged downtime.* Google’s SLA of 99.9% uptime supports that outages per month should be less than ~43 minutes.

**DR/BCP Testing Frequency:** Google conducts continuous testing of its infrastructure resilience. This includes drills like data center failovers, chaos engineering experiments, and simulating large-scale outages to ensure systems respond as expected. They haven’t disclosed a specific interval (e.g., quarterly or annually) for full BCP drills, but given their engineering culture, **automated failover is tested regularly**. Google’s services also have frequent **disaster simulations** – for example, they might intentionally take a data center offline to verify traffic routes to another. Additionally, Google’s incident post-mortems feed into BCP improvements. *This continual testing regime reduces the risk of any unforeseen failure during a real disaster.*

**Geo-Redundancy Capabilities:** Google Workspace data is geographically distributed. For instance, an email in Gmail is stored in multiple data centers in different locations by default for redundancy. If one site goes down (due to natural disaster or other issue), user data is still accessible from another site. Google’s network can automatically re-route user connections to the nearest active region. All core Workspace services (Gmail, Drive, etc.) are built on active-active replication across data centers. Furthermore, Google takes backups on separate media, and even these backups are encrypted and protected. The system is also highly scalable to handle failover load. **Geo-redundancy is a key strength for Google** – it significantly lowers the risk of data loss or prolonged outage due to any single-location event.

**Risk Score:** **1/10 (Very Low).**
 *Justification:* Google’s BC/DR posture for Workspace is extremely strong. The company’s massive, distributed infrastructure and proven redundancy mean that even in the event of disasters, operations can continue with minimal disruption. Past performance (Workspace historically has had few global outages and no significant data losses) backs this up. The risk of extended downtime or irrecoverable data loss is negligible. (The only caveat is dependent on an internet connection – as with any cloud service, customer-side continuity plans should ensure internet access and backup mail solutions if needed for extreme cases.)



#### 8. Human Resources and Training

**Background Checks on Employees:** Google has strict hiring standards and performs thorough **employee background checks** for personnel in sensitive positions. Before hiring, Google verifies education, previous employment, and references, and for roles with access to customer data or facilities, they also conduct identity and criminal checks as allowed by law. These checks help ensure that those with potential access to systems are vetted for trustworthiness. The company’s global workforce screening lowers the insider risk from the outset.

**Security Awareness Training:** **All Google employees receive security and privacy training** from day one and repeatedly during their tenure. New hires must complete security orientation and sign the Code of Conduct (emphasizing data protection). Ongoing, Google runs regular security refresher courses, phishing tests, and a security newsletter to keep staff aware of emerging threats. Engineers get additional secure coding training and are kept up-to-date on best practices. There are also internal campaigns like “Privacy Week” to reinforce the culture of security. This pervasive training regimen greatly reduces the likelihood of human error leading to security incidents.

**Insider Threat Mitigation Strategies:** Google employs multiple controls to mitigate insider threats (malicious or accidental). These include the least-privilege access model – employees are given access only to what they need, and access is tightly monitored. High-risk actions (like accessing customer accounts or data) require justification and are logged via Access Transparency for customer visibility. Google also has internal monitoring to detect unusual employee activity on systems. For example, if an employee tried to download large amounts of customer data, it would trigger alerts. The dedicated security team does behavioral analytics to spot insider anomalies. Additionally, Google fosters a culture where employees are encouraged to report suspicious activities or potential security issues (with anonymity options). Overall, these measures, along with background checks and training, create a strong defense against insider risks.

**Role-Based Access Control (RBAC):** Google’s internal systems and the administration of Google Workspace use robust RBAC. Access to production environments and customer data is limited to a small group of authorized engineers. Google uses an automated system to grant and revoke access rights based on role changes or termination – when an employee leaves or changes role, access is promptly removed. Administrative access requires approvals and is logged, and privileges are segregated (for instance, support engineers might be able to see metadata but not content unless escalated). On the customer side, Google Workspace allows administrators to implement RBAC for their IT admins (with predefined admin roles and the ability to create custom roles with least privilege). *The enforcement of RBAC internally ensures no single employee can unilaterally access or compromise the system without oversight.* Google’s zero-trust approach also means that even within the network, services authenticate and authorize each call, further implementing RBAC at a service-to-service level.

**Risk Score:** **2/10 (Low).**
 *Justification:* Google’s HR and security training practices significantly lower personnel-related risks. With comprehensive background checks, continuous training, and strong internal controls on access, the likelihood of an insider-caused incident or negligence is very low. The only residual risk comes from the human factor that no program can 100% eliminate (e.g., a highly sophisticated social engineering of an employee or a rogue insider at the highest privilege). However, given Google’s multiple overlapping controls (technical and cultural), the insider threat risk is well-managed.



#### 9. Financial Risk and Stability

**Balance Sheet / Income Statement Insights:** Alphabet Inc. (Google’s parent) is one of the financially strongest companies in the world. In 2024, Alphabet reported **annual revenues of $350 billion** with a net income of over **$100 billion**. The company has a huge asset base and minimal long-term debt (debt-to-equity is only ~8%). Alphabet maintains a cash reserve around **$95 billion** as of the most recent reports, providing ample liquidity. These figures show that Google can easily invest in and support Google Workspace operations; **financial failure or sudden bankruptcy risk is essentially zero** for a company of this scale and profitability.

**Profitability & Cash Flow:** Google’s core businesses (including Google Workspace within Google Cloud segment) are profitable. Google Cloud (which includes Workspace) is growing rapidly; while historically Google Cloud segment operated at a loss, it turned profitable in 2023. Alphabet overall is a cash flow machine, generating over $70 billion in free cash flow in 2024. Such strong cash flow means Google can cover operational costs, R&D, and any unforeseen expenses (like legal fines or incident costs) without impacting service delivery. The profit margins are high and trends are stable or improving. There’s no indication of financial stress. *This financial stability means continuity of the service and future investment in improvements are assured.*

**Insurance Coverage (Cyber, Liability):** Google/Alphabet carries extensive insurance, though exact policies are confidential. It is common for a company of Alphabet’s size to have cyber liability insurance, errors & omissions coverage, and general liability insurance in place with high coverage limits (often in the hundreds of millions). In addition, Alphabet’s balance sheet effectively self-insures many risks (they could absorb the cost of an incident). *Due to insufficient public info, we cannot quantify their insurance, but it’s reasonable to assume robust coverage.* Next steps if needed: Google may provide a certificate of insurance under NDA if required by a customer contract. However, **practical risk of financial loss to customers from Google’s insolvency is nil**. The insurance aspect mainly ensures Google can respond to legal liabilities or claims; given their financial muscle, this is a minor concern.

**Risk Score:** **1/10 (Very Low).**
 *Justification:* Alphabet’s financial strength virtually eliminates traditional vendor financial risks (like bankruptcy, going concern issues, or inability to invest in security). The company’s revenues and cash buffers are massive, and it has top-tier credit ratings indicating confidence in its stability. There is no significant risk that Google will be unable to fulfill its obligations due to financial problems. (Even large fines or market downturns have historically barely dented their operations.) Thus, financial risk to the customer is negligible.



#### 10. Legal and Contractual Risk

**MSA / DPA Review Notes:** Google’s standard **Master Services Agreement (MSA)** and Data Processing Addendum (DPA, now called the Cloud Data Processing Addendum - CDPA) for Google Workspace are publicly available and have been vetted by thousands of organizations. Key points: The DPA meets GDPR requirements, including Google’s role as a Processor and Model Contractual Clauses for data transfers. Google also contractually commits to security measures in the DPA (Annex with technical and organizational measures) and breach notification obligations. The **MSA** (Terms of Service) covers liability limits, use of service, customer data ownership (customer retains all rights to their data), and acceptable use. No unusual clauses have been noted – they are fairly standard for a cloud provider. One item: Google’s terms include that they do not use Workspace customer data for advertising purposes or sell it, which is explicitly stated and important for privacy. *If this assessment is internal, ensure Legal has reviewed the MSA/DPA versions signed; no red flags from a public review standpoint.*

**Termination / Liability Clauses:** Google’s liability clause in the Workspace agreement typically caps liability to the amount paid by the customer in the last 12 months (and often excludes indirect/consequential damages). This is a **standard limitation of liability** for SaaS providers. It means if Google fails in some way, their financial responsibility is limited. While this is common, it does present residual risk: in a hypothetical severe incident causing large losses, Google’s contractual payout is capped. The termination provisions usually allow either party to terminate for cause (e.g., material breach) and allow the customer to retrieve data (data export) upon termination. There’s also usually a clause that if services are terminated, Google will delete customer data per the DPA. No lock-in penalties beyond possibly remaining contract fees. *The contractual risk here is moderate only because of the typical liability cap.* To mitigate, some customers negotiate higher caps for data breach events – it’s worth evaluating if that’s needed for your risk appetite.

**SLA Terms:** Google Workspace provides a Service Level Agreement guaranteeing **99.9% uptime** for core services. If availability falls below this, customers can claim service credits (scaled by downtime, up to 50% of monthly fee for severe outages). The SLA excludes outages caused by factors outside Google’s control or scheduled maintenance (which is minimal, Google rarely has downtime windows). Historically, Google has met or exceeded its SLA most of the time – Google publishes uptime reports (Workspace had ~99.98% uptime in past years). The SLA is in line with industry norms. *Risk:* Low – the SLA provides some recourse for downtime, though credits may not cover the full business impact of an outage. Ensure you understand the credit claiming process (must file within 30 days of incident). No SLA for performance aside from uptime, but performance issues are rare given Google’s infrastructure.

**Audit Rights:** Under Google’s standard contract and DPA, **customers have limited audit rights**. Google generally does not permit on-site audits by each customer due to security and scalability, but the DPA Section 7.5 provides that customers can either review Google’s audit reports (SOC/ISO certifications) or commission an independent audit in certain circumstances. If a customer requires it (and regulatory requirements demand it), Google will allow an audit by an accredited third-party auditor on the customer’s behalf, subject to conditions (e.g., auditor can’t be a Google competitor, and reasonable advance notice). Google may charge for such audits. In practice, almost all customers rely on the provided **third-party attestations** instead of conducting their own audit. This approach is common in cloud contracts, but it means direct audit rights are somewhat restricted. *Risk:* For most, low – because the available documentation is comprehensive. However, if your organization requires direct audits, this could be a negotiation point.

**Risk Score:** **4/10 (Moderate).**
 *Justification:* Legally, Google’s contracts are standard and fair for a large provider, but from the customer perspective, the **limitations of liability and limited direct auditability introduce some risk**. The moderate score reflects that in a worst-case scenario (e.g., a major data breach), the customer’s ability to recover losses from Google is contractually limited. That said, Google’s strong performance and compliance reduce the likelihood of ever needing to invoke these clauses. The recommendation is to accept Google’s standard terms for most points (since they are an industry norm), while ensuring internal strategies (insurance, backups, etc.) account for the residual contractual limitations. No showstoppers in the contract were identified.



#### 11. Risk Scoring and Tiering

- **Inherent Risk Score:** **9/10 (High)**
   *Justification:* Google Workspace has access to a wide range of the organization’s data (email, documents, calendars) and is deeply integrated into daily operations. Inherently, a failure or breach of this vendor could have **critical impact** on confidentiality and availability of our information. The broad scope and criticality of the service make the raw risk high before considering controls (particularly in areas of data sensitivity and business dependence).
- **Residual Risk Score:** **2/10 (Low)**
   *Justification:* After evaluating Google’s strong controls, compliance posture, and reliability, the risk remaining is very low. Google’s security measures, resilience, and financial stability dramatically mitigate the inherent risks. For example, encryption and access controls protect data, and geo-redundancy protects availability. The gap between inherent and residual risk is large, showing Google’s controls are highly effective. The **2/10** residual rating indicates only a minimal likelihood of a significant adverse event affecting us via Google Workspace (though not zero – e.g., a black swan event could still occur).
- **Tier Recommendation:** **Critical (Tier 1)** vendor
   *Justification:* Google Workspace should be classified as a **Critical** supplier given its importance. This service underpins email communication, document storage, and collaboration for the organization – an outage or compromise would be immediately felt enterprise-wide. The vendor handles **sensitive data** and a high volume of business processes. Tiering it as Critical ensures the highest level of ongoing oversight (e.g. annual risk reviews, executive visibility). Despite the low residual risk, the impact of a worst-case scenario warrants a top-tier classification.
- **Overall Justification Summary:** In summary, **Google Workspace is a high-inherent-risk vendor that is managed to a low residual risk through excellent controls and assurances**. Google’s dominance in technology, massive investment in security, and plethora of compliance certifications give confidence in the service. We should maintain this vendor as a strategic partner, with periodic due diligence refresh (especially watching for any regulatory changes or reported incidents). The recommendation is to continue usage with standard monitoring. Areas with “Insufficient information” (like specific contacts or insurance details) can be addressed by engaging Google directly if needed. No immediate remediation actions are required from a vendor risk standpoint, other than ensuring our own configurations and contingency plans are in place in alignment with this assessment.



## ✅ To-Do / Future Enhancements

- [ ] Auto-classify vendors into buckets (Low / Medium / High)  
- [ ] Add contract document analysis using file attachments  
---

## 👨‍💻 Author

Created by Austin Songer
Contact: austin@songer.me
License: MIT
