from astropy.io import ascii
import numpy as np
from astropy.table import join, unique

class UnclusteredSuite:
    def setup(self):
        self.table = ascii.read('benchmarks/table/files/unclustered.txt')
        self.table2 = ascii.read('benchmarks/table/files/unclustered2.txt')
        self.groups = {}
        for name in ('str', 'int', 'float'):
            self.groups[name] = self.table.group_by(name)
    def time_group_str(self):
        self.table.group_by('str')
    def time_group_int(self):
        self.table.group_by('int')
    def time_group_float(self):
        self.table.group_by('float')
    def time_slice_str(self):
        self.groups['str'][0:-1]
    def time_slice_int(self):
        self.groups['int'][0:-1]
    def time_slice_float(self):
        self.groups['float'][0:-1]
    def time_mask_str(self):
        mask = self.groups['str'].groups.keys['str'] >= 'mm'
        self.groups['str'].groups[mask]
    def time_mask_int(self):
        mask = self.groups['int'].groups.keys['int'] >= 0
        self.groups['int'].groups[mask]
    def time_mask_float(self):
        mask = self.groups['float'].groups.keys['float'] >= 0.
        self.groups['float'].groups[mask]
    def time_aggregate(self):
        self.groups['str'].groups.aggregate(np.mean)
    def time_join(self):
        join(self.table, self.table2)
    def time_unique_str(self):
        unique(self.table, keys='str')
    def time_unique_int(self):
        unique(self.table, keys='int')
    def time_unique_float(self):
        unique(self.table, keys='float')

