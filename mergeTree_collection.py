#!/usr/bin/env python

from paraview.simple import *

basepath = "C:/Users/Grace/Documents/Clemson/Spring 2024/CPSC 8030 Scientific Visualization/8030_paraview_palmetto/"


# to do:
# from cinema database:
# create join tree, save join tree, create group, save group
# create split tree, save split tree, create group, save group
#
# from separate files:
# create join tree for EACH, save out
# create split tree for EACH, save out

# from separate files
# read in data
isabel_02vti = XMLImageDataReader(FileName=basepath+"isabel_small/Isabel_small.cdb/data/isabel_02.vti")
isabel_03vti = XMLImageDataReader(FileName=basepath+"isabel_small/Isabel_small.cdb/data/isabel_03.vti")

# create merge and contour tree
tTKMergeandContourTreeFTM_isabel_02vti_jt = TTKMergeandContourTreeFTM(Input=isabel_02vti)
tTKMergeandContourTreeFTM_isabel_02vti_jt.ScalarField = ["POINTS", "velocityMag"]
tTKMergeandContourTreeFTM_isabel_02vti_jt.TreeType = "Join Tree"

tTKMergeandContourTreeFTM_isabel_02vti_st = TTKMergeandContourTreeFTM(Input=isabel_02vti)
tTKMergeandContourTreeFTM_isabel_02vti_st.ScalarField = ["POINTS", "velocityMag"]
tTKMergeandContourTreeFTM_isabel_02vti_st.TreeType = "Split Tree"

tTKMergeandContourTreeFTM_isabel_03vti_jt = TTKMergeandContourTreeFTM(Input=isabel_03vti)
tTKMergeandContourTreeFTM_isabel_03vti_jt.ScalarField = ["POINTS", "velocityMag"]
tTKMergeandContourTreeFTM_isabel_03vti_jt.TreeType = "Join Tree"

tTKMergeandContourTreeFTM_isabel_03vti_st = TTKMergeandContourTreeFTM(Input=isabel_03vti)
tTKMergeandContourTreeFTM_isabel_03vti_st.ScalarField = ["POINTS", "velocityMag"]
tTKMergeandContourTreeFTM_isabel_03vti_st.TreeType = "Split Tree"

# # save
# 02_jt
SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_02_nodes_jt.vtu", tTKMergeandContourTreeFTM_isabel_02vti_jt, DataMode='Ascii') # u because unstructured grid, vtm is multiblock
SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_02_arcs_jt.vtu", OutputPort(tTKMergeandContourTreeFTM_isabel_02vti_jt,1), DataMode='Ascii') # u because unstructured grid, vtm is multiblock
SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_02_segmentation_jt.vti", OutputPort(tTKMergeandContourTreeFTM_isabel_02vti_jt,2), DataMode='Ascii') # u because unstructured grid, vtm is multiblock
# 02_st
SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_02_nodes_st.vtu", tTKMergeandContourTreeFTM_isabel_02vti_st, DataMode='Ascii') # u because unstructured grid, vtm is multiblock
SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_02_arcs_st.vtu", OutputPort(tTKMergeandContourTreeFTM_isabel_02vti_st,1), DataMode='Ascii') # u because unstructured grid, vtm is multiblock
SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_02_segmentation_st.vti", OutputPort(tTKMergeandContourTreeFTM_isabel_02vti_st,2), DataMode='Ascii') # u because unstructured grid, vtm is multiblock
# 03_jt
SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_03_nodes_jt.vtu", tTKMergeandContourTreeFTM_isabel_03vti_jt, DataMode='Ascii') # u because unstructured grid, vtm is multiblock
SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_03_arcs_jt.vtu", OutputPort(tTKMergeandContourTreeFTM_isabel_03vti_jt,1), DataMode='Ascii') # u because unstructured grid, vtm is multiblock
SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_03_segmentation_jt.vti", OutputPort(tTKMergeandContourTreeFTM_isabel_03vti_jt,2), DataMode='Ascii') # u because unstructured grid, vtm is multiblock
# 03_st
SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_03_nodes_st.vtu", tTKMergeandContourTreeFTM_isabel_03vti_st, DataMode='Ascii') # u because unstructured grid, vtm is multiblock
SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_03_arcs_st.vtu", OutputPort(tTKMergeandContourTreeFTM_isabel_03vti_st,1), DataMode='Ascii') # u because unstructured grid, vtm is multiblock
SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_03_segmentation_st.vti", OutputPort(tTKMergeandContourTreeFTM_isabel_03vti_st,2), DataMode='Ascii') # u because unstructured grid, vtm is multiblock

# SaveData(basepath+"isabel_small/isabel_02_st.vtu", tTKMergeandContourTreeFTM_isabel_02vti_st)
# SaveData(basepath+"isabel_small/isabel_03_jt.vtu", tTKMergeandContourTreeFTM_isabel_03vti_jt)
# SaveData(basepath+"isabel_small/isabel_03_st.vtu", tTKMergeandContourTreeFTM_isabel_03vti_st)

# # reading from database:
# # create a new 'TTK CinemaReader'
# tTKCinemaReader1 = TTKCinemaReader(DatabasePath=basepath+"isabel_small/Isabel_small.cdb")

# # create a new 'TTK CinemaProductReader'
# tTKCinemaProductReader1 = TTKCinemaProductReader(Input=tTKCinemaReader1)
# tTKCinemaProductReader1.AddFieldDataRecursively = 1

# # create a new 'TTK Merge and Contour Tree'
# tTKMergeandContourTreeFTM26 = TTKMergeandContourTreeFTM(Input=tTKCinemaProductReader1)
# tTKMergeandContourTreeFTM26.ScalarField = ["POINTS", "velocityMag"]
# tTKMergeandContourTreeFTM26.TreeType = "Join Tree"

# # create a new 'Group Datasets'
# mt_JT_all = GroupDatasets(
#     Input=[
#         tTKMergeandContourTreeFTM26,
#         OutputPort(tTKMergeandContourTreeFTM26, 1),
#         OutputPort(tTKMergeandContourTreeFTM26, 2),
#     ]
# )

# # create a new 'TTK Merge and Contour Tree'
# tTKMergeandContourTreeFTM25 = TTKMergeandContourTreeFTM(Input=tTKCinemaProductReader1)
# tTKMergeandContourTreeFTM25.ScalarField = ["POINTS", "velocityMag"]
# tTKMergeandContourTreeFTM25.TreeType = "Split Tree"

# # create a new 'Group Datasets'
# mt_ST_all = GroupDatasets(
#     Input=[
#         tTKMergeandContourTreeFTM25,
#         OutputPort(tTKMergeandContourTreeFTM25, 1),
#         OutputPort(tTKMergeandContourTreeFTM25, 2),
#     ]
# )

# # save join tree
# SaveData(basepath+"isabel_small/jt_from_db.vtm", tTKMergeandContourTreeFTM26)
# # save jt group
# SaveData(basepath+"isabel_small/jt_group_from_db.vtm", mt_JT_all)
# # save split tree
# SaveData(basepath+"isabel_small/st_from_db.vtm", tTKMergeandContourTreeFTM25)
# # save split group
# SaveData(basepath+"isabel_small/st_group_from_db.vtm", mt_ST_all)




# # save the output
# SaveData("MDS_trees.csv", threshold33)
# SaveData("MDS_centroids.csv", threshold34)