#!/usr/bin/env python
#
# generated by wxGlade 0.6.7 on Wed Apr 24 05:01:40 2013
#
 
import wx,gettext,os
import wx.lib.agw.multidirdialog as MDD

import SaPlotPanel,SaSettings,ListCtrlFilesSa
import gui.guiFunctions as gf
from AmphitriteEnums import *


#<136682597422437117wxGlade replace dependencies>
# begin wxGlade: extracode
# end wxGlade


class SpectralAveragingGui(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SpectralAveragingGui.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.window_1 = wx.SplitterWindow(self, -1, style=wx.SP_3D | wx.SP_BORDER)
        self.window_1_pane_1 = wx.Panel(self.window_1, -1)
        self.label_1 = wx.StaticText(self.window_1_pane_1, -1, _("MS Txt Files"))
        self.buttonOpenTxtFiles = wx.Button(self.window_1_pane_1, -1, _("Open"))
        self.label_2 = wx.StaticText(self.window_1_pane_1, -1, _("Amphitrite Data Files"))
        self.buttonOpenAmphiFiles = wx.Button(self.window_1_pane_1, -1, _("Open"))
        self.panelListCtrlFiles = wx.Panel(self.window_1_pane_1, -1)
        self.sizer_2_staticbox = wx.StaticBox(self.window_1_pane_1, -1, _("File List"))
        self.choicePlottingOptions = wx.Choice(self.window_1_pane_1, -1, choices=[_("Min/Max"), _("Standard Deviation"), _("None")])
        self.checkboxDisplayIndividualSpectra = wx.CheckBox(self.window_1_pane_1, -1, _("Display Individual Spectra"))
        self.checkboxLegend = wx.CheckBox(self.window_1_pane_1, -1, _("Show Legend"))
        self.radioBoxPlotPanel = wx.RadioBox(self.window_1_pane_1, -1, _("Plot Panel"), choices=[_("Mass Spectra"), _("Arrival Time Distributions"), _("Both")], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.sizer_3_staticbox = wx.StaticBox(self.window_1_pane_1, -1, _("Plotting Options"))
        self.label_3 = wx.StaticText(self.window_1_pane_1, -1, _("Atropos File"))
        self.textCtrlAtropos = wx.TextCtrl(self.window_1_pane_1, -1, "")
        self.buttonAtropos = wx.Button(self.window_1_pane_1, -1, _("Open"))
        self.label_4 = wx.StaticText(self.window_1_pane_1, -1, _("Species"))
        self.choiceSpecies = wx.Choice(self.window_1_pane_1, -1, choices=[])
        self.label_5 = wx.StaticText(self.window_1_pane_1, -1, _("Charge State"))
        self.choiceChargeState = wx.Choice(self.window_1_pane_1, -1, choices=[])
        self.label_6 = wx.StaticText(self.window_1_pane_1, -1, _("Width Multiplier L"))
        self.textCtrlWidthL = wx.TextCtrl(self.window_1_pane_1, -1, _("1.0"))
        self.label_7 = wx.StaticText(self.window_1_pane_1, -1, _("Width Multiplier R"))
        self.textCtrlWidthR = wx.TextCtrl(self.window_1_pane_1, -1, _("1.0"))
        self.sizer_7_staticbox = wx.StaticBox(self.window_1_pane_1, -1, _("Atropos"))
        self.checkboxDisplaySelection = wx.CheckBox(self.window_1_pane_1, -1, _("Display Selection"))
        self.buttonClickAndDrag = wx.ToggleButton(self.window_1_pane_1, -1, _("Activate"))
        self.buttonClearSelection = wx.Button(self.window_1_pane_1, -1, _("Clear Selection"))
        self.sizer_6_staticbox = wx.StaticBox(self.window_1_pane_1, -1, _("Click and Drag"))
        self.sizer_4_staticbox = wx.StaticBox(self.window_1_pane_1, -1, _("ATD Selection"))
        self.buttonExportIm = wx.Button(self.window_1_pane_1, -1, _("Amphi IM"))
        self.buttonExportTextFile = wx.Button(self.window_1_pane_1, -1, _("MS Txt File"))
        self.sizer_5_staticbox = wx.StaticBox(self.window_1_pane_1, -1, _("Export"))
        self.panePlotting = wx.Panel(self.window_1, -1)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.eventButtonOpenTxtFiles, self.buttonOpenTxtFiles)
        self.Bind(wx.EVT_BUTTON, self.eventButtonOpenAmphiFiles, self.buttonOpenAmphiFiles)
        self.Bind(wx.EVT_CHOICE, self.eventChoicePlottingOptions, self.choicePlottingOptions)
        self.Bind(wx.EVT_CHECKBOX, self.eventCheckboxDisplayIndividualSpectra, self.checkboxDisplayIndividualSpectra)
        self.Bind(wx.EVT_CHECKBOX, self.eventCheckboxLegend, self.checkboxLegend)
        self.Bind(wx.EVT_RADIOBOX, self.eventRadioBoxPlotPanel, self.radioBoxPlotPanel)
        self.Bind(wx.EVT_BUTTON, self.eventButtonAtropos, self.buttonAtropos)
        self.Bind(wx.EVT_CHOICE, self.eventChoiceSpecies, self.choiceSpecies)
        self.Bind(wx.EVT_CHOICE, self.eventChoiceChargeState, self.choiceChargeState)
        self.Bind(wx.EVT_TEXT, self.eventTextCtrlWidthL, self.textCtrlWidthL)
        self.Bind(wx.EVT_TEXT, self.eventTextCtrlWidthR, self.textCtrlWidthR)
        self.Bind(wx.EVT_CHECKBOX, self.eventCheckboxDisplaySelection, self.checkboxDisplaySelection)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.eventButtonClickAndDrag, self.buttonClickAndDrag)
        self.Bind(wx.EVT_BUTTON, self.eventButtonClearSelection, self.buttonClearSelection)
        self.Bind(wx.EVT_BUTTON, self.eventButtonExportIm, self.buttonExportIm)
        self.Bind(wx.EVT_BUTTON, self.eventButtonExportTextFile, self.buttonExportTextFile)
        # end wxGlade

        ########################################
        # Establish inter-object references

        self.settings.setPlotPanel(self.plotPanel)
        self.settings.setListCtrlFiles(self.listCtrlFiles)

        self.listCtrlFiles.setSettings(self.settings)
        self.listCtrlFiles.setPlotPanel(self.plotPanel)
        
        self.plotPanel.setSettings(self.settings)
        self.plotPanel.setGui(self)
        ########################################
        
    def __set_properties(self):
        # begin wxGlade: SpectralAveragingGui.__set_properties
        self.SetTitle(_("Spectral Averaging - Beta"))
        self.SetSize((982, 684))
        self.choicePlottingOptions.SetSelection(0)
        self.checkboxDisplayIndividualSpectra.SetValue(1)
        self.checkboxLegend.SetValue(1)
        self.radioBoxPlotPanel.SetSelection(0)
        self.checkboxDisplaySelection.SetValue(1)
        # end wxGlade

        ########################################
        # Creating my objects

        self.panePlotting.Hide()
        self.plotPanel = SaPlotPanel.SaPlotPanel(self.panePlotting)

        self.panelListCtrlFiles.Hide()
        self.panelListCtrlFiles = ListCtrlFilesSa.ListCtrlFiles(self.window_1_pane_1)
        self.listCtrlFiles = self.panelListCtrlFiles
        self.settings = SaSettings.SaSettings()

        ########################################
        
    def __do_layout(self):
        # begin wxGlade: SpectralAveragingGui.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(4, 1, 0, 0)
        self.sizer_5_staticbox.Lower()
        sizer_5 = wx.StaticBoxSizer(self.sizer_5_staticbox, wx.HORIZONTAL)
        grid_sizer_3 = wx.GridSizer(1, 2, 0, 0)
        self.sizer_4_staticbox.Lower()
        sizer_4 = wx.StaticBoxSizer(self.sizer_4_staticbox, wx.HORIZONTAL)
        grid_sizer_6 = wx.FlexGridSizer(4, 1, 0, 0)
        self.sizer_6_staticbox.Lower()
        sizer_6 = wx.StaticBoxSizer(self.sizer_6_staticbox, wx.HORIZONTAL)
        grid_sizer_9 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_10 = wx.GridSizer(1, 2, 0, 0)
        self.sizer_7_staticbox.Lower()
        sizer_7 = wx.StaticBoxSizer(self.sizer_7_staticbox, wx.HORIZONTAL)
        grid_sizer_11 = wx.FlexGridSizer(2, 1, 0, 0)
        grid_sizer_7 = wx.FlexGridSizer(4, 2, 0, 0)
        grid_sizer_8 = wx.FlexGridSizer(1, 3, 0, 0)
        self.sizer_3_staticbox.Lower()
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.HORIZONTAL)
        grid_sizer_5 = wx.FlexGridSizer(6, 1, 0, 0)
        self.sizer_2_staticbox.Lower()
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.HORIZONTAL)
        grid_sizer_2 = wx.FlexGridSizer(3, 1, 0, 0)
        grid_sizer_4 = wx.FlexGridSizer(2, 2, 0, 0)
        grid_sizer_4.Add(self.label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(self.buttonOpenTxtFiles, 0, 0, 0)
        grid_sizer_4.Add(self.label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_4.Add(self.buttonOpenAmphiFiles, 0, 0, 0)
        grid_sizer_4.AddGrowableCol(0)
        grid_sizer_2.Add(grid_sizer_4, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.panelListCtrlFiles, 1, wx.EXPAND, 0)
        grid_sizer_2.AddGrowableRow(1)
        grid_sizer_2.AddGrowableCol(0)
        sizer_2.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_5.Add(self.choicePlottingOptions, 0, wx.EXPAND, 0)
        grid_sizer_5.Add(self.checkboxDisplayIndividualSpectra, 0, 0, 0)
        grid_sizer_5.Add(self.checkboxLegend, 0, 0, 0)
        grid_sizer_5.Add(self.radioBoxPlotPanel, 0, wx.EXPAND, 0)
        grid_sizer_5.AddGrowableCol(0)
        sizer_3.Add(grid_sizer_5, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_8.Add(self.label_3, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_8.Add(self.textCtrlAtropos, 0, 0, 0)
        grid_sizer_8.Add(self.buttonAtropos, 0, 0, 0)
        grid_sizer_8.AddGrowableCol(0)
        grid_sizer_11.Add(grid_sizer_8, 1, wx.EXPAND, 0)
        grid_sizer_7.Add(self.label_4, 0, 0, 0)
        grid_sizer_7.Add(self.choiceSpecies, 0, 0, 0)
        grid_sizer_7.Add(self.label_5, 0, 0, 0)
        grid_sizer_7.Add(self.choiceChargeState, 0, 0, 0)
        grid_sizer_7.Add(self.label_6, 0, 0, 0)
        grid_sizer_7.Add(self.textCtrlWidthL, 0, wx.EXPAND, 0)
        grid_sizer_7.Add(self.label_7, 0, 0, 0)
        grid_sizer_7.Add(self.textCtrlWidthR, 0, wx.EXPAND, 0)
        grid_sizer_7.AddGrowableCol(0)
        grid_sizer_11.Add(grid_sizer_7, 1, wx.EXPAND, 0)
        grid_sizer_11.AddGrowableCol(0)
        sizer_7.Add(grid_sizer_11, 1, wx.EXPAND, 0)
        grid_sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        grid_sizer_9.Add(self.checkboxDisplaySelection, 0, 0, 0)
        grid_sizer_10.Add(self.buttonClickAndDrag, 0, wx.EXPAND, 0)
        grid_sizer_10.Add(self.buttonClearSelection, 0, wx.EXPAND, 0)
        grid_sizer_9.Add(grid_sizer_10, 1, wx.EXPAND, 0)
        grid_sizer_9.AddGrowableCol(0)
        sizer_6.Add(grid_sizer_9, 1, wx.EXPAND, 0)
        grid_sizer_6.Add(sizer_6, 1, wx.EXPAND, 0)
        grid_sizer_6.AddGrowableCol(0)
        sizer_4.Add(grid_sizer_6, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(sizer_4, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.buttonExportIm, 0, wx.EXPAND, 0)
        grid_sizer_3.Add(self.buttonExportTextFile, 0, wx.EXPAND, 0)
        sizer_5.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(sizer_5, 1, wx.EXPAND, 0)
        self.window_1_pane_1.SetSizer(grid_sizer_1)
        grid_sizer_1.AddGrowableRow(0)
        grid_sizer_1.AddGrowableCol(0)
        self.window_1.SplitVertically(self.window_1_pane_1, self.panePlotting, 300)
        sizer_1.Add(self.window_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def eventButtonOpenTxtFiles(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        dlg = wx.FileDialog(
            self,message = 'Select Coordinate Pair Txt Files',
            defaultFile = '',
            wildcard = 'Text file (*.txt)|*.txt|  All files (*.*)|*.*|',
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            self.listCtrlFiles.addTxtFiles(paths)
            self._turnOffImComponents()
        dlg.Destroy()
    def _turnOffImComponents(self):
        self.radioBoxPlotPanel.SetSelection(0)
        self.switchImComponents(False)

    def _turnOnImComponents(self):
        self.switchImComponents(True)

    def switchImComponents(self,onoff):
        # Radiobox
        self.radioBoxPlotPanel.Enable(onoff)
        # Atropos Stuff
        self.textCtrlAtropos.Enable(onoff)
        self.buttonAtropos.Enable(onoff)
        self.choiceSpecies.Enable(onoff)
        self.choiceChargeState.Enable(onoff)
        self.textCtrlWidthL.Enable(onoff)
        self.textCtrlWidthR.Enable(onoff)
        # Click and drag
        self.checkboxDisplaySelection.Enable(onoff)
        self.buttonClickAndDrag.Enable(onoff)
        self.buttonClearSelection.Enable(onoff)
        
    def eventButtonOpenAmphiFiles(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        home = os.path.expanduser('~')
        dlg = MDD.MultiDirDialog(self, title="Choose a directory:",
                                 defaultPath=os.path.join(home,
                                           '/Dropbox/workspaces/Amphitrite_2.0/gui/tempData'))
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            self.listCtrlFiles.addFiles(paths)        
        else:
            print 'multidir dialog error'
        dlg.Destroy()
        

    def eventChoicePlottingOptions(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        sel = event.GetSelection()
        if sel == 0:
            self.settings.boundaryAlgorithm = SaBndAlg.MIN_MAX
        elif sel == 1:
            self.settings.boundaryAlgorithm = SaBndAlg.STD
        elif sel == 2:
            self.settings.boundaryAlgorithm = SaBndAlg.NONE
        else:
            print 'Unrecognised boundary selection made'
            
        self.plotPanel.refresh_plot()

    def eventCheckboxDisplayIndividualSpectra(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        showLines = self.checkboxDisplayIndividualSpectra.IsChecked()
        selection = self.radioBoxPlotPanel.GetSelection()
        self.settings.setPlotType(selection,showLines)
        self.plotPanel.refresh_plot()
        

    def eventRadioBoxPlotPanel(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        showLines = self.checkboxDisplayIndividualSpectra.IsChecked()
        selection = event.GetSelection()
        self.settings.setPlotType(selection,showLines)
        self.plotPanel.refresh_plot()
    #=====================================================================
    # Atropos Stuff
    #=====================================================================
    def eventButtonAtropos(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        path = gf.openAtroposFile(self)
        if path:
            self.textCtrlAtropos.SetValue(path)
            self.settings.loadAtroposSpeciesAndCharges(path)
            self._populateSpeciesChoices()
        else:
            print 'Atropos path problem: %s' %path

    def _populateSpeciesChoices(self):
        self.choiceSpecies.Enable(True)
        self.choiceSpecies.Clear()
        
        spChoices = self.settings.speciesCharges.keys()
        for sp in spChoices:
            self.choiceSpecies.Append(item=sp)

    def _populateCharges(self):
        sp = self._getChoiceSpecies()
        zs = self.settings.speciesCharges[sp]

        self.choiceChargeState.Enable(True)
        self.choiceChargeState.Clear()
        for z in zs:
            self.choiceChargeState.Append(str(z))
            
    def _getChoiceSpecies(self):
        i = self.choiceSpecies.GetCurrentSelection()
        sp = self.settings.species[i]
        return sp
    def _getChoiceChargeState(self):
        sp = self._getChoiceSpecies()
        i = self.choiceChargeState.GetCurrentSelection()
        z = self.settings.speciesCharges[sp][i]
        return z

    
    def eventChoiceSpecies(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        self._populateCharges()
        
    def eventChoiceChargeState(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        sp = self._getChoiceSpecies()
        z = self._getChoiceChargeState()
        self.settings.setSpeciesAndCharge(sp,z)
        self.plotPanel.pickedValue = None
        self.plotPanel.releasedValue = None
        self.plotPanel.refresh_plot()

    def eventTextCtrlWidthL(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        val = gf.checkIfNumberTextCtrl(self.textCtrlWidthL)
        if type(val).__name__ != 'str':
            self.settings.setWidthL(val)
        else:
            message = 'Please only enter numbers in this box!'
            gf.warningDialog(message)
            self.textCtrlWidthL.SetValue(str(self.settings.widthL)) 

    def eventTextCtrlWidthR(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        val = gf.checkIfNumberTextCtrl(self.textCtrlWidthR)
        if type(val).__name__ != 'str':
            self.settings.setWidthR(val)
        else:
            message = 'Please only enter numbers in this box!'
            gf.warningDialog(message)
            self.textCtrlWidthR.SetValue(str(self.settings.widthR))

    # End Atropos Stuff
    #=====================================================================

    def eventButtonClearSelection(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        self.plotPanel.pickedValue = None
        self.plotPanel.releasedValue = None
        self.plotPanel.atroposLeft = None
        self.plotPanel.atroposRight = None
        self.plotPanel.refresh_plot()

    def eventButtonExportIm(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>

        dlg = wx.FileDialog(
            self, message="Save file as ...", 
            defaultDir=self.settings.defaultDirectory,
            defaultFile="",
            wildcard='Amphitrite data file (*.a)|*.a',
            style=wx.SAVE
            )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.settings.exportAmphiFile(path)
            self.settings.defaultDirectory = os.path.dirname(path)
        dlg.Destroy()


    def eventButtonExportTextFile(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        if len(self.settings.massSpectra):
            dlg = wx.FileDialog(
                self, message="Save file as ...", 
                defaultDir=self.settings.defaultDirectory,
                defaultFile="",
                wildcard='Text file (*.txt)|*.txt|  All files (*.*)|*.*',
                style=wx.SAVE
                )
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                self.settings.exportMsTxtFile(path)
                self.settings.defaultDirectory = os.path.dirname(path)
            dlg.Destroy()
        else:
            message = 'Load files before exporting!'
            gf.warningDialog(message)

    def eventCheckboxLegend(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        self.settings.showLegend = event.IsChecked()
        self.plotPanel.refresh_plot()

    def eventCheckboxDisplaySelection(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        print self.plotPanel.axes[0].get_xlim()
        print self.plotPanel.axes[0].get_xbound()
        xlims = self.plotPanel.axes[0].get_xbound()
        self.plotPanel.refresh_plot()
        print self.plotPanel.axes[0].get_xlim()
        self.plotPanel.axes[0].set_xlim(xlims)
        self.plotPanel.draw()

    def eventButtonClickAndDrag(self, event):  # wxGlade: SpectralAveragingGui.<event_handler>
        self.plotPanel.toggleClickAndDrag(event.IsChecked(),self)

# end of class SpectralAveragingGui
if __name__ == "__main__":
    gettext.install("app") # replace with the appropriate catalog name

    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = SpectralAveragingGui(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()