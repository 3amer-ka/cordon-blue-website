🧹 [code health improvement] Merge duplicate image optimization scripts

🎯 **Why:** To improve maintainability and readability by consolidating identical logic into a single configurable script.
💡 **What:** The `optimize_hotel_resort.py` and `optimize_image.py` scripts had 90% identical logic. This PR refactors `optimize_image.py` to accept parameters (`widths`, `base_name`, `fallback_width`, `fallback_suffix`) and uses it to optimize both `resort-design.jpg` and `hotel-resort-masterplan.jpg`, replacing the duplicate script.
✅ **Verification:** Verified the core resizing functionality matches and that the local test suite `test_optimize_image.py` passes successfully with mocking properly configured to bypass the JPEG RGB conversion logic.
✨ **Result:** Duplicate script `optimize_hotel_resort.py` is safely removed and the image processing pipeline uses a single, robust parameterizable implementation.
