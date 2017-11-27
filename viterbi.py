import numpy as np
class Viterbi:
    def __init__(self, initial, states, obs, possible_obs, trans, emiss):
        self.initial = initial
        self.states = states
        self.obs = obs
        self.possible_obs = possible_obs
        self.trans = trans
        self.emiss = emiss
        self.num_states = len(self.states)
        self.num_obs = len(self.obs)
        self.table = np.zeros((self.num_states, self.num_obs))

    def get_obs_num(self, obs):
        for i, ob in enumerate(self.possible_obs):
            if obs is ob:
                return i

    def run(self):
        path = []
        #set the initial values to the start of the table
        for st in range(self.num_states):
            self.table[st][0] = self.initial[st]
        #find the value for each state at each time
        for ob in range(self.num_obs):
            prob = []
            for st1 in range(self.num_states):
                for st2 in range(self.num_states):
                    p = self.table[ob][st1] * self.trans[ob][st2] * self.emiss[0][self.get_obs_num(self.obs[ob])]
                    prob.append(p)
                print(prob)
        print(prob)

    def print_table(self):
        print(self.table)

if __name__ == "__main__":
    states = ["Balanced", "Loaded_Heads", "Loaded_Tails"]
    obs = ["Tails", "Tails", "Heads", "Heads", "Tails"]
    possible_obs = ["Heads", "Tails"]
    initial = [0.333, 0.333, 0.333]
    #   trans matrix follows the following pattern:
    #       [[balanced->balanced, loaded_heads->balanced, loaded_tails->balanced],
    #       [balanced->loaded_heads, loaded_heads->loaded_heads, loaded_tails->loaded_heads],
    #       [balanced->loaded_tails, loaded_heads->loaded_tails, loaded_tails->loaded_tails]]
    trans = [[0.45, 0.52, 0.25], [0.35, 0.3, 0.13], [0.2, 0.18, 0.62]]
    #   emiss matrix follows the following pattern:
    #   [[balanced->heads, balanced->tails], [loaded_heads->heads, loaded_heads->tails] ...]
    emiss = [[0.5, 0.5], [0.85, 0.15], [0.1, 0.9]]
    v = Viterbi(initial, states, obs, possible_obs, trans, emiss)
    v.run()
    v.print_table()
