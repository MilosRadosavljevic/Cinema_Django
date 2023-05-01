$(document).ready(function () {
  $(".carousel").carousel({
    pause: false,
  });
  $(".carousel-item").click(function () {
    return false;
  });
  $(".carousel-item").hover(function () {
    $(this).css("cursor", "default");
  });
});
