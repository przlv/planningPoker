from pydantic import BaseModel, ConfigDict, field_serializer


class ModelConfig(BaseModel):
    """
    Базовый конфиг для моделей pydantic
    """

    model_config = ConfigDict(populate_by_name=True)
