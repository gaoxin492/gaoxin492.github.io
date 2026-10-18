(() => {
  const park = document.querySelector('.pixel-cat-park');
  if (!park) return;

  const sidebar = document.querySelector('.sidebar');
  const content = document.querySelector('.page');
  const platformLayer = park.querySelector('.pixel-cat-platforms');
  const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const random = (min, max) => min + Math.random() * (max - min);
  const cats = Array.from(park.querySelectorAll('.pixel-cat'), (element, index) => ({
    element,
    direction: element.querySelector('.pixel-cat__direction'),
    x: 16 + index * 80,
    y: 0,
    platform: 0,
    jump: null,
    target: 16 + index * 80,
    facing: index === 0 ? 1 : -1,
    state: 'idle',
    until: performance.now() + 1800 + index * 1200,
    blinkAt: performance.now() + random(2500, 6000),
    blinkEnd: 0,
    speed: random(24, 36),
    hovered: false,
    focused: false,
    reactionTimer: null
  }));
  let frame = null;
  let lastTime = 0;
  let chase = null;
  let nextChase = performance.now() + 10000;
  let platforms = [];
  let layoutKey = '';

  const held = cat => cat.hovered || cat.focused;
  const clamp = (x, level, cat) => {
    const platform = platforms[level];
    return Math.max(platform.left, Math.min(platform.right - cat.element.offsetWidth, x));
  };
  const setState = (cat, state, until) => {
    cat.state = state;
    cat.until = until;
    cat.element.dataset.state = state;
  };
  const paint = cat => {
    cat.element.style.left = `${Math.round(cat.x)}px`;
    cat.element.style.bottom = `${Math.round(cat.y)}px`;
    cat.element.dataset.level = cat.platform;
    cat.direction.style.transform = `scaleX(${cat.facing})`;
  };
  const travel = (cat, level, target, now) => {
    cat.target = clamp(target, level, cat);
    cat.facing = cat.target >= cat.x ? 1 : -1;
    if (level !== cat.platform) {
      cat.jump = { fromX: cat.x, fromY: cat.y, toX: cat.target, level, start: now, duration: 750 };
      setState(cat, 'jumping', Infinity);
    } else if (Math.abs(cat.target - cat.x) < 2) {
      setState(cat, 'idle', now + 1500);
    } else {
      setState(cat, 'walking', Infinity);
    }
  };
  const land = cat => {
    if (!cat.jump) return;
    cat.platform = cat.jump.level;
    cat.x = cat.jump.toX;
    cat.y = platforms[cat.platform].y;
    cat.jump = null;
  };
  const play = (cat, now) => {
    land(cat);
    setState(cat, 'playing', now + 1800);
  };
  const wander = (cat, now, climb = false) => {
    let level = cat.platform;
    if (platforms.length > 1 && (climb || Math.random() < 0.65)) {
      const direction = level === 0 ? 1 : level === platforms.length - 1 ? -1 : Math.random() < 0.5 ? -1 : 1;
      level += direction;
    }
    const platform = platforms[level];
    const target = level !== cat.platform
      ? (climb ? platform.right - cat.element.offsetWidth : random(platform.left, platform.right - cat.element.offsetWidth))
      : cat.x + (Math.random() < 0.5 ? -1 : 1) * random(60, 170);
    travel(cat, level, target, now);
  };
  const resize = () => {
    const rect = sidebar && sidebar.getBoundingClientRect();
    const pageRect = content && content.getBoundingClientRect();
    const bottom = parseFloat(getComputedStyle(park).bottom) || 10;
    const available = rect ? window.innerHeight - Math.max(rect.bottom + 12, 72) - bottom : 0;
    const useSidebar = rect && pageRect && rect.right <= pageRect.left + 4 && rect.width >= 170 && available >= 160;
    const left = useSidebar ? Math.round(rect.left + 8) : 12;
    const width = useSidebar ? Math.floor(rect.width - 16) : window.innerWidth - 24;
    const height = useSidebar ? Math.floor(available) : 72;
    const size = cats[0].element.offsetWidth;
    const key = `${left}:${width}:${height}:${size}:${Boolean(useSidebar)}`;
    if (key === layoutKey) return;
    const firstLayout = !layoutKey;
    layoutKey = key;
    park.classList.toggle('pixel-cat-park--sidebar', Boolean(useSidebar));
    park.style.left = `${left}px`;
    park.style.right = 'auto';
    park.style.width = `${width}px`;
    park.style.height = `${height}px`;
    const count = useSidebar ? Math.min(6, Math.max(2, Math.floor((height - size - 24) / 100) + 1)) : 1;
    const spacing = count > 1 ? Math.floor((height - size - 24) / (count - 1)) : 0;
    const ledgeWidth = Math.min(width - 16, Math.max(size * 2 + 12, Math.floor(width * 0.72)));
    platforms = Array.from({ length: Math.max(1, count) }, (_, index) => {
      const ledgeLeft = index === 0 ? 4 : index % 2 ? 8 : width - ledgeWidth - 8;
      return { left: ledgeLeft, right: index === 0 ? width - 4 : ledgeLeft + ledgeWidth, y: index * spacing };
    });
    const supports = [];
    if (useSidebar) {
      [0.28, 0.72].forEach((position, index) => {
        const post = document.createElement('span');
        const topLevel = (count - 1) % 2 === (index === 0 ? 1 : 0) ? count - 1 : count - 2;
        post.className = 'pixel-cat-tree__post';
        post.style.left = `${Math.round(width * position) - 4}px`;
        post.style.bottom = `${size * 3 / 32}px`;
        post.style.height = `${platforms[topLevel].y}px`;
        supports.push(post);
      });
      const base = document.createElement('span');
      base.className = 'pixel-cat-tree__base';
      base.style.width = `${width - 8}px`;
      base.style.height = `${size * 3 / 32}px`;
      supports.push(base);
      const house = document.createElement('span');
      house.className = 'pixel-cat-tree__house';
      house.style.left = `${Math.round(width * 0.46) - 32}px`;
      house.style.bottom = `${size * 3 / 32}px`;
      house.style.height = `${Math.min(64, spacing - 12)}px`;
      supports.push(house);
    }
    platformLayer.replaceChildren(...supports, ...platforms.map(platform => {
      const ledge = document.createElement('span');
      ledge.className = 'pixel-cat-platform';
      ledge.style.left = `${platform.left}px`;
      ledge.style.width = `${platform.right - platform.left}px`;
      ledge.style.bottom = `${platform.y + size * 3 / 32 - 4}px`;
      return ledge;
    }));
    chase = null;
    cats.forEach((cat, index) => {
      cat.platform = firstLayout ? (index === 0 ? platforms.length - 1 : 0) : Math.min(cat.platform, platforms.length - 1);
      cat.jump = null;
      cat.x = clamp(cat.x, cat.platform, cat);
      cat.y = platforms[cat.platform].y;
      cat.target = cat.x;
      setState(cat, 'idle', performance.now() + 1800 + index * 1200);
      paint(cat);
    });
  };

  cats.forEach(cat => {
    cat.element.addEventListener('pointerenter', event => {
      if (event.pointerType === 'mouse') cat.hovered = true;
    });
    cat.element.addEventListener('pointerleave', () => { cat.hovered = false; });
    cat.element.addEventListener('focus', () => { cat.focused = true; });
    cat.element.addEventListener('blur', () => { cat.focused = false; });
    cat.element.addEventListener('click', () => {
      chase = null;
      nextChase = performance.now() + 10000;
      clearTimeout(cat.reactionTimer);
      play(cat, performance.now());
      cat.reactionTimer = setTimeout(() => setState(cat, 'idle', performance.now() + 2000), 1800);
    });
  });

  const tick = now => {
    const elapsed = Math.min((now - lastTime) / 1000, 0.05);
    lastTime = now;

    if (!chase && now >= nextChase && cats.every(cat => !held(cat) && cat.state !== 'playing')) {
      const leader = cats[Math.random() < 0.5 ? 0 : 1];
      const follower = cats.find(cat => cat !== leader);
      wander(leader, now, true);
      chase = { leader, follower, until: now + 10000 };
      nextChase = now + random(18000, 26000);
    }

    if (chase) {
      const { leader, follower } = chase;
      if (held(leader) || held(follower) || now >= chase.until) {
        chase = null;
      } else {
        const gap = leader.element.offsetWidth + 8;
        if (leader.state !== 'jumping' && follower.state !== 'jumping') {
          const platform = platforms[leader.platform];
          const behind = leader.x - leader.facing * gap;
          const target = behind >= platform.left && behind <= platform.right - follower.element.offsetWidth
            ? behind
            : leader.x + leader.facing * gap;
          const level = follower.platform === leader.platform
            ? leader.platform
            : follower.platform + Math.sign(leader.platform - follower.platform);
          travel(follower, level, target, now);
          if (leader.state !== 'walking' && follower.state === 'idle' && follower.platform === leader.platform && Math.abs(leader.x - follower.x) <= gap + 3) {
            leader.facing = follower.x > leader.x ? 1 : -1;
            follower.facing = -leader.facing;
            cats.forEach(cat => play(cat, now));
            chase = null;
          }
        }
      }
    }

    cats.forEach(cat => {
      if (cat.state === 'jumping' && cat.jump) {
        const progress = Math.min(1, (now - cat.jump.start) / cat.jump.duration);
        cat.x = cat.jump.fromX + (cat.jump.toX - cat.jump.fromX) * progress;
        cat.y = cat.jump.fromY + (platforms[cat.jump.level].y - cat.jump.fromY) * progress + Math.sin(progress * Math.PI) * 24;
        if (progress === 1) {
          land(cat);
          setState(cat, 'idle', now + random(1200, 2500));
        }
      } else if (!held(cat) && cat.state === 'walking') {
        const distance = cat.target - cat.x;
        const speed = chase && chase.follower === cat ? chase.leader.speed + 12 : cat.speed;
        const step = Math.min(Math.abs(distance), speed * elapsed);
        cat.x = clamp(cat.x + Math.sign(distance) * step, cat.platform, cat);
        if (Math.abs(cat.target - cat.x) < 1) setState(cat, 'idle', now + random(1500, 4000));
      } else if (now >= cat.until && !chase) {
        if (held(cat)) {
          setState(cat, 'idle', now + 1000);
        } else if (Math.random() < 0.2) {
          setState(cat, 'sleeping', now + random(4000, 7000));
        } else {
          wander(cat, now);
        }
      }

      if (now >= cat.blinkAt) {
        cat.blinkEnd = now + 160;
        cat.blinkAt = now + random(3000, 6500);
      }
      cat.element.classList.toggle('is-blinking', now < cat.blinkEnd);
      paint(cat);
    });
    frame = requestAnimationFrame(tick);
  };

  const syncMotion = () => {
    cancelAnimationFrame(frame);
    frame = null;
    if (motion.matches) {
      chase = null;
      cats.forEach(cat => {
        land(cat);
        setState(cat, 'idle', performance.now() + 2000);
        cat.element.classList.remove('is-blinking');
        paint(cat);
      });
    }
    if (!document.hidden && !motion.matches) {
      lastTime = performance.now();
      frame = requestAnimationFrame(tick);
    }
  };

  window.addEventListener('resize', resize);
  window.addEventListener('scroll', resize, { passive: true });
  if (sidebar && window.ResizeObserver) new ResizeObserver(resize).observe(sidebar);
  document.addEventListener('visibilitychange', syncMotion);
  motion.addEventListener('change', syncMotion);
  resize();
  syncMotion();
})();
