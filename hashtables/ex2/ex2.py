#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    routes_dict = {}    
    routes_list = []
    for ticket in tickets:
        routes_dict[ticket.source] = ticket.destination

    routes_list.append(routes_dict["NONE"])
    for destination in routes_list:
        if routes_dict[destination] == "NONE":
            routes_list.append("NONE")
            break
        else:
            routes_list.append(routes_dict[destination])

    return routes_list
