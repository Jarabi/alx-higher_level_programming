function translateThis () {
  const language = $('input#language_code').val();

  $.ajax({
    url: `https://hellosalut.stefanbohacek.dev/?lang=${language}`,
    type: 'GET',
    success: function (response) {
      $('div#hello').text(response.hello);
    }
  });
}

$(document).ready(function () {
  // Click event
  $('input#btn_translate').on('click', translateThis);

  // 'Enter' press event
  $('input#language_code').on('keypress', function (event) {
    if (event.which === 13) { translateThis(); }
  });
});
