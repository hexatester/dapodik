from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta('waktu_penyelenggaraan_id')
@dataclass(eq=False, frozen=True)
class WaktuPenyelenggaraan(DapodikObject):
    waktu_penyelenggaraan_id: str
    nama: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
