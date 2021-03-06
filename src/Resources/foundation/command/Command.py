from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def run(self, current_path, argv):
        raise NotImplementedError("You must implement `run` method.")
