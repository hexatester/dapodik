from typing import List, Union
from typing_extensions import Literal
from uuid import UUID

from dapodik import __semester__
from dapodik.base import BaseDapodik, Message
from dapodik.rest import TingkatPendidikan
from . import (
    AnggotaRombel,
    Pembelajaran,
    RombonganBelajar,
)

__fetch__ = (
    AnggotaRombel,
    Pembelajaran,
    RombonganBelajar,
)


class BaseRombonganBelajar(BaseDapodik):
    __all__ = __fetch__

    def anggota_rombel(
        self,
        rombongan_belajar_id: Union[UUID, str],
        page: int = 1,
        start: int = 0,
        limit: Union[int, Literal["unlimited"]] = 25,
    ) -> List[AnggotaRombel]:
        url = "allanggotarombel/" + str(rombongan_belajar_id)
        res = self._get_rest(
            url, page=page, start=start, limit=limit, prefix="customrest/"
        )
        data: dict = res.json()
        return self._fl(AnggotaRombel, data.get("rows"))

    def pembelajaran(self) -> List[Pembelajaran]:
        res = self._get_rest("Pembelajaran")
        data: dict = res.json()
        return self._fl(Pembelajaran, data.get("rows"))

    def rombongan_belajar(
        self,
        sekolah_id: str,
        semester_id: str = __semester__,
        ascending: str = "#INjenis_rombel,tingkat_pendidikan_id,nama",
        callback: str = "rombonganbelajar",
        jenis_rombel: str = "#IN1,5,6,7,8,9,10",
        sks=0,
        limit: Union[int, Literal["unlimited"]] = "unlimited",
        page: int = 1,
        start: int = 0,
    ) -> List[RombonganBelajar]:
        params = {
            "sekolah_id": sekolah_id,
            "semester_id": semester_id,
            "ascending": ascending,
            "callback": callback,
            "jenis_rombel": jenis_rombel,
            "sks": sks,
        }
        res = self._get_rest("RombonganBelajar", params, page, start, limit)
        data: dict = res.json()
        return self._fr(RombonganBelajar, data)

    def kenaikan_kelas(
        self, rombongan_belajar_id: Union[UUID, str], semester_id: str = __semester__
    ) -> Message:
        """kenaikan_kelas rombongan belajar

        Args:
            rombongan_belajar_id (Union[UUID, str]): ID dari rombongan belajar
            semester_id (str, optional): Naikkan ke semester. Defaults dapodik.__semester__.

        Returns:
            Message: Pesan sukses / tidak
        """
        data = dict(
            rombongan_belajar_id=rombongan_belajar_id,
            semester_id=semester_id,
        )
        res = self._post("kenaikankelas", data)
        return self._msg(res.json())

    def filter_tingkat_pendidikan(
        self,
        fromui: str = None,
        callback: str = "rombonganbelajar",
        jurusan_id: str = None,
        page: int = 1,
        start: int = 0,
        limit: int = 50,
    ) -> List[TingkatPendidikan]:
        """filter_tingkat_pendidikan [summary]

        Args:
            fromui (str, optional): Misal tingkatpendidikanpaud. Defaults "".
            callback (str, optional): callback. Defaults "rombonganbelajar".
            jurusan_id (str, optional): id jurusan. Defaults "".
            page (int, optional): halaman. Defaults 1.
            start (int, optional): mulai. Defaults 0.
            limit (int, optional): batas. Defaults 50.

        Returns:
            List[TingkatPendidikan]: list dari TingkatPendidikan
        """
        params = {
            "callback": callback,
            "jurusan_id": jurusan_id or "",
            "fromui": fromui or "",
            "page": page,
            "start": start,
            "limit": limit,
        }
        res = self._get("filtertingkatpendidikan", params)
        return self._fr(TingkatPendidikan, res.json())