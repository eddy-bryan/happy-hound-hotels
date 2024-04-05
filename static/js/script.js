// Get the current year
var currentYear = new Date().getFullYear();

// Update the text content of the span element with the current year
document.getElementById("currentYear").textContent = currentYear;


$(function() {
    $("#id_check_in_date").datepicker({
        minDate: 1,  // Minimum date is tomorrow
        onSelect: function(selectedDate) {
            // Parse the selected check-in date
            var checkInDate = new Date(selectedDate);
            
            // Calculate the minimum check-out date (check-in date + 1 days)
            var minCheckOutDate = new Date(checkInDate);
            minCheckOutDate.setDate(minCheckOutDate.getDate() + 1);
            
            // Update minDate option of check-out date picker
            $("#id_check_out_date").datepicker("option", "minDate", minCheckOutDate);
        }
    }).attr('readonly', 'readonly');
    
    $("#id_check_out_date").datepicker({
        minDate: 2  // Initial minimum date is 2 days from today
    }).attr('readonly', 'readonly');
});

$(function() {
    $("form").submit(function(event) {
        var checkInDate = $("#id_check_in_date").val();
        var checkOutDate = $("#id_check_out_date").val();

        if (!checkInDate) {
            event.preventDefault();
            $("#check-in-error").removeClass("d-none");
        }
        if (!checkOutDate) {
            event.preventDefault();
            $("#check-out-error").removeClass("d-none");
        }
    });
});
