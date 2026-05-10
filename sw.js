const CACHE_NAME = 'aura-v1';
const ASSETS = [
  '/',
  '/index.html',
  '/partners.html',
  '/dev.html',
  '/updates.html',
  '/style.css' // Ensure your CSS filename matches
];

// Install: Cache core assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
  );
});

// Fetch: Network-first falling back to cache (keeps data fresh)
self.addEventListener('fetch', (event) => {
  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request))
  );
});
