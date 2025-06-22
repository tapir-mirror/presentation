# Psychology Text Extractor and Chunker

This project downloads, processes, and chunks psychology-related texts from various sources including Project Gutenberg and educational resources. The processed chunks are stored in Redis for efficient access and processing.

## Project Structure

```
extractors/
├── book_urls.txt           # List of book URLs to process
├── books.md               # Extracted book information
├── clean_gutenberg_texts.py # Script to clean Gutenberg texts
├── gutenberg_scraper.py   # Script to download from Gutenberg
├── psychology_books_scraper.py # Script to download from educational sources
├── textbook_chunker.py    # Script to chunk texts and store in Redis
├── check_redis.py         # Utility to inspect Redis storage
├── targets/              # Directory containing downloaded books
├── chunks/               # Directory for any filesystem-based chunks
└── docker-compose.yml    # Docker configuration
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start Redis using Docker:
```bash
docker-compose up -d
```

## Components

### 1. Text Scrapers

#### Gutenberg Scraper (`gutenberg_scraper.py`)
- Downloads books from Project Gutenberg
- Handles rate limiting and duplicates
- Extracts book metadata

#### Psychology Books Scraper (`psychology_books_scraper.py`)
- Downloads from various educational sources:
  - Pressbooks
  - OpenStax
  - Noba Project
- Handles different site structures
- Saves both HTML and PDF/EPUB versions

### 2. Text Processing

#### Clean Gutenberg Texts (`clean_gutenberg_texts.py`)
- Removes Project Gutenberg headers and footers
- Handles files with and without standard markers
- Skips already processed files

#### Textbook Chunker (`textbook_chunker.py`)
- Chunks texts into smaller segments
- Extracts author information
- Stores chunks in Redis
- Features:
  - Chunk size: 500 characters
  - Chunk overlap: 50 characters
  - Author extraction from first 50 lines
  - Parallel processing support

### 3. Data Storage

The project uses Redis for storing processed chunks and metadata. Current storage statistics:
- Total chunks: 1,404,192
- Total books: 1,478
- Storage size: ~741 MB for chunks, ~0.17 MB for metadata

#### Redis Structure

1. **Chunk Queue** (`chunk_queue` key)
   - Type: List
   - Each entry contains:
     ```json
     {
       "book_id": "book_40489",
       "chunk_id": "cb04b43d10964195b620fad349cd9e1a",
       "chunk": "Text content...",
       "source_file": "targets/book_40489.txt",
       "author": "Author Name"
     }
     ```

2. **Book Metadata** (`book_metadata` key)
   - Type: Hash
   - Each entry contains:
     ```json
     {
       "book_id": "book_40970",
       "total_chunks": 154,
       "source_file": "targets/book_40970.txt",
       "author": "Author Name"
     }
     ```

### 4. Utilities

#### Check Redis (`check_redis.py`)
- Monitors Redis storage usage
- Displays chunk and metadata statistics
- Shows storage structure and examples

## Docker Configuration

The project uses Docker Compose for Redis deployment:
- Redis version: 7.2.9
- Persistence: Enabled via Docker volume
- Port: 6379
- Data volume: `redis_data`

## Usage

1. Start Redis:
```bash
docker-compose up -d
```

2. Process books:
```bash
python textbook_chunker.py
```

3. Check processing status:
```bash
python check_redis.py
```

## Data Persistence

- Redis data is persisted in the Docker volume `redis_data`
- Current memory usage: ~781 MB
- Peak memory usage: ~1.50 GB

## Author Extraction

The system extracts author information using various patterns:
- "Author:" prefix
- "By" prefix
- Project Gutenberg headers
- Title page information

Author extraction success rate: High (most books have authors identified)

## Performance

- Parallel processing of books
- Redis for high-speed access
- Efficient chunk storage and retrieval
- Memory-optimized storage (~741 MB for 1.4M chunks) 