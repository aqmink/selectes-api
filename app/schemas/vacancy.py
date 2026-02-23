from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class VacancyBase(BaseModel):
    title: str
    timetable_mode_name: str
    tag_name: str
    city_name: Optional[str] = None
    published_at: datetime
    is_remote_available: bool
    is_hot: bool
    # external_id: Optional[int] = None     | Ошибка при большом external_id (большим 2^32)
    ### Начало фикса ###                                                     #
    external_id: Optional[int] = Field(le=(2 ** 31) - 1, ge=0, default=None) # 
    ### Конец фикса ###                                                      #


class VacancyCreate(VacancyBase):
    pass


class VacancyUpdate(VacancyBase):
    pass


class VacancyRead(VacancyBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
