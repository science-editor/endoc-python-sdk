from setuptools import setup, find_packages

setup(
    name="endoc-sdk",
    version="0.1.0",
    description="Endoc SDK: A note-taking app SDK powered by LLMs",
    packages=find_packages(),  # Automatically finds and includes your package
    python_requires='>=3.6',
)
