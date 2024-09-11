//phone auth//
document.getElementById('phone').addEventListener('input', function() {
    const phoneInput = this;
    const phonePattern = /^[0-9]{11}$/;

    if (phoneInput.validity.patternMismatch) {
        phoneInput.setCustomValidity("Phone number must be exactly 11 digits.");
    } else {
        phoneInput.setCustomValidity(""); 
    }
});
//email auth//
document.getElementById('email').addEventListener('input', function() {
const emailInput = this;

if (emailInput.validity.typeMismatch) {
    emailInput.setCustomValidity("Please enter a valid email address.");
} else {
    emailInput.setCustomValidity(""); // Clears the custom message when valid
}
});
// date auth//

document.getElementById('date').addEventListener('input', function() {
const dateInput = this;
const datePattern = /^\d{1,2}\/\d{1,2}\/\d{4}$/;

if (!datePattern.test(dateInput.value)) {
    dateInput.setCustomValidity("Please enter a valid date in the format dd/mm/yyyy");
} else {
    dateInput.setCustomValidity(""); // Clears the custom message when valid
}
});