import os
import datetime
import json
import marbles.core
import pandas as pd


#directorio = '/home/alfie-gonzalez/Documentos/Maestría/Segundo Semestre/Métodos de Gran Escala'
#os.chdir(directorio)
#file = 'afluencia-diaria-del-metro-cdmx.json'
#json_file = open(file, 'rb')
#class ExtractTestCase(marbles.core.TestCase):
#    def __init__(self):
#        pass
#    def featurize(self, X):
 
class ExtractTestCase(marbles.core.TestCase):
        def setUp(self):
                self.json_file = json_file   # ... #json_file

        #def __init__(self):
        #        self.json_file
        
        def tearDown(self):
                delattr(self, 'json_file')
        
        def test_extract(self):
                
#                with self.json_file.open('r') as json_file:
                #data = json.load(self.json_file)
                data = self.json_file
                columns_read = data['nhits']
                print("-----------------------imprimiendo columnsread")
                print(columns_read)
                self.assertTrue(columns_read != 0 , note = 'json file is empty')
                now = datetime.datetime.now()
                passfail=columns_read != 0
                nombreprueba='test load datos raw'
                print (now.strftime("%Y-%m-%d %H:%M:%S"))
                #return nombreprueba
                
                
                #como estaba antes de cambiarlo
                #self.assertTrue(self.json_file.read2 != '[]', note = 'json file is empty')
                #now = datetime.datetime.now()
                #passfail=self.json_file.read(2) != '[]'
                #nombreprueba='test load datos raw'
                #print (now.strftime("%Y-%m-%d %H:%M:%S"))
                #return nombreprueba
                
                data_a_cargar = {'prueba':[nombreprueba], 'estatus':[passfail], 'hora_ejecucion':[now]}
                df1 = pd.DataFrame(data = data_a_cargar)
                #print(df1)
                return df1

if __name__ == '__main__':
    marbles.core.main()