class stateManager:
    def __init__(self, state:str):
        self.__state = state
    
    def set_state(self, state:str):
        self.__state = state
    
    def get_state(self):
        return self.__state