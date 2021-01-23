access_log = [
    " 19.69.248.2 mmc2 [12/12/2018] ‘ GET / m / ’ 200 4263 ",
    " 19.69.248.2 mmc2 [12/12/2018] ‘ GET / m / index . php ’ 200 4494 ",
    " 46.72.177.4 gr4 [12/12/2018] ‘ GET / video / v . php ’ 200 4263 "]


def monthly_users(year: int) -> list:
    """This function takes in a parameter called year and returns a list 
    containing the number of unique IP addresses for each month of the given
    year"""
    if type(year) != int:  # Here error checking is handled
        print('Please parse an integer to the function')
        return None
    global access_log
    user_frequency = [0 for x in range(12)]
    valid_entries = []
    dates = []
    for entry in access_log:  # Here the code gets entries which are from the year parsed
        if str(year) in entry:
            valid_entries.append(entry)
    for entry in valid_entries:  # Here the code puts all the dates of entries into a list
        holder = entry.split()
        date = holder[2]
        dates.append(date)
    for date in dates:  # Here the code finds the month in the date and adds 1 user to its corresponding month in the user frequency list
        month = int(date[4:6])
        user_frequency[month-1] += 1
    return user_frequency


def annual_user_count(year: int) -> int:
    """This function counts the annual users that a site gets in a 
    year determined by the year parameter """
    if type(year) != int:  # Here error checking is handled
        print('Please parse an integer to the function')
        return None
    global access_log
    valid_entries = []
    users = []
    for entry in access_log:  # Here the code gets entries which are from the year parsed
        if str(year) in entry:
            valid_entries.append(entry)
    for entry in valid_entries:  # Here the code check if a user is in the users list if not then it adds the user to the users list if the user is already in the users list nothing happens
        holder = entry.split()
        user = holder[1]
        if user not in users:
            users.append(user)
        else:
            pass
    return len(users)


def annual_user_download_average(year: int) -> int:
    """This function claculates the average data download of users of the 
    course of a year determined by the value parsed in the year parameter"""
    if type(year) != int:  # Here error checking is handled
        print('Please parse an integer to the function')
        return None
    global access_log
    valid_entries = []
    total_data = []
    for entry in access_log:  # Here the code gets entries which are from the year parsed
        if str(year) in entry:
            valid_entries.append(entry)
    for entry in valid_entries:  # Here the code puts all the data size entries into a list
        holder = entry.split()
        data = int(holder[-1])
        total_data.append(data)
    # Here the mean average of data for the year is returned
    return sum(total_data)/len(total_data)
