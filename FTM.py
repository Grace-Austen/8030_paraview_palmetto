# trace generated using paraview version 5.12.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'TTK CinemaReader'
tTKCinemaReader1 = TTKCinemaReader(registrationName='TTKCinemaReader1', DatabasePath='')

# Properties modified on tTKCinemaReader1
tTKCinemaReader1.DatabasePath = 'C:/Users/Grace/Documents/Clemson/Spring 2024/CPSC 8030 Scientific Visualization/8030_paraview_palmetto/Isabel.cdb'

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

# show data in view
tTKCinemaReader1Display = Show(tTKCinemaReader1, spreadSheetView1, 'SpreadSheetRepresentation')

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

# find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'TTK CinemaProductReader'
tTKCinemaProductReader1 = TTKCinemaProductReader(registrationName='TTKCinemaProductReader1', Input=tTKCinemaReader1)

# show data in view
tTKCinemaProductReader1Display = Show(tTKCinemaProductReader1, spreadSheetView1, 'SpreadSheetRepresentation')

# hide data in view
Hide(tTKCinemaReader1, spreadSheetView1)

# update the view to ensure updated data information
spreadSheetView1.Update()

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM1 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM1', Input=tTKCinemaProductReader1)

# show data in view
tTKMergeandContourTreeFTM1Display = Show(tTKMergeandContourTreeFTM1, spreadSheetView1, 'SpreadSheetRepresentation')

# hide data in view
Hide(tTKCinemaProductReader1, spreadSheetView1)

# show data in view
tTKMergeandContourTreeFTM1Display_1 = Show(OutputPort(tTKMergeandContourTreeFTM1, 1), spreadSheetView1, 'SpreadSheetRepresentation')

# hide data in view
Hide(tTKCinemaProductReader1, spreadSheetView1)

# show data in view
tTKMergeandContourTreeFTM1Display_2 = Show(OutputPort(tTKMergeandContourTreeFTM1, 2), spreadSheetView1, 'SpreadSheetRepresentation')

# hide data in view
Hide(tTKCinemaProductReader1, spreadSheetView1)

# update the view to ensure updated data information
spreadSheetView1.Update()

# Properties modified on tTKMergeandContourTreeFTM1
tTKMergeandContourTreeFTM1.TreeType = 'Join Tree'

# update the view to ensure updated data information
spreadSheetView1.Update()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1134, 459)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 6.6921304299024635]
renderView1.CameraParallelScale = 1.7320508075688772


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------