(() => {
  const images = Array.from(document.querySelectorAll('img[loading="lazy"]'));
  if (!images.length) return;

  const onLoad = (img) => {
    img.classList.remove('is-lazy');
    img.classList.add('is-loaded');
  };

  images.forEach((img) => {
    img.classList.add('is-lazy');
    if (img.complete) {
      onLoad(img);
    } else {
      img.addEventListener('load', () => onLoad(img), { once: true });
      img.addEventListener('error', () => img.classList.remove('is-lazy'), { once: true });
    }
  });

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const target = entry.target;
          const dataSrc = target.dataset.src;
          if (dataSrc && target.src !== dataSrc) {
            target.src = dataSrc;
          }
          observer.unobserve(target);
        }
      });
    }, {
      rootMargin: '100px',
      threshold: 0.05
    });

    images.forEach((img) => observer.observe(img));
  }
})();
