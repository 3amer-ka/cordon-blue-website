/**
 * Cordon Blue Global Services - Navigation Components
 * Modern Web Components with semantic HTML and accessibility
 */

class MainHeader extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.render();
        this.addEventListeners();
    }

    /** Get navigation links with active state detection */
    getNavLinks() {
        const currentPath = window.location.pathname;
        const isActive = (filename) =>
            currentPath === '/' ||
            currentPath.endsWith('index.html') && filename === 'index.html' ||
            currentPath.endsWith(filename);

        return [
            { name: 'Home', href: 'index.html', active: isActive('index.html') },
            { name: 'About Us', href: 'about.html', active: isActive('about.html') },
            { name: 'Services', href: 'services.html', active: isActive('services.html') },
            { name: 'Projects', href: 'projects.html', active: isActive('projects.html') },
            { name: 'Why Choose Us', href: 'why-choose-us.html', active: isActive('why-choose-us.html') },
            { name: 'Contact', href: 'contact.html', active: isActive('contact.html') },
            { name: 'Clients', href: 'clients.html', active: isActive('clients.html') }
        ];
    }

    /** Render navigation link */
    renderNavLink = (link) => `
        <a href="${link.href}" 
           class="text-sm font-semibold transition-colors ${link.active ? 'text-primary' : 'text-slate-600 dark:text-slate-300 hover:text-primary dark:hover:text-white'}"
           ${link.active ? 'aria-current="page"' : ''}>
            ${link.name}
        </a>
    `;

    /** Render mobile navigation link */
    renderMobileNavLink = (link) => `
        <a href="${link.href}" 
           class="text-base font-semibold px-4 py-2 rounded-lg transition-colors ${link.active ? 'bg-primary/10 text-primary' : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-surface-dark'}"
           ${link.active ? 'aria-current="page"' : ''}>
            ${link.name}
        </a>
    `;

    render() {
        const navLinks = this.getNavLinks();

        this.innerHTML = `
            <header class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex h-16 items-center justify-between">
                    <div class="flex items-center gap-3">
                        <a href="index.html" class="flex items-center gap-3" aria-label="Cordon Blue Global Services - Home">
                            <div class="size-10 bg-white rounded-xl flex items-center justify-center overflow-hidden shrink-0 shadow-sm border border-slate-200/50">
                                <img alt="Cordon Blue Logo" class="w-full h-full object-contain p-0.5" src="./assets/logo_header.png" loading="eager"/>
                            </div>
                            <div class="flex flex-col">
                                <span class="text-lg md:text-xl font-bold leading-tight tracking-tight text-slate-900 dark:text-white">Cordon Blue</span>
                                <span class="text-[13px] md:text-sm text-slate-500 dark:text-slate-400 font-semibold leading-tight mt-0.5">Global Services Ltd.</span>
                            </div>
                        </a>
                    </div>

                    <nav class="hidden md:flex items-center gap-6" role="navigation" aria-label="Main navigation">
                        ${navLinks.map(this.renderNavLink).join('')}
                    </nav>

                    <div class="flex items-center gap-4">
                        <a href="contact.html" class="hidden sm:flex items-center justify-center rounded-xl bg-primary px-6 py-2.5 text-sm font-bold text-white hover:bg-primary/90 hover:scale-105 active:scale-95 transition-all shadow-lg shadow-primary/20">
                            Get a Quote
                        </a>
                        <button id="mobile-menu-button" class="md:hidden text-slate-900 dark:text-white p-2" aria-label="Toggle menu" aria-expanded="false" aria-controls="mobile-menu">
                            <span class="material-symbols-outlined" aria-hidden="true">menu</span>
                        </button>
                    </div>
                </div>
            </header>

            <!-- Mobile Menu -->
            <div id="mobile-menu" class="hidden md:hidden absolute top-20 left-0 w-full bg-white dark:bg-background-dark border-b border-slate-200 dark:border-white/5 z-50 transition-all duration-300 ease-in-out shadow-xl" role="dialog" aria-label="Mobile navigation">
                <nav class="flex flex-col p-4 space-y-4" aria-label="Mobile navigation links">
                    ${navLinks.map(this.renderMobileNavLink).join('')}
                    <a href="contact.html" class="flex items-center justify-center rounded-xl bg-primary px-6 py-3 text-base font-bold text-white hover:bg-primary/90 transition-all shadow-lg shadow-primary/20 mt-2">
                        Get a Quote
                    </a>
                </nav>
            </div>
        `;
    }

    addEventListeners() {
        const button = this.querySelector('#mobile-menu-button');
        const menu = this.querySelector('#mobile-menu');

        if (button && menu) {
            button.addEventListener('click', () => {
                const isHidden = menu.classList.toggle('hidden');
                button.setAttribute('aria-expanded', !isHidden);

                const icon = button.querySelector('.material-symbols-outlined');
                if (icon) {
                    icon.textContent = isHidden ? 'menu' : 'close';
                }
            });

            // Close menu on escape key
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && !menu.classList.contains('hidden')) {
                    menu.classList.add('hidden');
                    button.setAttribute('aria-expanded', 'false');
                    const icon = button.querySelector('.material-symbols-outlined');
                    if (icon) icon.textContent = 'menu';
                    button.focus();
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
        const currentYear = new Date().getFullYear();

        this.innerHTML = `
            <footer class="bg-white dark:bg-background-dark py-20 border-t border-slate-200 dark:border-white/5">
                <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="inline-block bg-white p-2 rounded-xl shadow-sm border border-slate-200/50 mb-12">
                        <img alt="Cordon Blue Global Services" loading="lazy" class="h-12 w-auto object-contain" src="./assets/logo_header.png"/>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 border-t border-slate-200 dark:border-white/5 pt-16">
                        <div class="space-y-6">
                            <div class="flex items-center gap-3">
                                <div class="flex items-center justify-center bg-primary p-1.5 rounded-lg" aria-hidden="true">
                                    <span class="material-symbols-outlined text-white text-xl">business</span>
                                </div>
                                <span class="text-lg font-bold tracking-tight text-slate-900 dark:text-white uppercase">Cordon Blue</span>
                            </div>
                            <p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">
                                A premier construction firm dedicated to transforming architectural visions into structural realities with precision and innovation.
                            </p>
                        </div>
                        <nav aria-label="Quick Links">
                            <h3 class="font-bold text-slate-900 dark:text-white mb-6 uppercase tracking-widest text-xs">Quick Links</h3>
                            <ul class="space-y-4 text-sm font-medium">
                                <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="index.html">Home</a></li>
                                <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="about.html">About Us</a></li>
                                <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="services.html">Our Services</a></li>
                                <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="projects.html">Featured Projects</a></li>
                            </ul>
                        </nav>
                        <nav aria-label="Company Links">
                            <h3 class="font-bold text-slate-900 dark:text-white mb-6 uppercase tracking-widest text-xs">Company</h3>
                            <ul class="space-y-4 text-sm font-medium">
                                <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="why-choose-us.html">Why Choose Us</a></li>
                                <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="contact.html">Contact Us</a></li>
                                <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="privacy.html">Privacy Policy</a></li>
                                <li><a class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors" href="terms.html">Terms of Service</a></li>
                            </ul>
                        </nav>
                        <address class="not-italic">
                            <h3 class="font-bold text-slate-900 dark:text-white mb-6 uppercase tracking-widest text-xs">Contact Info</h3>
                            <ul class="space-y-4 text-sm">
                                <li class="flex items-start gap-3">
                                    <span class="material-symbols-outlined text-primary text-xl" aria-hidden="true">location_on</span>
                                    <span class="text-slate-500 dark:text-slate-400">174, Ikorodu Road, Onipanu, Lagos, Nigeria</span>
                                </li>
                                <li class="flex items-start gap-3">
                                    <span class="material-symbols-outlined text-primary text-xl" aria-hidden="true">phone</span>
                                    <a href="tel:+2348124141514" class="text-slate-500 dark:text-slate-400 hover:text-primary transition-colors">+234 812 414 1514</a>
                                </li>
                                <li class="flex items-start gap-3">
                                    <span class="material-symbols-outlined text-primary text-xl" aria-hidden="true">mail</span>
                                    <a href="mailto:info@cordonblueglobal.com" class="break-all text-slate-500 dark:text-slate-400 hover:text-primary transition-colors">info@cordonblueglobal.com</a>
                                </li>
                                <li class="flex items-start gap-3">
                                    <a href="https://www.linkedin.com/company/cordon-blue-global-services-ltd" target="_blank" rel="noopener noreferrer" class="flex items-center gap-3 hover:text-primary transition-colors">
                                        <span class="material-symbols-outlined text-primary text-xl" aria-hidden="true">share</span>
                                        <span class="text-slate-500 dark:text-slate-400">LinkedIn</span>
                                    </a>
                                </li>
                            </ul>
                        </address>
                    </div>
                    <div class="mt-16 pt-8 border-t border-slate-200 dark:border-white/5 text-center text-sm text-slate-500 dark:text-slate-500">
                        <p>&copy; ${currentYear} Cordon Blue Global Services Ltd. All Rights Reserved.</p>
                    </div>
                </div>
            </footer>
        `;
    }
}

customElements.define('main-footer', MainFooter);
