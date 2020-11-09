#build graph with departure city as key and (destination, ticket_id) as value
#G = build_graph()
#itinerary = ['JFK']
#ticket_used = set()
#dfs()
    #if len(itinerary)==len(tickets)+1: return True
    #here = itinerary[-1]
    #if here not in G: return False
    #candidates = nei, ticket_id for nei, ticket_id in G[here] if ticket_id not in ticket_used
    #for nei, ticket_id in candidates:
        #ticket_used.add(ticket_id)
        #itinerary.append(nei)
        #if dfs(): return True
        #ticket_used.remove(ticket_id)
        #itinerary.pop()
    #return False

import collections

class Solution(object):
    def findItinerary(self, tickets):
        def dfs():
            if len(itinerary)==len(tickets)+1: return True
            here = itinerary[-1]
            if here not in G: return False

            candidates = [(nei, ticket_id) for nei, ticket_id in G[here] if ticket_id not in ticket_used]
            
            for nei, ticket_id in candidates:
                ticket_used.add(ticket_id)
                itinerary.append(nei)
                if dfs(): return True
                ticket_used.remove(ticket_id)
                itinerary.pop()
            return False

        G = collections.defaultdict(list)
        itinerary = ['JFK']
        ticket_used = set()

        #build graph
        ticket_id_counter = 0
        for n1, n2 in tickets:
            G[n1].append((n2, ticket_id_counter))
            ticket_id_counter += 1
        for k in G: G[k].sort(key=lambda x:x[0])
        
        return dfs()