
#communication variables ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
import serial
import time
import numpy as np

recieve_tag = 666
recieved_var1=0
recieved_var2=0
recieved_var3=0

send_tag = 555
send_var_1 = 0
send_var_2 = 0
send_var_3 = 0

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()
#communication variables eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

#communication functions SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
def update_recieved_variables(ser):
    global recieved_var1
    global recieved_var2
    global recieved_var3
    # print(ser.in_waiting)
    if(ser.in_waiting >0):

        try:
            input_string = ser.readline().decode("ASCII")
            word = input_string[:-1]
            # print(word)
            input_array =(word.split(','))
            x = np.array(input_array)
            float_array=x.astype(np.float)
            tag=int(float_array[0])
            
            if(tag==recieve_tag and float_array.size==4):
                recieved_var1=float_array[1]
                recieved_var2=float_array[2]
                recieved_var3=float_array[3]
        except:
            pass


def send_send_variables(ser):
        string = str(send_tag ) +"," +str(send_var_1) + "," +str(send_var_2) + "," + str(send_var_3) +"\n"
        # print(string)
        message = bytes(string, 'utf-8')
        ser.write(message)
        time.sleep(.01) #without this the recieved values keeps fluctuating
#communication functions eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

##GUI variables SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
import os
from  PyQt5.QtWidgets  import * 
from  PyQt5.uic  import  loadUi 
from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar ) 
import  numpy  as  np 
import  random 
     

##GUI variables eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee





class  MatplotlibWidget ( QMainWindow ): 
    def  __init__ ( self ) :
        QMainWindow . __init__ ( self ) 
        loadUi ( os.path.dirname(os.path.realpath(__file__))+"/"+"untitled.ui" , self ) #load the ui we designed in qtdesigne to start modifing it's functionality
        self . setWindowTitle ( "PyQt5 & Matplotlib Example GUI" )  
        self . pushButton1 . clicked . connect ( self . start_graphing ) 

        self . X=np.array([x for x in range(1000)] )
        self . Y=np.array([1.0 for x in range(1000)] )


    def start_graphing(self):
        # set timer to update graph every .001 second
        self._timer_ = self.MplWidget .canvas.new_timer(.001, [(self.update_graph, (), {})])
        self._timer_.start()
    def  update_graph( self ): 

            update_recieved_variables(ser)
            
            self .Y = np.append(self .Y,recieved_var1)
            self .Y = np.delete(self .Y,0)
            self .X = np.append(self .X,recieved_var2)
            self .X = np.delete(self .X,0)
            self . MplWidget . canvas . axes . clear () 
            self . MplWidget . canvas . axes . plot ( self.X , self.Y ) 
            self . MplWidget . canvas . axes.set_xlabel("foo")
            self . MplWidget . canvas . axes.set_ylabel("foo")
            self . MplWidget . canvas . draw () 



# ------------------------------------------------- ----- 
# ---------------------- main.py ------------------- ---- 
# --------------------------------------------- --------- 

app  =  QApplication ([]) 
window  =  MatplotlibWidget () 
window . show () 
app. exec_ ()