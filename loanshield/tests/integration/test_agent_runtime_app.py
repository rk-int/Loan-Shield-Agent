import json
import pytest
from google.adk.events.event import Event
from app.agent_runtime_app import AgentEngineApp

@pytest.fixture
def agent_app(monkeypatch: pytest.MonkeyPatch) -> AgentEngineApp:
    monkeypatch.setenv("INTEGRATION_TEST", "TRUE")
    from app.agent_runtime_app import agent_runtime
    agent_runtime.set_up()
    return agent_runtime

@pytest.mark.asyncio
async def test_agent_stream_query(agent_app: AgentEngineApp) -> None:
    payload = {
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

    events = []
    async for event in agent_app.async_stream_query(message=json.dumps(payload), user_id="test"):
        events.append(event)
    assert len(events) > 0, "Expected at least one chunk in response"

def test_agent_feedback(agent_app: AgentEngineApp) -> None:
    feedback_data = {
        "score": 5,
        "text": "Great response!",
        "user_id": "test-user-456",
        "session_id": "test-session-456",
    }
    agent_app.register_feedback(feedback_data)

    with pytest.raises(ValueError):
        invalid_feedback = {
            "score": "invalid",
            "text": "Bad feedback",
            "user_id": "test-user-789",
            "session_id": "test-session-789",
        }
        agent_app.register_feedback(invalid_feedback)
