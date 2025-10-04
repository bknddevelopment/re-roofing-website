/**
 * Town Service Navigation - Floating Sidebar
 * Displays contextual service links for the current town
 */

// Initialize town service navigation on page load
document.addEventListener('DOMContentLoaded', function() {
    initTownServiceNav();
});

function initTownServiceNav() {
    // Detect current town and service from URL
    const currentPath = window.location.pathname;
    const pageFile = currentPath.split('/').pop();

    // Extract town name from filename (e.g., "roofing-west-orange-nj.html" -> "west-orange")
    const townMatch = pageFile.match(/-([\w-]+)-nj\.html$/);
    if (!townMatch) return; // Not a town page

    const townSlug = townMatch[1];
    const townName = formatTownName(townSlug);

    // Detect current service type
    const currentService = detectCurrentService(pageFile);

    // Create floating navigation
    createFloatingNav(townSlug, townName, currentService);
}

function detectCurrentService(filename) {
    if (filename.includes('emergency-roof-repair')) return 'emergency';
    if (filename.includes('roof-leak-repair')) return 'leak';
    if (filename.includes('roof-replacement')) return 'replacement';
    if (filename.includes('roof-repair')) return 'repair';
    if (filename.includes('new-roof-installation')) return 'installation';
    if (filename.includes('siding-installation')) return 'siding-install';
    if (filename.includes('siding-repair')) return 'siding-repair';
    if (filename.includes('gutter-installation')) return 'gutter-install';
    if (filename.includes('gutter-repair')) return 'gutter-repair';
    if (filename.includes('roofing-')) return 'overview';
    return null;
}

function formatTownName(slug) {
    return slug
        .split('-')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

function createFloatingNav(townSlug, townName, currentService) {
    // Service configuration with icons and labels
    const services = [
        {
            id: 'overview',
            icon: 'fas fa-home',
            label: 'Overview',
            url: `roofing-${townSlug}-nj.html`,
            color: '#000000'
        },
        {
            id: 'emergency',
            icon: 'fas fa-exclamation-triangle',
            label: 'Emergency Repair',
            url: `emergency-roof-repair-${townSlug}-nj.html`,
            color: '#FF3B30'
        },
        {
            id: 'leak',
            icon: 'fas fa-tint',
            label: 'Leak Repair',
            url: `roof-leak-repair-${townSlug}-nj.html`,
            color: '#007AFF'
        },
        {
            id: 'repair',
            icon: 'fas fa-tools',
            label: 'Roof Repair',
            url: `roof-repair-${townSlug}-nj.html`,
            color: '#FF6B35'
        },
        {
            id: 'replacement',
            icon: 'fas fa-sync-alt',
            label: 'Replacement',
            url: `roof-replacement-${townSlug}-nj.html`,
            color: '#5856D6'
        },
        {
            id: 'installation',
            icon: 'fas fa-hammer',
            label: 'New Installation',
            url: `new-roof-installation-${townSlug}-nj.html`,
            color: '#34C759'
        },
        {
            id: 'siding-install',
            icon: 'fas fa-layer-group',
            label: 'Siding Install',
            url: `siding-installation-${townSlug}-nj.html`,
            color: '#AF52DE'
        },
        {
            id: 'gutter-install',
            icon: 'fas fa-water',
            label: 'Gutter Install',
            url: `gutter-installation-${townSlug}-nj.html`,
            color: '#00C7BE'
        }
    ];

    // Create floating nav container
    const navContainer = document.createElement('div');
    navContainer.className = 'floating-service-nav';
    navContainer.innerHTML = `
        <div class="floating-nav-header">
            <span class="town-label">${townName} Services</span>
        </div>
        <div class="floating-nav-items">
            ${services.map(service => `
                <a href="${service.url}"
                   class="floating-nav-item ${service.id === currentService ? 'active' : ''}"
                   data-service="${service.id}"
                   title="${service.label}">
                    <div class="nav-icon" style="background-color: ${service.color}">
                        <i class="${service.icon}"></i>
                    </div>
                    <span class="nav-label">${service.label}</span>
                </a>
            `).join('')}
        </div>
    `;

    // Add to page
    document.body.appendChild(navContainer);

    // Add CSS styles
    addFloatingNavStyles();

    // Handle scroll behavior
    handleScrollBehavior(navContainer);
}

function addFloatingNavStyles() {
    // Check if styles already added
    if (document.getElementById('floating-nav-styles')) return;

    const style = document.createElement('style');
    style.id = 'floating-nav-styles';
    style.textContent = `
        .floating-service-nav {
            position: fixed;
            left: 20px;
            top: 50%;
            transform: translateY(-50%);
            background: white;
            border-radius: 16px;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
            padding: 16px 12px;
            z-index: 900;
            max-width: 200px;
            transition: all 0.3s ease;
        }

        .floating-nav-header {
            padding-bottom: 12px;
            margin-bottom: 12px;
            border-bottom: 2px solid #f0f0f0;
        }

        .town-label {
            font-size: 13px;
            font-weight: 700;
            color: #333;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            display: block;
            text-align: center;
        }

        .floating-nav-items {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .floating-nav-item {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 10px 12px;
            border-radius: 10px;
            text-decoration: none;
            color: #333;
            transition: all 0.2s ease;
            background: #f8f8f8;
        }

        .floating-nav-item:hover {
            background: #e8e8e8;
            transform: translateX(4px);
        }

        .floating-nav-item.active {
            background: linear-gradient(135deg, #FF6B35 0%, #FF3B30 100%);
            color: white;
            box-shadow: 0 4px 12px rgba(255, 59, 48, 0.3);
        }

        .floating-nav-item.active .nav-icon {
            background: white !important;
            color: #FF3B30;
        }

        .nav-icon {
            width: 36px;
            height: 36px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            transition: all 0.2s ease;
        }

        .nav-icon i {
            font-size: 16px;
            color: white;
        }

        .floating-nav-item.active .nav-icon i {
            color: #FF3B30;
        }

        .nav-label {
            font-size: 13px;
            font-weight: 600;
            white-space: nowrap;
        }

        /* Hide on mobile */
        @media (max-width: 1024px) {
            .floating-service-nav {
                display: none;
            }
        }

        /* Adjust for tablet */
        @media (max-width: 1280px) {
            .floating-service-nav {
                left: 10px;
                max-width: 180px;
            }

            .nav-label {
                font-size: 12px;
            }

            .nav-icon {
                width: 32px;
                height: 32px;
            }

            .nav-icon i {
                font-size: 14px;
            }
        }

        /* Scroll hidden state */
        .floating-service-nav.scroll-hidden {
            opacity: 0;
            pointer-events: none;
            transform: translateY(-50%) translateX(-20px);
        }
    `;

    document.head.appendChild(style);
}

function handleScrollBehavior(navContainer) {
    let lastScrollTop = 0;
    let scrollTimeout;

    window.addEventListener('scroll', function() {
        clearTimeout(scrollTimeout);

        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        // Hide when scrolling down past header
        if (scrollTop > 100 && scrollTop > lastScrollTop) {
            navContainer.classList.add('scroll-hidden');
        } else {
            navContainer.classList.remove('scroll-hidden');
        }

        lastScrollTop = scrollTop;

        // Show again after scroll stops
        scrollTimeout = setTimeout(function() {
            navContainer.classList.remove('scroll-hidden');
        }, 500);
    });
}
