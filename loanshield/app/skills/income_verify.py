from typing import Dict, Any

def income_verify_skill(
    declared_income_monthly: float,
    average_monthly_deposits: float
) -> Dict[str, Any]:
    """Computes income variance and flags anomalies.

    Args:
        declared_income_monthly: The monthly income declared by the applicant.
        average_monthly_deposits: The average monthly deposits from bank statements.

    Returns:
        A dictionary containing verified income, variance percentage, and anomaly flag.
    """
    # Verified income is the average monthly deposits (ground truth)
    verified_income = average_monthly_deposits if average_monthly_deposits > 0 else 1.0
    
    # Calculate variance percentage
    variance_pct = (abs(declared_income_monthly - verified_income) / verified_income) * 100.0
    
    # Anomaly flags if declared income is more than 2x verified income
    # (i.e. declared_income_monthly > 2 * verified_income, which is variance > 100% and declared > verified)
    income_anomaly = declared_income_monthly > (2.0 * verified_income)
    
    return {
        "verified_income": average_monthly_deposits,
        "income_variance_pct": variance_pct,
        "income_anomaly": income_anomaly
    }
