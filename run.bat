@echo off

if not exist onnx (
    mkdir onnx
)

uv sync || exit /b
uv run python export.py || exit /b
uv run python convert_fp16.py || exit /b
