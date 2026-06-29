# LoanShield — Secure & Automated Credit Decisioning Engine

LoanShield is an enterprise-grade automated lending decision platform built on Google's Agent Development Kit (ADK 2.0). It ingests credit applications, redacts sensitive PII, executes parallel financial analysis and compliance verification using stdio Model Context Protocol (MCP) servers, calculates a multi-factor credit risk score, and dispatches regulatory ECOA-aligned explanation letters.

---

## 🏛️ System Architecture

The LoanShield processing pipeline is structured as a LangGraph state workflow:

```
                  [ START ]
                      │
                      ▼
             [ gatekeeper_node ] ──(Incomplete Docs)──► [ explanation_node ]
                      │ (Complete Docs)                         ▲
                      ▼                                         │
             ┌────────┴────────┐                                │
             ▼                 ▼                                │
    [ financial_analysis ] [ fraud_analysis ]                   │
             └────────┬────────┘                                │
                      ▼                                         │
               [ JoinNode ]                                     │
                      │                                         │
                      ▼                                         │
             [ risk_scoring ] ────(Auto Reject/Approve)─────────┤
                      │ (Human Review / Escalation)             │
                      ▼                                         │
        [ human_underwriter_hitl ] ─────────────────────────────┘
```

---

## 📁 Repository Structure

```
loanshield/
├── Makefile                        # Local dev commands (install, playground, test)
├── Dockerfile                      # Standardized container image definition
├── docker-compose.yml              # Multi-container orchestration configurations
├── pyproject.toml                  # Python package and dependency management (uv synced)
├── .github/workflows/              # CI/CD automated lint/test validation triggers
│   └── github_actions.yaml
├── datasets/                       # Reference mock datasets (JSON/CSVs)
├── app/
│   ├── __init__.py                 # Application initialization
│   ├── agent.py                    # LangGraph workflow coordination & agent nodes
│   ├── config.py                   # Environment variable mappings
│   ├── state.py                    # Graph state TypedDict and Pydantic schemas
│   ├── mcp_server.py               # Stdio MCP servers exposing databases as tools
│   └── skills/                     # Modular business verification functions
│       ├── pii_redactor.py         # Regex + LLM-based PII mask
│       ├── income_verify.py        # Plaid-style bank deposit validation
│       ├── dti_calculator.py       # Affordability DTI ratio checks
│       ├── stability_modifier.py   # Job tenure scoring adjustment
│       ├── risk_scoring.py         # Multi-factor score calculator
│       ├── fraud_detection.py      # Hard risk rules & limits
│       └── explanation.py          # ECOA regulatory notice builder
└── tests/
    ├── conftest.py                 # Global LLM mocks & patches (offline testing)
    ├── test_skills.py              # Unit tests for scoring/verification skills
    ├── test_mcp.py                 # Integration tests for MCP server tools
    └── test_graph.py               # End-to-end integration tests over all 54 rows
```

---

## 🚀 Local Development Commands

This project uses `uv` for dependency management. Access all tasks via the `Makefile`:

### 1. Installation
Install Python dependencies and sync the virtual environment:
```bash
make install
```

### 2. Playground Execution
Launch the local ADK web playground interface for manual underwriter checks:
```bash
make playground
```
*Access the interface locally at `http://127.0.0.1:18081`.*

### 3. Automated Testing
Run the complete unit, MCP, and graph integration test suite:
```bash
make test
```
*Note: The end-to-end test executes and verifies all 54 applicants from the benchmark dataset.*

---

## 📊 Decision Routing Grid

The LoanShield scoring engine generates risk scores ($0 - 100$) and routes decisions according to these criteria:

*   **Auto-Approve** (Score $\ge 70$, zero fraud flags): Applications are approved instantly.
*   **Human Review** (Score $40 - 69$, zero fraud flags): Suspends workflow with a HITL interrupt, requesting underwriter verification.
*   **Auto-Reject** (Score $< 40$ OR any fraud flag): Rejects application and drafts a regulatory ECOA-compliant adverse action letter.

---

## 🖥️ Custom Web Application Portal

We built a custom, high-fidelity web gateway interface for LoanShield, replacing the generic command-line or basic forms with a state-of-the-art underwriting workstation:
1.  **3D WebGL Backdrop**: Utilizes **Three.js** to render a real-time, dot-matrix animated particle field that responds dynamically to pointer coordinates via parallax drift and features a slow breathing pulse.
2.  **Translucent Glassmorphism Panels**: Built with a sleek dark aesthetic (`#0A0A0A`) accented by neon green (`#A3E635`), utilizing glass panels with `backdrop-filter: blur(12px)`.
3.  **Live Node Graph Workflow**: Displays the exact LangGraph agent node layout connected by active, pulsing SVG bezier connection paths that light up in real-time.
4.  **EventSource (SSE) Streaming**: Connects directly to the backend memory runner to stream node state transitions (`running`, `paused`, `completed`, `failed`) and transition logs.
5.  **Audit Trail Terminal Logs**: Simulates a CLI logs terminal directly on the page, with info/warning/critical color-coding.
6.  **Interactive Underwriter Overrides Box**: Pauses execution and pops up override control buttons (`APPROVE`, `REJECT`, `RESUME`) when human intervention is triggered.

---

## 📸 Web UI Execution Screenshots

### 1. Loan Shield Human in loop Approval
![Human in Loop Approval Escalation](docs/images/hitl_approval_pending.png)
*This screenshot illustrates the workflow paused at `human_underwriter_hitl_node` (pulsing orange). Because the risk score of 64.1 lies within the review threshold, the process suspends and displays interactive **APPROVE LOAN** and **REJECT LOAN** override buttons in the bottom-right panel.*

---

### 2. Loan Shield Rejected
![Synthetic Fraud Rejection](docs/images/application_rejected.png)
*This screenshot demonstrates the auto-rejection state for applicant Grace Carter. A synthetic fraud identity mismatch is flagged, resulting in a risk score of 80.8 being overridden to a **REJECTED** verdict. The formal ECOA Credit Notice letter details the specific adverse action reasons at the bottom.*

---

### 3. Loan Shield Auto Approved
![Prime Auto Approval](docs/images/auto_approved.png)
*This screenshot shows a prime credit application (Liam Smith) being successfully processed. The risk scorer evaluates the profile at a composite score of 85.4, resulting in a final verdict of **APPROVED** (green badge) and drafting the congratulations approval notice.*

---

### 4. Loan Shield Human in Loop Approved
![HITL Overridden Approval](docs/images/hitl_approved.png)
*This screenshot showcases the application state after the human underwriter clicks the **APPROVE LOAN** override button for Harper Robinson. The workflow resumes from its paused state, evaluates the final decision as **APPROVED**, and displays the completed audit trail logs.*

