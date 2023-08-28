document.addEventListener("DOMContentLoaded", function() {
  const events = document.querySelectorAll('.event');
  const seeAllButton = document.getElementById('seeAll');

  seeAllButton.addEventListener("click", function() {
    events.forEach(event => {
      event.classList.remove("hidden");
    });
    seeAllButton.style.display = 'none';
  });
});
