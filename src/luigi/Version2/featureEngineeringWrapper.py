import luigi

from luigi import WrapperTask
from featureEngineering import featureEngineering
from metadataFeatureengineering import metadataFeatureengineering


class featureEngineeringWrapper(luigi.WrapperTask):
    
    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name = 'Feature_Engineering_Wrapper_task_04_01'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================

    
    def requires(self):
        yield featureEngineering(date =self.date, bucket = self.bucket)
        yield metadataFeatureengineering(date =self.date, bucket = self.bucket)
