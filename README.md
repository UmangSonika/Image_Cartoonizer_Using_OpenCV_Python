# Image_Cartoonizer_Using_OpenCV_Python
Make your own Image Cartoonizer filter using the very powerful library OpenCV in python. It is just a matter of some filters that will generate something amazing out of normal.  
         
The method that i have used to convert any image into its cartoon version is pretty straight forward.         
 I will take and image and then apply smoothening filters such as gaussian blurr and then i will do adaptive thresolding to find the edges in the image.      
 At last i wil merge the edged image with the original one using bitwise and operator.               
                                    
                                    
PREREQUISITES:  
1.Basic Knowledge of Python syntax.  
2.Basic Knowledge of various filters in openCV.   
3.Image processing using OpenCV.       
4.Basic knowledge of how to handle command line arguements using Argparse in Python.       
                                    
                                                          
                                    
This code is made to run from command line arguements.                                                                         
But you can easily change the code and then you can give the image location directly in the code instead of using command line.   
                             
              
 You might have to install couple of libraries first.
                                 
I will tell you how you can install those libraries in window. If you are a linux or mac user you can search how to pip intall and library name of google to find instructions...                      
                                                   
 1.OpenCv : Type pip install opencv-python in cmd.                          
 2.matplotlib : Type pip install matplotlib in cmd.                               
 3.argparse : Type pip install argparse in cmd.
                                                    
                                                                      
Steps to run the code:                           
                                          
1.Download the source code and save it on Desktop.                    
                                                                             
2.Open the cmd terminal and using cd command change the directory to Desktop.            
                     
3.Now type the following command ---   python Image_Cartoon.py --image (location_of_image)          
  In the brackets you will have to give the absolute path to the image if it is not on desktop.                
  If the image is on desktop itself then just type the image name instead of that bracket.                         
                                                                                                          
Note:: Don't forget to include the (.JPG or .png) extension in the image name or else it will cause error.                  

