$(document).ready(function() {
  const MAX_IMAGES = 3;
  var body = $('body');
  var images = ['url(Canada1.png)', 'url(Canada2.png)', 'url(Canada3.png)'];
  var i = 1;

  function cycle() {
    if (i == MAX_IMAGES) {
      i = 0;
    }

    body.css('backgroundImage', images[i]);
    ++i;
    setTimeout(cycle, 5000);
  }

  setTimeout(cycle, 5000);
  body.css('backgroundImage', images[0]);
});

