var formsetContainer = document.querySelectorAll('.formset-container'),
    formset_factura = document.querySelector('#formset-factura'),
    addFormsetButton = document.getElementById('add-formset'),
    totalForms = document.getElementById('id_form-TOTAL_FORMS'),
    formsetNum = formsetContainer.length - 1;

function addformset(e) {

    e.preventDefault()
    var newForm = formsetContainer[0].cloneNode(true),
        formRegex = RegExp(`form-(\\d){1}-`, `g`);
    formsetNum++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formsetNum}-`);

    formset_factura.insertBefore(newForm, addFormsetButton);
    totalForms.setAttribute('value', `${formsetNum + 1}`)

}
addFormsetButton.addEventListener('click', addformset)

// file formset
var fileformsetContainer = document.querySelectorAll('.file-formset-container'),
    file_formset_factura = document.querySelector('#file-formset-factura'),
    fileAddFormsetButton = document.getElementById('add-file-formset'),
    filetotalForms = document.getElementById('id_file-TOTAL_FORMS'),
    fileformsetNum = fileformsetContainer.length - 1;


function fileaddformset(e) {
    e.preventDefault()

    var newFileForm = fileformsetContainer[0].cloneNode(true),
        formRegex = RegExp(`file-(\\d){1}-`, `g`);
    fileformsetNum++
    newFileForm.innerHTML = newFileForm.innerHTML.replace(formRegex, `file-${fileformsetNum}-`);
    // console.log(newFileForm)
    file_formset_factura.insertBefore(newFileForm, fileAddFormsetButton)
    filetotalForms.setAttribute('value', `${fileformsetNum + 1}`)
}

fileAddFormsetButton.addEventListener('click', fileaddformset)

// Image formset
var imageformsetContainer = document.querySelectorAll('.image-formset-container'),
    image_formset_factura = document.querySelector('#image-formset-factura'),
    imageAddFormsetButton = document.getElementById('add-image-formset'),
    imagetotalForms = document.getElementById('id_image-TOTAL_FORMS'),
    imageformsetNum = imageformsetContainer.length - 1;

function imageaddformset(e) {
    e.preventDefault()
    console.log(imageformsetContainer)
    var newImageForm = imageformsetContainer[0].cloneNode(true),
        formRegex = RegExp(`image-(\\d){1}-`, `g`);
    imageformsetNum++
    newImageForm.innerHTML = newImageForm.innerHTML.replace(formRegex, `image-${imageformsetNum}-`);
    image_formset_factura.insertBefore(newImageForm, imageAddFormsetButton)
    imagetotalForms.setAttribute('value', `${imageformsetNum + 1}`)
}


imageAddFormsetButton.addEventListener('click', imageaddformset)
