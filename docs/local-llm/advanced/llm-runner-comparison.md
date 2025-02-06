# LLM Runner Comparison

## Overview

This guide provides a detailed comparison of different LLM runners for local deployment.

## Comparison Matrix

| Feature | Ollama | LM Studio | KoboldCpp | Text Generation WebUI |
|---------|---------|------------|-----------|----------------------|
| Installation | Single curl command | GUI installer | Manual setup | Python pip install |
| Interface | CLI + API | GUI + API | GUI + API | Web UI + API |
| Model Management | Built-in pulls | Manual downloads | Manual downloads | HF integration |
| Hardware Support | CUDA + CPU | CUDA + CPU | CUDA + CPU | CUDA + CPU + ROCm |
| API Performance | ~65 tokens/s | Varies by model | ~13.89 tokens/s | ~3.47 tokens/s |
| VRAM Usage | Efficient | Standard | Very efficient | Standard |
| Context Window | Up to 32k | Model dependent | Model dependent | Model dependent |
| Quantization | Built-in | Custom GGUF | GGUF support | Multiple formats |

## Development Environment Comparison

### Ollama
**Pros:**
- One-line installation
- Built-in model management
- REST API + WSS support
- Docker integration

**Cons:**
- Limited model format support
- Fixed API implementation
- Less granular control

**Best for:** Quick deployment, container environments

### LM Studio
**Pros:**
- User-friendly GUI
- Multiple model sources
- Flexible quantization
- Built-in chat interface

**Cons:**
- Manual model downloads
- Windows/Mac focus
- Limited CLI options

**Best for:** Desktop development, model testing

### KoboldCpp
**Pros:**
- Memory efficient
- Advanced quantization
- High performance
- Full API access

**Cons:**
- Complex setup
- Manual dependency management
- Limited GUI features

**Best for:** Performance-critical deployments

### Text Generation WebUI
**Pros:**
- Extensive features
- Multiple backends
- Active community
- Training support

**Cons:**
- Complex configuration
- Higher resource usage
- More setup steps

**Best for:** Research, model fine-tuning

## Setup Instructions

### Ollama
```bash
# Install
curl -fsSL https://ollama.com/install.sh | sh

# Run
ollama run qwen2.5-coding
```

### LM Studio
1. Download installer
2. Install application
3. Download models
4. Configure API server

### KoboldCpp
1. Download release
2. Install dependencies
3. Configure CUDA
4. Run executable

### Text Generation WebUI
```bash
pip install text-generation-webui
python server.py --api
```

## Integration Notes

### API Endpoints
All runners support:
- `/api/generate` - Basic completion
- `/api/chat` - Chat completion
- Streaming responses
- Parameter control

### Language Support
- Python clients available for all
- REST APIs are language-agnostic
- WebSocket support varies

## Performance Comparison

### Token Generation Speed
- KoboldCpp/GPU: ~65 tokens/second
- llama.cpp/GPU: ~13.89 tokens/second
- CPU-only: ~3.47 tokens/second

### Memory Usage
Varies by model size and quantization:
- 4-bit: ~8GB VRAM
- 8-bit: ~16GB VRAM
- Full precision: ~24GB+ VRAM

## See Also
- [Hardware Optimization](hardware-optimization.md)
- [Model Selection](../quick-start/model-selection.md)
- [Tool Usage](../quick-start/tool-usage.md)