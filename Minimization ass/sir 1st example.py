"""Example 1 DFA Minimization

Original States: {A, B, C, D, E}
Minimized States: {[AB], [CD], [E]}
"""


class OriginalDFA1:
    """Original 5-State DFA from Example 1."""

    def __init__(self):
        self.start_state = "A"
        self.accept_states = {"E"}
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
                raise ValueError(f"Invalid symbol '{char}' in binary string.")
            current_state = self.transitions[current_state][char]
            path.append(current_state)
        return (current_state in self.accept_states), path


class MinimizedDFA1:
    """Minimized 3-State DFA from Example 1."""

    def __init__(self):
        self.start_state = "AB"
        self.accept_states = {"E"}
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
                raise ValueError(f"Invalid symbol '{char}' in binary string.")
            current_state = self.transitions[current_state][char]
            path.append(current_state)
        return (current_state in self.accept_states), path


if __name__ == "__main__":
    dfa_orig = OriginalDFA1()
    dfa_min = MinimizedDFA1()

    print("=== EXAMPLE 1 DFA MINIMIZATION ===")
    print("Enter binary strings (0s and 1s) to test. Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter input string: ").strip()

        if user_input.lower() in ("exit", "quit"):
            print("Exiting program.")
            break

        try:
            res_orig, path_orig = dfa_orig.process(user_input)
            res_min, path_min = dfa_min.process(user_input)

            status = "Accepted" if res_min else "Rejected"
            print(f"Result             : {status}")
            print(f"Original DFA path  : {' -> '.join(path_orig)}")
            print(f"Minimized DFA path : {' -> '.join(path_min)}\n")
        except ValueError as e:
            print(f"Error: {e}\n")