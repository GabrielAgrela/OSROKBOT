from Actions.action import Action

class ConditionalAction(Action):
    def __init__(self, primary_actions, primary_subsequent_actions, alternative_subsequent_actions, retry_times=0, skip_check_first_time=False):
        super().__init__(skip_check_first_time)
        self.primary_actions = primary_actions
        self.primary_subsequent_actions = primary_subsequent_actions or []
        self.alternative_subsequent_actions = alternative_subsequent_actions or []
        self.retry_times = retry_times

    def execute(self):
        for _ in range(self.retry_times + 1):  # the +1 allows for the first run + retry_times
            for action in self.primary_actions:
                if action.execute():
                    for subsequent_action in self.primary_subsequent_actions:
                        if not subsequent_action.execute():
                            return False  # handle failure of subsequent action
                    return True

            for action in self.alternative_subsequent_actions:
                if not action.execute():
                    return False  # handle failure of subsequent action
        return False  # if we've exhausted retries and still failed, return False
