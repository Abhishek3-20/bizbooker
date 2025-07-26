// floating.js
document.addEventListener('DOMContentLoaded', function() {
  const floatingContainer = document.createElement('div');
  floatingContainer.className = 'floating-container';
  floatingContainer.style.position = 'fixed';
  floatingContainer.style.top = '0';
  floatingContainer.style.left = '0';
  floatingContainer.style.width = '100%';
  floatingContainer.style.height = '100%';
  floatingContainer.style.pointerEvents = 'none';
  floatingContainer.style.zIndex = '-1';
  
  const colors = [
    'rgba(255, 215, 0, 0.1)',
    'rgba(255, 215, 0, 0.08)',
    'rgba(255, 215, 0, 0.05)'
  ];
  
  // Create 3 floating elements
  for (let i = 0; i < 3; i++) {
    const element = document.createElement('div');
    element.className = 'floating-element';
    element.style.width = `${100 + Math.random() * 200}px`;
    element.style.height = element.style.width;
    element.style.background = colors[i % colors.length];
    element.style.borderRadius = '50%';
    element.style.filter = 'blur(40px)';
    element.style.position = 'absolute';
    element.style.animation = `float ${15 + Math.random() * 10}s infinite ease-in-out`;
    element.style.animationDelay = `${Math.random() * 5}s`;
    element.style.top = `${Math.random() * 100}%`;
    element.style.left = `${Math.random() * 100}%`;
    
    floatingContainer.appendChild(element);
  }
  
  document.body.appendChild(floatingContainer);
});