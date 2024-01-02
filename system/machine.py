class Machine():
    def __init__(self, states, transitions):
        self.states = states
        self.transitions = transitions  
    
    def run(self, input):
        tape = input + '_'
        state = ('Start', input[0])
        pos = 0
        arr = []
        while 1:
            next_state = self.transitions[state]
            arr.append([tape, pos])
            if next_state == 'Reject' or next_state == 'Accept':
                arr.append(next_state)
                break
            
            new_tape = ''
            for i in range(len(tape)):
                if i == pos:
                    new_tape = new_tape + next_state[1]
                else:
                    new_tape = new_tape + tape[i]
            tape = new_tape
            if (next_state[2] == 'R'):
                pos += 1
            else:
                pos -= 1
            state = (next_state[0], tape[pos])
        return arr


#----------symbol-----------
symbol = []
for i in range(33, 127):
    if i == 92 or i == 95:
        continue
    symbol.append(chr(i))
#---------------------------
def have_sym(p):
    return 'Have' + symbol[p]
def match_sym(p):
    return 'Match' + symbol[p]
# States 
states = ['Start', 'Back']
for i in range(len(symbol)):
    states.append(have_sym(i))
    states.append(match_sym(i))


#Transitions
transitions = {}
#-------Transition: Start ------------
for i in range(len(symbol)):
    x1 = ('Start', symbol[i])
    x2 = (have_sym(i), '_', 'R')
    transitions[x1] = x2
    #print(x1, x2)
transitions[('Start', '_')] = 'Accept'
#--------Transition: Back --------------
for i in range(len(symbol)):
    x1 = ('Back', symbol[i])
    x2 = ('Back', symbol[i], 'L')
    transitions[x1] = x2
transitions[('Back', '_')] = ('Start', '_', 'R')
#---------Transition: Have (a, b, ..., z)
for i in range(len(symbol)):
    transitions[(have_sym(i), '_')] = (match_sym(i), '_', 'L')
    for j in range(len(symbol)):
        x1 = (have_sym(i), symbol[j])
        x2 = (have_sym(i), symbol[j], 'R')
        transitions[x1] = x2
#---------Transition: Match (a, b, ..., z)
for i in range(len(symbol)):
    for j in range(len(symbol)):
        if (i == j):
            x1 = (match_sym(i), symbol[j])
            x2 = ('Back', '_', 'L')
            transitions[x1] = x2
        else:
            x1 = (match_sym(i), symbol[j])
            x2 = 'Reject'
            transitions[x1] = x2
    transitions[(match_sym(i), '_')] = "Accept"

Turing = Machine(states, transitions)
