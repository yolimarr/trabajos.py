class Carro():
    def desplazamiento (self): #cada codigo tiene una diferente implementacion
        print("me dezplazo usando cuatro ruedas")
        
class Moto():
    def desplazamiento (self):
            print("me desplazo en dos ruedas")
            
class camion():
    def desplazamiento (self):
            print("me desplazo en seis ruedas") 
                    
def desplazamientoVehiculo (vehiculo):
        vehiculo.desplazamiento()
           
miVehiculo=Carro()
desplazamientoVehiculo (miVehiculo)
                
                    
                    
                    
                    
