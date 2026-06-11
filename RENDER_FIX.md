# Render Dashboard Update Required
Your deployment on Render failed because the dashboard settings are overriding the configuration in `render.yaml`.

Please update the following settings in your Render Dashboard (**Settings → Build & Deploy**):
- **Build Command:** `npm install && npm run build`
- **Publish Directory:** `.` (or whatever directory contains your static assets, like `assets` or root)

Render is currently seeing an empty build command and defaulting to a `build` directory which does not exist in this repository.
