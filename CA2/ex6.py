
queue=[]
def arrival(name: str) -> list:
    """Takes in a name argument and add it to the queue"""
    if type(name) != str:  # Here error checking is handled
        print('This is not a string please try again')
        return None
    # This line inserts a person into the end of a queue
    queue.insert(0, name)
    print(queue)


def next_patient(position: int = None) -> str:
    """This function takes in a position argument if none gets parsed then the 
    function returns the next person in the queue if a position is parsed then the 
    function then the person at that position is returned"""
    if position != None:
        next = queue[-position]
        queue.remove(next)  # Here the person at position is returned
        return next
    else:
        # Here the first person in queue is removed and stored in the value of next
        next = queue[-1]
        queue.remove(next)
        return next

arrival('pierre')
arrival('loot')