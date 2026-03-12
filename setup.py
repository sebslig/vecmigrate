from setuptools import setup, find_packages

setup(
    name="vecmigrate",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pinecone-client",
        "weaviate-client",
        "chromadb",
        "openclaw",
        "pydantic",
        "pyyaml"
    ],
    author="VectorMaintainers",
    description="Vector database migration tool with AI agents",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
