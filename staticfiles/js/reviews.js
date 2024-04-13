// Get all edit buttons
const editButtons = document.getElementsByClassName('btn-edit');

// Get review text area and form submit button
const reviewText = document.getElementById("id_body");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");

// Get delete modal and all delete buttons
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

// Event listener for edit buttons
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        // Get the review ID from the clicked button's data attribute
        let reviewId = e.target.getAttribute("data-review_id");
        
        // Get the content of the review to be edited
        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        
        // Set the value of the review text area to the review content
        reviewText.value = reviewContent;
        
        // Change the text of the submit button to "Update"
        submitButton.innerText = "Update";
        
        // Set the action attribute of the review form to include the review ID for editing
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);
    });
}


// Event listener for delete buttons
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        // Get the review ID from the clicked button's data attribute
        let reviewId = e.target.getAttribute("data-review_id");
        
        // Set the href attribute of the delete confirmation link to include the review ID for deletion
        deleteConfirm.href = `delete_review/${reviewId}`;
        
        // Show the delete modal
        deleteModal.show();
    });
}
