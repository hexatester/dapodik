from dataclasses import dataclass
from dapodik.base import BaseData


@dataclass
class SekolahPaud(BaseData):
    sekolah_id: str
    kategori_tk_id: str
    klasifikasi_lembaga_id: str
    sumber_dana_sekolah_id: str
    fasilitas_layanan_id: str
    jadwal_pmtas: str
    lembaga_pengangkat_id: str
    jadwal_ddtk: str
    freq_parenting: str
    bentuk_lembaga_id: str
    jadwal_kesehatan: str
    izin_paud: str
    pencatatan_ddtk: str
    rujukan_ddtk: str
    pelaksanaan_parenting: str
    parenting_kpo: str
    parenting_kelas: str
    parenting_kegiatan: str
    parenting_konsultasi: str
    parenting_kunjungan: str
    parenting_lainnya: str
    nilk: str
    nilm: str
    no_penetapan_pnf: str
    tanggal_penetapan_pnf: str
    create_date: str
    last_update: str
    soft_delete: str
    last_sync: str
    updater_id: str