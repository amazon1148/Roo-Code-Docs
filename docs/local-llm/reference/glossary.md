# Glossary of Local LLM Terms

## Core LLM Concepts

### A

**API Endpoint**
: A URL that exposes the functionality of an LLM runner, allowing other applications (like Roo Code) to interact with it programmatically.

### C

**Context Window**
: The amount of text (in tokens) that a model can consider at one time when generating output. Smaller context windows limit the model's ability to maintain coherence and understand complex tasks. Context window size directly impacts VRAM usage and model performance.

**Codebase Context**
: The project files or code snippets that the language model can access and reference when generating responses or making changes.

### D

**Distillation**
: A technique for creating smaller, more efficient LLMs by training them to mimic the behavior of larger models. While this reduces resource requirements, distilled models may sacrifice some performance and capabilities.

### G

**GGUF**
: A file format for storing quantized LLMs, commonly used with `llama.cpp` and KoboldCpp. Offers various quantization levels for balancing model size and performance.

**Generic Responses**
: When a model fails to engage with the specific input and instead generates non-relevant, generic output. Often indicates issues with context window size or model capabilities.

### I

**Inference**
: The process of running a trained LLM to generate output based on a given input prompt. Inference speed varies based on hardware capabilities and model optimization.

### L

**Large Language Model (LLM)**
: A deep learning model trained on massive datasets of text and code, capable of generating human-quality text, translating languages, writing creative content, and answering questions informatively.

**Local LLM Runner**
: Software that enables running LLMs on local hardware (CPU or GPU). Examples include Ollama, `llama.cpp`, vLLM, LM Studio, and KoboldCpp.

### M

**MLX**
: A file format optimized for Apple Silicon hardware, used by LM Studio to improve performance on Apple devices.

**Model Library**
: A collection of pre-trained models that can be easily downloaded and used with specific LLM runners.

### P

**Parameters**
: The adjustable values within an LLM that determine its behavior and complexity. More parameters generally mean a more capable model but also higher resource requirements.

**Provider Settings**
: The configuration options within Roo Code that allow users to specify how to interact with a model, including API endpoints, model selection, and performance parameters.

### Q

**Quantization**
: A technique used to reduce model size by using lower precision numbers. This significantly reduces resource requirements and improves inference speed but may impact model performance. Common types include:
- 4-bit: Highest compression, lowest accuracy
- 8-bit: Balanced compression and accuracy
- 16-bit (FP16): Lowest compression, highest accuracy

### S

**System Message**
: Special instructions provided to the model that define its role, behavior, and capabilities. These messages consume context window space but are crucial for proper model function.

## Hardware Terms

### C

**CPU (Central Processing Unit)**
: The primary processor in a computer. While not the primary compute device for most LLM operations, it's still important for overall system performance.

### G

**GPU (Graphics Processing Unit)**
: The primary compute device for running LLMs locally. GPU capabilities, particularly VRAM, are crucial for model performance.

### R

**RAM (Random Access Memory)**
: System memory used for general operations. If GPU VRAM is insufficient, some operations may fall back to system RAM, significantly impacting performance.

### V

**VRAM (Video RAM)**
: Memory on the GPU used for storing model weights and performing calculations. VRAM capacity is often the primary limiting factor in running larger models or using longer context windows. Requirements scale with:
- Model size
- Context window length
- Batch size
- Quantization level

## Performance Metrics

### C

**Context Length**
: The maximum number of tokens a model can process at once. Longer context allows for more comprehensive understanding but requires more VRAM.

### T

**Temperature**
: A parameter that controls the randomness in model outputs. Higher values make the output more diverse but potentially less focused.

**Token Usage**
: The number of tokens consumed by inputs and outputs. Important for managing context window limitations and ensuring efficient model usage.

**Top-P (Nucleus Sampling)**
: A parameter that controls the cumulative probability cutoff for token selection during text generation.

## Common Issues

### C

**Code Looping**
: When a model repeatedly generates the same code block or message, often indicating context window limitations or system prompt issues.

### O

**Out of Memory Errors**
: Occurs when the combined requirements of the model, context window, and operations exceed available VRAM.

## See Also

- [Architecture Guide](../advanced/architecture.md) - Technical implementation details
- [Hardware Requirements](../quick-start/hardware-requirements.md) - Detailed hardware specifications
- [Model Selection](../quick-start/model-selection.md) - Guide to choosing appropriate models