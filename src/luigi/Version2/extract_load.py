import luigi

from luigi import WrapperTask
#from copyToPostgres import copyToPostgres
from metadataExtract import metadataExtract
from metadataTestExtract import metadataTestExtract
#from metadataLoad import metadataLoad


class extractLoadSection(luigi.WrapperTask):
    
    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'extract_section_task_03_01'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================

    
    def requires(self):
        yield metadataExtract(date =self.date, bucket = self.bucket)
        yield metadataTestExtract(date =self.date, bucket = self.bucket)

if __name__ == '__main__':
    luigi.extractLoadSection()


