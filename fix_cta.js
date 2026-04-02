const fs = require('fs');
const path = require('path');

const siteDir = '/Users/amerkarameh/Cordon Blue Global/cordon-blue-website';
let indexHtml = fs.readFileSync(path.join(siteDir, 'index.html'), 'utf8');

// Update CTA button to "Let's Talk Now"
indexHtml = indexHtml.replace(/<span class="text-lg">Call Us Now<\/span>/g, '<span class="text-lg">Let\'s Talk Now</span>');
indexHtml = indexHtml.replace(/<span class="text-lg">Send Email<\/span>/g, '<span class="text-lg">Let\'s Talk Now</span>');

fs.writeFileSync(path.join(siteDir, 'index.html'), indexHtml);
console.log('Fixed CTA text.');