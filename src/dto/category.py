from datetime import datetime
from typing import Optional
from pydantic import Field, field_validator, ValidationError

from src.dto import PollResponseDTO
from src.dto.base import (
    BaseDTO,
    IdDTOMixin,
    TimestampDTOMixin
)

class CategoryRequestDTO(BaseDTO):
    name: str = Field(
        min_length=2,
        max_length=100
    )

class CategoryResponseDTO(CategoryRequestDTO, IdDTOMixin):
    pass





