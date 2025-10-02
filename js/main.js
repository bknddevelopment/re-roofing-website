// DOM Content Loaded
document.addEventListener('DOMContentLoaded', function() {
    initScrollEffects();
    initSmoothScrolling();
    initAnimations();
    initMobileMenu();
    initFAQ();
    initCalculator();
    initLiveChat();
    initBackToTop();
    initCookieConsent();
});

// Smooth scrolling for anchor links
function initSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                const headerHeight = 70; // Fixed header height
                const targetPosition = targetElement.offsetTop - headerHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Scroll effects
function initScrollEffects() {
    const header = document.querySelector('.header');

    // Header scroll effect
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
}

// Animation on scroll
function initAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);

    // Observe elements for animation
    const animateElements = document.querySelectorAll('.service-card, .feature, .process-step, .review');
    animateElements.forEach(element => {
        observer.observe(element);
    });
}

// Add CSS for animations
const style = document.createElement('style');
style.textContent = `
    .service-card,
    .feature,
    .process-step,
    .review {
        opacity: 0;
        transform: translateY(30px);
        transition: all 0.6s ease;
    }

    .animate-in {
        opacity: 1;
        transform: translateY(0);
    }

    .header.scrolled {
        box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
    }
`;

document.head.appendChild(style);

// Button interactions
document.querySelectorAll('.btn-primary, .cta-button').forEach(button => {
    button.addEventListener('click', function(e) {
        // Add click effect
        this.style.transform = 'translateY(-2px) scale(0.98)';
        setTimeout(() => {
            this.style.transform = '';
        }, 150);
    });
});

// Service card hover effects
document.querySelectorAll('.service-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-10px) scale(1.02)';
    });

    card.addEventListener('mouseleave', function() {
        // Reset to original state based on card type
        if (this.classList.contains('card-2')) {
            this.style.transform = 'scale(1.05) translateY(-20px)';
        } else {
            this.style.transform = '';
        }
    });
});

// Modal Functionality
const modal = document.getElementById('contactModal');
const closeModal = document.querySelector('.close-modal');
const contactForm = document.getElementById('contactForm');

// Open modal when CTA buttons are clicked
document.querySelectorAll('.cta-button, .btn-primary').forEach(button => {
    if (!button.classList.contains('submit-btn')) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            modal.classList.add('show');
            document.body.style.overflow = 'hidden';
        });
    }
});

// Close modal
closeModal.addEventListener('click', function() {
    modal.classList.remove('show');
    document.body.style.overflow = '';
});

// Close modal when clicking outside
modal.addEventListener('click', function(e) {
    if (e.target === modal) {
        modal.classList.remove('show');
        document.body.style.overflow = '';
    }
});

// Form Validation and Submission
contactForm.addEventListener('submit', function(e) {
    e.preventDefault();

    // Clear previous errors
    document.querySelectorAll('.error-message').forEach(msg => msg.remove());
    document.querySelectorAll('.error').forEach(field => field.classList.remove('error'));

    let isValid = true;

    // Validate required fields
    const requiredFields = contactForm.querySelectorAll('[required]');
    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            isValid = false;
            field.classList.add('error');
            const errorMsg = document.createElement('span');
            errorMsg.className = 'error-message';
            errorMsg.textContent = 'This field is required';
            field.parentElement.appendChild(errorMsg);
        }
    });

    // Validate email format
    const emailField = document.getElementById('email');
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailField.value && !emailRegex.test(emailField.value)) {
        isValid = false;
        emailField.classList.add('error');
        const errorMsg = document.createElement('span');
        errorMsg.className = 'error-message';
        errorMsg.textContent = 'Please enter a valid email address';
        emailField.parentElement.appendChild(errorMsg);
    }

    // Validate phone format
    const phoneField = document.getElementById('phone');
    const phoneRegex = /^[\d\s\-\(\)]+$/;
    if (phoneField.value && !phoneRegex.test(phoneField.value)) {
        isValid = false;
        phoneField.classList.add('error');
        const errorMsg = document.createElement('span');
        errorMsg.className = 'error-message';
        errorMsg.textContent = 'Please enter a valid phone number';
        phoneField.parentElement.appendChild(errorMsg);
    }

    if (isValid) {
        // Collect form data
        const formData = new FormData(contactForm);
        const data = Object.fromEntries(formData);

        // Show success message
        const successMsg = document.createElement('div');
        successMsg.className = 'success-message';
        successMsg.textContent = 'Thank you! We\'ll contact you within 24 hours.';
        contactForm.insertBefore(successMsg, contactForm.firstChild);

        // In production, this would be sent to a server
        // Example: fetch('/api/contact', { method: 'POST', body: JSON.stringify(data) });

        // Reset form after 2 seconds
        setTimeout(() => {
            contactForm.reset();
            successMsg.remove();
            modal.classList.remove('show');
            document.body.style.overflow = '';
        }, 2000);
    }
});

// Mobile Menu Functionality
function initMobileMenu() {
    const mobileToggle = document.querySelector('.mobile-menu-toggle');
    const mobileNav = document.querySelector('.mobile-nav');
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');
    const hasSubmenu = document.querySelectorAll('.has-submenu');

    // Toggle mobile menu
    mobileToggle.addEventListener('click', function() {
        mobileToggle.classList.toggle('active');
        mobileNav.classList.toggle('active');
        document.body.style.overflow = mobileNav.classList.contains('active') ? 'hidden' : '';
    });

    // Close menu when clicking a link
    mobileNavLinks.forEach(link => {
        if (!link.classList.contains('has-submenu')) {
            link.addEventListener('click', function() {
                mobileToggle.classList.remove('active');
                mobileNav.classList.remove('active');
                document.body.style.overflow = '';
            });
        }
    });

    // Handle submenu toggles
    hasSubmenu.forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            const submenu = this.nextElementSibling;
            if (submenu && submenu.classList.contains('mobile-submenu')) {
                submenu.classList.toggle('active');
            }
        });
    });
}

// FAQ Accordion
function initFAQ() {
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');

        question.addEventListener('click', function() {
            // Close other items
            faqItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                }
            });

            // Toggle current item
            item.classList.toggle('active');
        });
    });
}

// Roofing Calculator
function initCalculator() {
    const calculateBtn = document.getElementById('calculateBtn');
    if (!calculateBtn) return;

    calculateBtn.addEventListener('click', function() {
        // Get input values
        const roofSize = parseFloat(document.getElementById('roofSize').value) || 0;
        const roofType = document.getElementById('roofType').value;
        const material = document.getElementById('material').value;
        const layers = document.getElementById('layers').value;

        // Validate inputs
        if (roofSize < 500 || !roofType || !material) {
            alert('Please fill in all required fields');
            return;
        }

        // Base material costs per sq ft
        const materialCosts = {
            asphalt: { low: 3, high: 5 },
            architectural: { low: 4, high: 7 },
            metal: { low: 7, high: 12 },
            tile: { low: 8, high: 15 },
            slate: { low: 15, high: 25 }
        };

        // Complexity multipliers
        const complexityMultiplier = {
            gable: 1,
            hip: 1.1,
            flat: 0.9,
            shed: 0.95,
            complex: 1.25
        };

        // Calculate base cost
        const baseCost = materialCosts[material];
        const complexity = complexityMultiplier[roofType];

        let lowEstimate = roofSize * baseCost.low * complexity;
        let highEstimate = roofSize * baseCost.high * complexity;

        // Add tear-off costs if needed
        if (layers === '2') {
            lowEstimate += roofSize * 1;
            highEstimate += roofSize * 2;
        } else if (layers === '3') {
            lowEstimate += roofSize * 2;
            highEstimate += roofSize * 3.5;
        }

        // Add additional services
        const additionalServices = [];
        if (document.getElementById('gutters').checked) {
            lowEstimate += 1500;
            highEstimate += 3000;
            additionalServices.push({ name: 'New Gutters', low: 1500, high: 3000 });
        }
        if (document.getElementById('ventilation').checked) {
            lowEstimate += 500;
            highEstimate += 1500;
            additionalServices.push({ name: 'Ventilation', low: 500, high: 1500 });
        }
        if (document.getElementById('skylights').checked) {
            lowEstimate += 1000;
            highEstimate += 3000;
            additionalServices.push({ name: 'Skylights', low: 1000, high: 3000 });
        }
        if (document.getElementById('chimney').checked) {
            lowEstimate += 500;
            highEstimate += 2000;
            additionalServices.push({ name: 'Chimney Repair', low: 500, high: 2000 });
        }

        // Display results
        document.getElementById('lowPrice').textContent = '$' + Math.round(lowEstimate).toLocaleString();
        document.getElementById('highPrice').textContent = '$' + Math.round(highEstimate).toLocaleString();

        // Show breakdown
        const breakdown = document.getElementById('breakdown');
        const breakdownList = document.getElementById('breakdownList');

        breakdownList.innerHTML = '';

        // Add roofing cost
        const roofingItem = document.createElement('li');
        const roofingLabel = document.createElement('span');
        roofingLabel.textContent = `Roofing (${roofSize} sq ft)`;
        const roofingPrice = document.createElement('span');
        roofingPrice.textContent = `$${Math.round(roofSize * baseCost.low).toLocaleString()} - $${Math.round(roofSize * baseCost.high).toLocaleString()}`;
        roofingItem.appendChild(roofingLabel);
        roofingItem.appendChild(roofingPrice);
        breakdownList.appendChild(roofingItem);

        // Add tear-off if needed
        if (layers !== '1') {
            const tearOffItem = document.createElement('li');
            const tearOffLow = layers === '2' ? roofSize * 1 : roofSize * 2;
            const tearOffHigh = layers === '2' ? roofSize * 2 : roofSize * 3.5;
            const tearOffLabel = document.createElement('span');
            tearOffLabel.textContent = `Tear-off (${layers === '2' ? '1' : 'Multiple'} layer${layers === '2' ? '' : 's'})`;
            const tearOffPrice = document.createElement('span');
            tearOffPrice.textContent = `$${Math.round(tearOffLow).toLocaleString()} - $${Math.round(tearOffHigh).toLocaleString()}`;
            tearOffItem.appendChild(tearOffLabel);
            tearOffItem.appendChild(tearOffPrice);
            breakdownList.appendChild(tearOffItem);
        }

        // Add additional services
        additionalServices.forEach(service => {
            const serviceItem = document.createElement('li');
            const serviceLabel = document.createElement('span');
            serviceLabel.textContent = service.name;
            const servicePrice = document.createElement('span');
            servicePrice.textContent = `$${service.low.toLocaleString()} - $${service.high.toLocaleString()}`;
            serviceItem.appendChild(serviceLabel);
            serviceItem.appendChild(servicePrice);
            breakdownList.appendChild(serviceItem);
        });

        breakdown.style.display = 'block';

        // Scroll to results
        document.getElementById('calcResults').scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
}

// Live Chat Widget
function initLiveChat() {
    const chatToggle = document.querySelector('.chat-toggle');
    const chatWindow = document.querySelector('.chat-window');
    const chatClose = document.querySelector('.chat-close');
    const chatInput = document.getElementById('chatInput');
    const chatSend = document.querySelector('.chat-send');
    const chatBody = document.querySelector('.chat-body');
    const chatBadge = document.querySelector('.chat-badge');

    if (!chatToggle || !chatWindow) return;

    // Toggle chat window
    chatToggle.addEventListener('click', function() {
        chatWindow.classList.toggle('active');
        if (chatWindow.classList.contains('active')) {
            chatBadge.style.display = 'none';
            chatInput.focus();
        }
    });

    // Close chat window
    chatClose.addEventListener('click', function() {
        chatWindow.classList.remove('active');
    });

    // Send message
    function sendMessage() {
        const message = chatInput.value.trim();
        if (!message) return;

        // Add user message
        const userMessage = document.createElement('div');
        userMessage.className = 'chat-message user';
        const userParagraph = document.createElement('p');
        userParagraph.textContent = message;
        userMessage.appendChild(userParagraph);
        chatBody.appendChild(userMessage);

        // Clear input
        chatInput.value = '';

        // Scroll to bottom
        chatBody.scrollTop = chatBody.scrollHeight;

        // Simulate bot response
        setTimeout(() => {
            const botMessage = document.createElement('div');
            botMessage.className = 'chat-message bot';

            // Generate response based on keywords
            let response = '';
            const lowerMessage = message.toLowerCase();

            if (lowerMessage.includes('estimate') || lowerMessage.includes('quote') || lowerMessage.includes('cost')) {
                response = 'I\'d be happy to help with an estimate! Please click "Get Free Quote" at the top of the page or call us at (862) 224-6666.';
            } else if (lowerMessage.includes('emergency') || lowerMessage.includes('leak')) {
                response = 'For emergency repairs, please call us immediately at (862) 224-6666. We offer 24/7 emergency service!';
            } else if (lowerMessage.includes('insurance')) {
                response = 'Yes, we work with insurance companies! We can help navigate the claims process. Call us for assistance.';
            } else if (lowerMessage.includes('warranty')) {
                response = 'We offer comprehensive warranties on both materials and workmanship. Most materials come with 20-50 year warranties.';
            } else {
                response = 'Thank you for your message! One of our roofing experts will get back to you shortly. For immediate assistance, call (862) 224-6666.';
            }

            const botParagraph = document.createElement('p');
            botParagraph.textContent = response;
            botMessage.appendChild(botParagraph);
            chatBody.appendChild(botMessage);
            chatBody.scrollTop = chatBody.scrollHeight;
        }, 1000);
    }

    chatSend.addEventListener('click', sendMessage);
    chatInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
}

// Back to Top Button
function initBackToTop() {
    const backToTop = document.getElementById('backToTop');

    if (!backToTop) return;

    // Show/hide button based on scroll position
    window.addEventListener('scroll', function() {
        if (window.scrollY > 300) {
            backToTop.classList.add('show');
        } else {
            backToTop.classList.remove('show');
        }
    });

    // Scroll to top when clicked
    backToTop.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Cookie Consent (GDPR/ePrivacy Compliance)
function initCookieConsent() {
    const cookieBanner = document.getElementById('cookieConsent');

    if (!cookieBanner) return;

    // Check if user has already accepted cookies
    if (!localStorage.getItem('cookieConsent')) {
        cookieBanner.style.display = 'block';
    }
}

// Accept cookies function (called from HTML button)
function acceptCookies() {
    localStorage.setItem('cookieConsent', 'true');
    localStorage.setItem('cookieConsentDate', new Date().toISOString());
    const cookieBanner = document.getElementById('cookieConsent');
    if (cookieBanner) {
        cookieBanner.style.display = 'none';
    }
}