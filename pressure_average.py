# trace generated using paraview version 5.12.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *


#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

file_name = "pressure_25_to_1000_amplitude_time_average.vtu"
# file_name = "displacement_25_to_1000_amplitude_time_average.vtu"
# file_name = "displacement_0_to_25_time_average.vtu"
# file_name = "MaxPrincipalStrain_avg.xdmf"
# file_name="GreenLagrangeStrain_25_to_200_max_principal_amplitude_time_average.vtu"
# file_name="TAWSS.xdmf"
# file_name="OSI.xdmf"
# file_name="RRT.xdmf"
data = FindSource(file_name)
# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=data)

# Properties modified on clip1
clip1.ClipType = 'Sphere'
clip1.Scalars = ['POINTS', '']
clip1.Crinkleclip = 1

# Properties modified on clip1.ClipType
case_name="case_16"
print(case_name)

if case_name == "case_3":
    clip1.ClipType.Center = [0.108766998291016, 0.103787872314453, 0.0603882255554199]
    clip1.ClipType.Radius = 0.004
elif case_name == "case_9":
    clip1.ClipType.Center = [0.123043, 0.13458, 0.064187]
    clip1.ClipType.Radius = 0.004
elif case_name == "case_12":
    clip1.ClipType.Center = [0.114591857910156, 0.116493148803711, 0.0531824569702148]
    clip1.ClipType.Radius = 0.0069 
elif case_name == "case_16":
    clip1.ClipType.Center = [0.072546, 0.133805, 0.05778]
    clip1.ClipType.Radius = 0.007
else:
    print("Invalid case number")
    exit(1)

UpdatePipeline(time=0.0, proxy=clip1)

# create a new 'Python Annotation'
pythonAnnotation1 = PythonAnnotation(registrationName='PythonAnnotation1', Input=clip1)
pythonAnnotation1.ArrayAssociation = 'Point Data'

# Properties modified on pythonAnnotation1
pythonAnnotation1.Expression = 'mean(pressure_average)'

UpdatePipeline(time=0.0, proxy=pythonAnnotation1)

stringValue = FetchData(pythonAnnotation1)[0].GetRowData().GetAbstractArray(0).GetValue(0)

print(stringValue)

# clean up
Delete(pythonAnnotation1)
Delete(calculator1)
Delete(clip1)
Delete(data)