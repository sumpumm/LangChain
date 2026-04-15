# LangChain Learning Repository

This repository contains comprehensive examples and implementations of various LangChain components, demonstrating the key concepts and functionalities of the LangChain library for building applications with Large Language Models (LLMs).

## Overview

LangChain is a powerful framework for developing applications powered by language models. This repository serves as a learning resource covering all major components of LangChain, from basic chains to advanced retrieval-augmented generation (RAG) systems.

## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Core Components](#core-components)
  - [Chains](#chains)
  - [Document Loaders](#document-loaders)
  - [Models](#models)
  - [Output Parsers](#output-parsers)
  - [Prompts](#prompts)
  - [Retrievers](#retrievers)
  - [Runnables](#runnables)
  - [Structured Output](#structured-output)
  - [Text Splitters](#text-splitters)
  - [Vector Stores](#vector-stores)
- [Key Learnings](#key-learnings)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd LangChain
```

2. Create a virtual environment:
```bash
python -m venv env
source env/Scripts/activate  # On Windows
# or
source env/bin/activate     # On macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with your API keys:
```
HUGGINGFACEHUB_ACCESS_TOKEN=your_huggingface_token
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_key
```

## Project Structure

```
LangChain/
├── chains/                    # Different types of chains
│   ├── simple_chain.py       # Basic chain with prompt, model, and parser
│   ├── sequential_chain.py   # Multi-step sequential chains
│   ├── parallel_chain.py     # Parallel execution chains
│   └── conditional_chain.py  # Conditional routing chains
├── Document_loaders/         # Document loading utilities
│   ├── text_loader.py        # Loading text files
│   ├── pypdf_loader.py       # Loading PDF documents
│   ├── webbase_loader.py     # Loading web content
│   └── directory_loader.py   # Loading entire directories
├── models/                   # LLM and embedding models
│   ├── ChatModels/          # Chat-based language models
│   ├── EmbeddingModels/     # Text embedding models
│   └── LLMS/                # Traditional language models
├── output parser/           # Output parsing and formatting
│   ├── jsonoutputparser.py  # JSON output parsing
│   ├── pydanticoutputparser.py # Pydantic model parsing
│   ├── stroutputparser.py   # String output parsing
│   └── structured_output_parser.py # Structured data parsing
├── prompts/                 # Prompt templates and management
│   ├── promptTemplate.py    # Basic prompt templates
│   ├── chat_prompt_template.py # Chat-specific prompts
│   ├── message_placeholder.py # Dynamic message handling
│   └── chatbot.py           # Complete chatbot implementation
├── retrievers/              # Information retrieval systems
│   └── wikipedia_retriever.ipynb # Wikipedia-based retrieval
├── Runnables/               # Runnable components
│   ├── runnable_sequence.py # Sequential runnable execution
│   ├── runnable_parallel.py # Parallel runnable execution
│   ├── runnable_branch.py   # Conditional branching
│   ├── runnable_lambda.py   # Custom lambda runnables
│   └── runnable_passthrough.py # Pass-through runnables
├── structured_output/       # Structured data handling
│   ├── pydantic_demo.py     # Pydantic model usage
│   ├── structued_output_with_json.py # JSON schema validation
│   ├── structured_ouput_with_pydantic.py # Pydantic integration
│   └── structured_output_with_typeddict.py # TypedDict usage
├── text splitters/          # Text chunking strategies
│   ├── length_based.py      # Fixed-length text splitting
│   ├── semantic_based.py    # Semantic-aware splitting
│   ├── python_code_splitting.py # Code-specific splitting
│   └── text_structure_based.py # Structure-based splitting
├── vector stores/           # Vector database implementations
│   └── langchain-chroma.py  # ChromaDB integration
├── chroma_db/              # Persistent vector database
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Core Components

### Chains

Chains are the fundamental building blocks of LangChain applications, allowing you to combine multiple components into cohesive workflows.

- **Simple Chain**: Basic pipeline of prompt → model → output parser
- **Sequential Chain**: Multi-step chains where output of one step becomes input for the next
- **Parallel Chain**: Execute multiple chains simultaneously for efficiency
- **Conditional Chain**: Route execution based on conditions or previous outputs

### Document Loaders

Document loaders handle the ingestion of various data formats into LangChain's document format.

- **Text Loader**: Load plain text files with encoding support
- **PDF Loader**: Extract text content from PDF documents
- **Web Loader**: Scrape and load content from web pages
- **Directory Loader**: Load all files from a directory recursively

### Models

LangChain supports integration with various LLM providers and embedding models.

- **Chat Models**: Conversational models (OpenAI GPT, Google Gemini, HuggingFace)
- **LLMs**: Traditional language models for text generation
- **Embedding Models**: Convert text to vector representations (sentence-transformers, OpenAI embeddings)

### Output Parsers

Output parsers transform raw LLM responses into structured, usable formats.

- **String Output Parser**: Basic text extraction
- **JSON Output Parser**: Parse JSON responses with validation
- **Pydantic Output Parser**: Convert responses to Pydantic model instances
- **Structured Output Parser**: Handle complex nested data structures

### Prompts

Prompt management and templating for consistent and reusable prompts.

- **Prompt Templates**: Parameterized text templates
- **Chat Prompt Templates**: Structured conversation templates
- **Message Placeholders**: Dynamic message insertion
- **Prompt Loading**: Save and load prompts from files

### Retrievers

Information retrieval systems for finding relevant documents or data.

- **Wikipedia Retriever**: Search and retrieve Wikipedia articles
- **Vector Store Retriever**: Similarity search over embedded documents
- **Web Retriever**: Retrieve information from web sources

### Runnables

LangChain's execution abstraction for composable, chainable operations.

- **Runnable Sequence**: Chain multiple runnables in sequence
- **Runnable Parallel**: Execute runnables concurrently
- **Runnable Branch**: Conditional execution paths
- **Runnable Lambda**: Custom functions as runnables
- **Runnable Passthrough**: Pass data through unchanged

### Structured Output

Ensure LLMs generate responses conforming to specific schemas.

- **Pydantic Models**: Type-safe data validation and parsing
- **JSON Schema**: Define expected response structures
- **TypedDict**: Python type hints for structured data
- **Custom Validators**: Domain-specific validation rules

### Text Splitters

Strategies for breaking large documents into manageable chunks.

- **Length-based**: Fixed character/word limits
- **Semantic-based**: Split on semantic boundaries
- **Code Splitting**: Language-aware code chunking
- **Structure-based**: Preserve document structure

### Vector Stores

Persistent storage and retrieval of vector embeddings.

- **ChromaDB**: Open-source vector database optimized for LLMs
- **Similarity Search**: Find semantically similar content
- **Metadata Filtering**: Filter results based on document metadata
- **Persistent Storage**: Save and load vector databases

## Key Learnings

Through this repository, I've learned:

1. **Modular Architecture**: LangChain's component-based design allows building complex applications from simple, reusable parts.

2. **Chain Composition**: The pipe operator (`|`) enables intuitive chaining of components like prompts, models, and parsers.

3. **Multiple Integration Options**: Support for various LLM providers (OpenAI, Google, HuggingFace) and vector databases (Chroma, Pinecone, etc.).

4. **Output Structuring**: Techniques to ensure LLMs generate parseable, structured responses using Pydantic and JSON schemas.

5. **Retrieval-Augmented Generation (RAG)**: Combining vector search with LLMs for context-aware responses.

6. **Text Processing**: Various strategies for chunking large documents while preserving semantic meaning.

7. **Runnable Interface**: LangChain's execution abstraction that makes components composable and testable.

8. **Prompt Engineering**: Creating effective prompts and managing prompt templates for consistent results.

9. **Vector Embeddings**: Converting text to numerical representations for semantic search and similarity matching.

10. **Production Considerations**: Error handling, streaming responses, and optimizing for performance.

## Usage

Each component folder contains example scripts demonstrating usage. Start with simple examples and progress to complex chains:

```python
# Basic example from chains/simple_chain.py
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

template = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

chain = template | model | parser
result = chain.invoke({'topic': 'Linear regression'})
```

For more advanced usage, explore the RAG implementation combining document loading, text splitting, vector storage, and retrieval.

## Contributing

This repository is a personal learning resource. Feel free to:
- Suggest improvements
- Report issues
- Add more examples
- Share your own LangChain learnings

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langchain-ai/langgraph) - For complex multi-agent workflows
- [LangSmith](https://docs.smith.langchain.ai/) - For debugging and monitoring

---

*This repository represents my journey learning LangChain and building LLM-powered applications. Each example demonstrates practical implementation of LangChain concepts.*