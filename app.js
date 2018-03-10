var lessonIndex = 0;
var pageIndex = 0;
var lessons = [];
var slides = [];

$(function() {
  $('body').on('click', 'a', function(e) {
    e.preventDefault();
    var url = e.target.href;
    window.open(url);
  });

  initialize();

  function initialize() {
    $.get('lessons/lessons.json')
      .then(function(data) {
        lessons = data;
        lessonIndex = 1;
        restoreHashLocation();
      });
  }

  function restoreHashLocation() {
    if (location.hash) {
      var match = location.hash.match(/^\#([\w\-0-9]+)\/([\w\-0-9\.]+)(?:\/([0-9]+))?/);
      var course = match[1];
      var lesson = match[2];
      var slideNo = match[3];
      var targetPath = course + "/" + lesson;
      if (!slideNo) {
        lessonIndex = _.findIndex(lessons, function(l) { return l.path === targetPath; });
        startLesson();
      } else if (slideNo) {
        lessonIndex = _.findIndex(lessons, function(l) { return l.path === targetPath; });
        pageIndex = Number(slideNo);
        // console.log('lessonIndex', lessonIndex, 'pageIndex', pageIndex);
        startLesson();
      } else {
        throw new Error('Invalid path: ' + location.hash);
      }
      showSlides();
      hideLessonsList();
    } else {
      showLessonsList();
      hideSlides();
      listLessons();
    }
  }

  function hideLessonsList() {
    $("#lesson-list").hide();
  }

  function showLessonsList() {
    $("#lesson-list").show();
  }

  function showSlides() {
    $("#slide-contents").show();
  }

  function hideSlides() {
    $("#slide-contents").hide();
  }

  $(window).on('hashchange', function() {
    restoreHashLocation();
  });

  function listLessons() {
    var markup = '<ul>' + lessons.map(function(lesson) {
      return '<li><a href="#' + lesson.path + '">' + lesson.title + '</a></li>';
    }).join('') + '</ul>';
    $('#lesson-list').html(markup);
  }

  function startLesson() {
    // console.log("lessons", lessons);
    // console.log("lessonIndex", lessonIndex);
    var lesson = lessons[lessonIndex];
    $.get('lessons/' + lesson.path + '/presentation.md')
      .then(function(md) {
        var html = markdownRender(md);
        slides = splitSlides(html);
        showCurrentSlide();
      });
  }

  $('#next-button').click(advanceSlide);
  $(window).on('keydown', function(evt) {
    if (evt.keyCode === 39 || evt.keyCode === 40) {
      advanceSlide();
    } else if (evt.keyCode === 37 || evt.keyCode === 38) {
      retreatSlide();
    }
  });
  $('#previous-button').click(retreatSlide);

  function advanceSlide() {
    if (pageIndex < slides.length - 1) {
      pageIndex++;
      updateSlide();
    }
  }

  function retreatSlide() {
    if (pageIndex > 0) {
      pageIndex--;
      updateSlide();
    }
  }

  function updateSlide() {
    var lesson = lessons[lessonIndex];
    location.hash = lesson.path + '/' + pageIndex;
  }

  function showCurrentSlide() {
    $('#slide-contents .tooltip').tooltipster('close');
    var page = slides[pageIndex];
    $('#slide-contents')
      .html(page.slide)
      .find('.tooltip')
      .tooltipster({
        delay: 0,
        animationDuration: 0
      })
      .tooltipster('open');
    $('#speaker-notes')
      .html(page.speakerNotes || "");
    $('#page-number').text(pageIndex + 1);
    $('#total-page-number').text(slides.length);
  }

  function markdownRender(md) {
    md = preprocess(md);
    var html = markdownit({
      html: true
    }).render(md);
    html = postprocess(html);
    return html;
  }

  function preprocess(md) {
    return md;
  }

  function postprocess(html) {
    html = html.replace(/([^\[])\[\[((?:[^\[]|[\n])(?:.|[\n])*?)\]\]\[\[(.*?)\]\]/g, '$1<span title="$3" class="tooltip">$2</span>');
    html = html.replace(/\[\[\[((?:.|[\n])*?)\]\]\]([^\]]|$)/g, '<span class="highlight">$1</span>$2');
    html = html.replace(/---/g, "&#8212;");
    return html;
  }

  function splitSlides(html) {
    // console.log('html', html);
    var parts = html.split(/\<hr\>/g);
    // console.log('parts', parts);
    var pages = [];
    for (var i = 0; i < parts.length; i+=2) {
      pages.push({
        slide: parts[i],
        speakerNotes: parts[i + 1]
      });
    }
    return pages;
  }
});
