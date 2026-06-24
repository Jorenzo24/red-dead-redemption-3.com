document.addEventListener('DOMContentLoaded', () => {
    const yearEl = document.getElementById('year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();
    initNav();
});

function initNav() {
    const header = document.querySelector('.site-header');
    const menu = document.querySelector('.site-header__menu');
    if (!header || !menu) return;

    const fr = document.documentElement.lang === 'fr';
    const cHref = fr ? '/fr/personnages/' : '/characters/';
    const sHref = fr ? '/fr/histoire/' : '/story/';
    const nHref = fr ? '/fr/articles/' : '/articles/';

    const T = {
        featured: fr ? 'En vedette' : 'Featured',
        more: fr ? 'Autres personnages' : 'More characters',
        allChars: fr ? 'Tous les personnages' : 'All characters',
        readNow: fr ? 'À lire' : 'Read now',
        coming: fr ? 'À venir' : 'Coming next',
        guide: fr ? "Guide complet de l'histoire" : 'Full story guide',
        menu: 'Menu',
        close: fr ? 'Fermer le menu' : 'Close menu',
        open: fr ? 'Ouvrir le menu' : 'Open menu',
        news: fr ? 'Actus' : 'News',
        story: fr ? 'Histoire' : 'Story',
        chars: fr ? 'Personnages' : 'Characters',
        showChapters: fr ? 'Voir les chapitres' : 'Show chapters',
        showChars: fr ? 'Voir les personnages' : 'Show characters'
    };

    const charFeatured = [
        ['arthur-morgan', 'Arthur Morgan', fr ? 'Gang Van der Linde · RDR2' : 'Van der Linde gang · RDR2'],
        ['john-marston', 'John Marston', fr ? 'Gang Van der Linde · RDR1' : 'Van der Linde gang · RDR1'],
        ['dutch-van-der-linde', 'Dutch van der Linde', fr ? 'Le chef du gang' : 'The gang leader'],
        ['micah-bell', 'Micah Bell', fr ? 'Le traître' : 'The traitor']
    ];
    const charMore = [
        ['sadie-adler', 'Sadie Adler'],
        ['hosea-matthews', 'Hosea Matthews'],
        ['charles-smith', 'Charles Smith'],
        ['bill-williamson', 'Bill Williamson'],
        ['abigail-marston', 'Abigail Marston']
    ];
    const storyFeatured = [
        [sHref + (fr ? 'rdr2-chapitre-1-colter/' : 'rdr2-chapter-1-colter/'), '/assets/story/locations/colter.jpeg', fr ? 'Chapitre 1 : Colter' : 'Chapter 1: Colter', 'RDR2 · 1899'],
        [sHref + (fr ? 'rdr2-chapitre-2-horseshoe-overlook/' : 'rdr2-chapter-2-horseshoe-overlook/'), '/assets/story/locations/horseshoe.jpeg', fr ? 'Chapitre 2 : Horseshoe Overlook' : 'Chapter 2: Horseshoe Overlook', 'RDR2 · 1899']
    ];
    const storyComing = fr
        ? ['Chapitre 3 : Clemens Point', 'Chapitre 4 : Saint Denis', 'Chapitre 5 : Guarma', 'Chapitre 6 : Beaver Hollow', 'Épilogue']
        : ['Chapter 3: Clemens Point', 'Chapter 4: Saint Denis', 'Chapter 5: Guarma', 'Chapter 6: Beaver Hollow', 'Epilogue'];
    const portrait = (slug) => '/assets/characters/' + slug + '/portrait.jpeg';

    buildMega();
    buildDrawer();

    /* ---------- Desktop mega menu ---------- */
    function buildMega() {
        if (!window.matchMedia('(hover: hover) and (min-width: 761px)').matches) return;
        const card = (href, img, name, role, wide) =>
            '<a class="megacard' + (wide ? ' megacard--wide' : '') + '" href="' + href + '"><span class="megacard__img"><img src="' + img +
            '" alt="' + name + '" loading="lazy"></span><span class="megacard__name">' + name +
            '</span><span class="megacard__role">' + role + '</span></a>';
        const panel = (name, inner) => {
            const d = document.createElement('div');
            d.className = 'mega';
            d.setAttribute('data-mega', name);
            d.innerHTML = '<div class="mega__inner">' + inner + '</div>';
            return d;
        };
        const charPanel = panel('characters',
            '<div class="mega__featured"><p class="mega__label">' + T.featured + '</p><div class="mega__cards">' +
            charFeatured.map(c => card(cHref + c[0] + '/', portrait(c[0]), c[1], c[2], false)).join('') +
            '</div></div><div class="mega__list"><p class="mega__label">' + T.more + '</p><ul>' +
            charMore.map(c => '<li><a href="' + cHref + c[0] + '/">' + c[1] + '</a></li>').join('') +
            '</ul><a class="mega__all" href="' + cHref + '">' + T.allChars + ' &rarr;</a></div>');
        const storyPanel = panel('story',
            '<div class="mega__featured"><p class="mega__label">' + T.readNow + '</p><div class="mega__cards mega__cards--wide">' +
            storyFeatured.map(s => card(s[0], s[1], s[2], s[3], true)).join('') +
            '</div></div><div class="mega__list"><p class="mega__label">' + T.coming + '</p><ul>' +
            storyComing.map(x => '<li class="is-soon"><span>' + x + '</span></li>').join('') +
            '</ul><a class="mega__all" href="' + sHref + '">' + T.guide + ' &rarr;</a></div>');

        const links = {};
        const panels = { characters: charPanel, story: storyPanel };
        menu.querySelectorAll('a.site-header__link').forEach((a) => {
            const href = a.getAttribute('href');
            if (href === cHref) links.characters = a;
            else if (href === sHref) links.story = a;
        });
        const setOpen = (name) => {
            Object.keys(panels).forEach((k) => {
                const on = k === name;
                panels[k].classList.toggle('is-open', on);
                if (links[k]) links[k].setAttribute('aria-expanded', on ? 'true' : 'false');
            });
        };
        const close = () => setOpen(null);
        Object.keys(panels).forEach((name) => {
            const a = links[name];
            if (!a) return;
            const p = panels[name];
            a.classList.add('has-mega');
            a.setAttribute('aria-haspopup', 'true');
            a.setAttribute('aria-expanded', 'false');
            header.appendChild(p);
            a.addEventListener('mouseenter', () => setOpen(name));
            a.addEventListener('focus', () => setOpen(name));
            p.addEventListener('mouseenter', () => setOpen(name));
        });
        header.addEventListener('mouseleave', close);
        header.addEventListener('focusout', (e) => { if (!header.contains(e.relatedTarget)) close(); });
        document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
    }

    /* ---------- Mobile drawer ---------- */
    function buildDrawer() {
        const nav = header.querySelector('.site-header__nav');
        if (!nav) return;

        const burger = document.createElement('button');
        burger.className = 'navburger';
        burger.type = 'button';
        burger.setAttribute('aria-label', T.open);
        burger.setAttribute('aria-expanded', 'false');
        burger.setAttribute('aria-controls', 'mobile-drawer');
        burger.innerHTML = '<span></span><span></span><span></span>';
        nav.appendChild(burger);

        const overlay = document.createElement('div');
        overlay.className = 'drawer-overlay';

        const drawer = document.createElement('aside');
        drawer.className = 'drawer';
        drawer.id = 'mobile-drawer';
        drawer.setAttribute('aria-label', T.menu);
        drawer.setAttribute('aria-hidden', 'true');

        const charCards = charFeatured.map(c =>
            '<a class="drawer__card" href="' + cHref + c[0] + '/"><img src="' + portrait(c[0]) + '" alt="' + c[1] + '" loading="lazy"><span>' + c[1] + '</span></a>').join('');
        const charList = charMore.map(c => '<li><a href="' + cHref + c[0] + '/">' + c[1] + '</a></li>').join('');
        const storyCards = storyFeatured.map(s =>
            '<a class="drawer__card" href="' + s[0] + '"><img src="' + s[1] + '" alt="' + s[2] + '" loading="lazy"><span>' + s[2] + '</span></a>').join('');
        const storyList = storyComing.map(x => '<li class="is-soon"><span>' + x + '</span></li>').join('');

        const group = (label, href, expLabel, cardsWide, cards, list, allLabel) =>
            '<div class="drawer__group"><div class="drawer__row"><a class="drawer__link" href="' + href + '">' + label + '</a>' +
            '<button class="drawer__exp" type="button" aria-expanded="false" aria-label="' + expLabel + '"><span class="drawer__chev"></span></button></div>' +
            '<div class="drawer__sub" hidden><div class="drawer__cards' + (cardsWide ? ' drawer__cards--wide' : '') + '">' + cards + '</div>' +
            '<ul class="drawer__sublist">' + list + '</ul>' +
            '<a class="drawer__all" href="' + href + '">' + allLabel + ' &rarr;</a></div></div>';

        drawer.innerHTML =
            '<div class="drawer__head"><span class="drawer__title">' + T.menu + '</span>' +
            '<button class="drawer__close" type="button" aria-label="' + T.close + '">&times;</button></div>' +
            '<nav class="drawer__nav" aria-label="' + T.menu + '">' +
            '<a class="drawer__link drawer__link--solo" href="' + nHref + '">' + T.news + '</a>' +
            group(T.story, sHref, T.showChapters, true, storyCards, storyList, T.guide) +
            group(T.chars, cHref, T.showChars, false, charCards, charList, T.allChars) +
            '</nav><div class="drawer__lang"></div>';

        const langWrap = drawer.querySelector('.drawer__lang');
        header.querySelectorAll('.lang-switch > *').forEach(n => langWrap.appendChild(n.cloneNode(true)));

        document.body.appendChild(overlay);
        document.body.appendChild(drawer);

        const closeBtn = drawer.querySelector('.drawer__close');
        const open = () => {
            drawer.classList.add('is-open'); overlay.classList.add('is-open'); burger.classList.add('is-open');
            burger.setAttribute('aria-expanded', 'true'); burger.setAttribute('aria-label', T.close);
            drawer.setAttribute('aria-hidden', 'false'); document.body.classList.add('drawer-open');
            closeBtn.focus();
        };
        const close = () => {
            drawer.classList.remove('is-open'); overlay.classList.remove('is-open'); burger.classList.remove('is-open');
            burger.setAttribute('aria-expanded', 'false'); burger.setAttribute('aria-label', T.open);
            drawer.setAttribute('aria-hidden', 'true'); document.body.classList.remove('drawer-open');
        };

        burger.addEventListener('click', () => drawer.classList.contains('is-open') ? close() : open());
        overlay.addEventListener('click', close);
        closeBtn.addEventListener('click', () => { close(); burger.focus(); });

        drawer.querySelectorAll('.drawer__exp').forEach((btn) => {
            btn.addEventListener('click', () => {
                const sub = btn.closest('.drawer__group').querySelector('.drawer__sub');
                const isOpen = btn.getAttribute('aria-expanded') === 'true';
                btn.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
                sub.hidden = isOpen;
            });
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && drawer.classList.contains('is-open')) { close(); burger.focus(); }
        });
        drawer.addEventListener('keydown', (e) => {
            if (e.key !== 'Tab') return;
            const f = drawer.querySelectorAll('a[href], button:not([disabled])');
            if (!f.length) return;
            const first = f[0], last = f[f.length - 1];
            if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
            else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
        });
        const mq = window.matchMedia('(min-width: 761px)');
        if (mq.addEventListener) mq.addEventListener('change', (e) => { if (e.matches) close(); });
    }
}
