import sys
import traceback

# Try to import each component step by step
print("Step 1: Import pathlib")
try:
    from pathlib import Path
    print("✓ Success")
except Exception as e:
    print(f"✗ Error: {e}")
    traceback.print_exc()

print("\nStep 2: Import typing")
try:
    from typing import List, Any
    print("✓ Success")
except Exception as e:
    print(f"✗ Error: {e}")
    traceback.print_exc()

print("\nStep 3: Import langchain_community loaders")
try:
    from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
    print("✓ Success: PyPDFLoader, TextLoader, CSVLoader")
except Exception as e:
    print(f"✗ Error: {e}")
    traceback.print_exc()

try:
    from langchain_community.document_loaders import Docx2txtLoader
    print("✓ Success: Docx2txtLoader")
except Exception as e:
    print(f"✗ Error: {e}")
    traceback.print_exc()

try:
    from langchain_community.document_loaders.excel import UnstructuredExcelLoader
    print("✓ Success: UnstructuredExcelLoader")
except Exception as e:
    print(f"✗ Error: {e}")
    traceback.print_exc()

try:
    from langchain_community.document_loaders import JSONLoader
    print("✓ Success: JSONLoader")
except Exception as e:
    print(f"✗ Error: {e}")
    traceback.print_exc()

print("\nStep 4: Now try to actually import src.data_loader")
try:
    from src.data_loader import load_all_documents
    print("✓ Success! load_all_documents imported")
    print(f"load_all_documents is: {load_all_documents}")
except Exception as e:
    print(f"✗ Error: {e}")
    traceback.print_exc()
