import pytest
from unittest.mock import patch
from google.adk.agents import LlmAgent
from google.adk.events.event import Event
from app.mcp_server import get_credit_profile, get_banking_profile, get_employment_profile
from app.skills.explanation import generate_ecoa_letter

async def mock_llm_agent_run_async(self, ctx):
    if self.name == "financial_analysis_node":
        customer_id = ctx.session.state.get("customer_id")
        credit = get_credit_profile(customer_id)
        banking = get_banking_profile(customer_id)
        emp = get_employment_profile(customer_id)
        
        output = {
            "credit_score": credit["credit_score"],
            "credit_history_length_months": credit["credit_history_length_months"],
            "delinquencies": credit["delinquencies"],
            "total_tradelines": credit["total_tradelines"],
            "monthly_debt_obligations": credit["monthly_debt_obligations"],
            "average_monthly_deposits": banking["average_monthly_deposits"],
            "average_monthly_withdrawals": banking["average_monthly_withdrawals"],
            "current_balance": banking["current_balance"],
            "employer_name": emp["employer_name"],
            "employment_status": emp["employment_status"],
            "tenure_months": emp["tenure_months"]
        }
        
        yield Event(
            output=output,
            state={"financial_profile": output}
        )
    elif self.name == "explanation_node":
        name = ctx.session.state.get("name", ctx.session.state.get("redacted_name", "[REDACTED_NAME]"))
        decision = ctx.session.state.get("decision", "AUTO_REJECT")
        score = ctx.session.state.get("composite_score", 0.0)
        credit_score = ctx.session.state.get("financial_profile", {}).get("credit_score", 600) if ctx.session.state.get("financial_profile") else 600
        dti = ctx.session.state.get("calculated_dti", 0.0)
        reasons = ctx.session.state.get("fraud_reasons", [])
        
        letter = generate_ecoa_letter(name, decision, score, credit_score, dti, reasons)
        
        yield Event(
            output={"eco_letter": letter},
            state={"explanation_result": {"eco_letter": letter}}
        )
    else:
        return

# Override LlmAgent.run_async globally at class level
LlmAgent.run_async = mock_llm_agent_run_async

@pytest.fixture(autouse=True)
def mock_llm_agents():
    # Model client initialization mock to bypass API key verification checks
    import google.genai
    with patch("google.genai.Client") as mock_client:
        yield
