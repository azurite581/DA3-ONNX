import onnx
from onnxconverter_common import float16

model = onnx.load("onnx/depth_anything_3.onnx")
model_fp16 = float16.convert_float_to_float16(model, min_positive_val=1e-7, max_finite_val=1e4, keep_io_types=True)
onnx.save(model_fp16, "onnx/depth_anything_3_fp16.onnx")

print("FP16 conversion completed successfully!")
