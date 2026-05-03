# Setup Guide for Vietnamese Medical Q&A System

## Prerequisites

- Python 3.10+
- pip or conda
- Git
- (Optional) CUDA-capable GPU for faster fine-tuning on Colab

## Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/dibawng-ui/vietnamese-medical-qa-rag.git
cd vietnamese-medical-qa-rag
```

### 2. Create Virtual Environment

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n med-qa python=3.10
conda activate med-qa
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python -c "import torch; print(f'PyTorch version: {torch.__version__}')"
python -c "import transformers; print(f'Transformers version: {transformers.__version__}')"
```

## Google Colab Setup (Recommended for Fine-tuning)

### 1. Open Colab Notebook

- Go to https://colab.research.google.com
- Click "File" → "Open notebook"
- Go to GitHub tab and search: `dibawng-ui/vietnamese-medical-qa-rag`
- Open `notebooks/01_finetuning_llama2_colab.ipynb`

### 2. Enable GPU

- Click "Runtime" → "Change runtime type"
- Select "GPU" (T4 is available for free)
- Click "Save"

### 3. Authenticate HuggingFace

```python
from huggingface_hub import login
login()  # Will prompt for your HuggingFace token
```

Get your token from: https://huggingface.co/settings/tokens

### 4. Install Dependencies in Colab

```python
!pip install -q -U bitsandbytes
!pip install -q -U git+https://github.com/huggingface/transformers.git
!pip install -q -U git+https://github.com/huggingface/peft.git
!pip install -q -U git+https://github.com/huggingface/accelerate.git
```

## Directory Structure

Make sure to create these directories if they don't exist:

```bash
mkdir -p data/raw/documents
mkdir -p data/processed
mkdir -p data/embeddings
mkdir -p models
mkdir -p experiments/results
```

## Configuration

Edit `config/config.yaml` to customize settings:

- LLM model size (7B or 13B)
- Embedding model
- Fine-tuning parameters
- RAG settings

## Testing Installation

### Test data loading

```python
from src.data_preparation import DataLoader

loader = DataLoader("data/raw/documents/")
docs = loader.load_txt_files()
print(f"Loaded {len(docs)} documents")
```

### Test embeddings

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-case-sensitive-v2')
embedding = model.encode("Bệnh cúm là gì?")
print(f"Embedding dimension: {len(embedding)}")
```

## Common Issues & Solutions

### Issue 1: CUDA not found

**Solution:**
```bash
# Check CUDA installation
nvcc --version

# For Colab, CUDA should be available automatically
```

### Issue 2: Out of memory

**Solution:**
- Use QLoRA instead of LoRA for smaller memory footprint
- Reduce batch size in config.yaml
- Use 7B model instead of 13B

### Issue 3: HuggingFace authentication fails

**Solution:**
```bash
huggingface-cli login
# Enter your token when prompted
```

## Next Steps

1. Read [data_collection.md](data_collection.md) to create QA pairs
2. Follow [experiment_guide.md](experiment_guide.md) to run fine-tuning
3. Check [evaluation_guide.md](evaluation_guide.md) for evaluation
