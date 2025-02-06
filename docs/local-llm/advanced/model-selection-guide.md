# Model Selection Guide for Local Large Language Models

## Overview

This guide helps developers select appropriate local Large Language Models (LLMs) for use with Roo Code, focusing on compatibility, performance, and hardware requirements.

## Comparative Model Evaluation

| Feature | Ollama | `Llama.cpp` | vLLM | KoboldCpp |
|---------|---------|--------------|-------|------------|
| Ease of Use | Flexible library selection | Lightweight C++ implementation | Scalable with customization | User-friendly GUI + CLI |
| Hardware Support | Optimized for Nvidia GPUs | Broad CPU/GPU support | Focus on scalability | GPU-focused; GGUF quantization |
| Latency | Low latency | Moderate latency | Higher latency in real-time | Low latency with optimizations |
| Throughput | Moderate | High with optimized setup | High in batch processing | High with GPU optimization |
| Customization | Manual library overrides | Open-source flexibility | Extensive configuration options | Advanced quantization control |

## Performance Benchmarks

### KoboldCpp Performance
- Up to 65 tokens/second on optimized Nvidia CUDA setups
- Supports up to 8k context lengths
- Advanced layer offloading

### Llama.cpp Performance
- ~13.89 tokens/second with full GPU offload
- ~3.47 tokens/second without GPU support

## Recommended Models for Roo Code

### Top Recommended Models
1. Qwen 2.5 Coder
2. DeepSeek R1
3. Gemma 9B
4. Mistral Small Coder

## Model Selection Criteria

### Compatibility Factors
- Minimum 32k token context window
- Strong tool usage support
- Coding-specific fine-tuning
- Compatibility with Roo Code extensions

### Hardware Requirements
- Minimum: RTX 4080 or equivalent
- Recommended: 32GB Memory
- Ideal: High-end GPU with 64GB+ VRAM

## Model Selection Calculation

### VRAM Compatibility
- Use the formula: (model size) * 1.2 < Available VRAM
- Prefer models 70B or larger for complex coding tasks

## Model Evaluation Resources
- [Hugging Face BigCode Leaderboard](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard)
- Community testing and feedback
- Continuous model performance tracking

## Troubleshooting Model Selection

### Common Challenges
- Insufficient VRAM
- Limited context window
- Poor tool invocation capabilities
- Inconsistent code generation

### Mitigation Strategies
- Use quantization techniques
- Upgrade hardware
- Select models with broader compatibility
- Test thoroughly with Roo Code

## See Also
- [Hardware Optimization](hardware-optimization.md)
- [Model Tuning](model-tuning.md)
- [Token Management](token-management.md)
