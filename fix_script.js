const fs = require('fs');

let html = fs.readFileSync('projects.html', 'utf8');

// The CSS classes used in the project are different from my previous script. Let's update them to match the dark mode compatible buttons.
const newScript = `
<script>
document.addEventListener('DOMContentLoaded', () => {
    const filters = document.getElementById('project-filters');
    const grid = document.getElementById('project-grid');

    if (filters && grid) {
        const filterButtons = filters.querySelectorAll('button');
        const projectCards = grid.querySelectorAll('.group.flex.flex-col');

        filterButtons.forEach(button => {
            button.addEventListener('click', () => {
                // Update active state
                filterButtons.forEach(btn => {
                    btn.className = 'px-6 py-2 rounded-full bg-white dark:bg-surface-dark border border-slate-200 dark:border-border-dark font-semibold hover:border-primary dark:hover:border-primary transition-all';
                });
                button.className = 'px-6 py-2 rounded-full bg-primary text-white font-semibold shadow-lg shadow-primary/30 transition-all';

                const filterCategory = button.textContent.trim().toLowerCase();

                // Filter cards
                projectCards.forEach(card => {
                    const cardCategoryElement = card.querySelector('.absolute.top-4.left-4 span');
                    if (!cardCategoryElement) return;

                    const cardCategory = cardCategoryElement.textContent.trim().toLowerCase();

                    if (filterCategory === 'all projects' || cardCategory === filterCategory) {
                        card.style.display = 'flex';
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }
});
</script>
</body></html>
`;

html = html.replace(/<script>\s*document\.addEventListener\('DOMContentLoaded'[\s\S]*?<\/html>/m, newScript);
fs.writeFileSync('projects.html', html);
