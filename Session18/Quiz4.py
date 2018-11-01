#Quiz 4
#Connie Li & Siddhanth Goyal

ELECTORS = {'CA': 55, 'TX': 38, 'FL': 29, 'MA': 11}

class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=[], votes=0):
        """Initialize candidate.
        name: string
        winning_states: a list of strings representing initial winning state(s).
        votes: integer, representing number of votes
        """
        self.name = name
        self.winning_states = winning_states
        self.votes = votes
        #This self initializes, empty list (contents will be nothing, because set to empty)

    def __str__(self):
        """Return a string representaion of this candidate,
        including name and winning state(s).
        """
        return '{} won these states: {},.'.format(self.name, self.winning_states)
        #just removed total votes here because the quiz doesn't ask for it

    def win_state(self, state):
        """Adds a tate to winning_states and updates votes.
        state: a string of state abbreviation
        """
        self.winning_states.append(state)
        self.votes += ELECTORS.get(state,0)
        
    #Also needed an overload function because the last lines won't work
    def __gt__(self,other):
        return self.votes > other.votes 
    
def main():
    trump = Candidate('Donald Trump')
    clinton = Candidate('Hillary Clinton', winning_states=['CA']) 
    print(trump)
    print(clinton)
    print()
    print('After election:')
    trump.win_state('FL')
    trump.win_state('TX')
    clinton.win_state('MA')
    print(trump)
    print(clinton)
    print('Does Trump win?')
    print(trump > clinton)

if __name__ == '__main__':
    main()