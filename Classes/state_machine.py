class StateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, name, state, next_state_on_success=None, next_state_on_failure=None):
        self.states[name] = (state, next_state_on_success, next_state_on_failure)

    def set_initial_state(self, name):
        self.current_state = name

    def execute(self):
        if self.current_state is None:
            raise Exception("Initial state is not set")

        current_state_info = self.states[self.current_state]

        # Try to execute the current state
        state = current_state_info[0]
        result = state.perform()

        # If the action executes successfully, move to the next state
        if result:
            next_state_on_success = current_state_info[1]
            # Check if next_state_on_success is a function, and call it if it is
            if callable(next_state_on_success):
                self.current_state = next_state_on_success()
            else:
                self.current_state = next_state_on_success
        else:
            self.current_state = current_state_info[2]

        return result

