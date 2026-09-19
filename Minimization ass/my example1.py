"""Beverly Nicole S. Ompog - Automata Example 1

Exact Transition Table from Paper:
State | 0 | 1
--------------
-> A  | B | C
   B  | B | D
   C  | E | C
   D  | E | C
  *E  | E | E
"""


class OriginalDFA1:

    def __init__(self):
        self.start_state = "A"
        self.accept_states = {"E"}
        # Exact table from handwritten sheet
        self.transitions = {
            "A": {"0": "B", "1": "C"},
            "B": {"0": "B", "1": "D"},
            "C": {"0": "E", "1": "C"},
            "D": {"0": "E", "1": "C"},
            "E": {"0": "E", "1": "E"},
        }

    def process(self, input_str: str) -> tuple[bool, list[str]]:
        current_state = self.start_state
        path = [current_state]
        for char in input_str:
            if char not in ("0", "1"):
                raise ValueError(f"Invalid symbol '{char}'")
            current_state = self.transitions[current_state][char]
            path.append(current_state)
        return (current_state in self.accept_states), path


class MinimizedDFA1:

    def __init__(self):
        self.start_state = "AB"
        self.accept_states = {"E"}
        # Minimized table based on {AB}, {CD}, {E}
        self.transitions = {
            "AB": {"0": "AB", "1": "CD"},
            "CD": {"0": "E", "1": "CD"},
            "E": {"0": "E", "1": "E"},
        }

    def process(self, input_str: str) -> tuple[bool, list[str]]:
        current_state = self.start_state
        path = [current_state]
        for char in input_str:
            if char not in ("0", "1"):
                raise ValueError(f"Invalid symbol '{char}'")
            current_state = self.transitions[current_state][char]
            path.append(current_state)
        return (current_state in self.accept_states), path


if __name__ == "__main__":
    dfa_orig = OriginalDFA1()
    dfa_min = MinimizedDFA1()

    print("==========================================")
    print("      AUTOMATA: EXAMPLE 1 MINIMIZATION    ")
    print("==========================================")
    print("Type binary strings to test. Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter input string: ").strip()

        if user_input.lower() in ("exit", "quit"):
            print("Program terminated.")
            break

        if not user_input:
            continue

        try:
            res_orig, path_orig = dfa_orig.process(user_input)
            res_min, path_min = dfa_min.process(user_input)

            status = "Accepted ✓" if res_min else "Rejected ✗"

            print(f"Result             : {status}")
            print(f"Original DFA path  : {' -> '.join(path_orig)}")
            print(f"Minimized DFA path : {' -> '.join(path_min)}")
            print("-" * 42 + "\n")
        except ValueError as e:
            print(f"Error: {e}\n")