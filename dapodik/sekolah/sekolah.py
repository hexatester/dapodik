from dataclasses import dataclass
from dapodik.base import BaseData


@dataclass
class Sekolah(BaseData):
    sekolah_id: str
    nama: str
    nama_nomenklatur: str
    nss: str
    npsn: str
    bentuk_pendidikan_id: int
    alamat_jalan: str
    rt: str
    rw: str
    nama_dusun: str
    desa_kelurahan: str
    kode_wilayah: str
    kode_pos: str
    lintang: str
    bujur: str
    nomor_telepon: str
    nomor_fax: str
    email: str
    website: str
    kebutuhan_khusus_id: int
    status_sekolah: str
    sk_pendirian_sekolah: str
    tanggal_sk_pendirian: str
    status_kepemilikan_id: str
    yayasan_id: str
    sk_izin_operasional: str
    tanggal_sk_izin_operasional: str
    no_rekening: str
    nama_bank: str
    cabang_kcp_unit: str
    rekening_atas_nama: str
    mbs: str
    luas_tanah_milik: str
    luas_tanah_bukan_milik: str
    kode_registrasi: str
    npwp: str
    nm_wp: str
    keaktifan: str
    flag: str
    create_date: str
    last_update: str
    soft_delete: str
    last_sync: str
    updater_id: str
    bentuk_pendidikan_id_str: str
    kode_wilayah_str: str
    kebutuhan_khusus_id_str: str
    yayasan_id_str: str
    vld_count: int