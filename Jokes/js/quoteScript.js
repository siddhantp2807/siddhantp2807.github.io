const fetchData = async () => {
    const data = await fetch(`https://api.quotable.io/random`)
    const finalData =  data.json()
    return finalData
}

document.addEventListener('DOMContentLoaded', () => {

    // Get all "navbar-burger" elements
    const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {

        // Add a click event on each of them
        $navbarBurgers.forEach(el => {
            el.addEventListener('click', () => {

                // Get the target from the "data-target" attribute
                const target = el.dataset.target;
                const $target = document.getElementById(target);

                // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
                el.classList.toggle('is-active');
                $target.classList.toggle('is-active');

            });
        });
    }
    const quoteBox = document.querySelector('#quoteText');
    fetchData().then(res => {
        quoteBox.innerHTML = `${res.content}\n<strong>-${res.author}</strong>`;
    })
    const anotherQuote = document.querySelector('#anotherQuote');

    anotherQuote.addEventListener('click', () => {
        fetchData().then(res => {
            quoteBox.innerHTML = `${res.content}\n<strong>-${res.author}</strong>`;
            
        })
    })
});