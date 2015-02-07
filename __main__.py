# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 15:36:27 2014

@author: Darren
"""

from PyQt4 import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
from Oscilloscope import TDSOscilloscope
from ComparisonWindow import CompareWindow
import threading
from saveDialog_ui import Ui_Dialog
from mainWindow_ui import Ui_MainWindow
from commentDialogWindow import CommentDialogBox
import datetime
import re

class Win(QtGui.QMainWindow):
    boxCarPairsSignal = QtCore.pyqtSignal(dict)
    settings = dict()
    parentSettingsSignal = QtCore.pyqtSignal(dict)
    
    def __init__(self):
        super(Win,self).__init__()
        self.scope = TDSOscilloscope()
        self.emitting = False
        self.settings['location'] = ''
        self.settings['CHAFilename'] = ''
        self.settings['CHBFilename'] = ''
        self.settings['CompareFilename'] = ''
        self.settings['CHSave'] = (False, False)
        self.settings['isCollecting'] = False
        self.settings['channelNames'] = ['CH1', 'CH2', 'CH3', 'CH4']
        self.settings['commentText'] = '{DATE}'
        self.settings['activeChannels'] = [0, 1]
        self.settings['boxcarSizes'] = [0, 0, 0, 0] #CHAbg, CHAsg, CHBbg, CHBsg
        self.runTrue = False
        self.initUI()
        
    def closeEvent(self,event):
        self.runTrue = False
        try:
            self.collectionWindow.close()
        except:
            pass
        self.close()
        
    def initUI(self):
        #Import ui file from designer
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)  
        
        #Define the plot widgets where data is updated
        self.p1 = self.ui.pw1.plot()
        plotitem = self.ui.pw1.getPlotItem()
        plotitem.setLabel('top',text='Channel 1')
        plotitem.setLabel('left',text='Voltage',units='V')
        plotitem.setLabel('bottom',text='Time Index')
        self.p2 = self.ui.pw2.plot()
        plotitem = self.ui.pw2.getPlotItem()
        plotitem.setLabel('top',text='Channel 2')
        plotitem.setLabel('left',text='Voltage',units='V')
        plotitem.setLabel('bottom',text='Time Index')
        
        # Add the draggable regions for the plots and add the labels to display their values
        self.makeLabelGridbox(self.ui.BoundaryValuesBox)
        self.makeLinearRegion()
        self.updateLinearRegionPoints()
        self.addChannelSelectionMenu()
        
        #Connect all the interfaces
        self.ui.compareButton.clicked.connect(self.collectVersus)
        self.ui.startButton.clicked[bool].connect(self.toggleCollection)
        self.ui.saveButton.clicked.connect(self.saveData)
        
        self.ui.file_queryScope.triggered.connect(self.updateScope)
        self.ui.file_EditComments.triggered.connect(self.updateComments)
        
        
        self.boxcarText = QtGui.QLabel()
        self.ui.statusbar.addPermanentWidget(self.boxcarText)#, stretch = 1)
        
        self.show()
        
    def updateComments(self):
        newNames, newText, ok = CommentDialogBox.getComments(
                    self.settings['channelNames'], self.settings['commentText'], self)
        if not ok:
            return
        
        for i in range(len(newNames)):
            if newNames[i] is not '':
                self.settings['channelNames'][i] = newNames[i]
            self.CHActions['A'][i].setText(self.settings['channelNames'][i])
            self.CHActions['B'][i].setText(self.settings['channelNames'][i])
        self.settings['commentText'] = newText
        
        
        
        plotitem = self.ui.pw1.getPlotItem()
        plotitem.setLabel('top',text=self.settings['channelNames'][self.settings['activeChannels'][0]])
        plotitem = self.ui.pw2.getPlotItem()
        plotitem.setLabel('top',text=self.settings['channelNames'][self.settings['activeChannels'][1]])
        
        self.parentSettingsSignal.emit(self.settings)
        
    def updateScope(self):
        #Settings for the channels are not necessarily the same, so we must reset the scalings 
        # on each channel. Bad to have different reads, it'll causea timeout.
        self.ui.statusbar.showMessage('Pausing collection to reset scaling...')
        restart = self.runTrue
        if self.runTrue:
            self.runTrue = False
            self.ui.startButton.setEnabled(False)
            self.dcT.join()
        self.scope.getScopeValues()
        self.ui.statusbar.clearMessage()
        self.ui.startButton.setEnabled(True)
        if restart:
            self.toggleCollection()
        
        
    def addChannelSelectionMenu(self):
        menu = self.ui.menu_CHA
        #A dictionary to hold all of the channel-changing actions together
        self.CHActions = dict()
        CHAActions = [None]*4
        for i in range(4):
            CHAActions[i] = QtGui.QAction(self.settings['channelNames'][i], menu, checkable = True, enabled = True)
            CHAActions[i].triggered.connect(self.changedChannel)
            menu.addAction(CHAActions[i])
        CHAActions[self.settings['activeChannels'][0]].setChecked(True)
        CHAActions[self.settings['activeChannels'][0]].setEnabled(False)
        
        CHAActions[self.settings['activeChannels'][1]].setEnabled(False)
        self.CHActions['A'] = CHAActions
        
        menu = self.ui.menu_CHB
        CHBActions = [None]*4
        for i in range(4):
            CHBActions[i] = QtGui.QAction(self.settings['channelNames'][i], menu, checkable = True, enabled = True)
            CHBActions[i].triggered.connect(self.changedChannel)
            menu.addAction(CHBActions[i])
        CHBActions[self.settings['activeChannels'][0]].setEnabled(False)
        
        CHBActions[self.settings['activeChannels'][1]].setChecked(True)
        CHBActions[self.settings['activeChannels'][1]].setEnabled(False)
        
        self.CHActions['B'] = CHBActions
        
        
    def changedChannel(self):
        '''
        This method will update preferences to change which channel to read from.
        '''
        clickedChannel = QtCore.QObject.sender(self)
        isCHA = (clickedChannel.parentWidget()==self.ui.menu_CHA)
        #Set variables for whether channel A or B was toggled
        if isCHA:
            channel = 'A'
            altChan = 'B'
        else:
            channel = 'B'
            altChan = 'A'
        
        #Technically, two channels are checked before I forcebly uncheck one. Ensure
        #it doesn't accidentally pick the wrong channel
        curCH = [action for action in self.CHActions[channel] if (action.isChecked()==True and not action==clickedChannel)][0]
        #### CHANGE SCOPE TO NEW VALUE
        curCH.setChecked(False)
        curCH.setEnabled(True)
        clickedChannel.setEnabled(False)
        #modify the two channels in the second menu
        curCHidx = self.settings['activeChannels'][1-int(isCHA)]
        #newCHidx = int(clickedChannel.text()[-1])-1
        newCHidx = [i for i in range(4) if clickedChannel.text()==self.CHActions['A'][i].text()][0]
        print curCHidx, newCHidx
        
        self.CHActions[altChan][curCHidx].setEnabled(True)
        self.CHActions[altChan][newCHidx].setEnabled(False)
        
        self.settings['activeChannels'][1-int(isCHA)] = newCHidx
        print self.settings['activeChannels']
        
        #Get the plot to change the title. Also,c hange the scope values
        # so it reads the new ones
        if isCHA:
            plotitem = self.ui.pw1.getPlotItem()
#            self.scope.changeChannelstoRead(curCH.text(), clickedChannel.text())
        else:
            plotitem = self.ui.pw2.getPlotItem()
#            self.scope.changeChannelstoRead(clickedChannel.text(), curCH.text())
        self.scope.changeChannelstoRead('CH'+str(self.settings['activeChannels'][0]+1), 
                                        'CH'+str(self.settings['activeChannels'][1]+1))
            
        plotitem.setLabel('top', text=self.settings['channelNames'][newCHidx])
        self.parentSettingsSignal.emit(self.settings)
        
        self.updateScope()
        
    
    def makeLabelGridbox(self, gridbox = None):
        #gridbox = QtGui.QGridLayout()
        if gridbox == None:
            return
        
        t0 = QtGui.QLabel('BgCHAStart')
        t1 = QtGui.QLabel('BgCHAEnd')
        t2 = QtGui.QLabel('BgCHBStart')
        t3 = QtGui.QLabel('BgCHBEnd')
        t4 = QtGui.QLabel('SgCHAStart')
        t5 = QtGui.QLabel('SgCHAEnd')
        t6 = QtGui.QLabel('SgCHBStart')
        t7 = QtGui.QLabel('SgCHBEnd')
        
    
        self.boundaries = [None]*8
        for i in range(8):
            self.boundaries[i] = QtGui.QLineEdit()
            self.boundaries[i].setReadOnly(False)
            #self.boundaries[i].connect(self, QtCore.SIGNAL('changedText'))
            self.boundaries[i].editingFinished.connect(self.changedText)
        
        gridbox.addWidget(t0,1,0)
        gridbox.addWidget(self.boundaries[0],1,1)
        gridbox.addWidget(t1,1,2)
        gridbox.addWidget(self.boundaries[1],1,3)
        gridbox.addWidget(t2,1,5)
        gridbox.addWidget(self.boundaries[2],1,6)
        gridbox.addWidget(t3,1,7)
        gridbox.addWidget(self.boundaries[3],1,8)
        #Row two
        gridbox.addWidget(t4,2,0)
        gridbox.addWidget(self.boundaries[4],2,1)
        gridbox.addWidget(t5,2,2)
        gridbox.addWidget(self.boundaries[5],2,3)
        gridbox.addWidget(t6,2,5)
        gridbox.addWidget(self.boundaries[6],2,6)
        gridbox.addWidget(t7,2,7)
        gridbox.addWidget(self.boundaries[7],2,8)
        
        gridbox.setColumnStretch(4,3)
        gridbox.setColumnStretch(9,3)
        return gridbox
        
    def changedText(self):
        try:
            values = [float(boundary.text()) for boundary in self.boundaries]
        except:
            print 'fucked up converting the boundary text to floats'
            print [boundary.text() for boundary in self.boundaries]
                
        zippdVals = zip(values[0:8:2], values[1:8:2])
        for i in range(4):
            self.lr[i].setRegion(zippdVals[i])
        
        CHAbg = self.lr[0].getRegion()
        CHAsg = self.lr[1].getRegion()
        CHBbg = self.lr[2].getRegion()
        CHBsg = self.lr[3].getRegion()
        
        self.settings['boxcarSizes'] = [CHAbg[1]-CHAbg[0], CHAsg[1]-CHAsg[0], 
                                        CHBbg[1]-CHBbg[0], CHBsg[1]-CHBsg[0]]
        
        self.parentSettingsSignal.emit(self.settings)
            
    def makeLinearRegion(self):
        self.lr = [None]*4
        bgStart = 100
        bgEnd = 400
        sgStart = 900
        sgEnd = 1300
        bound = [0,self.scope.readLength]
        bgCol = pg.mkBrush(QtGui.QColor(255,0,0,50))
        sgCol = pg.mkBrush(QtGui.QColor(0,255,0,50))
        #Background region for plot1
        self.lr[0] = pg.LinearRegionItem([bgStart,bgEnd],bounds=bound,brush=bgCol)
        #Background region for plot2
        self.lr[1] = pg.LinearRegionItem([bgStart,bgEnd],bounds=bound,brush=bgCol)
        #Signal region for plot1
        self.lr[2] = pg.LinearRegionItem([sgStart,sgEnd],bounds=bound,brush=sgCol)
        #Signal region for plot2
        self.lr[3] = pg.LinearRegionItem([sgStart,sgEnd],bounds=bound,brush=sgCol)
        
        for i in range(4):
            self.lr[i].sigRegionChanged.connect(self.updateLinearRegionPoints)
        
        self.ui.pw1.addItem(self.lr[0])
        self.ui.pw1.addItem(self.lr[2])
        self.ui.pw2.addItem(self.lr[1])
        self.ui.pw2.addItem(self.lr[3])
        
    def updateLinearRegionPoints(self):
        #Make a single tuple to iterate over
        allvals = self.lr[0].getRegion()+self.lr[1].getRegion()+self.lr[2].getRegion()+self.lr[3].getRegion()
        for i in range(8):
            self.boundaries[i].setText('{:.1f}'.format(allvals[i]))
            
        CHAbg = self.lr[0].getRegion()
        CHAsg = self.lr[1].getRegion()
        CHBbg = self.lr[2].getRegion()
        CHBsg = self.lr[3].getRegion()
        
        self.settings['boxcarSizes'] = [CHAbg[1]-CHAbg[0], CHAsg[1]-CHAsg[0], 
                                        CHBbg[1]-CHBbg[0], CHBsg[1]-CHBsg[0]]
        4
        self.parentSettingsSignal.emit(self.settings) 
    def quitall(self):
        #QtGui.qApp.quit()
        self.close()
        
    
    def toggleCollection(self):
        self.runTrue = not self.runTrue
        if self.runTrue: #start data collection
            self.dcT = threading.Thread(target=self.collectionLoop)
            self.dcT.start()
        
    
    def collectVersus(self):
        self.collectionWindow = CompareWindow(self.settings, self.parentSettingsSignal, self.boxCarPairsSignal)
        self.collectionWindow.collectionSettingsSignal[dict].connect(self.updateSettings)
        self.collectionWindow.show()
        
    #This is the function which only queries the oscilloscope for data
    def collectionLoop(self):
        i = 0
        while self.runTrue:
            self.scope.start_acquire()
            if not self.scope.acq_complete(): print 'Action not complete?'
            self.scope.stop_acquire()
#            print "end wait" + str(i)
            #self.scope.stop_acquire()
            #Something weird is happening that the plots are updating individually.
            #Maybe python does something weird where it doens't wait for a void() function?
            #Force it to return so it has to wait for it
            if self.scope.read_both_channels(): pass
            i=i+1
            self.dataProcessing()
    
    def dataProcessing(self):
        self.scope.scaleWaveforms()
        self.p1.setData(y=self.scope.wfmDict[self.scope.CHA],x=range(len(self.scope.wfmDict[self.scope.CHA])))
        self.p2.setData(y=self.scope.wfmDict[self.scope.CHB],x=range(len(self.scope.wfmDict[self.scope.CHB])))
                                          
                                          
        abox = self.scope.boxcarIntegrate(self.scope.CHA,
                                          (int(float(self.boundaries[0].text())),int(float(self.boundaries[1].text()))),
                                          (int(float(self.boundaries[4].text())),int(float(self.boundaries[5].text()))))
        bbox = self.scope.boxcarIntegrate(self.scope.CHB,
                                          (int(float(self.boundaries[2].text())),int(float(self.boundaries[3].text()))),
                                          (int(float(self.boundaries[6].text())),int(float(self.boundaries[7].text()))))
                                          
                                          
        #self.ui.statusbar.showMessage('Channel A Boxcar: {:.2g} | Channel B Boxcar: {:.2g}'.format(abox,bbox))    

        self.boxcarText.setText('Channel A Boxcar: {:.2g} | Channel B Boxcar: {:.2g}'.format(abox,bbox))
        self.boxCarPairsSignal.emit({'CHA':abox, 'CHB':bbox})
        
    def getInt(self ,tup):
        return tuple(int(i) for i in tup)
        
    def saveData(self):
        CHA, CHB, ok = saveDialogBox.getSavePref(self.settings['CHSave'])
        if not ok:
            return
        self.settings['CHSave']=(CHA, CHB)
        if CHA:
            fname = str(QtGui.QFileDialog.getSaveFileName(self, "CHA Savename...",directory=self.settings['location']))
            print fname
            if not fname=='':
                directory = fname[:-fname[::-1].find('/')]
                self.settings['location'] = directory
                filename = fname[-fname[::-1].find('/'):]
                self.settings['CHAFilename']=filename
                np.savetxt(fname,
                       np.transpose(np.vstack((
                       np.arange(len(self.scope.wfmDict[self.scope.CHA]))*self.scope.dt,
                       self.scope.wfmDict[self.scope.CHA]))),
                        header=self.createHeaderText())
                        
        if CHB:
            fname = str(QtGui.QFileDialog.getSaveFileName(self, "CHB Savename...",directory=self.settings['location']))
            print fname
            if not fname=='':
                directory = fname[:-fname[::-1].find('/')]
                self.settings['location'] = directory
                filename = fname[-fname[::-1].find('/'):]
                self.settings['CHBFilename']=filename
                np.savetxt(fname,
                       np.transpose(np.vstack((
                       np.arange(len(self.scope.wfmDict[self.scope.CHB]))*self.scope.dt,
                       self.scope.wfmDict[self.scope.CHB]))),
                        header=self.createHeaderText())
        if CHA or CHB:
            self.parentSettingsSignal.emit(self.settings)
    
    def updateSettings(self, newSettings):
        print 'updated parent Settings'
        self.settings = newSettings
    
    def createHeaderText(self):
        scopeInfo = 'Volts per div: ' + str(self.scope.CHAVoltDiv) + '\nTime scale: '+str(self.scope.TimeScale)
        
        channels = self.settings['channelNames'][self.settings['activeChannels'][0]] + ' ' + \
            self.settings['channelNames'][self.settings['activeChannels'][1]]
            
        #parse self text
        miscHeader = re.sub('\{(DATE|date|Date)\}', str(datetime.datetime.now()), self.settings['commentText']  )
        
        return scopeInfo + '\n' + miscHeader +'\n' + channels
        
        
class saveDialogBox(QtGui.QDialog):
    def __init__(self,parent=None,pastPref=None):
        super(saveDialogBox,self).__init__(parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        if not pastPref == None:
            self.ui.CHABox.setChecked(pastPref[0])
            self.ui.CHBBox.setChecked(pastPref[1])        
        
    @staticmethod
    def getSavePref(pastPref,parent=None):
        dialog = saveDialogBox(parent,pastPref)
        result = dialog.exec_()
        return (dialog.ui.CHABox.isChecked(),dialog.ui.CHBBox.isChecked(),result == QtGui.QDialog.Accepted)
        
        
def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    ex = Win()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()