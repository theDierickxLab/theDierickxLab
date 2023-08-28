document.addEventListener('DOMContentLoaded', function() {

  const events = document.querySelectorAll('.event');
  

  events.forEach((event, index) => {
    if (index >= 3) {
      event.style.display = 'none';
    }
  });

  document.getElementById('seeAll').addEventListener('click', function() {
    events.forEach(event => {
      event.style.display = 'block';
    });
  });
});
