import os
import datetime
import json
import marbles.core
import pandas as pd

directorio = '/home/alfie-gonzalez/Documentos/Maestría/Segundo Semestre/Métodos de Gran Escala'
os.chdir(directorio)

file = 'afluencia-diaria-del-metro-cdmx.json'
json_file = open(file, 'rb')

class ExtractTestCase(marbles.core.TestCase):
    def setUp(self):
        self.json_file = json_file
    
    def test_extract(self):
        self.assertTrue(self.json_file.read(2) != '[]', 
                        note = 'json file is empty')
        now = datetime.datetime.now()
        passfail=self.json_file.read(2) != '[]'
        nombreprueba='test ingesta datos raw'
        passfail=self.json_file.read(2) != '[]'
        nombreprueba='test load datos raw'
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        df = pd.DataFrame([nombreprueba, passfail,nombreprueba])
        return 
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        df = pd.DataFra        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        df = pd.DataFrame([nombreprueba, passfail,])
        return 
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        df = pd.Dat
        return 
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
    



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
    



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
    



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
    



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
    



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
    



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
    



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
    



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 

        return 

        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return         
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 






        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 





        passfail=self.json_file.read(2) != '[]'
        nombre
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        
        passfail=self.json_file.read(2) != '[]'
        pas
        
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        df = pd.DataFrame({'prueba':nombreprueba, 'estatus':passfail, 'hora_ejecucion':now})
        return 

, 



        return 

        return 

        return 

        return 

        return 

        return 

        return 
asdasdasf
        return 
asdasdadasdasdasdasdafsadfafdasdfasdfa
if __name__ == '__main__':
    marbles.core.main()


ssss