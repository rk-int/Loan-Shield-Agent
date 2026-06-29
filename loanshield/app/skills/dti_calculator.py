from typing import Dict, Any

def dti_calculator_skill(
    monthly_debt_obligations: float,
    verified_income: float
) -> Dict[str, Any]:
    """Calculates the Debt-to-Income (DTI) ratio and its corresponding component score.

    Args:
        monthly_debt_obligations: The applicant's monthly debt payments.
        verified_income: The bank-verified income (average monthly deposits).

    Returns:
        A dictionary with calculated_dti and the DTI component score.
    """
    if verified_income <= 0:
        dti = 999.0  # high penalty
    else:
        dti = monthly_debt_obligations / verified_income
        
    # Scoring assignment
    if dti <= 0.30:
        dti_component = 100.0
    elif dti <= 0.45:
        dti_component = 60.0
    elif dti <= 0.55:
        dti_component = 30.0
    else:
        dti_component = 0.0
        
    return {
        "calculated_dti": dti,
        "dti_component": dti_component
    }
