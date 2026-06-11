/** Helper function to securely create DOM elements */
function createElement(tag, attributes = {}, ...children) {
    const el = document.createElement(tag);
    for (const [key, value] of Object.entries(attributes)) {
        if (key === 'className') {
            el.className = value;
        } else if (key === 'textContent') {
            el.textContent = value;
        } else if (key.startsWith('on') && typeof value === 'function') {
            el.addEventListener(key.toLowerCase().substring(2), value);
        } else if (value !== null && value !== undefined && value !== '') {
            el.setAttribute(key, value);
        } else if (value === '') {
            el.setAttribute(key, '');
        }
    }
    children.forEach((child) => {
        if (child) {
            if (typeof child === 'string') {
                el.appendChild(document.createTextNode(child));
            } else if (Array.isArray(child)) {
                child.forEach((c) => c && el.appendChild(c));
            } else if (child instanceof Node) {
                el.appendChild(child);
            }
        }
    });
    return el;
}

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
            (currentPath.endsWith('index.html') && filename === 'index.html') ||
            currentPath.endsWith(filename);

        return [
            {
                name: 'Home',
                href: 'index.html',
                active: isActive('index.html'),
            },
            {
                name: 'About Us',
                href: 'about.html',
                active: isActive('about.html'),
            },
            {
                name: 'Services',
                href: 'services.html',
                active: isActive('services.html'),
            },
            {
                name: 'Projects',
                href: 'projects.html',
                active: isActive('projects.html'),
            },
            {
                name: 'Why Choose Us',
                href: 'why-choose-us.html',
                active: isActive('why-choose-us.html'),
            },
            {
                name: 'Contact',
                href: 'contact.html',
                active: isActive('contact.html'),
            },
            {
                name: 'Clients',
                href: 'clients.html',
                active: isActive('clients.html'),
            },
        ];
    }

    /** Render navigation link */
    renderNavLink = (link) => {
        return createElement(
            'a',
            {
                href: link.href,
                className: `text-sm font-semibold transition-colors ${link.active ? 'text-primary' : 'text-slate-600 dark:text-slate-300 hover:text-primary dark:hover:text-white'}`,
                ...(link.active ? { 'aria-current': 'page' } : {}),
            },
            link.name,
        );
    };

    /** Render mobile navigation link */
    renderMobileNavLink = (link) => {
        return createElement(
            'a',
            {
                href: link.href,
                className: `text-base font-semibold px-4 py-2 rounded-lg transition-colors ${link.active ? 'bg-primary/10 text-primary' : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-surface-dark'}`,
                ...(link.active ? { 'aria-current': 'page' } : {}),
            },
            link.name,
        );
    };

    render() {
        const navLinks = this.getNavLinks();

        this.innerHTML = '';
        const elements = [
            createElement(
                'header',
                { className: 'max-w-7xl mx-auto px-4 sm:px-6 lg:px-8' },
                createElement(
                    'div',
                    { className: 'flex h-16 items-center justify-between' },
                    createElement(
                        'div',
                        { className: 'flex items-center gap-3' },
                        createElement(
                            'a',
                            {
                                href: 'index.html',
                                className: 'flex items-center gap-3',
                                'aria-label':
                                    'Cordon Blue Global Services - Home',
                            },
                            createElement(
                                'div',
                                {
                                    className:
                                        'size-10 bg-white rounded-xl flex items-center justify-center overflow-hidden shrink-0 shadow-sm border border-slate-200/50',
                                },
                                createElement('img', {
                                    alt: 'Cordon Blue Logo',
                                    className:
                                        'w-full h-full object-contain p-0.5',
                                    src: './assets/images/logo_header.png',
                                    loading: 'eager',
                                }),
                            ),
                            createElement(
                                'div',
                                { className: 'flex flex-col' },
                                createElement(
                                    'span',
                                    {
                                        className:
                                            'text-lg md:text-xl font-bold leading-tight tracking-tight text-slate-900 dark:text-white',
                                    },
                                    'Cordon Blue',
                                ),
                                createElement(
                                    'span',
                                    {
                                        className:
                                            'text-[13px] md:text-sm text-slate-500 dark:text-slate-400 font-semibold leading-tight mt-0.5',
                                    },
                                    'Global Services Ltd.',
                                ),
                            ),
                        ),
                    ),
                    createElement(
                        'nav',
                        {
                            className: 'hidden md:flex items-center gap-6',
                            role: 'navigation',
                            'aria-label': 'Main navigation',
                        },
                        ...navLinks.map((link) => this.renderNavLink(link)),
                    ),
                    createElement(
                        'div',
                        { className: 'flex items-center gap-4' },
                        createElement(
                            'a',
                            {
                                href: 'contact.html',
                                className:
                                    'hidden sm:flex items-center justify-center rounded-xl bg-primary px-6 py-2.5 text-sm font-bold text-white hover:bg-primary/90 hover:scale-105 active:scale-95 transition-all shadow-lg shadow-primary/20',
                            },
                            ' Get a Quote ',
                        ),
                        createElement(
                            'button',
                            {
                                id: 'mobile-menu-button',
                                className:
                                    'md:hidden text-slate-900 dark:text-white p-2',
                                'aria-label': 'Toggle menu',
                                'aria-expanded': 'false',
                                'aria-controls': 'mobile-menu',
                            },
                            createElement(
                                'span',
                                {
                                    className: 'material-symbols-outlined',
                                    'aria-hidden': 'true',
                                },
                                'menu',
                            ),
                        ),
                    ),
                ),
            ),
            createElement(
                'div',
                {
                    id: 'mobile-menu',
                    className:
                        'hidden md:hidden absolute top-20 left-0 w-full bg-white dark:bg-background-dark border-b border-slate-200 dark:border-white/5 z-50 transition-all duration-300 ease-in-out shadow-xl',
                    role: 'dialog',
                    'aria-label': 'Mobile navigation',
                },
                createElement(
                    'nav',
                    {
                        className: 'flex flex-col p-4 space-y-4',
                        'aria-label': 'Mobile navigation links',
                    },
                    ...navLinks.map((link) => this.renderMobileNavLink(link)),
                    createElement(
                        'a',
                        {
                            href: 'contact.html',
                            className:
                                'flex items-center justify-center rounded-xl bg-primary px-6 py-3 text-base font-bold text-white hover:bg-primary/90 transition-all shadow-lg shadow-primary/20 mt-2',
                        },
                        ' Get a Quote ',
                    ),
                ),
            ),
        ];
        elements.forEach((el) => this.appendChild(el));
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
                    const icon = button.querySelector(
                        '.material-symbols-outlined',
                    );
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

        this.innerHTML = '';
        const element = createElement(
            'footer',
            {
                className:
                    'bg-white dark:bg-background-dark py-20 border-t border-slate-200 dark:border-white/5',
            },
            createElement(
                'div',
                { className: 'max-w-7xl mx-auto px-4 sm:px-6 lg:px-8' },
                createElement(
                    'div',
                    {
                        className:
                            'inline-block bg-white p-2 rounded-xl shadow-sm border border-slate-200/50 mb-12',
                    },
                    createElement('img', {
                        alt: 'Cordon Blue Global Services',
                        loading: 'lazy',
                        className: 'h-12 w-auto object-contain',
                        src: './assets/images/logo_header.png',
                    }),
                ),
                createElement(
                    'div',
                    {
                        className:
                            'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 border-t border-slate-200 dark:border-white/5 pt-16',
                    },
                    createElement(
                        'div',
                        { className: 'space-y-6' },
                        createElement(
                            'div',
                            { className: 'flex items-center gap-3' },
                            createElement(
                                'div',
                                {
                                    className:
                                        'flex items-center justify-center bg-primary p-1.5 rounded-lg',
                                    'aria-hidden': 'true',
                                },
                                createElement(
                                    'span',
                                    {
                                        className:
                                            'material-symbols-outlined text-white text-xl',
                                    },
                                    'business',
                                ),
                            ),
                            createElement(
                                'span',
                                {
                                    className:
                                        'text-lg font-bold tracking-tight text-slate-900 dark:text-white uppercase',
                                },
                                'Cordon Blue',
                            ),
                        ),
                        createElement(
                            'p',
                            {
                                className:
                                    'text-slate-500 dark:text-slate-400 text-sm leading-relaxed',
                            },
                            ' A premier construction firm dedicated to transforming architectural visions into structural realities with precision and innovation. ',
                        ),
                    ),
                    createElement(
                        'nav',
                        { 'aria-label': 'Quick Links' },
                        createElement(
                            'h3',
                            {
                                className:
                                    'font-bold text-slate-900 dark:text-white mb-6 uppercase tracking-widest text-xs',
                            },
                            'Quick Links',
                        ),
                        createElement(
                            'ul',
                            { className: 'space-y-4 text-sm font-medium' },
                            createElement(
                                'li',
                                {},
                                createElement(
                                    'a',
                                    {
                                        className:
                                            'text-slate-500 dark:text-slate-400 hover:text-primary transition-colors',
                                        href: 'index.html',
                                    },
                                    'Home',
                                ),
                            ),
                            createElement(
                                'li',
                                {},
                                createElement(
                                    'a',
                                    {
                                        className:
                                            'text-slate-500 dark:text-slate-400 hover:text-primary transition-colors',
                                        href: 'about.html',
                                    },
                                    'About Us',
                                ),
                            ),
                            createElement(
                                'li',
                                {},
                                createElement(
                                    'a',
                                    {
                                        className:
                                            'text-slate-500 dark:text-slate-400 hover:text-primary transition-colors',
                                        href: 'services.html',
                                    },
                                    'Our Services',
                                ),
                            ),
                            createElement(
                                'li',
                                {},
                                createElement(
                                    'a',
                                    {
                                        className:
                                            'text-slate-500 dark:text-slate-400 hover:text-primary transition-colors',
                                        href: 'projects.html',
                                    },
                                    'Featured Projects',
                                ),
                            ),
                        ),
                    ),
                    createElement(
                        'nav',
                        { 'aria-label': 'Company Links' },
                        createElement(
                            'h3',
                            {
                                className:
                                    'font-bold text-slate-900 dark:text-white mb-6 uppercase tracking-widest text-xs',
                            },
                            'Company',
                        ),
                        createElement(
                            'ul',
                            { className: 'space-y-4 text-sm font-medium' },
                            createElement(
                                'li',
                                {},
                                createElement(
                                    'a',
                                    {
                                        className:
                                            'text-slate-500 dark:text-slate-400 hover:text-primary transition-colors',
                                        href: 'why-choose-us.html',
                                    },
                                    'Why Choose Us',
                                ),
                            ),
                            createElement(
                                'li',
                                {},
                                createElement(
                                    'a',
                                    {
                                        className:
                                            'text-slate-500 dark:text-slate-400 hover:text-primary transition-colors',
                                        href: 'contact.html',
                                    },
                                    'Contact Us',
                                ),
                            ),
                            createElement(
                                'li',
                                {},
                                createElement(
                                    'a',
                                    {
                                        className:
                                            'text-slate-500 dark:text-slate-400 hover:text-primary transition-colors',
                                        href: 'privacy.html',
                                    },
                                    'Privacy Policy',
                                ),
                            ),
                            createElement(
                                'li',
                                {},
                                createElement(
                                    'a',
                                    {
                                        className:
                                            'text-slate-500 dark:text-slate-400 hover:text-primary transition-colors',
                                        href: 'terms.html',
                                    },
                                    'Terms of Service',
                                ),
                            ),
                        ),
                    ),
                    createElement(
                        'address',
                        { className: 'not-italic' },
                        createElement(
                            'h3',
                            {
                                className:
                                    'font-bold text-slate-900 dark:text-white mb-6 uppercase tracking-widest text-xs',
                            },
                            'Contact Info',
                        ),
                        createElement(
                            'ul',
                            { className: 'space-y-4 text-sm' },
                            createElement(
                                'li',
                                { className: 'flex items-start gap-3' },
                                createElement(
                                    'span',
                                    {
                                        className:
                                            'material-symbols-outlined text-primary text-xl',
                                        'aria-hidden': 'true',
                                    },
                                    'location_on',
                                ),
                                createElement(
                                    'span',
                                    {
                                        className:
                                            'text-slate-500 dark:text-slate-400',
                                    },
                                    '174, Ikorodu Road, Onipanu, Lagos, Nigeria',
                                ),
                            ),
                            createElement(
                                'li',
                                { className: 'flex items-start gap-3' },
                                createElement(
                                    'span',
                                    {
                                        className:
                                            'material-symbols-outlined text-primary text-xl',
                                        'aria-hidden': 'true',
                                    },
                                    'phone',
                                ),
                                createElement(
                                    'a',
                                    {
                                        href: 'tel:+2348124141514',
                                        className:
                                            'text-slate-500 dark:text-slate-400 hover:text-primary transition-colors',
                                    },
                                    '+234 812 414 1514',
                                ),
                            ),
                            createElement(
                                'li',
                                { className: 'flex items-start gap-3' },
                                createElement(
                                    'span',
                                    {
                                        className:
                                            'material-symbols-outlined text-primary text-xl',
                                        'aria-hidden': 'true',
                                    },
                                    'mail',
                                ),
                                createElement(
                                    'a',
                                    {
                                        href: 'mailto:info@cordonblueglobal.com',
                                        className:
                                            'break-all text-slate-500 dark:text-slate-400 hover:text-primary transition-colors',
                                    },
                                    'info@cordonblueglobal.com',
                                ),
                            ),
                            createElement(
                                'li',
                                { className: 'flex items-start gap-3' },
                                createElement(
                                    'a',
                                    {
                                        href: 'https://www.linkedin.com/company/cordon-blue-global-services-ltd',
                                        target: '_blank',
                                        rel: 'noopener noreferrer',
                                        className:
                                            'flex items-center gap-3 hover:text-primary transition-colors',
                                    },
                                    createElement(
                                        'span',
                                        {
                                            className:
                                                'material-symbols-outlined text-primary text-xl',
                                            'aria-hidden': 'true',
                                        },
                                        'share',
                                    ),
                                    createElement(
                                        'span',
                                        {
                                            className:
                                                'text-slate-500 dark:text-slate-400',
                                        },
                                        'LinkedIn',
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
                createElement(
                    'div',
                    {
                        className:
                            'mt-16 pt-8 border-t border-slate-200 dark:border-white/5 text-center text-sm text-slate-500 dark:text-slate-500',
                    },
                    createElement(
                        'p',
                        {},
                        '© ',
                        currentYear.toString(),
                        ' Cordon Blue Global Services Ltd. All Rights Reserved.',
                    ),
                ),
            ),
        );
        this.appendChild(element);
    }
}

customElements.define('main-footer', MainFooter);
