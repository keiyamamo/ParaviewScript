# trace generated using paraview version 5.12.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
displacement_0_to_25_time_averagevtu = FindSource('displacement_0_to_25_time_average.vtu')

# set active source
SetActiveSource(displacement_0_to_25_time_averagevtu)

# find source
displacement_solidxdmf = FindSource('displacement_solid.xdmf')

# create a new 'Resample With Dataset'
resampleWithDataset1 = ResampleWithDataset(registrationName='ResampleWithDataset1', SourceDataArrays=displacement_0_to_25_time_averagevtu,
    DestinationMesh=displacement_solidxdmf)

UpdatePipeline(time=0.9510000000000366, proxy=resampleWithDataset1)

# set active source
SetActiveSource(displacement_solidxdmf)

# create a new 'Append Attributes'
appendAttributes1 = AppendAttributes(registrationName='AppendAttributes1', Input=[resampleWithDataset1, displacement_solidxdmf])

UpdatePipeline(time=0.9510000000000366, proxy=appendAttributes1)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=appendAttributes1)

# Properties modified on calculator1
calculator1.Function = 'displacement_0_to_25_average-displacement'

UpdatePipeline(time=0.9510000000000366, proxy=calculator1)

# create a new 'Warp By Vector'
warpByVector1 = WarpByVector(registrationName='WarpByVector1', Input=calculator1)

UpdatePipeline(time=0.9510000000000366, proxy=warpByVector1)

# Properties modified on warpByVector1
warpByVector1.Vectors = ['POINTS', 'displacement_0_to_25_average']

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=warpByVector1)

UpdatePipeline(time=0.9510000000000366, proxy=extractSurface1)

# create a new 'Generate Surface Normals'
generateSurfaceNormals1 = GenerateSurfaceNormals(registrationName='GenerateSurfaceNormals1', Input=extractSurface1)

UpdatePipeline(time=0.9510000000000366, proxy=generateSurfaceNormals1)