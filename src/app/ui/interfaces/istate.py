from abc import ABC, abstractmethod

from app.ui.common import ApplicationState


class IState(ABC):

    @abstractmethod
    def set_state(self, newState: ApplicationState) -> None:...

# IState
