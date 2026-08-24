🎯 **What:**
Refactored the image optimization scripts to eliminate code duplication. The duplicated image resizing logic in `optimize_hotel_resort.py` has been replaced by wrapping the core functionality from `optimize_image.py`.

💡 **Why:**
Maintaining duplicate image processing logic across multiple scripts increases the risk of bugs, makes updates harder, and violates the DRY (Don't Repeat Yourself) principle. Consolidating this logic into a single, parameterized function improves maintainability and ensures consistent image optimization across the codebase.

✅ **Verification:**
1. Ran local Python unit tests (`python3 -m unittest discover -p "test_optimize_*.py"`) and confirmed all 5 tests passed successfully.
2. Verified that both `optimize_hotel_resort.py` and `optimize_image.py` maintain their original structural signatures and fallback logic behaviors.

✨ **Result:**
The codebase is now cleaner, with image optimization centralized in `optimize_image.py`. The `test_optimize_image.py` script was also cleaned up by removing a hacky global PIL mock and replacing it with proper dependencies.
