import attr
from datetime import datetime
from typing import Optional
from dapodik import DapodikObject
from dapodik.utils.decorator import set_meta


@set_meta("id_hapus_buku")
@attr.s(auto_attribs=True, eq=False, frozen=True)
class JenisHapusBuku(DapodikObject):
    id_hapus_buku: str
    ket_hapus_buku: str
    u_prasarana: str
    u_sarana: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
