def email_addresses(first: list, last: list, domain: str = '@exeter.ac.uk') -> list:
    """ This function takes two list arguments first and last , and a string argument 
    domain that has a default value of @exeter.ac.uk. The function then returns a list of 
    suggested email addesses with the email addresses in the format of the first letter 
    of the name in first followed by a full stop followed by the whole of the corresponding name 
    from last, followed by the domain"""

    suggested_emails = []

    # Here error checking is handled
    if type(first) != list or type(last) != list or type(domain) != str or domain[0] != '@':
        print('One or more parameters have been passed incorrectly. Firstly parse two lists then parse a string beginning with a @ sign')
        return None
    elif len(first) > len(last) or len(last) > len(first):
        print('Please make sure each list has a corresponding first and last name')
        return None

    for index in range(len(first)):
        # a string called new email is formed by concatenating the nesscary parts together
        new_email = first[index][0].lower()+'.'+last[index].lower()+domain
        suggested_emails.append(new_email)

    return suggested_emails
