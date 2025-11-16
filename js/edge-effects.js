(() => {
  const images = Array.from(document.querySelectorAll('.chart-image'));
  if (!images.length) return;

  const EDGE_THRESHOLD = 0.12;

  const handleMove = (event) => {
    const img = event.currentTarget;
    const rect = img.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    const horizontalEdge = Math.min(x, rect.width - x) / rect.width;
    const verticalEdge = Math.min(y, rect.height - y) / rect.height;

    const isNearEdge = horizontalEdge <= EDGE_THRESHOLD || verticalEdge <= EDGE_THRESHOLD;
    if (isNearEdge) {
      const distanceFactor = Math.max(EDGE_THRESHOLD - Math.min(horizontalEdge, verticalEdge), 0) / EDGE_THRESHOLD;
      img.style.setProperty('--edge-x', `${(x / rect.width) * 100}%`);
      img.style.setProperty('--edge-y', `${(y / rect.height) * 100}%`);
      img.classList.add('edge-active');
      if (distanceFactor > 0.6) {
        img.classList.add('glow-strong');
      } else {
        img.classList.remove('glow-strong');
      }
    } else {
      img.classList.remove('edge-active', 'glow-strong');
    }
  };

  const handleLeave = (event) => {
    const img = event.currentTarget;
    img.classList.remove('edge-active', 'glow-strong');
  };

  images.forEach((img) => {
    img.addEventListener('pointermove', handleMove);
    img.addEventListener('pointerleave', handleLeave);
  });
})();
