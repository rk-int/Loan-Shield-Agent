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
