from typing import Dict, Any, List

def fraud_detection_skill(
    age: int,
    loan_amount: float,
    credit_history_length_months: int,
    credit_score: int,
    employment_status: str,
    declared_income_monthly: float,
    verified_income: float
) -> Dict[str, Any]:
    """Applies strict deterministic compliance and fraud checks.

    Args:
        age: The applicant's age.
        loan_amount: The requested loan amount.
        credit_history_length_months: The credit history length in months.
        credit_score: The credit score.
        employment_status: The employment status (e.g. Active, Terminated).
        declared_income_monthly: Stated monthly income.
        verified_income: Verified bank deposits monthly average.

    Returns:
        A dictionary with fraud_flag and reasons.
    """
    fraud_flag = False
    reasons = []
    
    # 1. Underage High Value Loan check
    if age < 21 and loan_amount > 100000.0:
        fraud_flag = True
        reasons.append(f"Age under 21 ({age}) with loan amount exceeding $100,000 (${loan_amount:,.2f})")
        
    # 2. Synthetic Identity Anomaly check
    if credit_history_length_months < 6 and credit_score > 780:
        fraud_flag = True
        reasons.append(f"Synthetic identity anomaly: Short credit history ({credit_history_length_months} months) with high credit score ({credit_score})")
        
    # 3. Employment Termination check
    if employment_status.lower() == "terminated":
        fraud_flag = True
        reasons.append("Employment status is Terminated")
        
    # 4. Stated Income Mismatch check
    if declared_income_monthly > (2.0 * verified_income):
        fraud_flag = True
        reasons.append(f"Income mismatch: Declared income (${declared_income_monthly:,.2f}) is more than 2x verified deposits (${verified_income:,.2f})")
        
    return {
        "fraud_flag": fraud_flag,
        "fraud_reasons": reasons
    }
