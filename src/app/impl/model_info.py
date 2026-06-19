from enum import Enum


# ==============================================================================
class ModelClassification(Enum):
    CLASS       = "class"
    INTERFACE   = "interface"
    ENUM        = "enum"


# ==============================================================================
class ModelInfo:
    def __init__(self,
                 model_name: str,
                 model_type: str,
                 model_namespaces: list[str],
                 model_include_guard: str
                 ):
        self._name: str                             = model_name
        self._classification: ModelClassification   = ModelClassification(model_type)
        self._namespaces: list[str]                 = model_namespaces
        self._include_guard: str                    = model_include_guard

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def classification(self) -> ModelClassification:
        return self._classification
    
    @property
    def namespaces(self) -> list[str]:
        return self._namespaces
    
    @property
    def include_guard(self) -> str:
        return self._include_guard
