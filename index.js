function plantHtml(date, daysBeforeToday) {
  var $div = $('<div></div>');
  var $fig = $('<figure class="figure"></figure>');
  var $img = $('<img class="mx-auto" src="https://s3.amazonaws.com/atengam-rpi3-photos/' + date + '.gif">');
  var caption = (daysBeforeToday > 1) ? daysBeforeToday + " Days Ago"  : "Yesterday"; 
  var $figCaption = $('<figcaption class="figure-caption text-center">' + caption + '</figcaption>');
  $div.append($fig);
  $fig.append($img);
  $fig.append($figCaption);
  return $div;
}

function formatDate(date) {
  var dd = date.getDate();
  var mm = date.getMonth() + 1; //January is 0!
  var yyyy = date.getFullYear();
  if (dd < 10) {
    dd = '0' + dd;
  }
  if (mm < 10) {
    mm = '0' + mm;
  }
  return yyyy + '-' + mm + '-' + dd;
}

$(document).ready(function() {
  var MS_PER_DAY = 60000 * 60 * 24;
  for (var i=1; i<=5; i++) {
    var today = new Date();
    var date = new Date(today - MS_PER_DAY * i);
    $('#row').append(plantHtml(formatDate(date), i));
  }
});