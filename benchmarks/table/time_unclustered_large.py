class UnclusteredLargeSuite(TableSuite):
    def setup(self):
        self.table = ascii.read('benchmarks/table/files/large/unclustered.txt')
        self.table2 = ascii.read('benchmarks/table/files/large/unclustered2.txt')
        self.form_groups()
