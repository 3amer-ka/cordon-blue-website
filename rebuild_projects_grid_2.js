const fs = require('fs');
const path = require('path');

const siteDir = '/Users/amerkarameh/Cordon Blue Global/cordon-blue-website';
let finalProjectsStr = fs.readFileSync(path.join(siteDir, 'projects.html'), 'utf8');

const projectsData = [
    { title: 'Modern Studio Design', category: 'Architecture', location: 'Design Phase', destImg: './assets/images/studio-design.jpg' },
    { title: 'Administrative Tower', category: 'Commercial', location: 'Concept', destImg: './assets/images/admin-tower.jpg' },
    { title: 'Luxury Hotel Design', category: 'Hospitality', location: 'Design Phase', destImg: './assets/images/hotel-design.jpg' },
    { title: 'Polivard City Design', category: 'Urban Planning', location: 'Masterplan', destImg: './assets/images/polivard-city.jpg' },
    { title: 'Resort Masterplan', category: 'Hospitality', location: 'Design Phase', destImg: './assets/images/resort-design.jpg' },
    { title: 'Center Gaming Bar', category: 'Interior Fit-Out', location: 'Lagos Club', destImg: './assets/images/lagos-gaming.jpg' },
    { title: 'Civil Works Contracting', category: 'Construction', location: 'Various Sites', destImg: './assets/images/civil-works.jpg' },
    { title: 'Karameh Industrial City', category: 'Industrial', location: 'Civil Works', destImg: './assets/images/karameh-industrial.jpg' }
];

const gridStartMatch = finalProjectsStr.match(/<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">/);
if (gridStartMatch) {
    const startIndex = gridStartMatch.index + gridStartMatch[0].length;
    // The end of the grid is before `<div class="mt-16 text-center">` or similar
    const endMatch = finalProjectsStr.match(/<\/div>\s*<div class="mt-16/);
    if (endMatch) {
        const beforeGrid = finalProjectsStr.substring(0, startIndex);
        const afterGrid = finalProjectsStr.substring(endMatch.index);
        
        let newGridContent = '';
        projectsData.forEach((project, index) => {
            newGridContent += `
                <div class="group flex flex-col bg-white rounded-xl overflow-hidden border border-slate-200 transition-all hover:shadow-[0_20px_50px_rgba(0,0,0,0.3)] hover:-translate-y-1">
                    <div class="relative aspect-[16/10] overflow-hidden">
                        <div class="absolute inset-0 bg-cover bg-center transition-transform duration-500 group-hover:scale-110" style="background-image: url('${project.destImg}')"></div>
                        <div class="absolute top-4 left-4">
                            <span class="px-3 py-1 bg-white/90 backdrop-blur rounded text-xs font-bold uppercase tracking-wider text-primary border border-primary/20">${project.category}</span>
                        </div>
                    </div>
                    <div class="p-6">
                        <h3 class="text-xl font-bold mb-2 group-hover:text-primary transition-colors text-slate-900">${project.title}</h3>
                        <div class="flex items-center gap-2 text-slate-500 text-sm">
                            <span class="material-symbols-outlined text-base text-primary">location_on</span>
                            <span>${project.location}</span>
                        </div>
                    </div>
                </div>
            `;
        });
        fs.writeFileSync(path.join(siteDir, 'projects.html'), beforeGrid + '\n' + newGridContent + '\n' + afterGrid);
        console.log('Restored projects grid.');
    } else {
        console.log('End match failed');
    }
}
