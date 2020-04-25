# ------------------------------------------------- ----- 
# ---------------------- main.py ------------------- ---- 
# --------------------------------------------- --------- 
from  PyQt5.QtWidgets  import * 
from  PyQt5.uic  import  loadUi 

from  matplotlib.backends.backend_qt5agg  import  ( NavigationToolbar2QT  as  NavigationToolbar ) 

import  numpy  as  np 
import  random 
     
class  MatplotlibWidget ( QMainWindow ): 
    
    def  __init__ ( self ) :
        
        QMainWindow . __init__ ( self ) 
        loadUi ( "/media/ghannam/728BA8B6158029C6/DESK_DRAWER/ projects/ZLabs/ball_and_beam/ball_and_beam/codes/gui_python/untitled.ui" , self ) #load the ui we designed in qtdesigne to start modifing it's functionality
        self . setWindowTitle ( "PyQt5 & Matplotlib Example GUI" )  
        self . pushButton1 . clicked . connect ( self . update_graph ) 



    def  update_graph( self ): 

        fs  =  500 
        f  =  random . randint ( 1 ,  100 ) 
        ts  =  1 / fs 
        length_of_signal  =  100 
        t  =  np . linspace ( 0 , 1 , length_of_signal ) 
        
        cosinus_signal  =  np . cos ( 2 * np . pi * f * t ) 
        sinus_signal  = np . sin ( 2 * np . pi * f * t ) 

        self . MplWidget . canvas . axes . clear () 
        self . MplWidget . canvas . axes . plot ( t ,  cosinus_signal ) 
        self . MplWidget . canvas . axes . plot ( t ,  sinus_signal ) 
        self .MplWidget . canvas . axes . legend (( 'cosinus' ,  'sinus' ), loc = 'upper right' ) 
        self . MplWidget . canvas . axes . set_title ( ' Cosinus - Sinus Signal' ) 
        self . MplWidget . canvas . draw () 
        

app  =  QApplication ([]) 
window  =  MatplotlibWidget () 
window . show () 
app. exec_ ()