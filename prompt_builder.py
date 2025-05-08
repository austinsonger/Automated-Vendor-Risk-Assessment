def build_prompt(data: dict) -> str:
    def val(field, default="[Not Provided]"):
        return data.get(field, default)

    return f"""
You are an expert vendor risk analyst. Use the information below to perform a comprehensive risk assessment of the vendor. Reference publicly available data and industry best practices where applicable.

---

🧾 1. Vendor Profile Information
- Vendor Name: {val("vendor_name")}
- Legal Business Name: {val("vendor_legal_name")}
- Website: {val("vendor_website")}
- Primary Contact(s): {val("vendor_contacts")}
- Type of Service: {val("vendor_service_type")}
- Geographic Locations (Ops/Data Centers): {val("vendor_geographic_scope")}
- Length and Terms of Relationship: {val("vendor_relationship_terms")}

---

🔍 2. Due Diligence and Background Checks
- Business Credit Report: {val("vendor_credit_report_summary")}
- Litigation or Legal History: {val("vendor_litigation_summary")}
- Ownership & Parent Companies: {val("vendor_ownership_structure")}
- Watchlist / Sanctions Screening: {val("vendor_watchlist_status")}
- Media & Reputation Scan: {val("vendor_reputation_summary")}

---

🔐 3. Information Security Controls
- Data Encryption Practices: {val("vendor_encryption_practices")}
- Network Security (firewalls, IDS/IPS): {val("vendor_network_security")}
- Endpoint Protection: {val("vendor_endpoint_protection")}
- Access Control & MFA: {val("vendor_access_controls")}
- Logging/Monitoring Practices: {val("vendor_logging_monitoring")}
- Secure SDLC / DevSecOps Maturity: {val("vendor_sdllc_practices")}

---

☁️ 4. Data Handling and Privacy
- Data Classification & Segregation: {val("vendor_data_classification")}
- Data Residency / Jurisdiction: {val("vendor_data_residency")}
- Data Retention & Destruction Policy: {val("vendor_data_retention")}
- Privacy Compliance (e.g., GDPR, CCPA, HIPAA): {val("vendor_privacy_compliance")}
- Use of Subcontractors / 4th Parties: {val("vendor_subcontractors")}

---

🧪 5. Compliance and Certifications
- SOC Reports: {val("vendor_soc_certifications")}
- ISO Certifications: {val("vendor_iso_certifications")}
- FedRAMP / NIST Alignment: {val("vendor_fedramp_nist_status")}
- Other Frameworks (PCI-DSS, HIPAA, HITRUST): {val("vendor_other_certifications")}
- External Pen Tests / Vulnerability Scans: {val("vendor_pentest_status")}

---

🧯 6. Incident Management
- Breach History: {val("vendor_breach_history")}
- Incident Response Plan Status: {val("vendor_irp_status")}
- Detection/Containment Metrics: {val("vendor_ttd_ttc")}
- Notification & Escalation Protocols: {val("vendor_notification_procedures")}

---

💼 7. Business Continuity & Disaster Recovery
- BCP/DRP Documentation: {val("vendor_bcp_drp_status")}
- RTO & RPO: {val("vendor_rto_rpo")}
- DR/BCP Testing Frequency: {val("vendor_bcp_testing")}
- Geo-Redundancy Capabilities: {val("vendor_geo_redundancy")}

---

👥 8. Human Resources and Training
- Background Checks on Employees: {val("vendor_background_checks")}
- Security Awareness Training: {val("vendor_security_training")}
- Insider Threat Mitigation Strategies: {val("vendor_insider_threat_mitigation")}
- Role-Based Access Control (RBAC): {val("vendor_rbac_controls")}

---

💲 9. Financial Risk and Stability
- Balance Sheet / Income Statement Insights: {val("vendor_financials_summary")}
- Profitability & Cash Flow: {val("vendor_profitability_analysis")}
- Insurance Coverage (cyber, liability): {val("vendor_insurance_coverage")}

---

⚖️ 10. Legal and Contractual Risk
- MSA / DPA Review Notes: {val("vendor_contract_summary")}
- Termination / Liability Clauses: {val("vendor_termination_liability")}
- SLA Terms: {val("vendor_sla_summary")}
- Audit Rights: {val("vendor_audit_rights")}

---

📊 11. Risk Scoring and Tiering
- Inherent Risk (Before Controls): {val("vendor_inherent_risk_score")}
- Residual Risk (After Controls): {val("vendor_residual_risk_score")}
- Tier Recommendation (Critical/High/Medium/Low): {val("vendor_risk_tier")}
- Justification Summary: {val("vendor_risk_summary_justification")}

---

🔗 12. External Sources and Supporting Links
Provide direct URLs to relevant vendor documentation, if available.

- SOC 2 Type II Report: {val("vendor_soc2_link")}
- ISO 27001 Certification: {val("vendor_iso27001_link")}
- Breach Disclosure Report: {val("vendor_breach_link")}
- Security Practices / Trust Center: {val("vendor_security_page")}
- Privacy Policy or Compliance Statement: {val("vendor_privacy_policy")}

---

Instructions:
- Include direct references or links to any public reports, press coverage, filings, or certifications you find.
- Be objective, cite sources where possible, and summarize key risk indicators across financial, legal, technical, and reputational domains.
- Add links to any information for SOC 2 Type 2 Reports or ISO 27001 Reports.
- If any section lacks sufficient information, explicitly note it as “Insufficient data available.” Do not speculate or fabricate findings. Recommend next steps to gather the missing data if appropriate.
- If any field is missing, marked “[Not Provided]”, or cannot be found, clearly state “Insufficient information available” in your analysis. Do not speculate.
- For each section, provide a short summary and a risk score (1–10 scale) if applicable.
- Return the findings in a structured format suitable for posting as a Jira ticket comment.
"""
