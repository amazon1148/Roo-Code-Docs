---
title: Quick Start Guide
nav_order: 1
parent: Local LLM Documentation
description: A beginner-friendly guide to getting started with local Large Language Models
---

# Quick Start Guide: Local LLMs

A comprehensive guide to get you started with local Large Language Models quickly and efficiently.

## Difficulty Level
Quick-start

## Estimated Reading Time
15 minutes

{: .note }
This guide assumes no prior experience with LLMs. Start here if you're new to local AI models.

## Prerequisites
None - this is the starting point for working with local LLMs.

## Topics Covered
- Basic system requirements
- Model selection basics
- Initial setup process
- First model run
- Basic troubleshooting

## Setup Process

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

{: .content-card }
Before starting, verify your system meets the minimum requirements:
- CPU/GPU specifications
- Memory requirements
- Storage space needed

See [hardware requirements](hardware-requirements.md) for detailed specifications.

## 2. Choose Your Model

Select a model based on your hardware capabilities:

| VRAM Available | Recommended Models | Use Case |
|----------------|-------------------|-----------|
| 8GB or Less | Gemma 7B, Phi-2 | Basic tasks |
| 16GB | CodeLlama 13B, Mistral Small | Development |
| 24GB+ | Qwen 2.5 Coder, DeepSeek 33B | Production |

## 3. Basic Setup

### Install Required Tools
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

## 4. First Run

{: .tip }
Start with a smaller model to verify your setup before moving to larger models.

### Download Model
```bash
# For systems with limited resources
ollama pull gemma-7b

# For more capable systems
ollama pull qwen2.5-coding
```

### Basic Test
```python
# Write a hello world program
print("Hello, World!")
```

## Common Issues

1. Hardware Verification
   - Check GPU compatibility
   - Verify VRAM availability
   - Confirm driver versions

2. Software Setup
   - Validate installation
   - Check dependencies
   - Review error messages

## Related Topics
- [Hardware Requirements](hardware-requirements.md) - Detailed system specifications
- [Model Selection](model-selection.md) - In-depth model comparison
- [Tool Usage Guide](tool-usage.md) - Comprehensive tool documentation
- [Troubleshooting](troubleshooting.md) - Common issues and solutions

## Next Steps
1. Review [Hardware Requirements](hardware-requirements.md)
2. Choose a model from [Model Selection](model-selection.md)
3. Learn tool basics in [Tool Usage Guide](tool-usage.md)
4. Check [Basic Troubleshooting](troubleshooting.md)
5. Explore [Advanced Topics](../advanced/architecture.md)
