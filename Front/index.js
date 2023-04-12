document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('addWord').addEventListener('click', function () {
            console.log("test");
    });
    let addButton = document.getElementById('addWord');
    let inputContainer = document.getElementById('inputContainer');
    // Fonction qui crée et ajoute un nouvel input
    function addInput() {
        let divElement = document.createElement('div');
        divElement.className = 'input-group';
        let newInput = document.createElement('input');
        newInput.type = 'name';
        newInput.className = 'form-control word';
        newInput.placeholder = 'Mot à saisir';
        inputContainer.appendChild(divElement);
        divElement.appendChild(newInput);
    }
    // Ajout d'un écouteur d'événement pour le clic sur le bouton
    addButton.addEventListener('click', addInput);
    document.getElementById('contact_form').addEventListener('submit', function (e) {
        let words = document.getElementsByClassName('word');
        let optionsChecked = document.getElementsByClassName('option');
        e.preventDefault();
        $.ajax({
            url:' http://127.0.0.1:5000/api',
            type: 'GET',
            success: function (data) {
                console.log(data);
            },
            error: function (data) {
                console.log(data);
            }
        });
        console.log('ok');
    });

});
//.on('success.form.bv', function(e) {
//             console.log("ok")
//             $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
//             $('#contact_form').data('bootstrapValidator').resetForm();
//
//             // Prevent form submission
//             e.preventDefault();
//
//             // Get the form instance
//             var $form = $(e.target);
//
//             // Get the BootstrapValidator instance
//             var bv = $form.data('bootstrapValidator');
//
//             // Use Ajax to submit form data
//             $.post($form.attr('action'), $form.serialize(), function(result) {
//                 console.log(result);
//             }, 'json');
//         });
//
// });
