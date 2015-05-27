class UnclusteredSuite(TableSuite):
    def setup(self):
        self.table = ascii.read('benchmarks/table/files/unclustered.txt')
        self.table2 = ascii.read('benchmarks/table/files/unclustered2.txt')
        self.form_groups()
