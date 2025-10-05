/**
 * R&E Roofing Website - Enterprise JavaScript
 * @version 2.0.0
 * @buildDate 2025-10-04
 * @description Production-ready JavaScript with enterprise security, analytics, and error handling
 * @license Proprietary
 */

(function(window, document) {
    'use strict';

    /**
     * =================================================================
     * CONFIGURATION & CONSTANTS
     * =================================================================
     */

    const CONFIG = {
        version: '2.0.0',
        buildDate: '2025-10-04',
        environment: (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') ? 'development' : 'production',
        debug: false, // Set to false in production builds
        phone: '(667) 204-1609',
        email: 'info@randeroofing.com',

        // Feature flags
        features: {
            analytics: true,
            errorTracking: true,
            reCaptcha: false, // Set to true when reCAPTCHA is configured
            serviceWorker: false, // Set to true when PWA is ready
            cookieConsent: true,
            formAutoSave: true,
            offlineSupport: false
        },

        // Rate limiting
        rateLimit: {
            formSubmissions: {
                maxAttempts: 3,
                windowMs: 60000 // 1 minute
            },
            chatMessages: {
                maxAttempts: 10,
                windowMs: 60000
            }
        },

        // Analytics configuration
        analytics: {
            gaId: 'G-XXXXXXXXXX', // Replace with actual GA4 ID
            gtmId: 'GTM-XXXXXXX', // Replace with actual GTM ID
            trackScrollDepth: true,
            trackEngagement: true,
            scrollDepthMilestones: [25, 50, 75, 90, 100]
        },

        // Security
        security: {
            csrfTokenName: '_csrf',
            honeypotFieldName: 'website_url',
            maxInputLength: 5000,
            sessionTimeout: 1800000 // 30 minutes
        }
    };

    /**
     * =================================================================
     * UTILITY FUNCTIONS
     * =================================================================
     */

    /**
     * Safely log messages (suppresses in production unless error)
     * @param {string} level - Log level (info, warn, error)
     * @param {string} message - Log message
     * @param {*} data - Optional data to log
     */
    const logger = {
        info: function(message, data) {
            if (CONFIG.environment === 'development' || CONFIG.debug) {
                console.log(`[INFO] ${message}`, data || '');
            }
        },
        warn: function(message, data) {
            if (CONFIG.environment === 'development' || CONFIG.debug) {
                console.warn(`[WARN] ${message}`, data || '');
            }
        },
        error: function(message, data) {
            console.error(`[ERROR] ${message}`, data || '');
            // In production, send to error tracking service
            if (CONFIG.environment === 'production' && CONFIG.features.errorTracking) {
                trackError(message, data);
            }
        }
    };

    /**
     * Debounce function to limit execution rate
     * @param {Function} func - Function to debounce
     * @param {number} wait - Wait time in milliseconds
     * @returns {Function} Debounced function
     */
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    /**
     * Throttle function to limit execution frequency
     * @param {Function} func - Function to throttle
     * @param {number} limit - Time limit in milliseconds
     * @returns {Function} Throttled function
     */
    function throttle(func, limit) {
        let inThrottle;
        return function(...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }

    /**
     * Sanitize HTML to prevent XSS attacks
     * @param {string} str - String to sanitize
     * @returns {string} Sanitized string
     */
    function sanitizeHTML(str) {
        if (!str) return '';
        const temp = document.createElement('div');
        temp.textContent = str;
        return temp.innerHTML;
    }

    /**
     * Sanitize user input
     * @param {string} input - Input to sanitize
     * @returns {string} Sanitized input
     */
    function sanitizeInput(input) {
        if (!input) return '';
        // Remove control characters and limit length
        let sanitized = String(input).replace(/[\x00-\x1F\x7F]/g, '');
        sanitized = sanitized.substring(0, CONFIG.security.maxInputLength);
        return sanitized.trim();
    }

    /**
     * Validate email address (RFC 5322 compliant)
     * @param {string} email - Email to validate
     * @returns {boolean} True if valid
     */
    function validateEmail(email) {
        const emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
        return emailRegex.test(String(email).toLowerCase());
    }

    /**
     * Validate phone number (international support)
     * @param {string} phone - Phone to validate
     * @returns {boolean} True if valid
     */
    function validatePhone(phone) {
        // Supports US, international formats, extensions
        const phoneRegex = /^[\+]?[(]?[0-9]{1,4}[)]?[-\s\.]?[(]?[0-9]{1,4}[)]?[-\s\.]?[0-9]{1,4}[-\s\.]?[0-9]{1,9}$/;
        const cleaned = phone.replace(/\s/g, '');
        return phoneRegex.test(cleaned) && cleaned.length >= 10;
    }

    /**
     * Generate CSRF token (placeholder - should be server-generated)
     * @returns {string} CSRF token
     */
    function generateCSRFToken() {
        // In production, this should come from the server
        return 'csrf_' + Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
    }

    /**
     * Get or create CSRF token
     * @returns {string} CSRF token
     */
    function getCSRFToken() {
        let token = sessionStorage.getItem(CONFIG.security.csrfTokenName);
        if (!token) {
            token = generateCSRFToken();
            sessionStorage.setItem(CONFIG.security.csrfTokenName, token);
        }
        return token;
    }

    /**
     * Rate limiter
     * @param {string} key - Unique key for rate limit tracking
     * @param {number} maxAttempts - Maximum attempts allowed
     * @param {number} windowMs - Time window in milliseconds
     * @returns {boolean} True if rate limit not exceeded
     */
    function checkRateLimit(key, maxAttempts, windowMs) {
        const now = Date.now();
        const storageKey = 'rateLimit_' + key;
        let attempts = JSON.parse(localStorage.getItem(storageKey) || '[]');

        // Filter out old attempts
        attempts = attempts.filter(timestamp => now - timestamp < windowMs);

        if (attempts.length >= maxAttempts) {
            logger.warn('Rate limit exceeded for: ' + key);
            return false;
        }

        attempts.push(now);
        localStorage.setItem(storageKey, JSON.stringify(attempts));
        return true;
    }

    /**
     * Secure localStorage wrapper with expiration
     */
    const secureStorage = {
        set: function(key, value, expiresInMs) {
            try {
                const item = {
                    value: value,
                    timestamp: Date.now(),
                    expires: expiresInMs ? Date.now() + expiresInMs : null
                };
                localStorage.setItem(key, JSON.stringify(item));
            } catch (e) {
                logger.error('localStorage set failed', e);
            }
        },
        get: function(key) {
            try {
                const itemStr = localStorage.getItem(key);
                if (!itemStr) return null;

                const item = JSON.parse(itemStr);

                // Check expiration
                if (item.expires && Date.now() > item.expires) {
                    localStorage.removeItem(key);
                    return null;
                }

                return item.value;
            } catch (e) {
                logger.error('localStorage get failed', e);
                return null;
            }
        },
        remove: function(key) {
            try {
                localStorage.removeItem(key);
            } catch (e) {
                logger.error('localStorage remove failed', e);
            }
        }
    };

    /**
     * =================================================================
     * ANALYTICS & TRACKING
     * =================================================================
     */

    /**
     * Track event to analytics platforms
     * @param {string} category - Event category
     * @param {string} action - Event action
     * @param {string} label - Event label
     * @param {number} value - Event value
     */
    function trackEvent(category, action, label, value) {
        if (!CONFIG.features.analytics) return;

        try {
            // Google Analytics 4
            if (window.gtag) {
                window.gtag('event', action, {
                    event_category: category,
                    event_label: label,
                    value: value
                });
            }

            // Google Tag Manager
            if (window.dataLayer) {
                window.dataLayer.push({
                    event: 'custom_event',
                    eventCategory: category,
                    eventAction: action,
                    eventLabel: label,
                    eventValue: value
                });
            }

            logger.info('Event tracked:', { category, action, label, value });
        } catch (e) {
            logger.error('Analytics tracking failed', e);
        }
    }

    /**
     * Track page view
     * @param {string} pagePath - Page path
     */
    function trackPageView(pagePath) {
        if (!CONFIG.features.analytics) return;

        try {
            if (window.gtag) {
                window.gtag('config', CONFIG.analytics.gaId, {
                    page_path: pagePath
                });
            }
        } catch (e) {
            logger.error('Page view tracking failed', e);
        }
    }

    /**
     * Track form submission
     * @param {string} formName - Form identifier
     * @param {boolean} success - Submission success status
     */
    function trackFormSubmission(formName, success) {
        trackEvent('Form', success ? 'Submit Success' : 'Submit Error', formName);
    }

    /**
     * Track conversion
     * @param {string} conversionType - Type of conversion
     * @param {number} value - Conversion value
     */
    function trackConversion(conversionType, value) {
        trackEvent('Conversion', conversionType, '', value || 0);

        // Add conversion pixels here (Facebook, Google Ads, etc.)
        logger.info('Conversion tracked:', conversionType);
    }

    /**
     * Track error
     * @param {string} message - Error message
     * @param {*} error - Error object
     */
    function trackError(message, error) {
        trackEvent('Error', message, error ? error.toString() : '', 0);
    }

    /**
     * Initialize scroll depth tracking
     */
    function initScrollDepthTracking() {
        if (!CONFIG.analytics.trackScrollDepth) return;

        const milestones = CONFIG.analytics.scrollDepthMilestones;
        const reached = {};

        const trackScrollDepth = throttle(() => {
            const scrollPercent = Math.round((window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100);

            milestones.forEach(milestone => {
                if (scrollPercent >= milestone && !reached[milestone]) {
                    reached[milestone] = true;
                    trackEvent('Scroll Depth', 'Reached ' + milestone + '%', window.location.pathname);
                }
            });
        }, 500);

        window.addEventListener('scroll', trackScrollDepth, { passive: true });
    }

    /**
     * Initialize engagement time tracking
     */
    function initEngagementTracking() {
        if (!CONFIG.analytics.trackEngagement) return;

        let startTime = Date.now();
        let isActive = true;

        // Track when user leaves/returns
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                const engagementTime = Math.round((Date.now() - startTime) / 1000);
                trackEvent('Engagement', 'Time on Page', window.location.pathname, engagementTime);
                isActive = false;
            } else {
                startTime = Date.now();
                isActive = true;
            }
        });

        // Track on page unload
        window.addEventListener('beforeunload', () => {
            if (isActive) {
                const engagementTime = Math.round((Date.now() - startTime) / 1000);
                trackEvent('Engagement', 'Time on Page', window.location.pathname, engagementTime);
            }
        });
    }

    /**
     * Track UTM parameters
     */
    function trackUTMParameters() {
        try {
            const urlParams = new URLSearchParams(window.location.search);
            const utmParams = {};

            ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'].forEach(param => {
                if (urlParams.has(param)) {
                    utmParams[param] = urlParams.get(param);
                }
            });

            if (Object.keys(utmParams).length > 0) {
                secureStorage.set('utm_params', utmParams, 1800000); // 30 min expiry
                trackEvent('UTM', 'Campaign Tracked', JSON.stringify(utmParams));
            }
        } catch (e) {
            logger.error('UTM tracking failed', e);
        }
    }

    /**
     * =================================================================
     * CORE FUNCTIONALITY
     * =================================================================
     */

    /**
     * Initialize smooth scrolling for anchor links
     */
    function initSmoothScrolling() {
        try {
            const links = document.querySelectorAll('a[href^="#"]');

            links.forEach(link => {
                link.addEventListener('click', function(e) {
                    e.preventDefault();

                    const targetId = this.getAttribute('href');
                    if (targetId === '#') return;

                    const targetElement = document.querySelector(targetId);

                    if (targetElement) {
                        const headerHeight = 70;
                        const targetPosition = targetElement.offsetTop - headerHeight;

                        window.scrollTo({
                            top: targetPosition,
                            behavior: 'smooth'
                        });

                        trackEvent('Navigation', 'Anchor Click', targetId);
                    }
                });
            });

            logger.info('Smooth scrolling initialized');
        } catch (e) {
            logger.error('Smooth scrolling init failed', e);
        }
    }

    /**
     * Initialize scroll effects with throttling
     */
    function initScrollEffects() {
        try {
            const header = document.querySelector('.header');
            if (!header) return;

            const handleScroll = throttle(() => {
                try {
                    if (window.scrollY > 50) {
                        header.classList.add('scrolled');
                    } else {
                        header.classList.remove('scrolled');
                    }
                } catch (e) {
                    logger.error('Scroll effect error', e);
                }
            }, 100);

            window.addEventListener('scroll', handleScroll, { passive: true });
            logger.info('Scroll effects initialized');
        } catch (e) {
            logger.error('Scroll effects init failed', e);
        }
    }

    /**
     * Initialize animations with Intersection Observer
     */
    function initAnimations() {
        try {
            // Check for Intersection Observer support
            if (!('IntersectionObserver' in window)) {
                logger.warn('IntersectionObserver not supported, skipping animations');
                // Show all elements immediately
                document.querySelectorAll('.service-card, .feature, .process-step, .review').forEach(el => {
                    el.classList.add('animate-in');
                });
                return;
            }

            const observerOptions = {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            };

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('animate-in');
                        observer.unobserve(entry.target); // Stop observing once animated
                    }
                });
            }, observerOptions);

            const animateElements = document.querySelectorAll('.service-card, .feature, .process-step, .review');
            animateElements.forEach(element => observer.observe(element));

            logger.info('Animations initialized with Intersection Observer');
        } catch (e) {
            logger.error('Animations init failed', e);
        }
    }

    /**
     * Add dynamic styles for animations
     */
    function injectAnimationStyles() {
        try {
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

                .error {
                    border-color: #dc3545 !important;
                    background-color: #fff5f5 !important;
                }

                .error-message {
                    color: #dc3545;
                    font-size: 0.875rem;
                    margin-top: 0.25rem;
                    display: block;
                }

                .success-message {
                    background-color: #d4edda;
                    border: 1px solid #c3e6cb;
                    color: #155724;
                    padding: 1rem;
                    border-radius: 4px;
                    margin-bottom: 1rem;
                }
            `;
            document.head.appendChild(style);
        } catch (e) {
            logger.error('Style injection failed', e);
        }
    }

    /**
     * Initialize button interactions with tracking
     */
    function initButtonInteractions() {
        try {
            document.querySelectorAll('.btn-primary, .cta-button').forEach(button => {
                button.addEventListener('click', function(e) {
                    try {
                        // Visual feedback using requestAnimationFrame
                        requestAnimationFrame(() => {
                            this.style.transform = 'translateY(-2px) scale(0.98)';
                            setTimeout(() => {
                                this.style.transform = '';
                            }, 150);
                        });

                        // Track button click
                        trackEvent('Button', 'Click', this.textContent.trim());
                    } catch (err) {
                        logger.error('Button interaction error', err);
                    }
                });
            });

            logger.info('Button interactions initialized');
        } catch (e) {
            logger.error('Button interactions init failed', e);
        }
    }

    /**
     * Initialize service card hover effects
     */
    function initServiceCardEffects() {
        try {
            document.querySelectorAll('.service-card').forEach(card => {
                card.addEventListener('mouseenter', function() {
                    requestAnimationFrame(() => {
                        this.style.transform = 'translateY(-10px) scale(1.02)';
                    });
                });

                card.addEventListener('mouseleave', function() {
                    requestAnimationFrame(() => {
                        if (this.classList.contains('card-2')) {
                            this.style.transform = 'scale(1.05) translateY(-20px)';
                        } else {
                            this.style.transform = '';
                        }
                    });
                });
            });

            logger.info('Service card effects initialized');
        } catch (e) {
            logger.error('Service card effects init failed', e);
        }
    }

    /**
     * =================================================================
     * MODAL MANAGEMENT
     * =================================================================
     */

    /**
     * Initialize contact modal with accessibility
     */
    function initContactModal() {
        try {
            const modal = document.getElementById('contactModal');
            const closeModal = document.querySelector('.close-modal');
            const contactForm = document.getElementById('contactForm');

            if (!modal || !closeModal || !contactForm) {
                logger.warn('Contact modal elements not found');
                return;
            }

            // Store last focused element
            let lastFocusedElement = null;

            // Open modal function
            function openModal() {
                lastFocusedElement = document.activeElement;
                modal.classList.add('show');
                document.body.style.overflow = 'hidden';
                modal.setAttribute('aria-hidden', 'false');

                // Focus first input
                const firstInput = modal.querySelector('input, textarea');
                if (firstInput) {
                    setTimeout(() => firstInput.focus(), 100);
                }

                trackEvent('Modal', 'Open', 'Contact Modal');
            }

            // Close modal function
            function closeModalFunc() {
                modal.classList.remove('show');
                document.body.style.overflow = '';
                modal.setAttribute('aria-hidden', 'true');

                // Restore focus
                if (lastFocusedElement) {
                    lastFocusedElement.focus();
                }

                trackEvent('Modal', 'Close', 'Contact Modal');
            }

            // Open modal when CTA buttons are clicked
            document.querySelectorAll('.cta-button, .btn-primary').forEach(button => {
                if (!button.classList.contains('submit-btn')) {
                    button.addEventListener('click', function(e) {
                        e.preventDefault();
                        openModal();
                    });
                }
            });

            // Close modal events
            closeModal.addEventListener('click', closeModalFunc);

            modal.addEventListener('click', function(e) {
                if (e.target === modal) {
                    closeModalFunc();
                }
            });

            // Keyboard support - ESC to close
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Escape' && modal.classList.contains('show')) {
                    closeModalFunc();
                }
            });

            // Trap focus within modal
            modal.addEventListener('keydown', function(e) {
                if (e.key === 'Tab') {
                    const focusableElements = modal.querySelectorAll(
                        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
                    );
                    const firstElement = focusableElements[0];
                    const lastElement = focusableElements[focusableElements.length - 1];

                    if (e.shiftKey && document.activeElement === firstElement) {
                        lastElement.focus();
                        e.preventDefault();
                    } else if (!e.shiftKey && document.activeElement === lastElement) {
                        firstElement.focus();
                        e.preventDefault();
                    }
                }
            });

            logger.info('Contact modal initialized');
        } catch (e) {
            logger.error('Contact modal init failed', e);
        }
    }

    /**
     * =================================================================
     * FORM HANDLING
     * =================================================================
     */

    /**
     * Initialize form with security and validation
     */
    function initContactForm() {
        try {
            const contactForm = document.getElementById('contactForm');
            if (!contactForm) return;

            // Add CSRF token (hidden field)
            const csrfInput = document.createElement('input');
            csrfInput.type = 'hidden';
            csrfInput.name = CONFIG.security.csrfTokenName;
            csrfInput.value = getCSRFToken();
            contactForm.appendChild(csrfInput);

            // Add honeypot field (hidden from users, catches bots)
            const honeypot = document.createElement('input');
            honeypot.type = 'text';
            honeypot.name = CONFIG.security.honeypotFieldName;
            honeypot.style.display = 'none';
            honeypot.setAttribute('tabindex', '-1');
            honeypot.setAttribute('autocomplete', 'off');
            contactForm.appendChild(honeypot);

            // Auto-save form data
            if (CONFIG.features.formAutoSave) {
                initFormAutoSave(contactForm);
            }

            // Mark sensitive fields to prevent session replay
            contactForm.querySelectorAll('input[type="email"], input[type="tel"], textarea').forEach(field => {
                field.setAttribute('data-private', 'true');
            });

            // Form submission handler
            contactForm.addEventListener('submit', function(e) {
                e.preventDefault();
                handleFormSubmission(contactForm);
            });

            logger.info('Contact form initialized with security features');
        } catch (e) {
            logger.error('Contact form init failed', e);
        }
    }

    /**
     * Handle form submission with validation and security
     * @param {HTMLFormElement} form - Form element
     */
    function handleFormSubmission(form) {
        try {
            // Check rate limiting
            if (!checkRateLimit('formSubmission', CONFIG.rateLimit.formSubmissions.maxAttempts, CONFIG.rateLimit.formSubmissions.windowMs)) {
                showFormError(form, 'Too many submission attempts. Please wait a minute and try again.');
                trackEvent('Form', 'Rate Limit Exceeded', 'Contact Form');
                return;
            }

            // Clear previous errors
            clearFormErrors(form);

            // Check honeypot (bot detection)
            const honeypotField = form.querySelector(`[name="${CONFIG.security.honeypotFieldName}"]`);
            if (honeypotField && honeypotField.value) {
                logger.warn('Honeypot triggered - potential bot submission');
                trackEvent('Security', 'Bot Detected', 'Contact Form');
                // Show success to bot, but don't process
                showFormSuccess(form, 'Thank you! We\'ll contact you within 24 hours.');
                setTimeout(() => {
                    form.reset();
                    closeContactModal();
                }, 2000);
                return;
            }

            // Validate all fields
            const validation = validateForm(form);
            if (!validation.isValid) {
                trackFormSubmission('Contact Form', false);
                return;
            }

            // Get form data
            const formData = new FormData(form);
            const data = {};

            formData.forEach((value, key) => {
                if (key !== CONFIG.security.honeypotFieldName) {
                    data[key] = sanitizeInput(value);
                }
            });

            // Add UTM parameters if available
            const utmParams = secureStorage.get('utm_params');
            if (utmParams) {
                data.utm_params = utmParams;
            }

            // Add session info
            data.sessionId = getSessionId();
            data.timestamp = new Date().toISOString();

            // Show loading state
            const submitBtn = form.querySelector('[type="submit"]');
            const originalBtnText = submitBtn ? submitBtn.textContent : '';
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.textContent = 'Sending...';
            }

            // Submit to backend (placeholder)
            submitFormData(data)
                .then(response => {
                    trackFormSubmission('Contact Form', true);
                    trackConversion('Contact Form Submission', 1);
                    showFormSuccess(form, 'Thank you! We\'ll contact you within 24 hours.');

                    // Clear auto-saved data
                    secureStorage.remove('formAutoSave_contact');

                    // Reset form after delay
                    setTimeout(() => {
                        form.reset();
                        closeContactModal();
                    }, 2000);
                })
                .catch(error => {
                    logger.error('Form submission failed', error);
                    trackFormSubmission('Contact Form', false);
                    showFormError(form, 'Sorry, something went wrong. Please try again or call us at ' + CONFIG.phone);
                })
                .finally(() => {
                    if (submitBtn) {
                        submitBtn.disabled = false;
                        submitBtn.textContent = originalBtnText;
                    }
                });

        } catch (e) {
            logger.error('Form submission error', e);
            showFormError(form, 'An error occurred. Please try again.');
        }
    }

    /**
     * Validate form fields
     * @param {HTMLFormElement} form - Form to validate
     * @returns {Object} Validation result
     */
    function validateForm(form) {
        let isValid = true;
        const errors = [];

        // Validate required fields
        const requiredFields = form.querySelectorAll('[required]');
        requiredFields.forEach(field => {
            if (!field.value.trim()) {
                isValid = false;
                showFieldError(field, 'This field is required');
                errors.push({ field: field.name, error: 'required' });
            }
        });

        // Validate email
        const emailField = form.querySelector('input[type="email"], #email');
        if (emailField && emailField.value) {
            if (!validateEmail(emailField.value)) {
                isValid = false;
                showFieldError(emailField, 'Please enter a valid email address');
                errors.push({ field: 'email', error: 'invalid_format' });
            }
        }

        // Validate phone
        const phoneField = form.querySelector('input[type="tel"], #phone');
        if (phoneField && phoneField.value) {
            if (!validatePhone(phoneField.value)) {
                isValid = false;
                showFieldError(phoneField, 'Please enter a valid phone number (10+ digits)');
                errors.push({ field: 'phone', error: 'invalid_format' });
            }
        }

        // Validate message length
        const messageField = form.querySelector('textarea[name="message"]');
        if (messageField && messageField.value) {
            if (messageField.value.length < 10) {
                isValid = false;
                showFieldError(messageField, 'Message must be at least 10 characters');
                errors.push({ field: 'message', error: 'too_short' });
            }
        }

        return { isValid, errors };
    }

    /**
     * Show field-specific error
     * @param {HTMLElement} field - Input field
     * @param {string} message - Error message
     */
    function showFieldError(field, message) {
        field.classList.add('error');
        field.setAttribute('aria-invalid', 'true');

        const errorMsg = document.createElement('span');
        errorMsg.className = 'error-message';
        errorMsg.textContent = message;
        errorMsg.setAttribute('role', 'alert');
        field.parentElement.appendChild(errorMsg);
    }

    /**
     * Show form success message
     * @param {HTMLFormElement} form - Form element
     * @param {string} message - Success message
     */
    function showFormSuccess(form, message) {
        const successMsg = document.createElement('div');
        successMsg.className = 'success-message';
        successMsg.textContent = message;
        successMsg.setAttribute('role', 'status');
        successMsg.setAttribute('aria-live', 'polite');
        form.insertBefore(successMsg, form.firstChild);
    }

    /**
     * Show form error message
     * @param {HTMLFormElement} form - Form element
     * @param {string} message - Error message
     */
    function showFormError(form, message) {
        const errorMsg = document.createElement('div');
        errorMsg.className = 'error-message';
        errorMsg.style.padding = '1rem';
        errorMsg.style.marginBottom = '1rem';
        errorMsg.style.backgroundColor = '#fff5f5';
        errorMsg.style.border = '1px solid #dc3545';
        errorMsg.style.borderRadius = '4px';
        errorMsg.textContent = message;
        errorMsg.setAttribute('role', 'alert');
        form.insertBefore(errorMsg, form.firstChild);
    }

    /**
     * Clear form errors
     * @param {HTMLFormElement} form - Form element
     */
    function clearFormErrors(form) {
        form.querySelectorAll('.error-message').forEach(msg => msg.remove());
        form.querySelectorAll('.success-message').forEach(msg => msg.remove());
        form.querySelectorAll('.error').forEach(field => {
            field.classList.remove('error');
            field.removeAttribute('aria-invalid');
        });
    }

    /**
     * Submit form data to backend (placeholder)
     * @param {Object} data - Form data
     * @returns {Promise} Submission promise
     */
    function submitFormData(data) {
        // In production, replace with actual API endpoint
        return new Promise((resolve, reject) => {
            // Simulate API call
            setTimeout(() => {
                logger.info('Form data to be submitted:', data);
                // Simulate success
                resolve({ success: true, message: 'Form submitted successfully' });

                // For actual implementation:
                // fetch('/api/contact', {
                //     method: 'POST',
                //     headers: {
                //         'Content-Type': 'application/json',
                //         'X-CSRF-Token': data._csrf
                //     },
                //     body: JSON.stringify(data)
                // })
                // .then(response => response.json())
                // .then(resolve)
                // .catch(reject);
            }, 1000);
        });
    }

    /**
     * Initialize form auto-save
     * @param {HTMLFormElement} form - Form element
     */
    function initFormAutoSave(form) {
        const storageKey = 'formAutoSave_contact';

        // Restore saved data
        const savedData = secureStorage.get(storageKey);
        if (savedData) {
            Object.keys(savedData).forEach(key => {
                const field = form.querySelector(`[name="${key}"]`);
                if (field && field.type !== 'password') {
                    field.value = savedData[key];
                }
            });
        }

        // Auto-save on input
        const autoSave = debounce(() => {
            const formData = new FormData(form);
            const data = {};
            formData.forEach((value, key) => {
                if (key !== CONFIG.security.csrfTokenName && key !== CONFIG.security.honeypotFieldName) {
                    data[key] = value;
                }
            });
            secureStorage.set(storageKey, data, 1800000); // 30 min expiry
        }, 1000);

        form.addEventListener('input', autoSave);
    }

    /**
     * Close contact modal
     */
    function closeContactModal() {
        const modal = document.getElementById('contactModal');
        if (modal) {
            modal.classList.remove('show');
            document.body.style.overflow = '';
        }
    }

    /**
     * =================================================================
     * MOBILE MENU
     * =================================================================
     */

    /**
     * Initialize mobile menu with accessibility
     */
    function initMobileMenu() {
        try {
            const mobileToggle = document.querySelector('.mobile-menu-toggle');
            const mobileNav = document.querySelector('.mobile-nav');
            const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');
            const hasSubmenu = document.querySelectorAll('.has-submenu');

            if (!mobileToggle || !mobileNav) {
                logger.warn('Mobile menu elements not found');
                return;
            }

            // Toggle mobile menu
            mobileToggle.addEventListener('click', function() {
                const isActive = mobileToggle.classList.toggle('active');
                mobileNav.classList.toggle('active');
                document.body.style.overflow = isActive ? 'hidden' : '';

                // Update ARIA attributes
                mobileToggle.setAttribute('aria-expanded', isActive);
                mobileNav.setAttribute('aria-hidden', !isActive);

                trackEvent('Navigation', isActive ? 'Open Mobile Menu' : 'Close Mobile Menu');
            });

            // Close menu when clicking a link
            mobileNavLinks.forEach(link => {
                if (!link.classList.contains('has-submenu')) {
                    link.addEventListener('click', function() {
                        mobileToggle.classList.remove('active');
                        mobileNav.classList.remove('active');
                        document.body.style.overflow = '';
                        mobileToggle.setAttribute('aria-expanded', 'false');
                        mobileNav.setAttribute('aria-hidden', 'true');
                    });
                }
            });

            // Handle submenu toggles
            hasSubmenu.forEach(item => {
                item.addEventListener('click', function(e) {
                    e.preventDefault();
                    const submenu = this.nextElementSibling;
                    if (submenu && submenu.classList.contains('mobile-submenu')) {
                        const isActive = submenu.classList.toggle('active');
                        this.setAttribute('aria-expanded', isActive);
                    }
                });
            });

            logger.info('Mobile menu initialized');
        } catch (e) {
            logger.error('Mobile menu init failed', e);
        }
    }

    /**
     * =================================================================
     * FAQ ACCORDION
     * =================================================================
     */

    /**
     * Initialize FAQ accordion with accessibility
     */
    function initFAQ() {
        try {
            const faqItems = document.querySelectorAll('.faq-item');

            if (faqItems.length === 0) return;

            faqItems.forEach(item => {
                const question = item.querySelector('.faq-question');
                const answer = item.querySelector('.faq-answer');

                if (!question || !answer) return;

                // Set ARIA attributes
                const questionId = 'faq-q-' + Math.random().toString(36).substr(2, 9);
                const answerId = 'faq-a-' + Math.random().toString(36).substr(2, 9);

                question.id = questionId;
                answer.id = answerId;
                question.setAttribute('aria-controls', answerId);
                question.setAttribute('aria-expanded', 'false');
                answer.setAttribute('aria-labelledby', questionId);

                question.addEventListener('click', function() {
                    // Close other items
                    faqItems.forEach(otherItem => {
                        if (otherItem !== item && otherItem.classList.contains('active')) {
                            otherItem.classList.remove('active');
                            const otherQuestion = otherItem.querySelector('.faq-question');
                            if (otherQuestion) {
                                otherQuestion.setAttribute('aria-expanded', 'false');
                            }
                        }
                    });

                    // Toggle current item
                    const isActive = item.classList.toggle('active');
                    question.setAttribute('aria-expanded', isActive);

                    trackEvent('FAQ', isActive ? 'Expand' : 'Collapse', question.textContent.trim());
                });

                // Keyboard support
                question.addEventListener('keydown', function(e) {
                    if (e.key === 'Enter' || e.key === ' ') {
                        e.preventDefault();
                        question.click();
                    }
                });
            });

            logger.info('FAQ accordion initialized');
        } catch (e) {
            logger.error('FAQ init failed', e);
        }
    }

    /**
     * =================================================================
     * ROOFING CALCULATOR
     * =================================================================
     */

    /**
     * Initialize roofing calculator with enhanced validation
     */
    function initCalculator() {
        try {
            const calculateBtn = document.getElementById('calculateBtn');
            if (!calculateBtn) return;

            calculateBtn.addEventListener('click', function() {
                try {
                    calculateEstimate();
                } catch (e) {
                    logger.error('Calculator error', e);
                    alert('An error occurred during calculation. Please check your inputs and try again.');
                }
            });

            logger.info('Calculator initialized');
        } catch (e) {
            logger.error('Calculator init failed', e);
        }
    }

    /**
     * Calculate roofing estimate
     */
    function calculateEstimate() {
        // Get input values
        const roofSizeInput = document.getElementById('roofSize');
        const roofTypeSelect = document.getElementById('roofType');
        const materialSelect = document.getElementById('material');
        const layersSelect = document.getElementById('layers');

        const roofSize = parseFloat(roofSizeInput?.value) || 0;
        const roofType = roofTypeSelect?.value || '';
        const material = materialSelect?.value || '';
        const layers = layersSelect?.value || '1';

        // Validate inputs
        if (roofSize < 500) {
            alert('Please enter a roof size of at least 500 sq ft');
            roofSizeInput?.focus();
            trackEvent('Calculator', 'Validation Error', 'Roof Size Too Small');
            return;
        }

        if (roofSize > 50000) {
            alert('For roofs larger than 50,000 sq ft, please contact us directly for a custom quote.');
            trackEvent('Calculator', 'Validation Error', 'Roof Size Too Large');
            return;
        }

        if (!roofType || !material) {
            alert('Please fill in all required fields');
            trackEvent('Calculator', 'Validation Error', 'Missing Fields');
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
        const guttersCheckbox = document.getElementById('gutters');
        const ventilationCheckbox = document.getElementById('ventilation');
        const skylightsCheckbox = document.getElementById('skylights');
        const chimneyCheckbox = document.getElementById('chimney');

        if (guttersCheckbox?.checked) {
            lowEstimate += 1500;
            highEstimate += 3000;
            additionalServices.push({ name: 'New Gutters', low: 1500, high: 3000 });
        }
        if (ventilationCheckbox?.checked) {
            lowEstimate += 500;
            highEstimate += 1500;
            additionalServices.push({ name: 'Ventilation', low: 500, high: 1500 });
        }
        if (skylightsCheckbox?.checked) {
            lowEstimate += 1000;
            highEstimate += 3000;
            additionalServices.push({ name: 'Skylights', low: 1000, high: 3000 });
        }
        if (chimneyCheckbox?.checked) {
            lowEstimate += 500;
            highEstimate += 2000;
            additionalServices.push({ name: 'Chimney Repair', low: 500, high: 2000 });
        }

        // Display results
        const lowPriceEl = document.getElementById('lowPrice');
        const highPriceEl = document.getElementById('highPrice');

        if (lowPriceEl) lowPriceEl.textContent = '$' + Math.round(lowEstimate).toLocaleString();
        if (highPriceEl) highPriceEl.textContent = '$' + Math.round(highEstimate).toLocaleString();

        // Show breakdown
        const breakdown = document.getElementById('breakdown');
        const breakdownList = document.getElementById('breakdownList');

        if (breakdownList) {
            breakdownList.innerHTML = '';

            // Add roofing cost
            const roofingItem = document.createElement('li');
            roofingItem.innerHTML = `
                <span>Roofing (${roofSize} sq ft)</span>
                <span>$${Math.round(roofSize * baseCost.low).toLocaleString()} - $${Math.round(roofSize * baseCost.high).toLocaleString()}</span>
            `;
            breakdownList.appendChild(roofingItem);

            // Add tear-off if needed
            if (layers !== '1') {
                const tearOffItem = document.createElement('li');
                const tearOffLow = layers === '2' ? roofSize * 1 : roofSize * 2;
                const tearOffHigh = layers === '2' ? roofSize * 2 : roofSize * 3.5;
                tearOffItem.innerHTML = `
                    <span>Tear-off (${layers === '2' ? '1' : 'Multiple'} layer${layers === '2' ? '' : 's'})</span>
                    <span>$${Math.round(tearOffLow).toLocaleString()} - $${Math.round(tearOffHigh).toLocaleString()}</span>
                `;
                breakdownList.appendChild(tearOffItem);
            }

            // Add additional services
            additionalServices.forEach(service => {
                const serviceItem = document.createElement('li');
                serviceItem.innerHTML = `
                    <span>${sanitizeHTML(service.name)}</span>
                    <span>$${service.low.toLocaleString()} - $${service.high.toLocaleString()}</span>
                `;
                breakdownList.appendChild(serviceItem);
            });
        }

        if (breakdown) {
            breakdown.style.display = 'block';
        }

        // Scroll to results
        const calcResults = document.getElementById('calcResults');
        if (calcResults) {
            calcResults.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }

        // Track calculator usage
        trackEvent('Calculator', 'Calculate', `${material} - ${roofType} - ${roofSize}sqft`, Math.round((lowEstimate + highEstimate) / 2));
    }

    /**
     * =================================================================
     * LIVE CHAT WIDGET
     * =================================================================
     */

    /**
     * Initialize live chat widget
     */
    function initLiveChat() {
        try {
            const chatToggle = document.querySelector('.chat-toggle');
            const chatWindow = document.querySelector('.chat-window');
            const chatClose = document.querySelector('.chat-close');
            const chatInput = document.getElementById('chatInput');
            const chatSend = document.querySelector('.chat-send');
            const chatBody = document.querySelector('.chat-body');
            const chatBadge = document.querySelector('.chat-badge');

            if (!chatToggle || !chatWindow) {
                logger.info('Chat widget not found on this page');
                return;
            }

            // Toggle chat window
            chatToggle.addEventListener('click', function() {
                const isActive = chatWindow.classList.toggle('active');
                if (isActive) {
                    if (chatBadge) chatBadge.style.display = 'none';
                    if (chatInput) chatInput.focus();
                    trackEvent('Chat', 'Open Widget');
                } else {
                    trackEvent('Chat', 'Close Widget');
                }
            });

            // Close chat window
            if (chatClose) {
                chatClose.addEventListener('click', function() {
                    chatWindow.classList.remove('active');
                    trackEvent('Chat', 'Close Widget');
                });
            }

            // Send message function
            function sendMessage() {
                if (!chatInput || !chatBody) return;

                const message = chatInput.value.trim();
                if (!message) return;

                // Check rate limiting
                if (!checkRateLimit('chatMessages', CONFIG.rateLimit.chatMessages.maxAttempts, CONFIG.rateLimit.chatMessages.windowMs)) {
                    addChatMessage('bot', 'Please slow down. You\'re sending messages too quickly.');
                    return;
                }

                // Sanitize and validate message
                const sanitizedMessage = sanitizeInput(message);
                if (sanitizedMessage.length < 2) return;

                // Add user message
                addChatMessage('user', sanitizedMessage);

                // Clear input
                chatInput.value = '';

                // Track chat interaction
                trackEvent('Chat', 'Send Message', sanitizedMessage.substring(0, 50));

                // Simulate bot response
                setTimeout(() => {
                    const response = generateChatResponse(sanitizedMessage);
                    addChatMessage('bot', response);
                }, 1000);
            }

            // Add message to chat
            function addChatMessage(type, text) {
                if (!chatBody) return;

                const messageDiv = document.createElement('div');
                messageDiv.className = 'chat-message ' + type;

                const messageParagraph = document.createElement('p');
                messageParagraph.textContent = text;
                messageDiv.appendChild(messageParagraph);

                chatBody.appendChild(messageDiv);
                chatBody.scrollTop = chatBody.scrollHeight;
            }

            // Generate bot response
            function generateChatResponse(message) {
                const lowerMessage = message.toLowerCase();

                if (lowerMessage.includes('estimate') || lowerMessage.includes('quote') || lowerMessage.includes('cost') || lowerMessage.includes('price')) {
                    return `I'd be happy to help with an estimate! Please click "Get Free Quote" at the top of the page or call us at ${CONFIG.phone}.`;
                } else if (lowerMessage.includes('emergency') || lowerMessage.includes('leak') || lowerMessage.includes('urgent')) {
                    return `For emergency repairs, please call us immediately at ${CONFIG.phone}. We offer 24/7 emergency service!`;
                } else if (lowerMessage.includes('insurance') || lowerMessage.includes('claim')) {
                    return 'Yes, we work with all major insurance companies! We can help navigate the claims process. Call us for assistance.';
                } else if (lowerMessage.includes('warranty') || lowerMessage.includes('guarantee')) {
                    return 'We offer comprehensive warranties on both materials and workmanship. Most materials come with 20-50 year warranties.';
                } else if (lowerMessage.includes('hour') || lowerMessage.includes('open') || lowerMessage.includes('available')) {
                    return 'We\'re available Monday-Friday 7am-6pm, Saturday 8am-4pm. Emergency service available 24/7!';
                } else if (lowerMessage.includes('service') || lowerMessage.includes('what do you do')) {
                    return 'We specialize in roof repair, replacement, new roofing, gutters, siding, and emergency repairs. Serving all of Essex County, NJ!';
                } else {
                    return `Thank you for your message! One of our roofing experts will get back to you shortly. For immediate assistance, call ${CONFIG.phone}.`;
                }
            }

            // Event listeners
            if (chatSend) {
                chatSend.addEventListener('click', sendMessage);
            }

            if (chatInput) {
                chatInput.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter' && !e.shiftKey) {
                        e.preventDefault();
                        sendMessage();
                    }
                });
            }

            logger.info('Live chat initialized');
        } catch (e) {
            logger.error('Live chat init failed', e);
        }
    }

    /**
     * =================================================================
     * BACK TO TOP BUTTON
     * =================================================================
     */

    /**
     * Initialize back to top button
     */
    function initBackToTop() {
        try {
            const backToTop = document.getElementById('backToTop');
            if (!backToTop) return;

            // Show/hide button based on scroll position (throttled)
            const handleScroll = throttle(() => {
                if (window.scrollY > 300) {
                    backToTop.classList.add('show');
                } else {
                    backToTop.classList.remove('show');
                }
            }, 200);

            window.addEventListener('scroll', handleScroll, { passive: true });

            // Scroll to top when clicked
            backToTop.addEventListener('click', function() {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
                trackEvent('Navigation', 'Back to Top Click');
            });

            logger.info('Back to top button initialized');
        } catch (e) {
            logger.error('Back to top init failed', e);
        }
    }

    /**
     * =================================================================
     * COOKIE CONSENT (GDPR/ePrivacy)
     * =================================================================
     */

    /**
     * Initialize cookie consent banner
     */
    function initCookieConsent() {
        try {
            if (!CONFIG.features.cookieConsent) return;

            const cookieBanner = document.getElementById('cookieConsent');
            if (!cookieBanner) return;

            // Check if user has already given consent
            const consent = secureStorage.get('cookieConsent');

            if (!consent) {
                cookieBanner.style.display = 'block';
                cookieBanner.setAttribute('role', 'dialog');
                cookieBanner.setAttribute('aria-label', 'Cookie consent');
            } else {
                // Apply consent preferences
                applyCookieConsent(consent);
            }

            logger.info('Cookie consent initialized');
        } catch (e) {
            logger.error('Cookie consent init failed', e);
        }
    }

    /**
     * Accept cookies (called from HTML button or granular selection)
     * @param {Object} preferences - Cookie preferences (optional)
     */
    window.acceptCookies = function(preferences) {
        try {
            const consent = preferences || {
                essential: true,
                analytics: true,
                marketing: true,
                timestamp: new Date().toISOString()
            };

            secureStorage.set('cookieConsent', consent, null); // No expiry

            const cookieBanner = document.getElementById('cookieConsent');
            if (cookieBanner) {
                cookieBanner.style.display = 'none';
            }

            applyCookieConsent(consent);
            trackEvent('Cookie Consent', 'Accept', JSON.stringify(consent));

            logger.info('Cookie consent accepted', consent);
        } catch (e) {
            logger.error('Cookie consent acceptance failed', e);
        }
    };

    /**
     * Reject non-essential cookies
     */
    window.rejectCookies = function() {
        try {
            const consent = {
                essential: true,
                analytics: false,
                marketing: false,
                timestamp: new Date().toISOString()
            };

            secureStorage.set('cookieConsent', consent, null);

            const cookieBanner = document.getElementById('cookieConsent');
            if (cookieBanner) {
                cookieBanner.style.display = 'none';
            }

            trackEvent('Cookie Consent', 'Reject');
            logger.info('Non-essential cookies rejected');
        } catch (e) {
            logger.error('Cookie rejection failed', e);
        }
    };

    /**
     * Apply cookie consent preferences
     * @param {Object} consent - Consent preferences
     */
    function applyCookieConsent(consent) {
        // Disable analytics if not consented
        if (!consent.analytics) {
            window['ga-disable-' + CONFIG.analytics.gaId] = true;
            CONFIG.features.analytics = false;
        }

        // Disable marketing cookies if not consented
        if (!consent.marketing) {
            // Prevent marketing pixels from loading
        }

        logger.info('Cookie consent applied', consent);
    }

    /**
     * =================================================================
     * NETWORK & OFFLINE HANDLING
     * =================================================================
     */

    /**
     * Initialize offline detection
     */
    function initOfflineDetection() {
        try {
            if (!CONFIG.features.offlineSupport) return;

            window.addEventListener('online', () => {
                logger.info('Network connection restored');
                showNetworkStatus('You\'re back online!', 'success');
            });

            window.addEventListener('offline', () => {
                logger.warn('Network connection lost');
                showNetworkStatus('You\'re offline. Some features may be unavailable.', 'warning');
            });

            logger.info('Offline detection initialized');
        } catch (e) {
            logger.error('Offline detection init failed', e);
        }
    }

    /**
     * Show network status message
     * @param {string} message - Status message
     * @param {string} type - Message type (success, warning, error)
     */
    function showNetworkStatus(message, type) {
        // Create status notification
        const statusDiv = document.createElement('div');
        statusDiv.className = 'network-status ' + type;
        statusDiv.textContent = message;
        statusDiv.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 1rem 1.5rem;
            background: ${type === 'success' ? '#d4edda' : '#fff3cd'};
            border: 1px solid ${type === 'success' ? '#c3e6cb' : '#ffeaa7'};
            color: ${type === 'success' ? '#155724' : '#856404'};
            border-radius: 4px;
            z-index: 10000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        `;

        document.body.appendChild(statusDiv);

        setTimeout(() => {
            statusDiv.remove();
        }, 5000);
    }

    /**
     * =================================================================
     * SERVICE WORKER (PWA)
     * =================================================================
     */

    /**
     * Register service worker for PWA
     */
    function initServiceWorker() {
        try {
            if (!CONFIG.features.serviceWorker) return;

            if ('serviceWorker' in navigator) {
                window.addEventListener('load', () => {
                    navigator.serviceWorker.register('/sw.js')
                        .then(registration => {
                            logger.info('Service Worker registered', registration);
                        })
                        .catch(error => {
                            logger.error('Service Worker registration failed', error);
                        });
                });
            }
        } catch (e) {
            logger.error('Service Worker init failed', e);
        }
    }

    /**
     * =================================================================
     * SESSION MANAGEMENT
     * =================================================================
     */

    /**
     * Get or create session ID
     * @returns {string} Session ID
     */
    function getSessionId() {
        let sessionId = sessionStorage.getItem('sessionId');
        if (!sessionId) {
            sessionId = 'session_' + Date.now() + '_' + Math.random().toString(36).substring(2);
            sessionStorage.setItem('sessionId', sessionId);
            sessionStorage.setItem('sessionStart', new Date().toISOString());
        }
        return sessionId;
    }

    /**
     * Initialize session timeout
     */
    function initSessionTimeout() {
        try {
            let timeoutId;

            function resetTimeout() {
                clearTimeout(timeoutId);
                timeoutId = setTimeout(() => {
                    logger.info('Session timeout');
                    // Clear sensitive data
                    secureStorage.remove('formAutoSave_contact');
                }, CONFIG.security.sessionTimeout);
            }

            // Reset timeout on user activity
            ['mousedown', 'keydown', 'scroll', 'touchstart'].forEach(event => {
                document.addEventListener(event, resetTimeout, { passive: true });
            });

            resetTimeout();
        } catch (e) {
            logger.error('Session timeout init failed', e);
        }
    }

    /**
     * =================================================================
     * GLOBAL ERROR HANDLING
     * =================================================================
     */

    /**
     * Initialize global error handlers
     */
    function initGlobalErrorHandlers() {
        // Catch unhandled errors
        window.addEventListener('error', function(event) {
            logger.error('Unhandled error', {
                message: event.message,
                filename: event.filename,
                lineno: event.lineno,
                colno: event.colno,
                error: event.error
            });

            // Prevent default error display in production
            if (CONFIG.environment === 'production') {
                event.preventDefault();
            }
        });

        // Catch unhandled promise rejections
        window.addEventListener('unhandledrejection', function(event) {
            logger.error('Unhandled promise rejection', event.reason);

            if (CONFIG.environment === 'production') {
                event.preventDefault();
            }
        });

        logger.info('Global error handlers initialized');
    }

    /**
     * =================================================================
     * BROWSER COMPATIBILITY
     * =================================================================
     */

    /**
     * Check for required browser features
     */
    function checkBrowserCompatibility() {
        const requiredFeatures = {
            'localStorage': typeof(Storage) !== 'undefined',
            'addEventListener': !!window.addEventListener,
            'querySelector': !!document.querySelector,
            'classList': 'classList' in document.createElement('div'),
            'JSON': typeof JSON !== 'undefined'
        };

        const missingFeatures = [];

        Object.keys(requiredFeatures).forEach(feature => {
            if (!requiredFeatures[feature]) {
                missingFeatures.push(feature);
            }
        });

        if (missingFeatures.length > 0) {
            logger.warn('Missing browser features:', missingFeatures);

            // Show browser upgrade message
            const message = document.createElement('div');
            message.style.cssText = 'background: #fff3cd; border: 1px solid #ffeaa7; color: #856404; padding: 1rem; text-align: center;';
            message.textContent = 'Your browser is outdated. Some features may not work properly. Please upgrade to a modern browser.';
            document.body.insertBefore(message, document.body.firstChild);
        } else {
            logger.info('Browser compatibility check passed');
        }
    }

    /**
     * =================================================================
     * INITIALIZATION
     * =================================================================
     */

    /**
     * Initialize all features when DOM is ready
     */
    function init() {
        try {
            logger.info('R&E Roofing Website v' + CONFIG.version + ' initializing...');
            logger.info('Environment: ' + CONFIG.environment);

            // Check browser compatibility
            checkBrowserCompatibility();

            // Initialize global error handlers first
            initGlobalErrorHandlers();

            // Inject styles
            injectAnimationStyles();

            // Initialize core features
            initSmoothScrolling();
            initScrollEffects();
            initAnimations();
            initButtonInteractions();
            initServiceCardEffects();

            // Initialize UI components
            initContactModal();
            initContactForm();
            initMobileMenu();
            initFAQ();
            initCalculator();
            initLiveChat();
            initBackToTop();
            initCookieConsent();

            // Initialize analytics & tracking
            trackUTMParameters();
            initScrollDepthTracking();
            initEngagementTracking();

            // Initialize session & security
            getSessionId();
            initSessionTimeout();

            // Initialize network features
            initOfflineDetection();
            initServiceWorker();

            // Track page view
            trackPageView(window.location.pathname);

            logger.info('Initialization complete');

        } catch (e) {
            logger.error('Initialization failed', e);
        }
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Expose version info
    window.RERoofing = {
        version: CONFIG.version,
        buildDate: CONFIG.buildDate,
        environment: CONFIG.environment
    };

})(window, document);
