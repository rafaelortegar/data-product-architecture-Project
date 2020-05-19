import luigi

from luigi import WrapperTask
from copyToPostgres import copyToPostgres
from metadataExtract import metadataExtract
from testExtract import testExtract
from metadataLoad import metadataLoad


class extractLoadSection(luigi.WrapperTask):
    
    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'extract_load_task_03_01'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================

    
    def requires(self):
        yield copyToPostgres(date =self.date, bucket = self.bucket)
        yield metadataExtract(date =self.date, bucket = self.bucket)
        yield metadataLoad(date =self.date, bucket = self.bucket)
        yield testExtract(date =self.date, bucket = self.bucket)

if __name__ == '__main__':
    luigi.extractLoadSection()


