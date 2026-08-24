import json
with open('.github/pull_request.json', 'w') as f:
    json.dump({
        "title": "🧪 Add test for RGBA to RGB image conversion in optimize_image.py",
        "body": "🎯 **What:** Added a missing test case in `test_optimize_image.py` for testing image conversion to RGB in `optimize_image.py` when saving an image in JPEG format.\n\n📊 **Coverage:** Added coverage for the edge case where an input image might be in `RGBA` (or any mode other than `RGB`). This ensures that `resized_jpg.convert(\"RGB\")` is called before saving, preventing a crash.\n\n✨ **Result:** Test suite coverage has been improved for the image optimization pipeline, explicitly catching edge cases when Pillow tries to save non-RGB formats as JPEG."
    }, f)
