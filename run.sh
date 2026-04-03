#!/bin/sh

if [ ! -d "onnx" ]; then
    mkdir onnx
fi

uv sync || exit 1
uv run python export.py || exit 1
uv run python convert_fp16.py || exit 1
