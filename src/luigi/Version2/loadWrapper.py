import luigi

from extract_load import extractLoadSection
from metadataLoad import metadataLoad
from metadataTestLoad import metadataTestLoad

class loadWrapper(luigi.WrapperTask):
    """
    Function to load metadata from the extracting process from mexico city metro data set on the specified date. It
    uploads the data into the specified S3 bucket on AWS. Note: user MUST have the credentials to use the aws s3
    bucket.
    """
    
    #==============================================================================================================
    # Parameters
    #==============================================================================================================
    task_name='loadWrapper_task'
    date = luigi.Parameter()
    bucket = luigi.Parameter(default='dpaprojs3')
    #==============================================================================================================

    def requires(self):
        yield extractLoadSection(bucket=self.bucket, date=self.date)
        yield metadataLoad(bucket=self.bucket, date=self.date)
        yield metadataTestLoad(bucket=self.bucket, date=self.date)


if __name__ == '__main__':
    luigi.loadWrapper()


#




