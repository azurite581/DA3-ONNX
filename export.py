import torch
import torch.nn as nn
from depth_anything_3.api import DepthAnything3

class DA3ExportWrapper(nn.Module):
    def __init__(self, model):
        super().__init__()
        self.model = model

    def forward(self, x):
        x = x.unsqueeze(1)

        with torch.autocast(device_type="cpu", enabled=False):
            output = self.model(
                x,
                extrinsics=None,
                intrinsics=None,
                export_feat_layers=[],
                infer_gs=False,
            )
        depth = output["depth"]
        return depth

def export_to_onnx():
    device = torch.device("cpu")
    model_id = "depth-anything/DA3METRIC-LARGE"
    print(f"Loading {model_id}...")

    da3_model = DepthAnything3.from_pretrained(model_id).to(device)
    da3_model = da3_model.float()
    da3_model.eval()

    wrapped_model = DA3ExportWrapper(da3_model).eval()

    dummy_input = torch.randn(1, 3, 518, 518, device=device, dtype=torch.float32)
    output_path = "onnx/depth_anything_3.onnx"

    with torch.no_grad():
        torch.onnx.export(
            wrapped_model,
            dummy_input,
            output_path,
            export_params=True,
            opset_version=18,
            external_data=False,
            do_constant_folding=True,
            input_names=["input"],
            output_names=["depth"],
        )

    print("ONNX export completed successfully!")

if __name__ == "__main__":
    export_to_onnx()
