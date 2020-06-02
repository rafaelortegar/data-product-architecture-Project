import luigi

from luigi import WrapperTask
from cleanWrapper import cleanWrapper
from metadataFeatureEngineering import metadataFeatureEngineering
from metadataTestFeatureEng import metadataTestFeatureEng


class featureEngineeringWrapper(luigi.WrapperTask):
    
    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'Feature_Engineering_Wrapper_task_05_01'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================

    
    def requires(self):
        yield metadataTestFeatureEng(date =self.date, bucket = self.bucket)
        yield metadataFeatureEngineering(date =self.date, bucket = self.bucket)
        yield cleanWrapper(date =self.date, bucket = self.bucket)
