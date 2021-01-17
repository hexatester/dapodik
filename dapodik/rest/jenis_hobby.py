from datetime import datetime
from typing import Optional

from dapodik.base import dataclass


@dataclass(frozen=True, slots=True)
class JenisHobby:
    id_hobby: int
    nm_hobby: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
