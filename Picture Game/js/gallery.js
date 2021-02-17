

const getData = (query) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            fetch(`https://images-api.nasa.gov/search?q=${query}`).then(res => {
                resolve(res.json())
            })
            .catch(err => {
                reject({})
            })
        })
    })

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
    const ids = ['#one', '#two', '#three', '#four', '#five', '#six', '#seven', '#eight', '#nine', '#ten', '#eleven', '#twelve']
    const searchTerm = document.querySelector('#term');
    const submitButton = document.querySelector('#query');
    submitButton.addEventListener('click', () => {
        console.log(searchTerm.value);
        getData(searchTerm.value).then(res => {
            for (let i = 0; i < 12; i++) {
                if (res.collection.items[i]) {
                    document.querySelector(ids[i]).children[0].src = res.collection.items[i].links[0].href;
                    document.querySelector(ids[i]).classList.remove('is-hidden');
                    
                }
            }

        })
            .catch(err => {
                console.log(err)
            })
        
    })

    



});


