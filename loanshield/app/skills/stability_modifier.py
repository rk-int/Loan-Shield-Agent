from typing import Dict, Any

def stability_modifier_skill(tenure_months: int) -> Dict[str, Any]:
    """Calculates the employment stability modifier based on job tenure.

    Args:
        tenure_months: The applicant's tenure at their current job in months.

    Returns:
        A dictionary containing the stability modifier.
    """
    if tenure_months < 6:
        modifier = 0.85
    elif tenure_months <= 24:
        modifier = 1.00
    else:
        modifier = 1.05
        
    return {
        "stability_modifier": modifier
    }
