# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
from pathlib import Path
import argparse
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

def parse_command_line_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", type=str, required=True)
    return parser.parse_args()


def compute_time_average(input_path):
    # based on the input path, defined registration name and file name
    file_name = Path(input_path).name

    # create a new 'Xdmf3ReaderS'
    xdmf_file = Xdmf3ReaderS(registrationName=file_name, FileName=[input_path])

    # create a new 'Temporal Statistics'
    temporalStatistics1 = TemporalStatistics(registrationName='TemporalStatistics1', Input=xdmf_file)

    # Properties modified on temporalStatistics1
    temporalStatistics1.ComputeMinimum = 0
    temporalStatistics1.ComputeMaximum = 0
    temporalStatistics1.ComputeStandardDeviation = 0
    output_path = input_path.replace('.xdmf', '_time_average.vtu')
    # save data
    SaveData(output_path, proxy=temporalStatistics1, DataMode='Ascii')

def main():
    args = parse_command_line_args()
    compute_time_average(args.input_path)

if __name__ == "__main__":
    main()