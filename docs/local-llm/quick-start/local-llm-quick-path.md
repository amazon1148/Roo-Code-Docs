# Quick Start Guide: Local LLMs

## Difficulty Level
Quick-start

## Estimated Reading Time
15 minutes

## Prerequisites
None - this is the starting point

## Topics Covered
- Basic system requirements
- Model selection basics
- Initial setup process
- First model run
- Basic troubleshooting

## Quick Setup Steps

```mermaid
graph TD
    Start([Begin Setup]) --> Hardware[Check Hardware]
    Hardware --> Model[Select Model]
    Model --> Install[Install Tools]
    Install --> Configure[Basic Config]
    Configure --> Test[Test Model]
    Test --> Use[Start Using]
```

## 1. Check Your Hardware
Before starting, verify your system meets the minimum requirements:
- CPU/GPU specifications
- Memory requirements
- Storage space needed

See [hardware requirements](hardware-requirements.md) for detailed specifications.

## 2. Choose Your Model
Select a model based on your hardware:

### 8GB VRAM or Less
- Gemma 7B
- Phi-2
- Other small models

### 16GB VRAM
- CodeLlama 13B
- Mistral Small
- Medium-sized models

### 24GB+ VRAM
- Qwen 2.5 Coder
- DeepSeek 33B
- Large models

## 3. Basic Setup

### Install Required Tools
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## 4. First Run

### Download Model
```bash
ollama pull qwen2.5-coding
# Or for limited hardware
ollama pull gemma-7b
```

### Basic Test
```python
# Write a hello world program
```

## Common Issues
1. Verify hardware requirements
2. Check model compatibility
3. Confirm tool installation
4. Review error messages

## Related Topics
- [Hardware Requirements](hardware-requirements.md) - System specifications
- [Model Selection](model-selection.md) - Choosing the right model
- [Tool Usage Guide](tool-usage.md) - Using LLM tools
- [Troubleshooting](troubleshooting.md) - Common issues and solutions

## Technical Terms
- VRAM - Virtual RAM, crucial for model loading
- Model Quantization - Technique for reducing model size
- Context Window - Model's working memory size
- Token Usage - Text processing units

## Next Steps
1. [Hardware Requirements](hardware-requirements.md)
2. [Model Selection](model-selection.md)
3. [Tool Usage Guide](tool-usage.md)
4. [Basic Troubleshooting](troubleshooting.md)
5. [Advanced Topics](../advanced/architecture.md)