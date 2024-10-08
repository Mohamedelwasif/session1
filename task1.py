def validate_and_process_email(email):
    # Input Validation
    if email.count('@') != 1 or email.rfind('.') < email.find('@') + 1:
        return "Invalid email"
    
    # Extract Username
    username = email.split('@')[0]
    
    # Extract Domain
    domain_part = email.split('@')[1]
    domain = domain_part[:domain_part.rfind('.')]
    
    # Check for Domain Ending
    if email.endswith('.com'):
        domain_type = "Commercial Domain"
    elif email.endswith('.edu'):
        domain_type = "Educational Domain"
    else:
        domain_type = "Other Domain"
    
    return username, domain, domain_type

# Example usage
email = "Amit_ml@gmail.edu"
result = validate_and_process_email(email)

if result == "Invalid email":
    print(result)
else:
    username, domain, domain_type = result
    print("Username:", username)
    print("Domain:", domain)
    print("Domain Type:", domain_type)
