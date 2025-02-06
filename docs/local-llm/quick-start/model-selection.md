# Model Selection Guide

## Difficulty Level
Quick-start

## Estimated Reading Time
25 minutes

## Prerequisites
- [Quick Start Guide](local-llm-quick-path.md)
- [Hardware Requirements](hardware-requirements.md)

## Topics Covered
- Model size considerations
- Hardware compatibility
- Performance expectations
- Quantization options
- Model setup steps

```mermaid
graph TD
    Start([Choose Model]) --> VRAM{VRAM Available?}
    VRAM -->|8GB| Small[Small Models]
    VRAM -->|16GB| Medium[Medium Models]
    VRAM -->|24GB+| Large[Large Models]
    Small --> SmallRec["Gemma 7B, Phi-2"]
    Medium --> MediumRec["CodeLlama 13B, Mistral Small"]
    Large --> LargeRec["Qwen 2.5 Coder, DeepSeek 33B"]
```

## Quick Model Recommendations

### Best Overall Models
1. **Qwen 2.5 Coder** (32B)
   - Excellent coding ability
   - Requires 24GB+ VRAM

2. **Mistral Small** (24B)
   - Good balance of size/performance
   - Works with 16GB VRAM

3. **CodeLlama** (13B)
   - Good for basic to medium tasks
   - Works on mid-range hardware

### For Limited Hardware (≤8GB VRAM)
- **Gemma** (7B)
  - Basic code completion
  - Fits in 8GB VRAM

## Model Settings Guide
| Setting | Small Models | Medium Models | Large Models |
|---------|--------------|---------------|--------------|
| Context | 8k tokens | 16k tokens | 32k tokens |
| Temp | 0.7 | 0.7 | 0.7 |
| Top P | 0.9 | 0.9 | 0.9 |

## Related Topics
- [Hardware Requirements](hardware-requirements.md) - System needs
- [Token Management](../advanced/token-management.md) - Context handling
- [Model Tuning](../advanced/model-tuning.md) - Performance optimization
- [Tool Usage](tool-usage.md) - Setup instructions

## Technical Terms
- Context Window - Model's working memory size
- Temperature - Output randomness control
- Top-P - Token sampling parameter
- Quantization - Model compression method

## Next Steps
1. [Tool Usage Guide](tool-usage.md)
2. [Model Tuning](../advanced/model-tuning.md)
3. [Token Management](../advanced/token-management.md)