import pytest
from app.mcp_server import get_document_status, get_credit_profile, get_banking_profile, get_employment_profile, send_notification

def test_mcp_doc_status():
    # Test CU-001 (COMPLETE)
    res1 = get_document_status("CU-001")
    assert res1["document_vault_status"] == "COMPLETE"
    
    # Test CU-047 (INCOMPLETE)
    res2 = get_document_status("CU-047")
    assert res2["document_vault_status"] == "INCOMPLETE"
    assert "Government_ID" in res2["missing_requirements"]

def test_mcp_credit_profile():
    res = get_credit_profile("CU-001")
    assert res["credit_score"] == 742
    assert res["delinquencies"] == 0
    assert res["monthly_debt_obligations"] == 1269.0

def test_mcp_banking_profile():
    res = get_banking_profile("CU-001")
    assert res["average_monthly_deposits"] == 11171.0
    assert res["current_balance"] == 17433.0

def test_mcp_employment_profile():
    res = get_employment_profile("CU-001")
    assert res["employer_name"] == "Enterprise Corp"
    assert res["employment_status"] == "Active"
    assert res["tenure_months"] == 99

def test_mcp_send_notification():
    res = send_notification("CU-001", "AUTO_APPROVE", "Congratulations!")
    assert res["status"] == "success"
    assert res["delivered"]
