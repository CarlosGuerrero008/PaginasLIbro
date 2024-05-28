document.addEventListener('DOMContentLoaded', function() {
    console.log('DOMContentLoaded event fired');
    let selectElement = document.getElementById('category-select');
    let titleElement = document.getElementById('selected-category');

    selectElement.addEventListener('change', function() {
        titleElement.textContent = this.value;
    });
});