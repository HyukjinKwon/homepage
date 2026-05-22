(function () {
  var root = document.documentElement;
  var btn = document.getElementById('theme-toggle');
  if (!btn) return;

  function sync() {
    var theme = root.getAttribute('data-theme') || 'light';
    btn.querySelector('[data-icon="dark"]').hidden = theme === 'light';
    btn.querySelector('[data-icon="light"]').hidden = theme !== 'light';
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', theme === 'light' ? '#ffffff' : '#0a0a0a');
  }

  sync();
  btn.addEventListener('click', function () {
    var next = (root.getAttribute('data-theme') || 'light') === 'light' ? 'dark' : 'light';
    root.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    sync();
  });
})();
