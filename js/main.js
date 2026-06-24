document.addEventListener('DOMContentLoaded', () => {
    const yearEl = document.getElementById('year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    initMegaMenu();
});

function initMegaMenu() {
    const header = document.querySelector('.site-header');
    const menu = document.querySelector('.site-header__menu');
    if (!header || !menu) return;
    // Desktop, hover-capable pointers only. On touch/mobile the top links just navigate.
    if (!window.matchMedia('(hover: hover) and (min-width: 761px)').matches) return;

    const fr = document.documentElement.lang === 'fr';
    const cHref = fr ? '/fr/personnages/' : '/characters/';
    const sHref = fr ? '/fr/histoire/' : '/story/';

    const card = (href, img, name, role) =>
        '<a class="megacard" href="' + href + '"><span class="megacard__img"><img src="' + img +
        '" alt="' + name + '" loading="lazy"></span><span class="megacard__name">' + name +
        '</span><span class="megacard__role">' + role + '</span></a>';
    const wcard = (href, img, name, role) =>
        '<a class="megacard megacard--wide" href="' + href + '"><span class="megacard__img"><img src="' + img +
        '" alt="' + name + '" loading="lazy"></span><span class="megacard__name">' + name +
        '</span><span class="megacard__role">' + role + '</span></a>';
    const li = (href, label) => '<li><a href="' + href + '">' + label + '</a></li>';
    const soon = (label) => '<li class="is-soon"><span>' + label + '</span></li>';

    const buildPanel = (name, inner) => {
        const d = document.createElement('div');
        d.className = 'mega';
        d.setAttribute('data-mega', name);
        d.innerHTML = '<div class="mega__inner">' + inner + '</div>';
        return d;
    };

    const charPanel = buildPanel('characters',
        '<div class="mega__featured"><p class="mega__label">' + (fr ? 'En vedette' : 'Featured') + '</p>' +
        '<div class="mega__cards">' +
        card(cHref + 'arthur-morgan/', '/assets/characters/arthur-morgan/portrait.jpeg', 'Arthur Morgan', fr ? 'Gang Van der Linde · RDR2' : 'Van der Linde gang · RDR2') +
        card(cHref + 'john-marston/', '/assets/characters/john-marston/portrait.jpeg', 'John Marston', fr ? 'Gang Van der Linde · RDR1' : 'Van der Linde gang · RDR1') +
        card(cHref + 'dutch-van-der-linde/', '/assets/characters/dutch-van-der-linde/portrait.jpeg', 'Dutch van der Linde', fr ? 'Le chef du gang' : 'The gang leader') +
        card(cHref + 'micah-bell/', '/assets/characters/micah-bell/portrait.jpeg', 'Micah Bell', fr ? 'Le traître' : 'The traitor') +
        '</div></div>' +
        '<div class="mega__list"><p class="mega__label">' + (fr ? 'Autres personnages' : 'More characters') + '</p><ul>' +
        li(cHref + 'sadie-adler/', 'Sadie Adler') +
        li(cHref + 'hosea-matthews/', 'Hosea Matthews') +
        li(cHref + 'charles-smith/', 'Charles Smith') +
        li(cHref + 'bill-williamson/', 'Bill Williamson') +
        li(cHref + 'abigail-marston/', 'Abigail Marston') +
        '</ul><a class="mega__all" href="' + cHref + '">' + (fr ? 'Tous les personnages' : 'All characters') + ' &rarr;</a></div>');

    const storyPanel = buildPanel('story',
        '<div class="mega__featured"><p class="mega__label">' + (fr ? 'À lire' : 'Read now') + '</p>' +
        '<div class="mega__cards mega__cards--wide">' +
        wcard(sHref + (fr ? 'rdr2-chapitre-1-colter/' : 'rdr2-chapter-1-colter/'), '/assets/story/locations/colter.jpeg', fr ? 'Chapitre 1 : Colter' : 'Chapter 1: Colter', 'RDR2 · 1899') +
        wcard(sHref + (fr ? 'rdr2-chapitre-2-horseshoe-overlook/' : 'rdr2-chapter-2-horseshoe-overlook/'), '/assets/story/locations/horseshoe.jpeg', fr ? 'Chapitre 2 : Horseshoe Overlook' : 'Chapter 2: Horseshoe Overlook', 'RDR2 · 1899') +
        '</div></div>' +
        '<div class="mega__list"><p class="mega__label">' + (fr ? 'À venir' : 'Coming next') + '</p><ul>' +
        soon(fr ? 'Chapitre 3 : Clemens Point' : 'Chapter 3: Clemens Point') +
        soon(fr ? 'Chapitre 4 : Saint Denis' : 'Chapter 4: Saint Denis') +
        soon(fr ? 'Chapitre 5 : Guarma' : 'Chapter 5: Guarma') +
        soon(fr ? 'Chapitre 6 : Beaver Hollow' : 'Chapter 6: Beaver Hollow') +
        soon(fr ? 'Épilogue' : 'Epilogue') +
        '</ul><a class="mega__all" href="' + sHref + '">' + (fr ? "Guide complet de l'histoire" : 'Full story guide') + ' &rarr;</a></div>');

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
