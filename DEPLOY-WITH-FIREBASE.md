# Deploying cordonblueglobal.com with Firebase Hosting + Google Admin Console

A step-by-step guide to get your website live at **www.cordonblueglobal.com** using Firebase Hosting (free) and pointing your domain through Google Admin Console.

---

## Prerequisites

- Google Workspace account: `admin@cordonblueglobal.com`
- Domain: `cordonblueglobal.com` (managed through Google Admin Console)
- Node.js installed on your computer (download from nodejs.org if needed)
- Your website files (the folder containing index.html, css/, js/, images/)

---

## Part 1: Set Up Firebase Hosting

### Step 1 — Install Firebase CLI

Open Terminal (Mac) and run:

```bash
npm install -g firebase-tools
```

### Step 2 — Log in to Firebase

```bash
firebase login
```

This opens a browser window. Sign in with your **admin@cordonblueglobal.com** Google account.

### Step 3 — Create a Firebase Project

1. Go to [console.firebase.google.com](https://console.firebase.google.com)
2. Click **"Add project"**
3. Name it: `cordon-blue-website`
4. Disable Google Analytics (optional, not needed for a static site)
5. Click **Create project**

### Step 4 — Initialize Firebase in Your Website Folder

Open Terminal, navigate to your website folder, and run:

```bash
cd /path/to/cordon-blue-website
firebase init hosting
```

When prompted:

| Question | Answer |
|----------|--------|
| Select a project | Choose `cordon-blue-website` |
| Public directory | Type `.` (just a dot — your files are in the root) |
| Single-page app? | **No** |
| Set up automatic builds with GitHub? | **No** |
| Overwrite index.html? | **No** |

This creates two files: `firebase.json` and `.firebaserc`. Leave them as-is.

### Step 5 — Deploy

```bash
firebase deploy
```

You'll see output like:

```
✔ Deploy complete!
Hosting URL: https://cordon-blue-website.web.app
```

Your site is now live at that `.web.app` URL. Next, connect your custom domain.

---

## Part 2: Connect Your Domain in Firebase

### Step 6 — Add Custom Domain in Firebase Console

1. Go to [console.firebase.google.com](https://console.firebase.google.com)
2. Select your project → **Hosting** (left sidebar)
3. Click **"Add custom domain"**
4. Enter: `cordonblueglobal.com`
5. Firebase will give you **two DNS records** to add. They look like:

| Type | Name | Value |
|------|------|-------|
| A | @ | 151.101.1.195 |
| A | @ | 151.101.65.195 |

6. Also add **www**:
   - Click **"Add custom domain"** again
   - Enter: `www.cordonblueglobal.com`
   - Firebase will give you a **CNAME** record:

| Type | Name | Value |
|------|------|-------|
| CNAME | www | cordon-blue-website.web.app |

**Copy these exact values.** You'll add them in Google Admin Console next.

---

## Part 3: Update DNS in Google Admin Console

Since your domain is managed through Google Workspace, you update DNS records in Google Admin Console.

### Step 7 — Open Google Admin Console

1. Go to [admin.google.com](https://admin.google.com)
2. Sign in with `admin@cordonblueglobal.com`

### Step 8 — Navigate to DNS Settings

1. Click **Account** → **Domains** → **Manage domains**
2. Find `cordonblueglobal.com`
3. Click **"Manage domain"** or **"DNS"**

**Note:** If your domain registrar is separate from Google (e.g., GoDaddy, Namecheap), Google Admin Console may redirect you to your registrar's DNS panel. In that case:

- For **GoDaddy**: Go to godaddy.com → My Products → DNS → Manage
- For **Namecheap**: Go to namecheap.com → Domain List → Manage → Advanced DNS
- For **Google Domains** (now Squarespace): Go to domains.google.com → DNS

### Step 9 — Add the A Records

Add the two A records Firebase gave you:

| Type | Host/Name | Points to / Value | TTL |
|------|-----------|-------------------|-----|
| A | @ | 151.101.1.195 | 1 hour |
| A | @ | 151.101.65.195 | 1 hour |

### Step 10 — Add the CNAME Record for www

| Type | Host/Name | Points to / Value | TTL |
|------|-----------|-------------------|-----|
| CNAME | www | cordon-blue-website.web.app | 1 hour |

### Step 11 — DO NOT Delete Existing MX Records

**Critical:** Your email (admin@cordonblueglobal.com, support@cordonblueglobal.com) runs on Google Workspace. The MX records that make email work look like:

| Type | Priority | Value |
|------|----------|-------|
| MX | 1 | ASPMX.L.GOOGLE.COM |
| MX | 5 | ALT1.ASPMX.L.GOOGLE.COM |
| MX | 5 | ALT2.ASPMX.L.GOOGLE.COM |
| MX | 10 | ALT3.ASPMX.L.GOOGLE.COM |
| MX | 10 | ALT4.ASPMX.L.GOOGLE.COM |

**Do NOT touch these.** Only add the A and CNAME records above.

Also keep any existing TXT records (SPF, DKIM, DMARC) — these protect your email from being spoofed.

### Step 12 — Verify in Firebase

1. Go back to Firebase Console → Hosting
2. Your domain will show as **"Pending"** while DNS propagates
3. Wait 15 minutes to 48 hours (usually under 1 hour)
4. Firebase automatically provisions a free SSL certificate
5. Once verified, status changes to **"Connected"**

---

## Part 4: Verify Everything Works

### Test these URLs:

- `https://cordonblueglobal.com` → should load your website
- `https://www.cordonblueglobal.com` → should load your website
- `http://cordonblueglobal.com` → should redirect to HTTPS automatically
- Send a test email to `support@cordonblueglobal.com` → should still arrive in Gmail

### Test the contact form:

1. Go to the Contact page
2. Fill out the form and submit
3. Your email client should open with a pre-filled message to support@cordonblueglobal.com

---

## Part 5: Future Updates

Whenever you update the website files, just run:

```bash
cd /path/to/cordon-blue-website
firebase deploy
```

Changes go live within seconds. Firebase keeps a history of deployments, so you can roll back if needed from the Firebase Console.

---

## Quick Reference: Final DNS Records

Your complete DNS setup should look like this:

| Type | Name | Value | Purpose |
|------|------|-------|---------|
| A | @ | 151.101.1.195 | Website (Firebase) |
| A | @ | 151.101.65.195 | Website (Firebase) |
| CNAME | www | cordon-blue-website.web.app | www subdomain |
| MX | @ | ASPMX.L.GOOGLE.COM (priority 1) | Email (Google) |
| MX | @ | ALT1.ASPMX.L.GOOGLE.COM (priority 5) | Email (Google) |
| MX | @ | ALT2.ASPMX.L.GOOGLE.COM (priority 5) | Email (Google) |
| TXT | @ | v=spf1 include:_spf.google.com ~all | Email security |

**Note:** The exact Firebase IP addresses may differ — always use the values Firebase gives you in Step 6.

---

## Troubleshooting

**"Domain verification failed"** → Make sure you added the A records correctly. Use [dnschecker.org](https://dnschecker.org) to verify propagation.

**Email stopped working** → You accidentally deleted MX records. Re-add them from the table above.

**Site shows "Not Secure"** → SSL certificate hasn't provisioned yet. Wait up to 24 hours. Firebase handles this automatically.

**Changes not showing after deploy** → Clear your browser cache (Cmd+Shift+R on Mac) or try incognito mode.
