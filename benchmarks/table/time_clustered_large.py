class ClusteredLargeSuite(TableSuite):
    def setup(self):
        self.table = ascii.read('benchmarks/table/files/large/clustered.txt')
        self.table2 = ascii.read('benchmarks/table/files/large/clustered2.txt')
        self.form_groups()
