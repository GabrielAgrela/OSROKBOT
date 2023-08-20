class GlobalVars:
    _instance = None
    UI=None
    def __new__(cls, UI_INSTANCE=None):
        if cls._instance is None:
            cls._instance = super(GlobalVars, cls).__new__(cls)
            cls._instance.UI_INSTANCE = UI_INSTANCE
            print(cls._instance.UI_INSTANCE)
        return cls._instance

# Usage
GLOBAL_VARS = GlobalVars("Your UI Instance")
another_instance = GlobalVars()  # Will return the same instance as GLOBAL_VARS

# Both references point to the same object
assert GLOBAL_VARS is another_instance
