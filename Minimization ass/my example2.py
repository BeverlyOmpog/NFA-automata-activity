"""Beverly Nicole S. Ompog - Automata Example 2

Original States: {A, B, C, D, F}
Minimized States: {[A], [B], [CF], [D]}
"""


class OriginalDFA2:
    """Original DFA for Example 2 (with corrected clean B transitions)."""

    def __init__(self):
        self.start_state = "A"
        self.accept_states = {"D"}
        self.transitions = {
            "A": {"0": "B", "1": "C"},
            "B": {"0": "B", "1": "D"},
            "C": {"0": "F", "1": "C"},
            "D": {"0": "D", "1": "D"},
            "F": {"0": "F", "1": "F"},
        }

    def process(self, input_str: str) -> tuple[bool, list[str]]:
        current_state = self.start_state
        path = [current_state]
        for char in input_str:
            if char not in ("0", "1"):
                raise ValueError(f"Invalid symbol '{char}' in binary string.")
            current_state = self.transitions[current_state][char]
            path.append(current_state)
        return (current_state in self.accept_states), path


class MinimizedDFA2:
    """Minimized DFA for Example 2."""

    def __init__(self):
        self.start_state = "A"
        self.accept_states = {"D"}
        self.transitions = {
            "A": {"0": "B", "1": "CF"},
            "B": {"0": "CF", "1": "D"},
            "CF": {"0": "CF", "1": "CF"},
            "D": {"0": "D", "1": "D"},
        }

    def process(self, input_str: str) -> tuple[bool, list[str]]:
        current_state = self.start_state
        path = [current_state]
        for char in input_str:
            if char not in ("0", "1"):
                raise ValueError(f"Invalid symbol '{char}' in binary string.")
            current_state = self.transitions[current_state][char]
            path.append(current_state)
        return (current_state in self.accept_states), path


if __name__ == "__main__":
    dfa_orig = OriginalDFA2()
    dfa_min = MinimizedDFA2()

    print("=== BEVERLY'S EXAMPLE 2 DFA MINIMIZATION ===")
    print("Enter binary strings (0s and 1s) to test. Type 'exit' to stop.\n")

    while True:
        user_input = input("Enter input string: ").strip()

        if user_input.lower() in ("exit", "quit"):
            print("Exiting program.")
            break

        try:
            res_orig, path_orig = dfa_orig.process(user_input)
            res_min, path_min = dfa_min.process(user_input)

            status = "Accepted ✓" if res_min else "Rejected ✗"
            print(f"Result             : {status}")
            print(f"Original DFA path  : {' -> '.join(path_orig)}")
            print(f"Minimized DFA path : {' -> '.join(path_min)}\n")
        except ValueError as e:
            print(f"Error: {e}\n")