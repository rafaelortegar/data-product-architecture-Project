import luigi

from luigi import WrapperTask
from loadWrapper import loadWrapper
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
        yield metadataTestCleaned(date =self.date, bucket = self.bucket)
        yield metadataCleaned(date =self.date, bucket = self.bucket)
        yield loadWrapper(date =self.date, bucket = self.bucket)


if __name__ == '__main__':
    luigi.cleanWrapper()

