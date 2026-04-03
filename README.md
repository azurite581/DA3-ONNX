# DA3-ONNX

ONNX conversion for [Depth Anything 3](https://github.com/ByteDance-Seed/Depth-Anything-3).

## Prerequisites

- Git
- Python >=3.10, <3.13
- [uv](https://docs.astral.sh/uv/)

## Tested Environment

- Windows 11 Home
- Python 3.12.10
- uv 0.11.3

## Usage

1. Clone this repository.
2. Run `run.bat` or `run.sh` depending on your OS.
These scripts create a virtual environment using uv, install the dependencies, and execute the ONNX conversion script.
3. If successful, the following ONNX files will be output under `onnx/`:
    - `depth_anything_3.onnx`
    - `depth_anything_3_fp16.onnx`

### Output Model Information

- `depth_anything_3.onnx`
  - Model: `DA3METRIC_LARGE`
  - Input: `[1, 3, 518, 518]`, dtype float32
  - Output: `[1, 3, 518, 518]`, dtype float32
  - Device: cpu
  - Monocular depth estimation only
  - Size: Approx. 1.25 GB
- `depth_anything_3_fp16.onnx`: A float16 version of `depth_anything_3.onnx`. Input and output remain in float32. The size is approximately halved (approx. 650 MB).

Please check `export.py` for more details.

## Notes

- This has not been tested in environments other than the tested environment.
- Sufficient optimization processing has not been performed.
- Please edit `export.py` or `convert_fp16.py` as needed.

## License

Apache License 2.0

The licenses for each model follow the original [Depth Anything 3](https://github.com/ByteDance-Seed/Depth-Anything-3).

## Acknowledgments

- [Depth Anything 3](https://github.com/ByteDance-Seed/Depth-Anything-3)
- [Depth Anything 3 ONNX](https://github.com/MoonCodeMaster/Depth-Anything-3-Onnx)
- [Depth Anything V3 TensorRT ROS 2 Node](https://github.com/ika-rwth-aachen/ros2-depth-anything-v3-trt)
