from django.test import SimpleTestCase
from django.urls import reverse
from .forms import SearchForm, BookingForm, ReviewForm


class StaticViewTests(SimpleTestCase):
    """
    Test suite for static views within the project.

    These tests focus on views that render static content or perform basic actions,
    such as displaying the home page or booking success page.
    """

    def test_home_view_reverse(self):
        """Test whether the home page URL resolves correctly."""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        """Test whether the home page uses the correct template."""
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "kennel_manager/index.html")

    def test_home_page_content(self):
        """Test whether the home page contains expected content."""
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Find a kennel...")
        self.assertNotContains(response, "Not on the page")

    def test_booking_success_view_reverse(self):
        """Test whether the booking success page URL resolves correctly."""
        response = self.client.get(reverse("booking_success"))
        self.assertEqual(response.status_code, 200)

    def test_booking_success_template(self):
        """Test whether the booking success page uses the correct template."""
        response = self.client.get(reverse("booking_success"))
        self.assertTemplateUsed(response, "kennel_manager/booking_success.html")

    def test_booking_success_content(self):
        """Test whether the booking success page contains expected content."""
        response = self.client.get(reverse("booking_success"))
        self.assertContains(response, "Booking Successful!")
        self.assertNotContains(response, "Not on the page")


class StaticFileTests(SimpleTestCase):
    """
    Test suite for static files.

    These tests ensure that static CSS and JavaScript files are accessible.
    """

    def test_css_file_access(self):
        """Test whether the CSS file is accessible."""
        response = self.client.get('/static/css/style.css')
        self.assertEqual(response.status_code, 200)

    def test_script_js_file_access(self):
        """Test whether the JavaScript file is accessible."""
        response = self.client.get('/static/js/script.js')
        self.assertEqual(response.status_code, 200)

    def test_reviews_js_file_access(self):
        """Test whether the reviews JavaScript file is accessible."""
        response = self.client.get('/static/js/reviews.js')
        self.assertEqual(response.status_code, 200)


class SearchFormTest(SimpleTestCase):
    """
    Test suite for the search form.

    These tests verify the behavior of the search form.
    """

    def test_search_form_fields(self):
        """Test whether the SearchForm has the expected fields."""
        form = SearchForm()
        self.assertTrue('check_in_date' in form.fields)
        self.assertTrue('check_out_date' in form.fields)
        self.assertTrue('num_pets' in form.fields)

    def test_search_form_required_fields(self):
        """Test whether the SearchForm validation fails for missing required fields."""
        form = SearchForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['check_in_date'], ['This field is required.'])
        self.assertEqual(form.errors['check_out_date'], ['This field is required.'])
        self.assertEqual(form.errors['num_pets'], ['This field is required.'])

    def test_search_form_valid(self):
        """Test whether the search form is valid with valid data."""
        form_data = {
            'check_in_date': '01/01/2023',
            'check_out_date': '03/01/2023',
            'num_pets': '2'
        }
        form = SearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_search_form_invalid(self):
        """Test whether the search form is invalid with invalid data."""
        form_data = {
            'check_in_date': '01/01/2023',
            'check_out_date': 'DD/MM/YYYY',
            'num_pets': '2'
        }
        form = SearchForm(data=form_data)
        self.assertFalse(form.is_valid())


class BookingFormTest(SimpleTestCase):
    """
    Test suite for the booking form.

    These tests verify the behavior of the booking form.
    """

    def test_booking_form_valid(self):
        """Test whether the booking form is valid with valid data."""
        form_data = {
            'check_in_date': '01/01/2023',
            'check_out_date': '03/01/2023',
            'num_pets': '2'
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_booking_form_invalid(self):
        """Test whether the booking form is invalid with invalid data."""
        form_data = {
            'check_in_date': '01/01/2023',
            'check_out_date': 'DD/MM/YYYY',
            'num_pets': '2'
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_booking_form_fields(self):
        """Test whether the BookingForm has the expected fields."""
        form = BookingForm()
        self.assertTrue('check_in_date' in form.fields)
        self.assertTrue('check_out_date' in form.fields)
        self.assertTrue('num_pets' in form.fields)

    def test_booking_form_required_fields(self):
        """Test whether the BookingForm validation fails for missing required fields."""
        form = BookingForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['check_in_date'], ['This field is required.'])
        self.assertEqual(form.errors['check_out_date'], ['This field is required.'])
        self.assertEqual(form.errors['num_pets'], ['This field is required.'])


class ReviewFormTest(SimpleTestCase):
    """
    Test suite for the review form.

    These tests verify the behavior of the review form.
    """

    def test_review_form_fields(self):
        """Test whether the ReviewForm has the expected fields."""
        form = ReviewForm()
        self.assertTrue('body' in form.fields)

    def test_review_form_required_fields(self):
        """Test whether the ReviewForm validation fails for missing required fields."""
        form = ReviewForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['body'], ['This field is required.'])

    def test_review_form_valid(self):
        """Test whether the review form is valid with valid data."""
        form_data = {
            'body': 'This is a review body'
        }
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_review_form_invalid(self):
        """Test whether the review form is invalid with invalid data."""
        form_data = {
            'body': ''
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(form.is_valid())
