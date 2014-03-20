import wx,os,re,copy
import cPickle as pickle
from collections import OrderedDict
import numpy as np

from classes import MassSpectrum
from imClasses import Im
import gui.guiFunctions as gf
from lib import utils
from AmphitriteEnums import *

class SaSettings():

    def __init__(self):

        # Atropos stuff
        self.atrOb = None
        self.species = []
        self.speciesCharges = OrderedDict()

        self.speciesSelected = None
        self.chargeSelected = None
        self.widthL = 1.0
        self.widthR = 1.0

        # Plotting
        self.plotPanel = None
        self.boundaryAlgorithm = SaBndAlg.MIN_MAX
        self.plotState = SaPlotState.MS_LINES

        self.loadedFiles = OrderedDict()
        self.imFilenames = []              # should be set by listctrlfiles
        
        self.txtFilenames = []
        self.loadedTxtFiles = OrderedDict()

        self.massSpectra = OrderedDict()
        self.msFitApplied = OrderedDict()
        
        self.showMsExtRange = True
        self.showLegend = True

        self.defaultDirectory = ''

    #====================
    # Adding other panel components
    def setListCtrlFiles(self,listCtrl):
        self.listCtrlFiles = listCtrl

    def setPlotPanel(self,plotPanel):
        self.plotPanel = plotPanel

    #====================

    def loadAtroposSpeciesAndCharges(self,path):
        self.atrOb = pickle.load(open(path,'rb'))

        # reset variables
        self.species = []
        self.speciesCharges = OrderedDict()
        
        for sp in sorted(self.atrOb.simulatedSpecies.keys()):
            self.species.append(sp)
            self.speciesCharges[sp] = self.atrOb.simulatedSpecies[sp].charges
        for k,v in self.msFitApplied:
            self.msFitApplied[k] = False

        self.setTxtFileAtropos()
        self.setImObsAtropos()

    def setImFilenames(self,filenames):
        self.imFilenames = filenames
        self.loadImData(filenames)
        
    def loadImData(self,filenames):
        # have already been checked by listctrl
        for fn in filenames:
            if not fn in self.loadedFiles.keys():
                print fn 
                imOb = Im.Im()
                imOb.loadFolderAuto(fn)              
                imOb.generateMassSpectrum()
                imOb.massSpectrum.normalisationBpi()
                basename = os.path.basename(fn)
                self.loadedFiles[basename] = imOb
                self.massSpectra[basename] = imOb.getMassSpectrum()
        self.setImObsAtropos()

    def setTxtFilenames(self,filenames):
        # added to self.txtFilenames by the above function
        toRemove = self.loadTxtData(filenames)

    def loadTxtData(self,filenames):
        toRemove = []
        print 'herhe'
        for fn in filenames:
            if not fn in self.loadedTxtFiles.keys():
                try:
                    msOb = MassSpectrum.MassSpectrum()
                    msOb.readFile(fn)
                    self.loadedTxtFiles[fn] = msOb
                    self.massSpectra[fn] = msOb
                    print 'Sucessfully Added: %s' %fn
                    # save the filename
                    self.txtFilenames.append(fn)
                    self.msFitApplied[fn] = False
                except:
                    toRemove.append(fn)
        if len(toRemove):
            if len(toRemove) == 1:
                message = 'Incorrect file format for: %s' %fn
            else:
                s = ['\n%s' %fn for fn in toRemove]
                s = ''.join(s)
                message = 'Incorrect file format for:'+s 
            gf.warningDialog(message)

        return toRemove

    def setTxtFileAtropos(self):
        for fn in self.self.loadedTxtFiles.keys():
            if not self.msFitApplied[fn]:
                self.setMsFit(fn)
                
    def setMsFit(self,fn):
        
        xvals = self.massSpectra[fn].xvals.copy()
        yvals = self.massSpectra[fn].yvals.copy()
        msOb = copy.deepcopy(self.atrOb)
        msOb.xvals = xvals
        msOb.yvals = yvals

        self.massSpectra[fn] = msOb
        
        
    def setImObsAtropos(self):
        if self.atrOb:
            for fn,imOb in self.loadedFiles.items():
                imOb.setMsFit(self.atrOb)
        
    def setWidthL(self,val):
        self.widthL = val
        if self.showMsExtRange:
            self.plotPanel.refresh_plot()
    def setWidthR(self,val):
        self.widthR = val
        if self.showMsExtRange:
            self.plotPanel.refresh_plot()
            
    def getMsXaxisYaxes(self):
        ##################################################
        # THIS FUNCTION COULD BE OPTIMISED
        # Interpolation shouldn't happen everytime
        # Perhaps save the processed data back into the objects
        ##################################################
        
        # Collect the data
        mzAxes,itsAxes = [],[]
        fns = self.massSpectra.keys()
        for msOb in self.massSpectra.values():
            msOb.normalisationBpi()
            mzAxes.append(msOb.xvals)
            itsAxes.append(msOb.yvals)
	# Interpolate axes if they don't match
        if len(mzAxes):
            lengths = [ len(axis) for axis in mzAxes ]
            if lengths.count(lengths[0]) != len(lengths):
                # If the x axis lengths don't match
                index = lengths.index(max(lengths))
                mzAxisOut = mzAxes[index]
                itsAxesOut = []
                for i in range(len(mzAxes)):
                    if not lengths[i] == max(lengths):
                        itsAxesOut.append(
                            np.interp(mzAxisOut,mzAxes[i],itsAxes[i]))
                    else:
                        itsAxesOut.append(itsAxes[i])
                return mzAxisOut,itsAxesOut,fns
            else:
                # If they match 
                return mzAxes[0],itsAxes,fns
        else:
            # If there is no data
            return [],[],fns

    def getAtdXaxisYaxes(self,xaxes,yaxes):
        ##################################################
        # SHOULD BE OPTIMISED (interp'd everytime)
        ##################################################
        xmin,xmax = None,None
        xaxisOut,yaxesOut = [],[]
        if len(xaxes):
            # check if they are all the same
            xaxesList = [list(x) for x in xaxes]
            if xaxesList.count(xaxesList[0]) == len(xaxesList):
                xaxisOut = xaxes[0]
                print 'all the xaxes are the same'
                yaxesOut = yaxes
            else:
                xmin = min([min(axis) for axis in xaxes])
                xmax = max([max(axis) for axis in xaxes])
                xaxisOut = np.arange(xmin,xmax+0.1,0.1)
                for xaxis,yaxis in zip(xaxes,yaxes):
                    yaxesOut.append(np.interp(xaxisOut,xaxis,yaxis))
        return xaxisOut,yaxesOut
                
        
    def setPlotType(self,radioSelection,showLines):
        s = SaPlotState
        state = -1
        if showLines == False:
            if radioSelection == 0:
                state = s.MS
            elif radioSelection == 1:
                state = s.ATD
            elif radioSelection == 2:
                state = s.MS_ATD
        elif showLines == True:
            if radioSelection == 0:
                state = s.MS_LINES
            elif radioSelection == 1:
                state = s.ATD_LINES
            elif radioSelection == 2:
                state = s.MS_ATD_LINES
        if state != -1:
            self.plotState = state
        else:
            print 'plot state problem (see settings class)'
    #=====================================================================
    # Atropos Stuff
    #=====================================================================
    def loadAtroposSpeciesAndCharges(self,path):
        self.atrOb = pickle.load(open(path,'rb'))

        # reset variables
        self.species = []
        self.speciesCharges = OrderedDict()
        
        for sp in sorted(self.atrOb.simulatedSpecies.keys()):
            self.species.append(sp)
            self.speciesCharges[sp] = self.atrOb.simulatedSpecies[sp].charges
        self.setImObsAtropos()
        
    def setSpeciesAndCharge(self,species,charge):
        self.speciesSelected = species
        self.chargeSelected = charge
        lims = self._getMzLimits(species,charge)
        self.plotPanel.atroposLeft = lims[0]
        self.plotPanel.atroposRight = lims[1]
         
    def getSpeciesAndCharge(self):
        return self.speciesSelected,self.chargeSelected
    def _getMzLimits(self,species,charge):
        limits = self.atrOb.simulatedSpecies[species].getPeakLimits(
            charge,self.widthL,self.widthR)
        return limits

    # End Atropos Stuff
    #=====================================================================

    
    #=====================================================================
    # Exporting Functions
    #=====================================================================
    def exportMsTxtFile(self,fn):
        xaxis, yaxes, fns = self.getMsXaxisYaxes()
        yaxis = np.average(yaxes,axis=0)
        yaxis = yaxis/yaxis.max()*100
        fout = open(fn,'w')
        for x,y in zip(xaxis,yaxis):
            print>>fout, '%11.4f\t%8.4f' %(x,y)
        fout.close()
    def exportAmphiFile(self,fn):
        # normalise and average the mobilities
        # get the appropriate x and y axes
        # pickle them all together in the new single file format
        imObs = [imOb for imOb in self.loadedFiles.values()]
        xaxis,yaxis,matrices = self.interpAxesMultiAmphiFiles(imObs)
        matrixOut = np.average(matrices,axis=0)
        utils.pickleAmphitriteProject(fn,imOb.xaxis,imOb.yaxis,matrixOut)

    def interpAxesMultiAmphiFiles(self,imObs):
        matrices = []
        xaxes = []
        yaxes = []
        for imOb in imObs:
            imOb.normalisationBpiByMs()
            matrices.append(imOb.matrix)
            xaxes.append(imOb.xaxis)
            yaxes.append(imOb.yaxis)

        if not self._axesEqual(xaxes):
            pass
        if not self._axesEqual(yaxes):
            pass
        #bodging for testing
        xaxis = xaxes[0]
        yaxis = yaxes[0]

        return xaxis,yaxis,matrices

    def interpolateGrid(self):
        #http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html#id1
        from scipy.interpolate import Rbf
        
        
    def _axesEqual(self,listOfAxes):
        axes = [list(axis) for axis in listOfAxes]
        if axes.count(axes[0]) == len(axes):
            return True
        else:
            return False
        
        
    # End Exporting Functions
    #=====================================================================