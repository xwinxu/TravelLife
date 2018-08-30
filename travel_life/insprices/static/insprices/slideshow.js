function retrieveURL(filename) {
    var scripts = document.getElementsByTagName('script');
    if (scripts && scripts.length > 0) {
        for (var i in scripts) {
            if (scripts[i].src && scripts[i].src.match(new RegExp(filename+'\\.js$'))) {
                return scripts[i].src.replace(new RegExp('(.*)'+filename+'\\.js$'), '$1');
            }
        }
    }
};

$(document).ready(function() {
  const MAX_IMAGES = 3;
  var body = $('body');
  var src = retrieveURL('slideshow');
  var images = ["url(" + src + "images/Canada1.png)",
  "url(" + src + "images/Canada2.png)", "url(" + src + "images/Canada3.png)"];
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

