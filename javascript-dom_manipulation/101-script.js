document.addEventListener('DOMContentLoaded', function () {
  const translateBtn = document.getElementById('btn_translate');
  const langSelect = document.getElementById('language_code');
  const output = document.getElementById('hello');

  translateBtn.addEventListener('click', function () {
    const lang = langSelect.value;
    if (!lang) {
      output.textContent = 'Please select a language.';
      return;
    }

    const url = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
    fetch(url)
      .then(response => response.json())
      .then(data => {
        output.textContent = data.hello;
      })
      .catch(error => {
        output.textContent = 'Error fetching translation.';
        console.error('Fetch error:', error);
      });
  });
});
