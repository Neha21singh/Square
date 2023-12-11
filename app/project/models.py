import uuid
from datetime import date
from typing import Optional, Dict
from pydantic import BaseModel, Field, Json

class AnyJson(BaseModel):
    data: Dict

class Project(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    SECTORS: str = Field(...)
    BLOCKS: str  = Field(...)
    ADDRESS: str = Field(...)
    PLOTSINMT:str = Field(...)
    TAINSQFT: str = Field(...)
    A_PER_FLOOR: str = Field(...)
    FLOOR: str = Field(...)
    CONT_PERSON: str = Field(...)
    CONT_NO : str = Field(...)
    AVAILABLE_AREA_IN_SQ_FT: str = Field(...)
    DEMAND: str = Field(...)
    SALE_RENT_SU: str = Field(...)
    TYPE: str = Field(...)
    AVAILABLE_OR_NOT: str = Field(...)
    DATE: str = Field(...)
    REMARK: str = Field(...)

class ProjectUpdate(BaseModel):
    SECTORS: Optional[str]
    BLOCKS: Optional[str]
    ADDRESS: Optional[str]
    PLOTSINMT: Optional[str]
    TAINSQFT: Optional[str]
    A_PER_FLOOR: Optional[str]
    FLOOR: Optional[str]
    CONT_PERSON: Optional[str]
    CONT_NO : Optional[str]
    AVAILABLE_AREA_IN_SQ_FT: Optional[str]
    DEMAND: Optional[str]
    SALE_RENT_SU: Optional[str]
    TYPE: Optional[str]
    AVAILABLE_OR_NOT: Optional[str]
    DATE: Optional[str]
    REMARK: Optional[str]
