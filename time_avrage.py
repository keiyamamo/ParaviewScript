# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Xdmf3ReaderS'
wSSxdmf = Xdmf3ReaderS(registrationName='WSS.xdmf', FileName=['/Users/keiyamamoto/Documents/VaSP/src/vasp/simulations/offset_stenosis_results/14/Hemodynamic_indices/WSS.xdmf'])

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

UpdatePipeline(time=0.95, proxy=wSSxdmf)

# create a new 'Temporal Statistics'
temporalStatistics1 = TemporalStatistics(registrationName='TemporalStatistics1', Input=wSSxdmf)

# Properties modified on temporalStatistics1
temporalStatistics1.ComputeMinimum = 0
temporalStatistics1.ComputeMaximum = 0
temporalStatistics1.ComputeStandardDeviation = 0

UpdatePipeline(time=0.95, proxy=temporalStatistics1)

# save data
SaveData('/Users/keiyamamoto/Documents/VaSP/src/vasp/simulations/offset_stenosis_results/14/Hemodynamic_indices/time_averaged_wss.vtu', proxy=temporalStatistics1, PointDataArrays=['WSS_average'],
    DataMode='Ascii')