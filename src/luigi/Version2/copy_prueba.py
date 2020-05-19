from luigi.contrib.postgres import CopyToTable

#import pandas as pd
import luigi
import psycopg2

class Task2(CopyToTable):
    x = luigi.IntParameter()

    user = 'postgres'
    password = 'jvg1991'
    database = 'dpa'
    host = '127.0.0.1'
    table = 'raw.prueba'

    columns = [("x", "VARCHAR"),
               ("y", "VARCHAR")]

    def rows(self):
        z = str(self.x + self.x)
        print("########### ", z)
        r = [("test 1", z), ("test 2","45")]
        for element in r:
            yield element


class Task1(luigi.Task):
    x = luigi.IntParameter()
    y = luigi.IntParameter(default=45)

    def requires(self):
        return Task2(self.x)

    def run(self):
        z = str(self.x + self.y)
        print("******* ", z)
        with self.output().open('w') as output_file:
            output_file.write(z)

    def output(self):
        return luigi.local_target.LocalTarget('~/pruebacopy.txt')
