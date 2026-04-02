const fs = require('fs');
const path = require('path');

const siteDir = '/Users/amerkarameh/Cordon Blue Global/cordon-blue-website';
let indexHtml = fs.readFileSync(path.join(siteDir, 'index.html'), 'utf8');

// Because I did a global replace for "Our Services" to "Start Your Project", I accidentally renamed the "Our Services Section" and the footer links.
// Let's fix that.
indexHtml = indexHtml.replace(/<!-- Start Your Project Section -->/g, '<!-- Our Services Section -->');
indexHtml = indexHtml.replace(/<a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="services.html">Start Your Project<\/a>/g, '<a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="services.html">Our Services</a>');

// Also need to fix button links on Hero banner
indexHtml = indexHtml.replace(/<button class="px-10 py-4 bg-white\/10 backdrop-blur-md border border-white\/20 text-white font-bold rounded-xl hover:bg-white\/20 active:scale-95 transition-all text-lg">\s*Start Your Project\s*<\/button>/g,
    '<button onclick="window.location.href=\'#contact\'" class="px-10 py-4 bg-white/10 backdrop-blur-md border border-white/20 text-white font-bold rounded-xl hover:bg-white/20 active:scale-95 transition-all text-lg">\n                        Start Your Project\n                    </button>');

indexHtml = indexHtml.replace(/<button class="px-10 py-4 bg-primary text-white font-bold rounded-xl hover:scale-105 active:scale-95 transition-all text-lg shadow-xl shadow-primary\/25">\s*View Portfolio\s*<\/button>/g,
    '<button onclick="window.location.href=\'projects.html\'" class="px-10 py-4 bg-primary text-white font-bold rounded-xl hover:scale-105 active:scale-95 transition-all text-lg shadow-xl shadow-primary/25">\n                        View Portfolio\n                    </button>');

fs.writeFileSync(path.join(siteDir, 'index.html'), indexHtml);
console.log('Fixed button links.');