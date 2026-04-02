const fs = require('fs');
const path = require('path');

const siteDir = '/Users/amerkarameh/Cordon Blue Global/cordon-blue-website';

const files = ['index.html', 'services.html', 'projects.html'];

files.forEach(file => {
    let content = fs.readFileSync(path.join(siteDir, file), 'utf8');

    // Footer Copyright Update
    content = content.replace(/© \d{4} Cordon Blue Global Services Ltd\. All Rights Reserved\./g, '© 2022 Cordon Blue Global Services Ltd. All Rights Reserved.');
    
    // Contact Info Update
    content = content.replace(/174, Ikorodu Road Onipanu, Lagos/g, '174, Ikorodu Road, Onipanu, Lagos');

    if (file === 'index.html') {
        // Tagline Reversion
        // Replace "HERE TO SATISFY YOUR HUNGER" back to "IMAGINE. BUILD. SUCCEED."
        content = content.replace(/HERE TO SATISFY YOUR HUNGER<br\/><span class="text-primary text-3xl md:text-5xl lg:text-6xl" drop-shadow-\[0_10px_20px_rgba\(14,165,233,0\.3\)\]">FOR QUALITY SERVICE DELIVERY\.<\/span>/g, 
            'IMAGINE.<br/>BUILD.<br/><span class="text-primary drop-shadow-[0_10px_20px_rgba(14,165,233,0.3)]">SUCCEED.</span>');

        // Sub-tagline update
        content = content.replace(/Engineering Your Dreams from Concept to Concrete\. Premier construction services for a sustainable future\./g,
            'Real Estate • Building & Civil Engineering Construction • Project Management • Interior Design & Decoration • Automobile & Haulage');

        // Buttons update
        content = content.replace(/View Our Projects/g, 'View Portfolio');
        content = content.replace(/Our Services/g, 'Start Your Project');

        // About Us section
        content = content.replace(/CORDON BLUE GLOBAL SERVICES is an indigenous provider of professional Architects, Engineers, Quantity Surveyors, Estate Managers, and Project Managers fully engaged in integrated and qualitative services in her chosen field of specialization from inception through design, construction, supervision to handing over to clients and closing out\./g,
            'CORDON BLUE GLOBAL SERVICES is an indigenous provider of professional Architects, Engineers, Quantity Surveyors, Estate Managers, and Project Managers fully engaged in integrated and qualitative services in their chosen field of specialization from inception through design, construction, supervision, to handing over to clients and closing out.');

        content = content.replace(/Our practice combines traditional architectural features, techniques and materials with foreign and contemporary architectural innovations for good results\./g,
            'Our practice combines traditional architectural features, techniques, and materials with foreign and contemporary architectural innovations for good results.');

        // Vision & Mission Section
        content = content.replace(/To become a regional\/national market leader in provision of Building & civil engineering construction services and Property maintenance service provider\./g,
            'To become a regional/national market leader in the provision of Building & civil engineering construction services and a property maintenance service provider.');

        content = content.replace(/We aim to be a world class engineering Construction Company providing efficient, affordable, sustainable, cost-effective services of highest level of quality\./g,
            'We aim to be a world-class engineering Construction Company providing efficient, affordable, and sustainable services of the highest quality.');

        content = content.replace(/We believe in maintaining the highest standard of professionalism, integrity, creativity, positive attitude, delivery that meets and surpass expectations while offering prompt and lasting solutions that stand the test of time\./g,
            'We believe in maintaining the highest standard of professionalism, integrity, creativity, positive attitude, and delivery that meets and surpasses expectations while offering prompt and lasting solutions that stand the test of time.');
            
        // Contact CTA Update
        content = content.replace(/Ready to start your next<br\/>/g, 'Ready to start your next<br/>');
        // Let's Talk Now is already the text for the button, but we should ensure it's there.
    }

    if (file === 'services.html') {
        content = content.replace(/Commercial buildings, Office complex/g, 'Commercial buildings, Office complexes');
    }

    fs.writeFileSync(path.join(siteDir, file), content);
});

console.log('Applied MD changes.');