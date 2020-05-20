import luigi

from luigi import WrapperTask
from loadCleaned import loadCleaned
from metadataCleaned import metadataCleaned
from metadataTestCleaned import metadataTestCleaned


class cleanWrapper(luigi.WrapperTask):
    
    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'cleanWrapper_task_04_01'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================

    
    def requires(self):
        yield loadCleaned(date =self.date, bucket = self.bucket)
        yield metadataCleaned(date =self.date, bucket = self.bucet)
        yield metadataTestCleaned(date =self.date, bucket = self.bucet)


if __name__ == '__main__':
    luigi.cleanWrapper()

