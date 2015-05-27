class ClusteredSuite(TableSuite):
    def setup(self):
        self.table = ascii.read('benchmarks/table/files/clustered.txt')
        self.table2 = ascii.read('benchmarks/table/files/clustered2.txt')
        self.form_groups()
