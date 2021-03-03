import cv2 as cv
import numpy as np

"""
------------------------------------------------------------------------------
CUSTOM ERROR CLASSES
------------------------------------------------------------------------------
"""
    
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class FunctionNameExistsError(Error):
    """Raised when attempt made to create a function with a non-unique name"""
    def __init__(self,message):
        self.message = message
        
class KernelNameExistsError(Error):
    """Raised when attempt made to create a kernel with a non-unique name"""
    def __init__(self,message):
        self.message = message
        
class KernalNotFoundError(Error):
    """Raised when attempt made to use an undefined kernel name"""
    def __init__(self,message):
        self.message = message
        
class FunctionNotFoundError(Error):
    """Raised when attempt made to use an undefined function name"""
    def __init__(self,message):
        self.message = message

"""
------------------------------------------------------------------------------
MAIN MODULE CLASSES
------------------------------------------------------------------------------
"""

class glomCV:
    
    """
    --------------------------------------------------------------------------
    CLASS SETUP METHODS
    --------------------------------------------------------------------------
    """
    
    def __init__(self,image):
        self.img = image
        self.imgShape = np.shape(image)
        self.funcDict = dict()
        self.kernelDict = dict()
        
    def ___str___(self):
        pass
    
    def __repr__(self):
        pass
    
    """
    --------------------------------------------------------------------------
    GENERAL METHODS
    --------------------------------------------------------------------------
    """    
        
    def minCalc(self,col,fac):
        """Determines a lower bound scaled between col and 0 by fac"""
        return col*fac/100
        
    def maxCalc(self,col,fac):
        """Determines an upper bound scaled between col and 255 by fac"""
        return col + (255 - col)*(100 - fac)/100
    
    def lowBound(self,r,g,b,fac):
        """Generates lower bound RGB tuple, outputs (B,G,R)"""
        b_min = self.minCalc(b,fac)
        g_min = self.minCalc(g,fac)
        r_min = self.minCalc(r,fac)
        
        return (b_min,g_min,r_min)
    
    def highBound(self,r,g,b,fac):
        """Generates upper bound RGB tuple, outputs (B,G,R)"""
        b_max = self.maxCalc(b,fac)
        g_max = self.maxCalc(g,fac)
        r_max = self.maxCalc(r,fac)
        
        return (b_max,g_max,r_max)
    
    
    """
    --------------------------------------------------------------------------
    FUNCTION ADDER METHODS
    --------------------------------------------------------------------------
    """
    
    def checkName(self,name):
        """Checks for function name uniqueness"""
        if str(name) in self.funcDict:
            raise FunctionNameExistsError(str(name)+" already exists")
        else:
            pass    
    
    def add_colThreshold(self,name,rgb=None,fac=None):
        """ Adds a colour thresholding layer to the output image"""
        
        self.checkName(self,name)
        self.funcDict[str(name)] = ("colThreshold",rgb,fac)
        
        cv.createTrackbar(str(name)+'red','trackbar', 0, 255, self.nothing)
        cv.createTrackbar(str(name)+'green','trackbar',0, 255,self.nothing)
        cv.createTrackbar(str(name)+'blue','trackbar', 0, 255,self.nothing)
        cv.createTrackbar(str(name)+'factor','trackbar',0,100,self.nothing)
        
    def add_kernel(self,name,x,y):
        """Defines a custom kernel"""
        
        if str(name) in self.kernelDict:
            raise KernelNameExistsError(str(name) + " already exists with shape " 
                                        + str(np.shape(self.kernelDict[str(name)])))
        else:
            self.kernelDict[str(name)] = np.ones((x,y),np.uint8)
    
    def add_Canny(self,name,threshold1 = None, Threshold2 = None):
        """ Adds a Canny edge detection layer to the output image"""
        self.checkName(self,name)
        pass
        
    """
    --------------------------------------------------------------------------
     CV FUNCTION METHODS
    --------------------------------------------------------------------------
    """     
            
    def colThreshold(self,lowBound,highBound):
        self.image()
        mask = cv.inRange(disp,lowBound,highBound)
        disp = cv.cvtColor(mask,cv.COLOR_GRAY2BGR)
        disp = disp & img.copy()

    """
    --------------------------------------------------------------------------
     CLASS MANIPULATION METHODS
    --------------------------------------------------------------------------
    """                 
    
    def listFunc(self):
        """Returns a list of function names in order of application to image"""
        return list(self.funcDict.keys())
    
    def listKernels(self):
        """Returns a list of kernel names"""
        return list(self.kernelDict.keys())
    
    def returnKernel(self,name):
        """Returns a specified kernel"""
        return self.kernelDict[str(name)]

    def returnKernelShape(self,name):
        """Returnsthe shape of a specified kernel"""
        return np.shape(self.kernelDict[str(name)])
        
    def removeFunc(self,name):
        """Remove specified function from function dictionary"""
        self.funcDict.pop(str(name))
        
    def removeKernel(self,name):
        """Remove specified kernel from kernel dictionary"""
        self.kernelDict.pop(str(name))
    
    def variableShow(self,window):
        """Displays image with changeable function variables"""
        cv.namedWindow(str(window))
        disp = self.image.copy()
        while(1):
            for iter in self.func:
                pass
            cv.imshow(str(window),disp)
            k = cv.waitKey(1) & 0xFF
            if k == 27:
                break
        cv.destroyAllWindows()
        
    def imageShow(self,window):
        """Displays image with predefined function variables"""
        cv.namedWindow(str(window))
        disp = self.image.copy()
        while(1):
            cv.imshow(str(window),disp)
            k = cv.waitKey(1) & 0xFF
            if k == 27:
                break
        cv.destroyAllWindows()
        





if __name__ == '__main__':
    pass


















