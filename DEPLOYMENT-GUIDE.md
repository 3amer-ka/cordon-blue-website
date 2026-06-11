# Quick Deployment Guide for Cordon Blue Website

## 🎯 Immediate Next Steps

### 1. Extract and Organize Images (15 minutes)

From your provided files, you need to:

**A. Logo Setup:**
- Save the approved logo image to `images/`
- Rename to `brand-mark.svg`

**B. Project Photos Setup:**
Create `images/projects/` folder and extract images from your PDF:
- Lekki project photos → `lekki-main.jpg`, `lekki-1.jpg`, `lekki-2.jpg`, `lekki-3.jpg`
- Officer's Lodge → `officers-lodge.jpg`
- Mini-Flats → `mini-flats.jpg`
- Drain project → `drain-before.jpg`, `drain-after.jpg`
- Water tank → `water-tank-1.jpg`, `water-tank-2.jpg`
- RCCG Auditorium → `rccg-1.jpg`, `rccg-2.jpg`
- Minimah Estate → `minimah-estate.jpg`

### 2. Test Locally (5 minutes)

```bash
# Navigate to the website folder
cd ~/Desktop/cordon-blue-website

# Open in browser (Mac)
open index.html

# Or just double-click index.html
```

Check:
- ✅ All pages load correctly
- ✅ Navigation works
- ✅ Images display properly
- ✅ Mobile menu works (resize browser)
- ✅ Contact form validates

---

## 🚀 Recommended: Firebase Hosting (FREE)

**Why Firebase?**
- ✅ FREE forever
- ✅ Fast global CDN
- ✅ Free SSL certificate (HTTPS)
- ✅ Easy domain connection
- ✅ Integrated with Google (you already have Google Workspace)

### Firebase Setup (10 minutes)

**Step 1: Install Firebase Tools**
```bash
# Open Terminal and run:
npm install -g firebase-tools
```

**Step 2: Login to Firebase**
```bash
firebase login
```
This opens your browser to login with your Google account (admin@cordonblueglobal.com).

**Step 3: Initialize Your Project**
```bash
cd ~/Desktop/cordon-blue-website
firebase init hosting
```

Answer the prompts:
- Use existing project or create new? → **Create new**
- Project name: `cordon-blue-website`
- Public directory: **. (current directory)**
- Single-page app: **No**
- Overwrite index.html: **No**

**Step 4: Deploy**
```bash
firebase deploy
```

You'll get a URL like: `https://cordon-blue-website.web.app`

**Step 5: Connect Your Domain**
1. Go to Firebase Console: https://console.firebase.google.com
2. Select your project
3. Click "Hosting" in left sidebar
4. Click "Add custom domain"
5. Enter: `cordonblueglobal.com`
6. Follow the DNS verification steps

### DNS Configuration for Firebase

Add these records to your domain registrar:

```
Type    Name    Value
A       @       151.101.1.195
A       @       151.101.65.195
TXT     @       [Firebase verification code]
```

**Important:** Don't touch your existing MX records for Google Workspace email!

---

## 💰 Alternative: Traditional Hosting

### Option A: Namecheap Hosting (~$3/month)

1. **Purchase Hosting**
   - Go to namecheap.com
   - Buy "Stellar Shared Hosting" plan
   - Link to your domain: cordonblueglobal.com

2. **Upload Files via cPanel**
   - Login to cPanel (check Namecheap email for details)
   - Go to "File Manager"
   - Navigate to `public_html`
   - Upload all website files

3. **Test**
   - Visit: http://cordonblueglobal.com
   - Enable SSL in cPanel → "SSL/TLS Status"

### Option B: Bluehost (~$3-7/month)

1. Purchase hosting at bluehost.com
2. Connect your domain
3. Use FTP or File Manager to upload files
4. Enable free SSL certificate

---

## 🔧 Contact Form Enhancement

### Immediate Solution: FormSubmit (FREE, No Coding)

Edit `contact.html`, find the `<form>` tag and change it to:

```html
<form action="https://formsubmit.co/admin@cordonblueglobal.com" method="POST" class="contact-form" id="contactForm">
    <!-- Add these hidden inputs -->
    <input type="hidden" name="_subject" value="New inquiry from Cordon Blue website">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="_honey" style="display:none">
    
    <!-- Rest of your form fields stay the same -->
</form>
```

Also update `js/main.js` - remove the `e.preventDefault()` line from the form submission handler (line 56).

**What this does:**
- ✅ Emails go directly to admin@cordonblueglobal.com
- ✅ No spam (honeypot protection)
- ✅ Works immediately
- ✅ 100% free

**First time setup:**
1. Submit a test form
2. FormSubmit sends confirmation email
3. Click confirmation link
4. All future submissions go straight to your inbox

---

## 📊 Optional: Add Google Analytics

Track your website visitors (FREE):

1. Go to: https://analytics.google.com
2. Create account (use admin@cordonblueglobal.com)
3. Get tracking ID (looks like: G-XXXXXXXXXX)
4. Add to every HTML file before `</head>`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## ✅ Final Checklist

Before going live:

- [ ] All images added and displaying correctly
- [ ] Logo appears on all pages
- [ ] Test all navigation links
- [ ] Test mobile menu (hamburger icon)
- [ ] Test contact form submission
- [ ] Phone numbers are correct
- [ ] Email addresses are correct
- [ ] Company address is correct
- [ ] All project images load
- [ ] Website works on mobile phone
- [ ] SSL certificate is active (HTTPS)
- [ ] Google Analytics installed (optional)

---

## 📞 Support Contact

**For Firebase Issues:**
- Documentation: https://firebase.google.com/docs/hosting
- Support: https://firebase.google.com/support

**For Domain Issues:**
- Check your domain registrar (where you bought cordonblueglobal.com)
- Look for "DNS Management" or "Domain Settings"

**For Website Updates:**
- Edit HTML files in text editor
- Make changes
- Re-deploy using `firebase deploy`

---

## 🎓 Learning Resources

**Want to learn more?**
- HTML/CSS: https://www.w3schools.com
- Firebase Hosting: https://firebase.google.com/docs/hosting/quickstart
- Domain Management: https://support.google.com/domains

---

## ⏰ Timeline Estimate

| Task | Time |
|------|------|
| Extract and organize images | 15 min |
| Test website locally | 5 min |
| Setup Firebase hosting | 10 min |
| Deploy to Firebase | 2 min |
| Connect custom domain | 10 min |
| DNS propagation wait | 1-24 hours |
| **Total active time** | **~45 minutes** |

---

## 🎉 You're Ready!

Your website is production-ready. Follow the Firebase deployment steps above for the fastest, free hosting solution that scales with your business.

**Questions?** All the technical details are in the main README.md file.

**Good luck with your launch! 🚀**
