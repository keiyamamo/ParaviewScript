# trace generated using paraview version 5.12.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()



extract_time = 0.9100000000000003
max_value = 30.0

# find source
displacement_fluidxdmf = FindSource('displacement_fluid.xdmf')

# set active source
SetActiveSource(displacement_fluidxdmf)

# create a new 'Warp By Vector'
warpByVector1 = WarpByVector(registrationName='WarpByVector1', Input=displacement_fluidxdmf)

# find source
tawss_vtu = FindSource('TAWSS.xdmf')

# Properties modified on warpByVector1
warpByVector1.ScaleFactor = -1.0

UpdatePipeline(time=0.01, proxy=warpByVector1)

# set active source
SetActiveSource(tawss_vtu)

# create a new 'Resample With Dataset'
resampleWithDataset1 = ResampleWithDataset(registrationName='ResampleWithDataset1', SourceDataArrays=tawss_vtu,
    DestinationMesh=warpByVector1)

# Properties modified on resampleWithDataset1
resampleWithDataset1.SnapToCellWithClosestPoint = 1

UpdatePipeline(time=extract_time, proxy=resampleWithDataset1)

# set active source
SetActiveSource(displacement_fluidxdmf)

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[resampleWithDataset1, displacement_fluidxdmf])

UpdatePipeline(time=extract_time, proxy=appendAttributes1)

# create a new 'Warp By Vector'
warpByVector2 = WarpByVector(registrationName='WarpByVector2', Input=appendAttributes1)

UpdatePipeline(time=extract_time, proxy=warpByVector2)

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=warpByVector2)

UpdatePipeline(time=extract_time, proxy=extractSurface1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(registrationName='GenerateSurfaceNormals1', Input=extractSurface1)

UpdatePipeline(time=extract_time, proxy=generateSurfaceNormals1)

# get color transfer function/color map for 'TAWSS'
TAWSSLUT = GetColorTransferFunction('TAWSS')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
TAWSSLUT.ApplyPreset('Rainbow Desaturated', True)

# Rescale transfer function
TAWSSLUT.RescaleTransferFunction(0.0, max_value)

# get opacity transfer function/opacity map for 'TAWSS'
TAWSSPWF = GetOpacityTransferFunction('TAWSS')

# get 2D transfer function for 'TAWSS'
TAWSSTF2D = GetTransferFunction2D('TAWSS')

# Rescale transfer function
TAWSSPWF.RescaleTransferFunction(0.0, max_value)

# Rescale 2D transfer function
TAWSSTF2D.RescaleTransferFunction(0.0, max_value, 0.0, 1.0)

