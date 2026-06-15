import sys
import traceback

try:
    print("Attempting to import src.data_loader...")
    import src.data_loader as dl
    print(f"Success! Module contents: {[x for x in dir(dl) if not x.startswith('_')]}")
    print(f"Has load_all_documents: {hasattr(dl, 'load_all_documents')}")
except Exception as e:
    print(f"Error during import:")
    traceback.print_exc()

print("\nNow trying direct import of langchain_community components...")
try:
    from langchain_community.document_loaders import PyPDFLoader, TextLoader, CSVLoader
    print("✓ PyPDFLoader, TextLoader, CSVLoader imported")
except Exception as e:
    print(f"✗ Failed: {e}")

try:
    from langchain_community.document_loaders import Docx2txtLoader
    print("✓ Docx2txtLoader imported")
except Exception as e:
    print(f"✗ Failed: {e}")

try:
    from langchain_community.document_loaders.excel import UnstructuredExcelLoader
    print("✓ UnstructuredExcelLoader imported")
except Exception as e:
    print(f"✗ Failed: {e}")

try:
    from langchain_community.document_loaders import JSONLoader
    print("✓ JSONLoader imported")
except Exception as e:
    print(f"✗ Failed: {e}")
