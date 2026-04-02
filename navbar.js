class MainHeader extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
        this.setupMobileMenu();
    }

    setupMobileMenu() {
        const menuToggle = this.querySelector('#menu-toggle');
        const mobileMenu = document.getElementById('mobile-menu');
        if (menuToggle && mobileMenu) {
            menuToggle.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
                const icon = menuToggle.querySelector('span');
                icon.textContent = mobileMenu.classList.contains('hidden') ? 'menu' : 'close';
            });
        }
    }

    render() {
        const currentPath = window.location.pathname;
        const isHome = currentPath === '/' || currentPath.endsWith('index.html');
        const isProjects = currentPath.endsWith('projects.html');
        const isServices = currentPath.endsWith('services.html');

        this.innerHTML = `
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex h-16 items-center justify-between">
        <div class="flex items-center gap-3">
            <div class="flex items-center justify-center bg-primary p-2 rounded-xl shadow-lg shadow-primary/20">
                <span class="material-symbols-outlined text-white text-2xl">architecture</span>
            </div>
            <span class="text-xl font-bold tracking-tight text-slate-900 dark:text-white uppercase">Cordon Blue Global Services Ltd.</span>
        </div>

        <nav class="hidden md:flex items-center gap-8">
            <a href="index.html" class="text-sm font-semibold transition-colors ${isHome ? 'text-primary' : 'text-slate-600 dark:text-slate-300 hover:text-primary dark:hover:text-white'}">Home</a>
            <a href="index.html#about" class="text-sm font-semibold transition-colors text-slate-600 dark:text-slate-300 hover:text-primary dark:hover:text-white">About Us</a>
            <a href="services.html" class="text-sm font-semibold transition-colors ${isServices ? 'text-primary' : 'text-slate-600 dark:text-slate-300 hover:text-primary dark:hover:text-white'}">Services</a>
            <a href="projects.html" class="text-sm font-semibold transition-colors ${isProjects ? 'text-primary' : 'text-slate-600 dark:text-slate-300 hover:text-primary dark:hover:text-white'}">Projects</a>
            <a href="index.html#contact" class="text-sm font-semibold transition-colors text-slate-600 dark:text-slate-300 hover:text-primary dark:hover:text-white">Contact</a>
        </nav>

        <div class="flex items-center gap-4">
            <a href="index.html#contact" class="hidden sm:flex items-center justify-center rounded-xl bg-primary px-6 py-2.5 text-sm font-bold text-white hover:bg-primary/90 hover:scale-105 active:scale-95 transition-all shadow-lg shadow-primary/20">
                Get a Quote
            </a>
            <button id="menu-toggle" class="md:hidden text-slate-900 dark:text-white p-2">
                <span class="material-symbols-outlined">menu</span>
            </button>
        </div>
    </div>
</div>
        `;
    }
}

customElements.define('main-header', MainHeader);
