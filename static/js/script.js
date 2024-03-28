$(function() {
    $("#id_check_in_date").datepicker({
        minDate: 1,  // Minimum date is tomorrow
        onSelect: function(selectedDate) {
            // Parse the selected check-in date
            var checkInDate = new Date(selectedDate);
            
            // Calculate the minimum check-out date (check-in date + 2 days)
            var minCheckOutDate = new Date(checkInDate);
            minCheckOutDate.setDate(minCheckOutDate.getDate() + 2);
            
            // Update minDate option of check-out date picker
            $("#id_check_out_date").datepicker("option", "minDate", minCheckOutDate);
        }
    });
    
    $("#id_check_out_date").datepicker({
        minDate: 2  // Initial minimum date is 2 days from today
    });
});
