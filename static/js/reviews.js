const editButtons = document.getElementsByClassName('btn-edit');
const reviewText = document.getElementById("id_body");
const reviewRating = document.getElementById("id_rating");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");


console.log("reviews.js loaded successfully.")


for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("data-review_id");

        console.log(reviewId)
        console.log("Edit clicked")

        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        reviewText.value = reviewContent;
        reviewRating.value = reviewContent;
        submitButton.innerText = "Update";
        reviewForm.setAttribute("action", `edit_review/${reviewId}`);
    });
}
