from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class Agama(BaseData):
    agama_id: int
    nama: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
