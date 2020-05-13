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
#df = pd.read_json(r'metro_2019-01-01.json',encoding='utf-8', orient='values', lines=True)
#df[nhits]


class ExtractTestCase(marbles.core.TestCase):
        def setUp(self):
                self.json_file = json_file   # ... #json_file
                self.json_file = pd_json
        #def __init__(self):
        #        self.json_file
        
        def tearDown(self):
                delattr(self, 'json_file')
        
        def test_extract(self):
                #df = pd.read_json(r'contenido.json',encoding='utf-8', orient='values', lines=True)
                #cuenta=df['nhits'][0]
                self.assertTrue(passfail=self.json_file.shape[0] != 0, note = 'json file is empty')
                now = datetime.datetime.now()
                #passfail=self.json_file.read(2) != ''
                passfail=self.json_file.shape[0] != 0
                nombreprueba='test load datos raw'
                print (now.strftime("%Y-%m-%d %H:%M:%S"))

                if passfail==True:
                        print("#############")
                        print("prueba exitosa")
                        print("#############")
                else:
                        print("#############")
                        print("prueba fallida")
                        print("#############")

                return print(passfail)
                #df1 = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
                #return df1.head()

#if(json.length<=0) 
#{
#   alert('empty') ;
#} 
#else 
#{
#   alert('not empty'); 
#}





if __name__ == '__main__':
    marbles.core.main()