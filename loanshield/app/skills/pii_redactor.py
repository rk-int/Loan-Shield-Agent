import re
from typing import Dict, Any

def pii_redactor_skill(
    name: str, 
    ssn: str, 
    dob: str, 
    phone_number: str, 
    home_address: str
) -> Dict[str, str]:
    """Redacts PII (Name, SSN, DOB, Phone, Address) from the application input.

    Args:
        name: The applicant's name.
        ssn: The applicant's Social Security Number.
        dob: The applicant's Date of Birth.
        phone_number: The applicant's phone number.
        home_address: The applicant's home address.

    Returns:
        A dictionary containing the redacted fields.
    """
    # Masks name
    redacted_name = "[REDACTED_NAME]"
    
    # Masks SSN: match standard \d{3}-\d{2}-\d{4} or similar
    if re.match(r"^\d{3}-\d{2}-\d{4}$", ssn.strip()):
        redacted_ssn = "[REDACTED_SSN]"
    else:
        redacted_ssn = "[REDACTED_SSN_INVALID_FORMAT]"
        
    # Masks DOB: match standard dates like DD-MM-YYYY or YYYY-MM-DD
    if re.match(r"^\d{2}-\d{2}-\d{4}$", dob.strip()) or re.match(r"^\d{4}-\d{2}-\d{2}$", dob.strip()):
        redacted_dob = "[REDACTED_DOB]"
    else:
        redacted_dob = "[REDACTED_DOB_INVALID_FORMAT]"
        
    # Masks phone number: matches negative integers or formatted phone numbers
    redacted_phone_number = "[REDACTED_PHONE]"
    
    # Masks home address
    redacted_home_address = "[REDACTED_ADDRESS]"
    
    return {
        "redacted_name": redacted_name,
        "redacted_ssn": redacted_ssn,
        "redacted_dob": redacted_dob,
        "redacted_phone_number": redacted_phone_number,
        "redacted_home_address": redacted_home_address
    }
