def vat(pretax_price: float, kids: bool = False, category: str = 'miscellaneous') -> float:
    """ This function calculates the total price of a purchase by having the arguments
    pretax_price, category and kids passed in. If the category is clothing and kids is 
    true then there should be no vat tax added to the price"""
    if type(pretax_price) != float or type(category) != str or type(kids) != bool:  # Here error checking is handled
        print('One or more of the parameters passed is not valid. Please enter the following types in the following order: float,string and boolean')
        return None
    elif category == 'clothing' and kids == True:
        return pretax_price
    else:
        # adds 20% of pretax price to final price rounded to 2 decimal places
        return round(pretax_price*1.20, 2)
