class MainHeader extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
        this.addEventListeners();
    }

    render() {
        const currentPath = window.location.pathname;
        const isHome = currentPath === '/' || currentPath.endsWith('index.html');
        const isAbout = currentPath.endsWith('about.html');
        const isServices = currentPath.endsWith('services.html');
        const isProjects = currentPath.endsWith('projects.html');
        const isWhyChooseUs = currentPath.endsWith('why-choose-us.html');
        const isContact = currentPath.endsWith('contact.html');

        const navLinks = [
            { name: 'Home', href: 'index.html', active: isHome },
            { name: 'About Us', href: 'about.html', active: isAbout },
            { name: 'Services', href: 'services.html', active: isServices },
            { name: 'Projects', href: 'projects.html', active: isProjects },
            { name: 'Why Choose Us', href: 'why-choose-us.html', active: isWhyChooseUs },
            { name: 'Contact', href: 'contact.html', active: isContact }
        ];

        this.innerHTML = `
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex h-20 items-center justify-between">
        <div class="flex items-center gap-3">
            <a href="index.html" class="flex items-center gap-3">
                <div class="size-12 bg-white rounded-2xl flex items-center justify-center overflow-hidden shrink-0 shadow-sm border border-slate-200/50">
                    <img alt="Cordon Blue Logo" class="w-full h-full object-cover p-1" src="./assets/logo.jpg"/>
                </div>
                <div class="flex flex-col">
                    <h2 class="text-xl md:text-2xl font-black leading-tight tracking-tight text-slate-900 dark:text-white">Cordon Blue</h2>
                    <p class="text-[13px] md:text-sm text-slate-500 dark:text-slate-400 font-semibold leading-tight mt-0.5">Global Services Ltd.</p>
                </div>
            </a>
        </div>

        <nav class="hidden md:flex items-center gap-6">
            ${navLinks.map(link => `
                <a href="${link.href}" class="text-sm font-semibold transition-colors ${link.active ? 'text-primary' : 'text-slate-600 dark:text-slate-300 hover:text-primary dark:hover:text-white'}">${link.name}</a>
            `).join('')}
        </nav>

        <div class="flex items-center gap-4">
            <a href="contact.html" class="hidden sm:flex items-center justify-center rounded-xl bg-primary px-6 py-2.5 text-sm font-bold text-white hover:bg-primary/90 hover:scale-105 active:scale-95 transition-all shadow-lg shadow-primary/20">
                Get a Quote
            </a>
            <button id="mobile-menu-button" class="md:hidden text-slate-900 dark:text-white p-2">
                <span class="material-symbols-outlined">menu</span>
            </button>
        </div>
    </div>
</div>

<!-- Mobile Menu -->
<div id="mobile-menu" class="hidden md:hidden absolute top-20 left-0 w-full bg-white dark:bg-background-dark border-b border-slate-200 dark:border-white/5 z-50 transition-all duration-300 ease-in-out shadow-xl">
    <div class="flex flex-col p-4 space-y-4">
        ${navLinks.map(link => `
            <a href="${link.href}" class="text-base font-semibold px-4 py-2 rounded-lg transition-colors ${link.active ? 'bg-primary/10 text-primary' : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-surface-dark'}">${link.name}</a>
        `).join('')}
        <a href="contact.html" class="flex items-center justify-center rounded-xl bg-primary px-6 py-3 text-base font-bold text-white hover:bg-primary/90 transition-all shadow-lg shadow-primary/20 mt-2">
            Get a Quote
        </a>
    </div>
</div>
        `;
    }

    addEventListeners() {
        const button = this.querySelector('#mobile-menu-button');
        const menu = this.querySelector('#mobile-menu');

        if (button && menu) {
            button.addEventListener('click', () => {
                menu.classList.toggle('hidden');
                const icon = button.querySelector('.material-symbols-outlined');
                if (icon) {
                    icon.textContent = menu.classList.contains('hidden') ? 'menu' : 'close';
                }
            });
        }
    }
}

customElements.define('main-header', MainHeader);

class MainFooter extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
    }

    render() {
        this.innerHTML = `
<footer class="bg-white dark:bg-background-dark py-20 border-t border-slate-200 dark:border-white/5">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="relative w-full rounded-3xl overflow-hidden shadow-2xl ring-1 ring-slate-200 dark:ring-white/10 mb-20">
            <div class="bg-white dark:bg-surface-dark overflow-hidden">
                <img alt="Cordon Blue Global Services" class="w-full h-auto object-cover block" src="./assets/logo.jpg"/>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 border-t border-slate-200 dark:border-white/5 pt-16">
            <div class="space-y-6">
                <div class="flex items-center gap-3">
                    <div class="flex items-center justify-center bg-primary p-1.5 rounded-lg">
                        <span class="material-symbols-outlined text-white text-xl">architecture</span>
                    </div>
                    <span class="text-lg font-bold tracking-tight text-slate-900 dark:text-white uppercase">Cordon Blue</span>
                </div>
                <p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                    A premier construction firm dedicated to transforming architectural visions into structural realities with precision and innovation.
                </p>
            </div>
            <div>
                <h4 class="font-bold text-slate-900 dark:text-white mb-6 uppercase tracking-widest text-xs">Quick Links</h4>
                <ul class="space-y-4 text-sm font-medium">
                    <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="index.html">Home</a></li>
                    <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="about.html">About Us</a></li>
                    <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="services.html">Our Services</a></li>
                    <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="projects.html">Featured Projects</a></li>
                </ul>
            </div>
            <div>
                <h4 class="font-bold text-slate-900 dark:text-white mb-6 uppercase tracking-widest text-xs">Company</h4>
                <ul class="space-y-4 text-sm font-medium">
                    <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="why-choose-us.html">Why Choose Us</a></li>
                    <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="contact.html">Contact Us</a></li>
                    <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="index.html">Privacy Policy</a></li>
                    <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="index.html">Terms of Service</a></li>
                </ul>
            </div>
            <div>
                <h4 class="font-bold text-slate-900 dark:text-white mb-6 uppercase tracking-widest text-xs">Contact Info</h4>
                <ul class="space-y-4 text-sm">
                    <li class="flex items-start gap-3">
                        <span class="material-symbols-outlined text-primary text-xl">location_on</span>
                        <span class="text-slate-500 dark:text-slate-400">174, Ikorodu Road, Onipanu, Lagos, Nigeria</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="material-symbols-outlined text-primary text-xl">phone</span>
                        <span class="text-slate-500 dark:text-slate-400">+234 812 414 1514</span>
                    </li>
                    <li class="flex items-start gap-3">
                        <span class="material-symbols-outlined text-primary text-xl">mail</span>
                        <span class="break-all text-slate-500 dark:text-slate-400">admin@cordonblueglobal.com</span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="mt-16 pt-8 border-t border-slate-200 dark:border-white/5 text-center text-sm text-slate-500 dark:text-slate-500">
            <p>© 2022 Cordon Blue Global Services Ltd. All Rights Reserved.</p>
        </div>
    </div>
</footer>
        `;
    }
}

customElements.define('main-footer', MainFooter);
