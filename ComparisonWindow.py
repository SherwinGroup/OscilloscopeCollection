import sys
from PyQt4 import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from ComparisonWindow_ui import Ui_MainWindow
import re
import datetime
        
class CompareWindow(QtGui.QMainWindow):
    collectionSettingsSignal = QtCore.pyqtSignal(dict)
    def __init__(self, settingsParent, parentSettingsSignal, boxcarSignal=None):
        super(CompareWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        boxcarSignal[dict].connect(self.updateGraph)
        parentSettingsSignal[dict].connect(self.updateSettings)
        self.CHA = np.array([])
        self.CHB = np.array([])
        self.ui.collectButton.clicked[bool].connect(self.clickedCollect)
        self.ui.resetButton.clicked.connect(self.reset)
        self.ui.saveButton.clicked.connect(self.save)
        self.pw = self.ui.graphicsView.plot()#labels={'bottom':'Channel A','left':'Channel B'}
        self.settings = settingsParent
        #self.ui.graphicsView.setLabels({bottom = self.settings['channelNames'][self.settings['activeChannels'][0]],
        #                               left = self.settings['channelNames'][self.settings['activeChannels'][1]]})
                                       
        plotitem = self.ui.graphicsView.getPlotItem()
        plotitem.setLabel('left', self.settings['channelNames'][self.settings['activeChannels'][1]])
        plotitem.setLabel('bottom',text=self.settings['channelNames'][self.settings['activeChannels'][0]])
        
        
    def clickedCollect(self,pushed):
        self.settings['isCollecting']=pushed
    
    def reset(self):
        self.CHA = np.array([])
        self.CHB = np.array([])
        self.pw.setData(x=self.CHA,y=self.CHB)
    
    def save(self):
        fname = str(QtGui.QFileDialog.getSaveFileName(self, "Select Filename...",directory=self.settings['location']))
        print fname
        if not fname=='':
            directory = fname[:-fname[::-1].find('/')]
            self.settings['location'] = directory
            self.collectionSettingsSignal.emit(self.settings)
            #filename = fname[-fname[::-1].find('/'):]
            #self.saveSettings['CHBFilename']=filename
            np.savetxt(fname,
                   np.transpose(np.vstack((
                   self.CHA, self.CHB))),
                    header=self.createHeaderText())
    def updateGraph(self,values):
        if self.settings['isCollecting']:
            self.CHA = np.append(self.CHA,values['CHA'])
            self.CHB = np.append(self.CHB,values['CHB'])
            self.pw.setData(x=self.CHA,y=self.CHB)
        
    def updateSettings(self,newSettings):
        self.settings = newSettings
        plotitem = self.ui.graphicsView.getPlotItem()
        plotitem.setLabel('left',self.settings['channelNames'][self.settings['activeChannels'][1]])
        plotitem.setLabel('bottom',text=self.settings['channelNames'][self.settings['activeChannels'][0]])
        print 'child settings updated'
        
    def createHeaderText(self):
        channels = self.settings['channelNames'][self.settings['activeChannels'][0]] + ' ' + \
            self.settings['channelNames'][self.settings['activeChannels'][1]]
            
        #parse self text
        miscHeader = re.sub('\{(DATE|date|Date)\}', str(datetime.datetime.now()), self.settings['commentText']  )
        
        firstlen = max(len(self.settings['channelNames'][self.settings['activeChannels'][0]]), 
                       len(self.settings['channelNames'][self.settings['activeChannels'][1]]))+3
        
        boxcarInfo = ' '*(firstlen-3) +\
                              'BoxcarBGSize   BoxcarSGSize\n'
        boxcarInfo = boxcarInfo + self.settings['channelNames'][self.settings['activeChannels'][0]]+\
                        ' '*(firstlen - len(self.settings['channelNames'][self.settings['activeChannels'][0]])) + \
                        str(self.settings['boxcarSizes'][0]) + '   '+str(self.settings['boxcarSizes'][1]) + '\n'
        boxcarInfo = boxcarInfo + self.settings['channelNames'][self.settings['activeChannels'][1]]+\
                        ' '*(firstlen - len(self.settings['channelNames'][self.settings['activeChannels'][1]])) + \
                        str(self.settings['boxcarSizes'][2]) + '   '+str(self.settings['boxcarSizes'][3]) + '\n'
        
        return miscHeader +'\n' + boxcarInfo + channels
        
        
        

def main(args):
    global app
    app = App(args)
    app.exec_()

if __name__ == "__main__":
    main(sys.argv)