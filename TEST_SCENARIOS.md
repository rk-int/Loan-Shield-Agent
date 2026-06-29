# LoanShield — Local Testing Scenarios & Benchmark Cases

This document outlines the **6 core test scenarios** to validate the security and underwriting decision workflows of the LoanShield application locally.

---

## 🚀 Setting Up the Local Host Engines

You can test these scenarios using two different interfaces:

### Option A: Premium 3D Custom Portal (Recommended)
This portal is built specifically for this application, implementing the visual guidelines, 3D particles, and real-time SVG flowcharts:
1.  In your terminal, navigate to the `loanshield` directory:
    ```bash
    cd loanshield
    ```
2.  Run the custom gateway server:
    ```bash
    make custom-ui
    ```
3.  Open **[http://127.0.0.1:18080](http://127.0.0.1:18080)** in your web browser.
4.  Use the **Select Benchmark Template** grid at the top to auto-fill the forms instantly.

### Option B: Built-in Google ADK Playground
This is the default Google ADK developer playground portal:
1.  In the `loanshield` directory, run:
    ```bash
    make playground
    ```
2.  Open **[http://127.0.0.1:18081](http://127.0.0.1:18081)** in your web browser.
3.  Select the `loanshield_workflow` from the dropdown list.
4.  Copy/paste the JSON inputs below into the prompt area to execute them.

---

## 📋 The 6 Test Scenarios & Inputs

### Scenario 1: Prime Profile (Auto Approve)
*   **Applicant**: Liam Smith
*   **Objective**: Test clean, low-risk workflow execution that results in immediate automated approval without interruptions.
*   **Expected Verdict**: `APPROVED` (Score ~ 98.0)
*   **ADK JSON Input**:
    ```json
    {
      "applicant_id": "APP-001",
      "customer_id": "CU-001",
      "name": "Liam Smith",
      "ssn": "960-24-6191",
      "dob": "01-05-1976",
      "phone_number": "-7853",
      "home_address": "566 Oak Ave, Los Angeles, CA 47194",
      "age": 50,
      "declared_income_monthly": 11171,
      "loan_amount": 31023,
      "purpose": "Used Car Loan",
      "target_scenario": "Prime"
    }
    ```

---

### Scenario 2: Thin Credit Profile (HITL Underwriter Review)
*   **Applicant**: Harper Robinson
*   **Objective**: Test Escalation to Human Underwriting. The applicant has thin credit history causing a risk score in the review band (60 to 75).
*   **Expected Flow**: The engine pauses at `human_underwriter_hitl_node` and requests input.
*   **Action Required**: Click **APPROVE LOAN** or **REJECT LOAN** in the override panel to resume.
*   **Expected Final Verdict**: `APPROVED` (if approved) or `REJECTED` (if rejected).
*   **ADK JSON Input**:
    ```json
    {
      "applicant_id": "APP-018",
      "customer_id": "CU-018",
      "name": "Harper Robinson",
      "ssn": "917-34-9716",
      "dob": "10-04-1999",
      "phone_number": "-6719",
      "home_address": "2468 Maple Dr, Houston, TX 87575",
      "age": 27,
      "declared_income_monthly": 4971,
      "loan_amount": 16002,
      "purpose": "Major Purchase",
      "target_scenario": "Thin Credit"
    }
    ```

---

### Scenario 3: High Debt-to-Income Ratio (Auto Reject)
*   **Applicant**: Jackson Nguyen
*   **Objective**: Test automated reject due to financial insolvency (high DTI).
*   **Expected Verdict**: `REJECTED` (Score < 50.0)
*   **Adverse Action Reasons**: Low FICO credit score, high debt-to-income ratio.
*   **ADK JSON Input**:
    ```json
    {
      "applicant_id": "APP-031",
      "customer_id": "CU-031",
      "name": "Jackson Nguyen",
      "ssn": "507-37-5468",
      "dob": "06-03-1994",
      "phone_number": "-8346",
      "home_address": "3819 Oak Ave, Los Angeles, CA 94665",
      "age": 32,
      "declared_income_monthly": 4540,
      "loan_amount": 64835,
      "purpose": "Emergency Expenses",
      "target_scenario": "High DTI"
    }
    ```

---

### Scenario 4: Identity / Synthetic Fraud Flag (Auto Reject)
*   **Applicant**: Grace Carter
*   **Objective**: Test automated fraud prevention. The SSN matches the credit bureau records but the associated name does not, indicating identity mismatch/synthetic fraud.
*   **Expected Verdict**: `REJECTED` (Fraud Flag = True)
*   **Adverse Action Reasons**: High-risk synthetic fraud flag triggered (identity mismatch).
*   **ADK JSON Input**:
    ```json
    {
      "applicant_id": "APP-042",
      "customer_id": "CU-042",
      "name": "Grace Carter",
      "ssn": "322-15-8489",
      "dob": "06-05-1985",
      "phone_number": "-10792",
      "home_address": "8937 Washington Blvd, San Antonio, TX 10117",
      "age": 41,
      "declared_income_monthly": 8551,
      "loan_amount": 44309,
      "purpose": "Used Car Loan",
      "target_scenario": "Fraud"
    }
    ```

---

### Scenario 5: Missing Required Documents (HITL Document Bypass)
*   **Applicant**: John Turner
*   **Objective**: Test Escalation to Document Check. The applicant's document storage checklist is incomplete.
*   **Expected Flow**: The engine pauses at `gatekeeper_node` and requests input (`document_override`).
*   **Action Required**: Click **Override & Resume** (approves bypassing document checks) or **Reject Application**.
*   **Expected Final Verdict**: If overridden, continues and completes risk assessment.
*   **ADK JSON Input**:
    ```json
    {
      "applicant_id": "APP-047",
      "customer_id": "CU-047",
      "name": "John Turner",
      "ssn": "715-60-2970",
      "dob": "01-09-1987",
      "phone_number": "-3443",
      "home_address": "5667 Lakeview Dr, San Diego, CA 66819",
      "age": 39,
      "declared_income_monthly": 6692,
      "loan_amount": 20408,
      "purpose": "Business Venture",
      "target_scenario": "Missing Documents"
    }
    ```

---

### Scenario 6: Terminated Employment Status (Auto Reject)
*   **Applicant**: James Vance
*   **Objective**: Test rejection due to lack of stable source of income (recent termination status in employment records).
*   **Expected Verdict**: `REJECTED` (Score < 50.0)
*   **Adverse Action Reasons**: Employment termination flag (unstable income source).
*   **ADK JSON Input**:
    ```json
    {
      "applicant_id": "APP-051",
      "customer_id": "CU-051",
      "name": "James Vance",
      "ssn": "415-88-2931",
      "dob": "14-11-1988",
      "phone_number": "-4311",
      "home_address": "812 Willow St, Miami, FL 33101",
      "age": 37,
      "declared_income_monthly": 9500,
      "loan_amount": 45000,
      "purpose": "Debt Consolidation",
      "target_scenario": "Terminated Employment"
    }
    ```
