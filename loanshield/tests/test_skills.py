import pytest
from app.skills.pii_redactor import pii_redactor_skill
from app.skills.income_verify import income_verify_skill
from app.skills.dti_calculator import dti_calculator_skill
from app.skills.stability_modifier import stability_modifier_skill
from app.skills.risk_scoring import risk_scoring_skill
from app.skills.fraud_detection import fraud_detection_skill

def test_pii_redactor():
    res = pii_redactor_skill(
        name="Liam Smith",
        ssn="960-24-6191",
        dob="01-05-1976",
        phone_number="-7853",
        home_address="566 Oak Ave, Los Angeles, CA 47194"
    )
    assert res["redacted_name"] == "[REDACTED_NAME]"
    assert res["redacted_ssn"] == "[REDACTED_SSN]"
    assert res["redacted_dob"] == "[REDACTED_DOB]"
    assert res["redacted_phone_number"] == "[REDACTED_PHONE]"
    assert res["redacted_home_address"] == "[REDACTED_ADDRESS]"

def test_income_verify():
    # Test normal case
    res1 = income_verify_skill(declared_income_monthly=10000.0, average_monthly_deposits=9000.0)
    assert not res1["income_anomaly"]
    assert res1["income_variance_pct"] == pytest.approx(11.111, 0.01)
    
    # Test mismatch anomaly
    res2 = income_verify_skill(declared_income_monthly=25000.0, average_monthly_deposits=10000.0)
    assert res2["income_anomaly"]

def test_dti_calculator():
    res1 = dti_calculator_skill(monthly_debt_obligations=3000.0, verified_income=10000.0)
    assert res1["calculated_dti"] == 0.30
    assert res1["dti_component"] == 100.0
    
    res2 = dti_calculator_skill(monthly_debt_obligations=4000.0, verified_income=10000.0)
    assert res2["calculated_dti"] == 0.40
    assert res2["dti_component"] == 60.0

def test_stability_modifier():
    assert stability_modifier_skill(5)["stability_modifier"] == 0.85
    assert stability_modifier_skill(12)["stability_modifier"] == 1.00
    assert stability_modifier_skill(36)["stability_modifier"] == 1.05

def test_risk_scoring():
    # Prime applicant scoring test
    res = risk_scoring_skill(
        credit_score=750,
        delinquencies=0,
        dti_component=100.0,
        current_balance=20000.0,
        loan_amount=5000.0,
        average_monthly_deposits=10000.0,
        average_monthly_withdrawals=6000.0,
        stability_modifier=1.05
    )
    # Credit base: (750-300)/550 * 100 = 81.81. Delinquencies: 0. Credit component = 81.81.
    # DTI component: 100
    # Current balance 20000 >= 2 * 5000 (10000) -> Savings buffer = 50.
    # Deposits 10000 > withdrawals 6000 -> Burn rate = 50.
    # Cash flow component = 100.
    # Base: 81.81 * 0.40 + 100 * 0.30 + 100 * 0.30 = 32.72 + 30 + 30 = 92.72.
    # Final adjusted: min(100.0, 92.72 * 1.05) = 97.36
    assert res["composite_score"] == pytest.approx(97.36, 0.05)

def test_fraud_detection():
    # Underage check
    r1 = fraud_detection_skill(
        age=19, loan_amount=120000.0, credit_history_length_months=12,
        credit_score=700, employment_status="Active", declared_income_monthly=5000.0, verified_income=5000.0
    )
    assert r1["fraud_flag"]
    
    # Synthetic credit age check
    r2 = fraud_detection_skill(
        age=25, loan_amount=20000.0, credit_history_length_months=4,
        credit_score=790, employment_status="Active", declared_income_monthly=5000.0, verified_income=5000.0
    )
    assert r2["fraud_flag"]
    
    # Terminated check
    r3 = fraud_detection_skill(
        age=30, loan_amount=20000.0, credit_history_length_months=48,
        credit_score=700, employment_status="Terminated", declared_income_monthly=5000.0, verified_income=5000.0
    )
    assert r3["fraud_flag"]
