import pandas as pd
import numpy as np
from typing import Dict

class MesinRekomendasi:
    def __init__(self, pengolah_data):
        self.df = pengolah_data.muat_data()
        self._praproses_data()
        
    def _praproses_data(self):
        self.scaler = {}
        for kolom in ['lingkar_dada', 'lebar_pundak', 'lingkar_perut', 'panjang_body']:
            self.scaler[kolom] = {
                'rata_rata': self.df[kolom].mean(),
                'std': self.df[kolom].std()
            }
            self.df[kolom+'_norm'] = (self.df[kolom] - self.scaler[kolom]['rata_rata']) / self.scaler[kolom]['std']

    def _normalisasi_input(self, input_data: Dict[str, float]):
        return {
            kolom + '_norm': (input_data[kolom] - self.scaler[kolom]['rata_rata']) / self.scaler[kolom]['std']
            for kolom in self.scaler.keys()
        }

    def cari_ukuran(self, data_input: Dict[str, float]) -> str:
        def hitung_jarak(row):
            return sum(abs(row[kolom] - data_input[kolom]) for kolom in ['lingkar_dada', 'lebar_pundak', 'lingkar_perut', 'panjang_body'])
    
        self.df['jarak'] = self.df.apply(hitung_jarak, axis=1)
        ukuran_terbaik = self.df.loc[self.df['jarak'].idxmin(), 'ukuran']
        return ukuran_terbaik