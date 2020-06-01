import luigi

from luigi import WrapperTask
from cleanWrapper import cleanWrapper
from metadataFeatureengineering import metadataFeatureengineering
from testFeatureEngineering import testFeatureEngineering


class featureEngineeringWrapper(luigi.WrapperTask):
    
    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'Feature_Engineering_Wrapper_task_04_01'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================

    
    def requires(self):
        yield cleanWrapper(date =self.date, bucket = self.bucket)
        yield metadataFeatureengineering(date =self.date, bucket = self.bucket)
        yield testFeatureEngineering(date =self.date, bucket = self.bucket)
