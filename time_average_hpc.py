"""
This script works with Paraview on Saga HPC.
"""

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
    # create a new 'Xdmf3ReaderS'
    print(" -- Reading file: ", input_path)
    xdmf_file = XDMFReader(FileNames=[input_path])
    print(" -- File read successfully")
    # create a new 'Temporal Statistics'
    print(" -- Computing time average")
    temporalStatistics1 = TemporalStatistics(registrationName='TemporalStatistics1', Input=xdmf_file)

    # Properties modified on temporalStatistics1
    temporalStatistics1.ComputeMinimum = 0
    temporalStatistics1.ComputeMaximum = 0
    temporalStatistics1.ComputeStandardDeviation = 0
    output_path = input_path.replace('.xdmf', '_time_average.vtu')
    # save data

    SaveData(output_path, proxy=temporalStatistics1, DataMode='Ascii')
    print(" -- Time average computed successfully and saved to: ", output_path)


def main():
    args = parse_command_line_args()
    compute_time_average(args.input_path)


if __name__ == "__main__":
    main()