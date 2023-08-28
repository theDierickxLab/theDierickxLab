document.addEventListener('DOMContentLoaded', function() {
    const seeAllButton = document.getElementById('seeAll');
    seeAllButton.addEventListener('click', function() {
        const galleries = document.querySelectorAll('.gallery');
        galleries.forEach(function(gallery) {
            gallery.style.display = (gallery.style.display === 'none' || gallery.style.display === '') ? 'block' : 'none';
        });
    });
});
