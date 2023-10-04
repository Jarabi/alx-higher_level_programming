$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const language = $('input#language_code').val();

    $.ajax({
      url: `https://hellosalut.stefanbohacek.dev/?lang=${language}`,
      type: 'GET',
      success: function (response) {
        $('div#hello').text(response.hello);
      }
    });
  });
});
