# Cordon Blue Global Services Ltd - Website

A professional, modern website for Cordon Blue Global Services Ltd, a leading construction and engineering company in Lagos, Nigeria.

## 🏗️ Website Structure

The website includes the following pages:
- **index.html** - Cover/Home page
- **about.html** - Company information, mission, vision, values
- **services.html** - Core services and additional offerings
- **why-choose-us.html** - Company credentials and team
- **projects.html** - Portfolio of completed projects
- **contact.html** - Contact form and company details

## 📁 Directory Structure

```
cordon-blue-website/
├── index.html
├── about.html
├── services.html
├── why-choose-us.html
├── projects.html
├── contact.html
├── css/
│   └── styles.css
├── js/
│   └── main.js
├── images/
│   ├── brand-mark.svg (active site logo)
│   └── projects/ (project photos)
└── README.md
```

## 🎨 Design Features

- **Color Scheme**: Navy dark (#1a2332), Steel blue (#4a6fa5), Gold accent (#d4a650)
- **Typography**: 
  - Headings: Serif fonts (Georgia)
  - Body text: Sans-serif (Helvetica Neue, Arial)
- **Responsive**: Mobile-first design, works on all devices
- **Modern**: Clean layouts, smooth animations, professional appearance

## 📝 Setup Instructions

### Step 1: Add Your Logo

1. Save your approved logo image as `brand-mark.svg`
2. Place it in the `images/` folder
3. Keep this as the single source logo used across all pages

### Step 2: Add Project Images

Extract project images from your PDF and place them in `images/projects/` with these names:
- `lekki-main.jpg`, `lekki-1.jpg`, `lekki-2.jpg`, `lekki-3.jpg`
- `officers-lodge.jpg`, `mini-flats.jpg`
- `drain-before.jpg`, `drain-after.jpg`
- `water-tank-1.jpg`, `water-tank-2.jpg`
- `rccg-1.jpg`, `rccg-2.jpg`
- `minimah-estate.jpg`

### Step 3: Test Locally

1. Open `index.html` in your web browser
2. Test all navigation links
3. Test the contact form
4. Check mobile responsiveness (resize browser window)

## 🚀 Deployment Options

### Option 1: Google Cloud (Free Hosting with Your Domain)

Since you have Google Workspace for admin@cordonblueglobal.com, you can use:

1. **Firebase Hosting** (Free, Fast, SSL included)
   ```bash
   # Install Firebase CLI
   npm install -g firebase-tools
   
   # Login to Firebase
   firebase login
   
   # Initialize project
   firebase init hosting
   
   # Deploy
   firebase deploy
   ```

2. **Connect Your Domain**:
   - Go to Firebase Console → Hosting → Add custom domain
   - Enter: www.cordonblueglobal.com
   - Follow DNS instructions to verify domain ownership

### Option 2: Traditional Web Hosting

1. **Choose a hosting provider**:
   - Namecheap
   - Bluehost
   - HostGator
   - SiteGround

2. **Upload files via FTP**:
   - Use FileZilla or similar FTP client
   - Connect using credentials from your host
   - Upload all files to `public_html` or `www` folder

3. **Point your domain**:
   - Update DNS A records to point to hosting IP
   - Update DNS records in your domain registrar

### Option 3: GitHub Pages (Free)

1. Create a GitHub account at github.com
2. Create a new repository named `cordonblueglobal`
3. Upload all website files
4. Enable GitHub Pages in Settings
5. Connect custom domain in repository settings

## ⚙️ Contact Form Configuration

The current contact form uses `mailto:` which opens the user's email client. For better functionality, consider:

### Option A: FormSubmit (Free, No Setup)

Replace the form action:
```html
<form action="https://formsubmit.co/admin@cordonblueglobal.com" method="POST">
```

### Option B: Google Forms Integration

1. Create a Google Form
2. Use a service like Formfacade to embed it
3. Responses go directly to Google Sheets

### Option C: Backend Service (Recommended for Production)

1. Use EmailJS for client-side email sending
2. Set up Netlify Forms (if hosting on Netlify)
3. Use a backend service like PHP or Node.js

## 🔧 Customization

### Updating Colors

Edit `css/styles.css` root variables:
```css
:root {
    --navy-dark: #1a2332;     /* Main dark color */
    --steel-blue: #4a6fa5;    /* Accent color */
    --gold-accent: #d4a650;   /* Highlight color */
}
```

### Adding New Pages

1. Copy an existing HTML file
2. Update the navigation links
3. Change the page content
4. Update the active state in navigation

### Updating Contact Information

Edit `contact.html` to update:
- Office address
- Phone numbers
- Email addresses
- Business registration details

## 📱 Features

✅ Fully responsive design
✅ Mobile navigation menu
✅ Smooth scrolling
✅ Image lightbox for projects
✅ Contact form validation
✅ SEO-friendly structure
✅ Fast loading
✅ Professional appearance

## 🌐 Domain Configuration

Your domain: **cordonblueglobal.com**
Email: **admin@cordonblueglobal.com** (Google Workspace)

### DNS Records to Add (After choosing hosting):

```
Type    Name    Value
A       @       [Your hosting IP]
CNAME   www     @
```

Note: Keep existing MX records for Google Workspace email!

## 🆘 Support

For technical assistance with:
- Firebase: firebase.google.com/support
- Google Workspace: support.google.com
- Domain issues: Contact your domain registrar

## 📄 Browser Compatibility

- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Edge (latest)
- ✅ Mobile browsers

## 🔐 Security

- Always use HTTPS (SSL certificate)
- Keep contact form protected from spam
- Regularly update content
- Backup website files

## 📞 Company Information

**Cordon Blue Global Services Ltd**
- RC: 1941741
- Address: 174, Ikorodu Road, Onipanu, Lagos, Nigeria
- Email: admin@cordonblueglobal.com
- Website: www.cordonblueglobal.com

---

**Built with:** HTML5, CSS3, JavaScript  
**Design:** Corporate/Engineering/Premium theme  
**Status:** Production Ready ✅

*"Here to satisfy your hunger for quality service delivery."*
