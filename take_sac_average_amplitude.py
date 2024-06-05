# trace generated using paraview version 5.12.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *
import argparse
from pathlib import Path
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source

def parse_command_line_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, required=True)
    parser.add_argument("--case_name", type=str, required=True)
    return parser.parse_args()

def compute_sac_average(input_path, case_name):
    # based on the input path, defined registration name and file name
    file_name = Path(input_path).name
    # data = XMLUnstructuredGridReader(registrationName=file_name, FileName=[input_path])
    data = Xdmf3ReaderS(registrationName=file_name, FileName=[input_path])
    # create a new 'Clip'
    clip1 = Clip(registrationName='Clip1', Input=data)

    # Properties modified on clip1
    clip1.ClipType = 'Sphere'
    clip1.Scalars = ['POINTS', '']
    clip1.Crinkleclip = 1

    # Properties modified on clip1.ClipType

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
        ValueError('Invalid case number')

    UpdatePipeline(time=0.0, proxy=clip1)
    vector_name = clip1.GetPointDataInformation().GetArray(0).Name
    # calculator1 = Calculator(registrationName='Calculator1', Input=clip1)
    # # calculator1.Function = f'mag({vector_name})'
    # calculator1.Function = 'displacement_25_to_1000_amplitude_average_Z'
    # breakpoint()
    # UpdatePipeline(time=0.0, proxy=calculator1)
    # create a new 'Python Annotation'
    pythonAnnotation1 = PythonAnnotation(registrationName='PythonAnnotation1', Input=clip1)
    pythonAnnotation1.ArrayAssociation = 'Point Data'

    # Properties modified on pythonAnnotation1
    pythonAnnotation1.Expression = f'mean({vector_name})'

    UpdatePipeline(time=0.0, proxy=pythonAnnotation1)

    stringValue = FetchData(pythonAnnotation1)[0].GetRowData().GetAbstractArray(0).GetValue(0)

    print(stringValue)

def main():
    args = parse_command_line_args()
    compute_sac_average(args.input_path, args.case_name)

if __name__ == "__main__":
    main()