// "use strict"
//

// for link table
 let r_list = document.querySelectorAll('tbody tr')
 r_list.forEach((e) => {
            e.addEventListener('click', () => {
                window.document.location = e.dataset.href
            })
        })


