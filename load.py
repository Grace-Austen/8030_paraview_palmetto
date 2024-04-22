from paraview.simple import *

basepath = "C:/Users/Grace/Documents/Clemson/Spring 2024/CPSC 8030 Scientific Visualization/8030_paraview_palmetto/"

# isabel_02_jtvtu = XMLUnstructuredGridReader(registrationName='isabel_02_jt.vtu', FileName=basepath+"isabel_small/isabel_02_jt.vtu")
# isabel_02_jtvtu = XMLUnstructuredGridReader( FileName=basepath+"isabel_small/isabel_02_jt.vtu")

tTKMergeandContourTreeFTM_isabel_02vti_jt = XMLUnstructuredGridReader(FileName=basepath+"isabel_small/isabel_02_jt.vtu") # u because unstructured grid, vtm is multiblock
tTKMergeandContourTreeFTM_isabel_02vti_st = XMLUnstructuredGridReader(FileName=basepath+"isabel_small/isabel_02_st.vtu")
tTKMergeandContourTreeFTM_isabel_03vti_st = XMLUnstructuredGridReader(FileName=basepath+"isabel_small/isabel_03_jt.vtu")
tTKMergeandContourTreeFTM_isabel_03vti_st = XMLUnstructuredGridReader(FileName=basepath+"isabel_small/isabel_03_st.vtu")

# incomplete below...

# 02_jt
# SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_02_nodes_jt.vtu", tTKMergeandContourTreeFTM_isabel_02vti_jt) # u because unstructured grid, vtm is multiblock
# SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_02_arcs_jt.vtu", OutputPort(tTKMergeandContourTreeFTM_isabel_02vti_jt,1)) # u because unstructured grid, vtm is multiblock
# SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_02_segmentation_jt.vti", OutputPort(tTKMergeandContourTreeFTM_isabel_02vti_jt,2)) # u because unstructured grid, vtm is multiblock
# # 02_st
# SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_02_nodes_st.vtu", tTKMergeandContourTreeFTM_isabel_02vti_st) # u because unstructured grid, vtm is multiblock
# SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_02_arcs_st.vtu", OutputPort(tTKMergeandContourTreeFTM_isabel_02vti_st,1)) # u because unstructured grid, vtm is multiblock
# SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_02_segmentation_st.vti", OutputPort(tTKMergeandContourTreeFTM_isabel_02vti_st,2)) # u because unstructured grid, vtm is multiblock
# # 03_jt
# SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_03_nodes_jt.vtu", tTKMergeandContourTreeFTM_isabel_03vti_jt) # u because unstructured grid, vtm is multiblock
# SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_03_arcs_jt.vtu", OutputPort(tTKMergeandContourTreeFTM_isabel_03vti_jt,1)) # u because unstructured grid, vtm is multiblock
# SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_03_segmentation_jt.vti", OutputPort(tTKMergeandContourTreeFTM_isabel_03vti_jt,2)) # u because unstructured grid, vtm is multiblock
# # 03_st
# SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_03_nodes_st.vtu", tTKMergeandContourTreeFTM_isabel_03vti_st) # u because unstructured grid, vtm is multiblock
# SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_03_arcs_st.vtu", OutputPort(tTKMergeandContourTreeFTM_isabel_03vti_st,1)) # u because unstructured grid, vtm is multiblock
# SaveData(basepath+"isabel_small/single_merge_tree_components/isabel_03_segmentation_st.vti", OutputPort(tTKMergeandContourTreeFTM_isabel_03vti_st,2)) # u because unstructured grid, vtm is multiblock
