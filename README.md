# VecMigrate

VecMigrate is a robust, production-grade migration engine designed to move vector embeddings and metadata between popular vector databases including Pinecone, Weaviate, and ChromaDB. It features a pluggable architecture and built-in AI agents powered by OpenClaw to handle schema mapping and data validation.

## Features

*   **Multi-Provider Support**: Seamlessly move data between Pinecone, Weaviate, and ChromaDB.
*   **Batch Processing**: Optimized for high-throughput transfers with configurable batch sizes.
*   **Metadata Mapping**: Intelligent mapping of metadata fields across different database schemas.
*   **OpenClaw Agents**: Autonomous agents that verify migration integrity and suggest optimal indexing strategies.
*   **Checkpointing**: Resume long-running migrations from the last successful batch.

## Installation

```bash
pip install vecmigrate
```

## Quick Start

```python
from vecmigrate import MigrationEngine
from vecmigrate.adapters import PineconeAdapter, ChromaAdapter

source = PineconeAdapter(api_key="...", environment="...", index_name="old-index")
target = ChromaAdapter(path="./local_db", collection_name="new-collection")

engine = MigrationEngine(source=source, target=target)
engine.migrate(batch_size=100)
```

## Architecture

VecMigrate uses an Adapter pattern to abstract provider-specific APIs into a common `VectorStore` interface. The `MigrationEngine` coordinates the flow of data, while `OpenClaw` agents monitor the process for anomalies.

*   **Adapters**: Handle low-level communication with DB providers.
*   **Core**: Manages the migration loop, error handling, and batching.
*   **Agents**: Leverages OpenClaw to perform semantic validation on migrated data.

## Configuration

Configuration can be managed via environment variables or a YAML config file. See `config.example.yaml` for details.
