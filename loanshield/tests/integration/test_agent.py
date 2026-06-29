import json
from google.adk.agents.run_config import RunConfig, StreamingMode
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from app.agent import root_agent

def test_agent_stream() -> None:
    session_service = InMemorySessionService()
    session = session_service.create_session_sync(user_id="test_user", app_name="test")
    runner = Runner(agent=root_agent, session_service=session_service, app_name="test")

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

    message = types.Content(
        role="user", parts=[types.Part.from_text(text=json.dumps(payload))]
    )

    events = list(
        runner.run(
            new_message=message,
            user_id="test_user",
            session_id=session.id,
            run_config=RunConfig(streaming_mode=StreamingMode.SSE),
        )
    )
    assert len(events) > 0, "Expected at least one message"
