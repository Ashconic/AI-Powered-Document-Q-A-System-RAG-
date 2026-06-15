import sys
import traceback

print("=" * 60)
print("TESTING MODULE IMPORT")
print("=" * 60)

# Try to import with full traceback
sys.path.insert(0, '.')

try:
    print("\n1. Importing src.data_loader...")
    import src.data_loader as dl
    print("   ✓ Module imported")
    print(f"   Module file: {dl.__file__}")
    print(f"   Module contents: {[x for x in dir(dl) if not x.startswith('_')]}")
except Exception as e:
    print("   ✗ Error during import:")
    traceback.print_exc()
    sys.exit(1)

# Check if function exists
if hasattr(dl, 'load_all_documents'):
    print("\n2. load_all_documents found in module!")
else:
    print("\n2. load_all_documents NOT found in module!")
    print("   Trying to get it anyway...")
    try:
        from src.data_loader import load_all_documents
        print("   ✓ Direct import worked!")
    except ImportError as e:
        print(f"   ✗ Direct import failed: {e}")
