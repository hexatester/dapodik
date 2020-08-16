from dataclasses import dataclass
from typing import Optional
from dapodik.base import BaseData


@dataclass
class KebutuhanKhusus(BaseData):
    kebutuhan_khusus_id: int
    kebutuhan_khusus: str
    kk_a: str
    kk_b: str
    kk_c: str
    kk_c1: str
    kk_d: str
    kk_d1: str
    kk_e: str
    kk_f: str
    kk_h: str
    kk_i: str
    kk_j: str
    kk_k: str
    kk_n: str
    kk_o: str
    kk_p: str
    kk_q: str
    untuk_lembaga: str
    untuk_ptk: str
    untuk_pd: str
    create_date: str
    last_update: str
    expired_date: Optional[str]
    last_sync: str
