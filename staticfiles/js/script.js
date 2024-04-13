/**
 * Code to display current year for copyright tag within footer
 */
// Get the current year
var currentYear = new Date().getFullYear();

// Update the text content of the span element with the current year
document.getElementById("currentYear").textContent = currentYear;


// jQuery function to initialize datepicker for check-in and check-out dates
$(function() {
    // Initialize datepicker for check-in date
    $("#id_check_in_date").datepicker({
        minDate: 1,  // Minimum date is tomorrow
        dateFormat: 'dd/mm/yy', // Set the date format to UK format
        onSelect: function(selectedDate) {
            // Parse the selected check-in date
            var checkInDate = $.datepicker.parseDate("dd/mm/yy", selectedDate);
            
            // Calculate the minimum check-out date (check-in date + 1 days)
            var minCheckOutDate = new Date(checkInDate);
            minCheckOutDate.setDate(minCheckOutDate.getDate() + 1);
            
            // Update minDate option of check-out date picker
            $("#id_check_out_date").datepicker("option", "minDate", minCheckOutDate);
        }
    }).attr('readonly', 'readonly'); // Set input field to readonly mode
    
    // Initialize datepicker for check-out date
    $("#id_check_out_date").datepicker({
        minDate: 2,  // Initial minimum date is 2 days from today
        dateFormat: 'dd/mm/yy' // Set the date format to UK format
    }).attr('readonly', 'readonly'); // Set input field to readonly mode
});


// Event listener for search button click
$('#search').on('click', function(event) {
    // Get the input fields and error messages
    var checkInDateField = $('#id_check_in_date');
    var checkOutDateField = $('#id_check_out_date');
    var checkInError = $('#check-in-error');
    var checkOutError = $('#check-out-error');

    // Check if the check-in date is empty or equal to the placeholder text
    if ($.trim(checkInDateField.val()) === '' || $.trim(checkInDateField.val()) === checkInDateField.attr('placeholder')) {
        checkInError.addClass('d-block').removeClass('d-none');
        event.preventDefault(); // Prevent form submission
    } else {
        checkInError.removeClass('d-block').addClass('d-none');
    }

    // Check if the check-out date is empty or equal to the placeholder text
    if ($.trim(checkOutDateField.val()) === '' || $.trim(checkOutDateField.val()) === checkOutDateField.attr('placeholder')) {
        checkOutError.addClass('d-block').removeClass('d-none');
        event.preventDefault(); // Prevent form submission
    } else {
        checkOutError.removeClass('d-block').addClass('d-none');
    }
});
