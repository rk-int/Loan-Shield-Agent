from typing import Dict, Any

def risk_scoring_skill(
    credit_score: int,
    delinquencies: int,
    dti_component: float,
    current_balance: float,
    loan_amount: float,
    average_monthly_deposits: float,
    average_monthly_withdrawals: float,
    stability_modifier: float
) -> Dict[str, Any]:
    """Calculates all component scores and final risk-adjusted composite score.

    Args:
        credit_score: The FICO credit score.
        delinquencies: The number of historical delinquencies.
        dti_component: The DTI component score (0-100).
        current_balance: The current bank account balance.
        loan_amount: The requested loan amount.
        average_monthly_deposits: The average monthly deposits.
        average_monthly_withdrawals: The average monthly withdrawals.
        stability_modifier: The employment stability modifier multiplier.

    Returns:
        A dictionary with component scores and the final composite score.
    """
    # 1. Credit Component (40% Weight)
    credit_base = ((credit_score - 300.0) / 550.0) * 100.0
    credit_component = max(0.0, credit_base - (20.0 * delinquencies))
    credit_component = min(100.0, credit_component)
    
    # 2. Cash Flow Component (30% Weight)
    # Savings Buffer
    if current_balance >= (2.0 * loan_amount):
        savings_buffer = 50.0
    else:
        if loan_amount > 0:
            savings_buffer = (current_balance / (2.0 * loan_amount)) * 50.0
        else:
            savings_buffer = 50.0
    savings_buffer = max(0.0, min(50.0, savings_buffer))
            
    # Burn Rate
    if average_monthly_deposits > average_monthly_withdrawals:
        burn_rate = 50.0
    else:
        burn_rate = 0.0
        
    cash_flow_component = savings_buffer + burn_rate
    
    # 3. Base Score
    base_score = (credit_component * 0.40) + (dti_component * 0.30) + (cash_flow_component * 0.30)
    
    # 4. Final Risk-Adjusted Score
    composite_score = min(100.0, base_score * stability_modifier)
    composite_score = max(0.0, composite_score)
    
    return {
        "credit_score_component": credit_component,
        "cash_flow_component": cash_flow_component,
        "composite_score": composite_score
    }
