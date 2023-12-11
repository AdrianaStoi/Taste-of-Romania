# Testing

## Table of contents

- [Testing](#testing)
  - [Table of contents](#table-of-contents)
  - [Browser Compatibility](#browser-compatibility)
  - [Lighthouse](#lighthouse)
  - [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [Javascript](#javascript)
    - [Python](#python)
  - [Manual Testing](#manual-testing)
    - [Home page Features](#Home-page-Features) 
    - [Register Login Logout and Reset password](#Register-login-logout-and-Reset-password)
    - [Products and Product information page](#Products-and-Product-information-page)
    - [Checkout](#Checkout)
    - [My Profile My inquiries and My Favorites pages](#My-Profile-My-inquiries-and-My-Favorites-pages)
    - [Product administration](#Product-administration) 
  - [User Story Testing](#user-story-testing)
  - [Testing Responsiveness](#testing-responsiveness)
   - [Responsiveness on devices](#responsiveness-on-devices)
  - [Bugs](#bugs)
    - [Fixed Bugs](#fixed-bugs)


## Browser Compatibility

* I tested the website on different browsers, including Google Chrome, Edge, and Mozilla. The site's functionalities are operating as intended, and the images are presented accurately.

* The layout and various features, such as buttons, the search bar, add to favorites/remove from favorites, comment form, inquiry form, add to cart, remove from cart, ordering process, and alerts, are all displayed correctly and functioning as expected. I created a new account and placed orders from all browsers without experiencing any errors. 

| Browser       | Layout rendered as expected | Features and buttons work as expected | Images work as expected |
| ------------- | --------------------------- | -------------------- | ------------------ |
| Google Chrome | Yes                         | Yes                  | Yes                |
| Edge          | Yes                         | Yes                  | Yes                |
| Mozilla       | Yes                         | Yes                  | Yes                |

## Lighthouse

* I tested performance, accessibility, best practice, and SEO using Lighthouse accessed via DevTools and here are the results:

![Lighoutse-Taste of Romania](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/lighthouse_report_taste_of_romania.png)


[Back to table of contents](#table-of-contents)


## Code Validation

### HTML

I passed all html pages through the [W3C](https://validator.w3.org/) official validator. These are the results:

| Page       | Result|
| ---------- | ----- |
| Home page  | Pass |
| Products - All products | Refer to notes below |
| Products - Sort by price   | Pass |
| Products – Sorting by category | Pass |
| Products - Products by categories  | Pass |
| Search results | Pass |
| Product information page  | Pass |
| Edit comment page  | Pass |
| Delete comment page  | Pass |
| Product administration – Add product  | Refer to notes below |
| Product administration – Edit product   | Refer to notes below |
| My profile page  | Pass |
| My Inquiries page   | Pass |
| My Inquiry page  | Pass |
| My Favorites page  | Pass |
| Shopping cart empty  | Pass |
| Shopping cart page | Refer to notes below |
| Login page  | Pass |
| Logout page  | Pass |
| Register page  | Pass |
| Forgot Password page  | Pass |
| Password Reset change page  | Pass |
| Reset Done page  | Pass |
| Custom Error pages | Pass |

__Products page__

* Error received for the “login-modal” id. For the favorite icon, when the users are not logged in they have a pop-up modal that appears. I used JavaScript to show and close modal, however I used “getElementById” which rendered an error in the HTML validator as this applies to all products. 
* I have changed the “login-modal” to class and changed the JavaScript accordingly. The error is no longer displayed. 

![Products page error](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/products_page_modal.png)

![Products page solved](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/products_page_modal_solved.png)

__Product administration – Add product and Edit product__

* Error received for duplicate ID. 

![Product administration – Add product](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/html_validator_product_administration.png)

<details>

<summary>Product administration – Edit product duplicate ID</summary>

![Product administration – Edit product error](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/edit_product_product_admin.png)

</details>

* The first ID was “id="new-image"”, and second ID was coming from the {% include "django/forms/widgets/attrs.html" %} which includes an ID, but I cannot access it (see image below). 

![Double id screenshot-id="id_image](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/html_validator_admin_double_id.png)

* I fixed this issue by removing the {% include "django/forms/widgets/attrs.html" %}. I have added the attribute [“accept=image/*”](https://www.w3schools.com/tags/att_input_accept.asp)

* The error is no longer being displayed for “Add product” and “Edit a product”. 

![Add product - solved](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/html_validator_add_product_admin_solved.png)

![Edit a product - solved](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/html_validator_edit_product_admin.png)


__Shopping cart page__

* I encountered an error indicating a duplicate ID on the shopping cart page, which was also highlighted in the "boutique_ado" walkthrough. To resolve this issue, I modified the ID to a class and adjusted the JavaScript to target the class element. As a result, the error is no longer present.

![Shopping cart id error](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/html_validator_shopping_cart_error_id.png)

![Shopping cart solved](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/html_validator_shopping_cart_solved.png)

[Back to table of contents](#table-of-contents)


### CSS

The base.css and checkout.css files successfully passed through the [Jigsaw](https://jigsaw.w3.org/css-validator/) official validator without any errors being detected.
Each file triggered only a single warning. The base.css file received a warning related to the imported Google fonts, while the checkout.css warning pointed to the use of the " -webkit-transition" as a vendor extension.

__Base.css__

![Base css](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/css_validator_base_css.png)

![Base css warning](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/css_validator_base_css_warning.png)

__Checkout__

![Checkout](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/css_validator_checkout_css.png)

![Checkout warning](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/css_validator_checkout_css_warning.png)


### Javascript

No errors were found for JS when passing through the official [Jshin](https://jshint.com/) validator.

__Shopping Cart__

![Cart app jshint](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/jshint_cart_page_no_errors.png)
![Cart Quantity_form jshint](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/jshint_validator_quantity_form.png)

__Products__

![Products page jshint](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/jshint_products_page_no_errors.png)

__My Profile__

![Profile page jshint](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/jshint_profile_page.png)

__Product Administration - Add products__

![Add_product jshint](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/jshint_add_product_no_errors.png)

### Python

* All python files form all apps were successfully passed through the [PEP8]( https://pep8ci.herokuapp.com/#) official validator. Long lines were present in many files. These lines were shortened and resubmitted to the validator without any errors being detected.
* The only file containing a message is the "settings.py" for the "AUTH_PASSWORD_VALIDATORS". This is auto-generated by Django.

<details>

<summary>Taste of Romania - Settings.py</summary>

![Settings.py](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/pep_settings_py.png)

</details>

Below are the results for views.py in all apps: 

__Home - views.py__

![Home - views.py](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/pep_validator_home_views_py.png)

__Products - views.py__

![Products - views.py](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/pep_validator_products_views_py.png)

__Cart app - views.py__

![Cart app](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/pep_validator_cart_views.png)

__Checkout - views.py__

![Checkout](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/pep_validator_checkout_views_py.png)

__My Favorites - views.py__

![My Favorites - views.py](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/pep_validator_favorites_views_py.png)

__My inquiries - views.py__

![My inquiries - views.py](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/pep_validator_inquiries_py.png)

__My profile - views.py__

![My profile - views.py](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/pep_validator_profiles_views_py.png)


[Back to table of contents](#table-of-contents)

## Manual Testing 

* I have thoroughly tested all functions and features, confirming their proper functionality as expected.

### Home page Features 

|     Feature       |        Expectation          |        Action        |       Outcome      |
| ----------------- | --------------------------- | -------------------- | ------------------ |
| Logo name (upper left corner)| When clicked should bring back to Home page.| Click | When clicked it leads to Home page. ![Navbar](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar.png)|
| My Account icon (upper right corner) |When clicking on it, a dropdown should be displayed with the options “Login” and “Register”. Users who logged in should see “My Profile”, My Inquiries” and “Logout”. The admin should additionally see “Product Administration. | Click | When clicking on it, a dropdown is displayed with the options “Login” and “Register”. ![Navbar-guest user](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar_myaccount_unregistered.png) Users who logged in see “My Profile”, My Inquiries” and “Logout”. ![Navbar-logged in user](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar_loggedin_regular_user.png) The admin can also see “Product Administration. ![Navbar-admin](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/myaccount_signed_in_admin.png) |
|My Favorites icon (upper right corner)  | When clicking on it, users should be directed to Favorites page. | Click | When clicking on it, users are directed to Favorites page. |
|Shopping cart icon (upper right corner) | When clicked it should lead to the Shopping cart page. | Click | When clicked, it leads to Shopping cart page. |
|Search bar function  | When entering product names or entering a word that is included in the product description, the user should be redirected to an results page with the corresponding products, if any products are found. Otherwise , there should be a message stating “0  products found” | Enter query | When entering product names or entering a word that is included in the product description, the user should be redirected to a results page with the corresponding products, if any products are found. Otherwise, there should be a message stating “0  products found”. ![Search results](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/search_results.png)|
| All products dropdown menu | When clicking on “All products”, and then on any of the three options “By Price”, “By Category” and “All products” users should be directed to the corresponding page with products sorted accordingly. | Click | When clicking on “All products”, and then on any of the three options “By Price”, “By Category” and “All products” users are directed to the corresponding page with products sorted accordingly.![All products menu](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar_menu_categorization.png) |
|Romanian specialties dropdown menu  | When clicking on “Romanian specialties”, and then on any of the options “Cheese”, “Meat Products”, “Sweets”, “Snacks” etc. users should be directed to the corresponding page with products sorted accordingly. | Click | When clicking on “Romanian specialties”, and then on any of the options “Cheese”, “Meat Products”, “Sweets”, “Snacks” etc. users are directed to the corresponding page with products sorted accordingly. |
|Drinks link | When clicking on “Drinks” users should be directed to the corresponding “Drinks” page. | Click | When clicking on “Drinks” users are directed to the corresponding “Drinks” page. |
|Artisanal products dropdown menu | When clicking on “Artisanal products”, and then on any of the options “Traditional clothing”, “Handmade pottery”, “Handmade bracelet”, or “All Artisanal products” etc. users should be directed to the corresponding page with products sorted accordingly. | Click | When clicking on “Artisanal products”, and then on any of the options “Traditional clothing”, “Handmade pottery”, “Handmade bracelet”, or “All Artisanal products” etc. users are directed to the corresponding page with products sorted accordingly. |
|See all products button | When clicked, it should direct to the Product page. | Click | When clicked, it directs to the Product page. |
|Choose a Category section with links “Sweet and Savory”, “Alcoholic Drinks”, “Clothing and Handmade pottery” | When clicking on each of the three categories, users should be directed to the Products page displaying the respective products. | Click | When clicking on each of the three categories, users are directed to the Products page displaying the respective products. |
| Privacy Policy link | When clicked, it should open Privacy policy page on a new tab. | Click | When clicked, it opens Privacy policy page on a new tab. ![Privacy Policy](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/privacy_policy.png) |
| Subscribe to newsletter | When a user enters their email address, a confirmation message should be displayed, indicating “Thank you for subscribing!” | Enter data | When a user enters their email address, a confirmation message is displayed, indicating “Thank you for subscribing!” ![Subscribe newsletter](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/subscribe_newsletter_submitted.png) |
| Footer - Social media icons Facebook and Instagram | When clicking on Facebook and Instagram, they should redirect to the corresponding site by opening in a new tab. | Click | When clicking on Facebook and Instagram, they redirect to the corresponding site by opening in a new tab. |

[Back to table of contents](#table-of-contents)


### Register Login Logout and Reset password

|     Feature       |        Expectation          |        Action        |       Outcome      |
| ----------------- | --------------------------- | -------------------- | ------------------ |
|Register navigation link (upper right corner under My Account)  | When clicked it should lead to the “Register” page. | Click and redirection to Register page | When clicked it directs to “Register” page. |
|  | To register the user should have “Email”, “Username” and “Password” as mandatory fields.  | Enter data | "Email",“Username” and “Password are mandatory fields.  |
|  | The conditions indicated must be met to create a password.| Enter data | If the conditions are not met the account is not created, the user . |
|  | After entering the data, the user should be directed to the page “Verify your email address” which states a link has been sent to finish the signup process. | Email Verification | Once registered, the user is directed to the “Verify your email address” which states a link has been sent to finish the signup process ![Verify email page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/verify_email_page.png) |
|  | Once the user clicks on the link, he should be redirected to the confirmation page. | Click | Once the user clicks on the link, he is redirected to the confirmation page. When they click on confirm, they can then login to their account. ![Confirm email page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/email_confirm_page.png) |
| Login | After entering their valid credentials and clicking the Login button, the user should be logged in. They should see a green alert message at the top of the page. Their username should be displayed in the top-right corner. If user enters wrong username or password, they should be prompted with the message” The username and/or password you specified are not correct.” | Click | After entering their credentials and clicking the “Login” button, the user is logged in. The green alert is displayed. The username is displayed in the top-right  corner. ![Navbar logged in user](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/logged_in_user.png)|
|  | If user enters wrong username or password, they should be prompted with the message” The username and/or password you specified are not correct.” | Type valid data | If user enters wrong username or password, they are prompted with the message ”The username and/or password you specified are not correct.” ![Login wrong credentials](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/login_incorrect_password.png)|
| Logout (upper right corner) | To logout, the user should click on “Logout”. They should be redirected to the “Log Out” page. When clicking on “Log Out” they should be redirected to the “Home” page. | Click | When clicking on Logout, the user is redirected to the “Log Out” page. When clicking on “Log Out”  to confirm the action, they are redirected to the “Home” page. |
|Reset password | Users should be able to reset their passwords by clicking on “Forgot Password” available on the login page. A link should be sent to their email to reset their password.  | Click and Enter data | Users can  reset their password by clicking on “Forgot Password” available on the login page. ![Reset password](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/password_reset_page.png) A link is sent to their email to reset their password. ![Password reset link ](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/password_reset_sent.png) When clicking on the link, the user is directed to “Change password page. ![Change password page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/change_password_page.png) Once they enter their new password, they are directed to the confirmation page. ![Password Changed](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/password_reset_done.png)|

[Back to table of contents](#table-of-contents)


### Products and Product information page 

|     Feature       |        Expectation          |        Action        |       Outcome      |
| ----------------- | --------------------------- | -------------------- | ------------------ |
|Product items on Product page page  | On the products page, users should see each product along with its corresponding image. Below the image, there is brief information about the product, including the product name, price, product category with a tag icon, a heart icon to add to favorites, and a “See Product” button. Clicking on the product category name should direct the user to the corresponding page displaying products from that category. The “See Product” button should direct to the “Product Information” page. Additionally, when users click on the product image, they should be directed to the “Product Information” page. | Click | On the products page, users see each product along with its corresponding image. Below the image, there is brief information about the product, including the product name, price, product category with a tag icon, a heart icon to add to favorites, and a “See Product” button. ![Products page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/products_page.png) Clicking on the product category name directs the user to the corresponding page displaying products from that category. The “See Product” button directs to the “Product Information” page. Additionally, when users click on the product image, they are directed to the “Product Information” page. ![Product information page ](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/products_page_clothing.png) |
| Products Home button | In the upper left corner, users should be able to click on 'Product Home,' which should direct them to the main Products page displaying all products. This button is available also on “Product information” page and “My favorites page” | Click | In the upper left corner, users can click on 'Product Home,' which directs them to the main Products page displaying all products. The buttons works on all pages it is present. |
| Sort by dropdown menu | When clicking on the “Sort by” drop-down menu, users should see options to sort products by price, category name, or by name. Clicking on each of these options should sort the products on the page accordingly. | Click | When clicking on the “Sort by” drop-down menu, users see options to sort products by price, category name, or by name. Clicking on each of these options sort the products on the page accordingly. ![Sort by](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/products_sortby.png)|
| Quantity increase/decrease buttons on Product Information page | Quantity increase/decrease buttons from the Product Information page should enable users to increase or decrease the product quantity. The default displayed quantity should be 1. | Click | Quantity increase/decrease buttons from the Product Information page enables the user to adjust the product quantity. The default displayed quantity should be 1. ![Quantity increase/decrease](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/quantity_default.png)|
| Continue Shopping button | Under the quantity, the user should find the “Continue shopping” button which should direct to the “Products” page. | Click | Under the quantity, the user finds the “Continue shopping” button which directs them to the “Products” page. |
| Add to cart | When clicking on add to cart button, the product should be added to the cart. A success message for adding to cart should be visible in the upper right corner along with the cart summary. | Click | When clicking on add to cart button, the product is added to the cart. A success message for adding to cart is visible in the upper right corner along with the cart summary. ![Shopping cart](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/shopping_cart.png) |
| Reviews section- Submit comment form | When users are logged in, they should see a “Leave a Comment” form beneath the product details on the right side. After submitting the form, the comment should be displayed on the left side. | Enter data and submit | When users are logged in, they see a “Leave a Comment” form beneath the product details on the right side. After submitting the form, the comment being displayed on the left side. ![Review - comment](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/reviews_comment_loggedin_user.png) |
|  | Guest users should only read comments and should not have accesss to add, edit or delete other users comments. | View | Guest users can only read comments and they do not have accesss to add, edit or delete other users comments. ![Read review](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/reviews_view.png) |
| Edit comment – logged in user | Logged in users should be able to edit their own comments. When editing the comment, the user is redirected to a new page where they can make the necessary changes. After editing, they are redirected to the previous page and they are be prompted with a success message alert.| Edit | Logged in users can edit their own comments. When editing the comment, the user is redirected to a new page where they can make the necessary changes. ![Edit comment ](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/comment_edit.png) After editing, they are redirected to the previous page, and they are be prompted with a success message alert. |
| Delete comment – logged in user | Logged in users should be able to delete their own comments. When deleting a comment, the user should be prompted with a confirmation message to confirm the deletion. After confirming, the comment should be deleted. They are redirected to the previous page and they are prompted with a success message alert. | Delete | Logged in users can delete their own comments. When deleting a comment, the user is prompted with a confirmation message to confirm the deletion. ![Delete comment ](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/comment_deletion.png) After confirming, the comment will be deleted. They are redirected to the previous page and they are prompted with a success message alert. |

[Back to table of contents](#table-of-contents)

### Checkout

|     Feature       |        Expectation          |        Action        |       Outcome      |
| ----------------- | --------------------------- | -------------------- | ------------------ |
|Secure checkout button – summary view shopping cart (guest user and logged in user) | After adding a product to the cart, a notification message containing a summary of items and their prices, as well as a "Secure Checkout" button, should appear in the upper right corner. Clicking on the "Secure Checkout" button should redirect the user to the "Checkout" page to finalize the order. | Click | After adding a product to the cart, a notification message containing a summary of items and their prices, as well as a "Secure Checkout" button, appears in the upper right corner. Clicking on the "Secure Checkout" button redirects the user to the "Checkout" page to finalize the order. |
| Shopping cart page - Secure checkout button | When clicking on “Secure checkout” on the “Shopping cart”, the user should be directed to the “Checkout” page. | Click | When clicking on “Secure checkout” on the “Shopping cart”, the user is directed to the “Checkout” page. ![Shopping cart page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/shopping_cart_page.png)|
| Quantity increase/decrease buttons on Shopping cart page  | Quantity increase/decrease buttons from the Shopping cart page should enable users to increase or decrease the product quantity. The default displayed quantity should be 1.  | Click | Quantity increase/decrease buttons from the Shopping cart page enables the user to adjust the product quantity. The default displayed quantity should be 1. ![Quantity increase/decrease](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/quantity_default.png) |
| Update/Remove links on shopping cart page| Clicking on the "Update" button should result in the product quantity being updated, accompanied by a success message alert in the upper right corner. The adjusted quantity should be reflected under "Qty." When clicking on "Remove," the product should be deleted, and a success message should appear in the upper right corner.| Click | Clicking on the "Update" button results in the product quantity being updated, accompanied by a success message alert in the upper right corner. The adjusted quantity is reflected under "Qty." When clicking on "Remove," the product is deleted, and a success message appears in the upper right corner.|
| Continue Shopping button | Under the quantity, the user should find the “Continue shopping” button which should direct to the “Products” page. | Click | Under the quantity, the user finds the “Continue shopping” button which directs them to the “Products” page. |
| Checkout form | Users should be able to input data into each checkout form field. Mandatory fields must feature a placeholder denoted by “*”. In case a user enters an invalid card number, an error message should promptly appear. The submission of the order should be restricted until valid data is provided in all the required fields. | Enter data | Users can input data into each checkout form field. Mandatory fields must feature a placeholder denoted by “*”. In case a user enters an invalid card number, an error message appears promptly. The submission of the order is restricted until valid data is provided in all the required fields. ![Checkout page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/checkout_page.png) |
| Adjust cart button | Clicking on "Adjust Cart" should navigate back to the shopping cart page. | Click | Clicking on "Adjust Cart" navigates back to the shopping cart page. |
| Complete order button (Guest or logged in user) | Upon clicking "Complete Order" after entering the necessary details, users should be redirected to the "Thank You for Your Order" page, accompanied by a success message displayed in the upper right corner. | Click | Upon clicking "Complete Order" after entering the necessary details, users are redirected to the "Thank You for Your Order" page, accompanied by a success message displayed in the upper right corner. ![Thank You for Your Order page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/order_confirmation.png) |
| Thank You for Your Order page -  Browser our products button | At the bottom of the "Thank You for Your Order" page, a "Browse Our Products" button should be present. Clicking on this button should redirect the user back to the main products page. | Click | At the bottom of the "Thank You for Your Order" page, a "Browse Our Products" button is present. Clicking on this button redirects the user back to the main products page. |

[Back to table of contents](#table-of-contents)


### My Profile My inquiries and My Favorites pages 

|     Feature       |        Expectation          |        Action        |       Outcome      |
| ----------------- | --------------------------- | -------------------- | ------------------ |
| Default delivery information – form | On the "My Profile" page, users should find their saved delivery information displayed on the left side. They should be able to modify existing data and input new information as required. | Enter data | On the "My Profile" page, users find their saved delivery information displayed on the left side. They can modify existing data and input new information as required. ![My profile page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/myprofile_page.png)|
| My Profile - Update information button | On  "My Profile" page, at the bottom of the "Default Delivery Information," users should find the "Update Information" button. Clicking on this button should allow the user to update their information accordingly. | Click | On "My Profile" page, at the bottom of the "Default Delivery Information," users can find the "Update Information" button. Clicking on this button allows the user to update their information accordingly. |
| Order history – Order number link | On the right side of the "Default Delivery Information," users should find the order history, listing all their previous orders. Clicking on the order number should redirect the user to the corresponding Order Confirmation page, where they can view detailed order information. | Click | On the right side of the "Default Delivery Information," users can find the order history, listing all their previous orders. Clicking on the order number redirects the user to the corresponding Order Confirmation page, where they can view detailed order information. |
| Back to profile | When navigating to the order confirmation page from the "Order History," at the bottom of the confirmation page, a "Back to Profile" button should be displayed. Clicking on this button should redirect the user back to their profile. | Click | When navigating to the order confirmation page from the "Order History," at the bottom of the confirmation page, a "Back to Profile" button should be displayed. Clicking on this button redirects the user back to their profile. ![Order confirmation profile page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/order_confirmation_profile.png) |
| My inquiries page – New inquiry form | On the Inquiries page, users should find a form on the left side, allowing them to input data into each form field. Mandatory fields must include a placeholder marked by “*”. The submission of the inquiry should be restricted until valid data is provided in all the required fields. | Enter data | On the Inquiries page, users can find a form on the left side, allowing them to input data into each form field. Mandatory fields must include a placeholder marked by “*”. The submission of the inquiry are restricted until valid data is provided in all the required fields. ![My inquiries page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_inquiries_page.png) |
| Submit button | Upon clicking "Submit" after entering the necessary details, users should be redirected to the "Request number" page, accompanied by a success message displayed in the upper right corner. | Click | Upon clicking "Submit" after entering the necessary details, users are redirected to the "Request number" page, accompanied by a success message displayed in the upper right corner. |
| Inquiry History list – Request number link | On the "My Inquiries" page, users should view their Inquiry History on the right side. Clicking on the Request number should redirect the user to the corresponding request, providing access to detailed information. | Click | On the "My Inquiries" page, users can view their Inquiry History on the right side. Clicking on the Request number redirects the user to the corresponding request, providing access to detailed information. |
| My inquiry page – Reply form  | On the "My Inquiry" page, beneath the request details, users should find a "Reply" text box. The user should be prevented from submitting an empty "Reply." | Input data  | On the "My Inquiry" page, beneath the request details, users can find a "Reply" text box. The user cannot submit an empty "Reply." They are prompted with an error message indicating to fill out the field. ![My inquiry page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_inquiry_details.png) |
| Reply request button | Upon clicking the "Reply Request" button, the user's reply should be added to the request details section. A success message alert should be displayed in the upper right corner. Additionally, a new line labeled "Your Replies" should be presented under the Message section in the request details. | Click | Upon clicking the "Reply Request" button, the user's reply is added to the request details section. A success message alert is displayed in the upper right corner. A new line labeled "Your Replies" is presented under the Message section in the request details. |
| Delete request button | At the bottom of the request page, users should find the "Delete Request" button. Clicking on it should direct the user to the "Confirm Deletion" page. If deletion is confirmed, the request should be removed, and a success message alert should be displayed in the upper right corner. | Click | At the bottom of the request page, users can find the "Delete Request" button. Clicking on it directs the user to the "Confirm Deletion" page. If deletion is confirmed by the user, the request is removed, and a success message alert is displayed in the upper right corner. |
| Back to my inquiries button | In the upper right corner of the "My Inquiry" page, users should find the "Back to My Inquiries" button. Clicking on this button should redirect the user to the "My Inquiries" page. | Click | In the upper right corner of the "My Inquiry" page, users find the "Back to My Inquiries" button. Clicking on this button redirects the user to the "My Inquiries" page. |
| Add to favorites/Remove from favorites function - Heart icon (Logged in user) | Users should be able to add products to favorites and remove products from favorites by clicking on the heart icon, which should be visible on all products, whether on the Products page or the product information page. The regular heart icon should indicate that the product is not added to favorites, while the solid heart should indicate that the product is added to favorites. Added products should be listed in the "My Favorites" page. | Click | Users can add products to favorites and remove products from favorites by clicking on the heart icon, which is being visible on all products, whether on the Products page or the product information page. The regular heart icon indicates that the product is not added to favorites, while the solid heart indicates that the product is added to favorites. Added products are listed in the "My Favorites" page. ![Favorites product information](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_existing_prod_info.png) ![Favorites products](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/favorites_products.png) |
|Add to favorites - Heart icon (Guest User) | When guest users click on the heart icon, they should be prompted with a message indicating that they must be log in or register to add the product to favorites. | Click | When guest users click on the heart icon, they are  prompted with a message indicating that they must be log in or register to add the product to favorites. ![Favorites - guest users ](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_guest_users_popup_message.png) |
| Remove from favorites -  Trash can icon  | All products added to favorites should be visible on the "My Favorites" page. A trash icon should be displayed under each product name. Clicking on the trash icon should remove the product from the favorites page and trigger an alert displayed in the upper right corner. | Click | All products added to favorites are visible on the "My Favorites" page. A trash icon is displayed under each product name. Clicking on the trash icon removes the product from the favorites page and triggers an alert displayed in the upper right corner. ![Favorites page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_products.png) ![Favorites removed](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_removed.png)|

[Back to table of contents](#table-of-contents)

### Product administration


|     Feature       |        Expectation          |        Action        |       Outcome      |
| ----------------- | --------------------------- | -------------------- | ------------------ |
| Product administration - Add product form  | The admin should access the “Add Product” form from “Product Administration”, which should be available in the dropdown menu displayed when clicking on the user icon in the upper right corner.Admins should have the capability to add a product from the frontend by completing the form. The “Category “and “Has Sizes” fields should be presented as dropdowns, allowing the admin to conveniently select existing options. Mandatory fields must include a placeholder marked by “*”. The submission of the inquiry should be restricted until valid data is provided in all the required fields. | Input data | The admin can access the “Add Product” form from “Product Administration”, which is available in the dropdown menu displayed when clicking on the user icon in the upper right corner. Admins can add a product from the frontend by completing the form. The “Category” and “Has Sizes “fields are presented as dropdowns, allowing the admin to conveniently select existing options. Mandatory fields must include a placeholder marked by “*”. The submission of the inquiry restricted until valid data is provided in all the required fields. ![Admin add product](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/add_product_admin.png) ![Admin add product form](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/add_product_admin_form.png)|
| Select image button (on Add product and Edit product)  | When the admin clicks on the “Select Image'” button, they should be able to choose and upload an image. Upon selecting the image, a notification should appear below the button stating “Image will be set to:...” | Click | When the admin clicks on the “Select Image'” button, they are able to choose and upload an image. Upon selecting the image, a notification appears below the button stating “Image will be set to:...”  ![Select image](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/select_image_admin.png)|
| Cancel button (on Add product and Edit product page) | When clicking on “Cancel” button, the admin should be redirected back to “Products” page. | Click | When clicking on “Cancel” button, the admin is redirected back to “Products” page. |
| Add Product button  | When clicking on “Add Product”, the admin should be directed to the Product Information page for the product they just added. | Click | When the admin clicks on “Add Product”, they are redirected to the Product Information page for the product they just added. |
| Edit product | The edit link should be displayed either on the Products page on all products and on the Product details page of the respective product when the admin is logged in on the site. When logged in, they will see the “Edit” option displayed under the category tag. Admins should have the capability to edit a product from the frontend by adjusting the existing form. The “Category “and “Has Sizes” fields should be presented as dropdowns, allowing the admin to conveniently select existing options. At the bottom of the form, the “Current image” should be displayed. The admin should have a checkbox to “Remove” the existing image. If this box is checked and the form submitted, the image should be removed. Mandatory fields must include a placeholder marked by " * ". The submission of the inquiry should be restricted until valid data is provided in all the required fields.| Input data | Administrators can edit a product either from the Products page or the Product information page. When logged in, they will see the “Edit” option displayed under the category tag. ![Edit product - products page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/products_edit_product_admin.png) ![Edit product - product details page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/product_info_edit_product_admin.png) Admins can add a product from the frontend by completing the form. The “Category” and “Has Sizes “fields are presented as dropdowns, allowing the admin to conveniently select existing options. At the bottom of the form, the “Current image” is displayed. The admin has a checkbox to “Remove” the existing image. If this box is checked and the form submitted, the image is removed. ![Edit product - current image](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/select_image_admin.png) Mandatory fields must include a placeholder marked by “*”. The submission of the inquiry restricted until valid data is provided in all the required fields. |
| Update Product button | When clicking on “Edit Product”, the admin should be directed to the Product Information page for the product they just edited. | Click | When the admin clicks on “Edit Product”, they are redirected to the Product Information page for the product they just edited. |
| Delete product  | The delete link should be displayed either on the Products page on all products and on the Product details page of the respective product when the admin is logged in on the site. When logged in, they should see the “Delete” option displayed under the category tag. Upon clicking on “Delete” the admin should be redirected to the confirmation deletion page. If confirmed, the product should be deleted, and a success message alert should be displayed in the upper right corner. | Click | Administrators can delete a product either from the Products page or the Product information page. When logged in, they see the “Delete” option displayed under the category tag. Upon clicking on “Delete” the admin is redirected to the confirmation deletion page. ![Delete product-confirm deletion](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/confirm_deletion_product_admin.png) If confirmed, the product is deleted, and a success message alert is displayed in the upper right corner. |

[Back to table of contents](#table-of-contents)


## User story Testing

__EPIC: Back-end Store Administration__

_1.	As store owner, I can access an admin panel where I can view users, edit, delete, products, categories, orders, comments, and ratings and filter in the sections so that I can efficiently manage the store._

* The admin can access the admin panel in the backend. In the Admin panel, he can view users, comments, and articles. He can filter each section accordingly.

__EPIC: Store viewing and navigation__

_2.	As a site user I want to be able to easily navigate on the site so that I can find the products available._

* The users can easily navigate from page to page using the navigation bar and menu.  

* In the left corner, there is the logo site image. When clicking on the logo, the users are directed to the Home page. Then there is the “Search bar” which is used for quick searches on the site without having to browse the products.

* At the top of the page in the upper right corner, under “My Account”, they can Register/Login. When logged in the users have the options to navigate to “My Profile”, “My Inquiries”, and “Logout”.

* Next to “My Account”, the user can navigate to “My Favorites” page and lastly there is the Shopping cart.

![Navbar](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar_myaccount_unregistered.png)


* Under this section there is the navigation menu allowing users to access all products or to access them by different categories.  

![Navbar-categorization](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar_menu_categorization.png)

_3.	As a shopper I want to be able to view a list of products so that I can select the products I would like to purchase._

* The user can view all products, from the “See products” button on the landing image on home page, or from the navigation by Selecting “All products”.

![Landing image](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/landing_image.png)

![Navbar-categorization](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar_menu_categorization.png)

_4.	As a shopper I want to be able to view details of a product so that I can check the price, description, ingredients, comment, rating before buying._

* The shoppers can view product details by clicking on the product image or “See product” button available on the “Product” page. 

![Product information](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/product_info_page.png)

__EPIC: User Login/Registration and Profile__

_5.	As a frequent site user, I can register on the site, so I can have an account to place an order, keep an order history and provide feedback on the products._

* The user can register on the site by clicking on “My Account” in the upper right corner. A drop-down menu will be displayed, and they can then select “Register”.
After entering the required details, they will be directed to the "Verify your e-mail" page, indicating they will recieve an email with the link to finalize the signup process.

![Navbar](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar_myaccount_unregistered.png)

![Register page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/register_page.png)

![Verify email page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/verify_email_page.png)


_6.	As a frequent site user, I want to be able to login or logout so that I can access my account information._

* Users can log in and log out from their accounts by clicking on “My Account” and choosing the respective actions: “Login” or “Logout.”

![Login](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/login_page.png)

![Logout](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/confirm_logout.png)


_7.	As a frequent site user, I want to be able to recover my password in case I forget it so that I can recover my access account._

* Users can recover their password by clicking on “Forgot password”. They will receive an email with a link to confirm the account. Once the user clicks on the link, they are directed to a confirmation page. 

| Reset      |       |
| ---------- | ----- |
| ![Password Reset Page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/password_reset_page.png) | ![Password reset sent](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/password_reset_sent.png)|
|       |       |
| ![Change password](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/change_password_page.png) | ![Reset Done](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/password_reset_done.png) | 

[Back to table of contents](#table-of-contents)

_8.	As a registered user, I want to be able to access my user profile page, so that I can save my details for next purchases and view my orders._

* Users can access their profile page from the dropdown menu under My Account icon.

![My Profile](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/myprofile_page.png)

_9.	As a site user I want to be able to add the products to "Favorites" so that I can save the product in the profile and purchase it later._

* Users can add products to their favorites from either the "Products" page or the "Product Information" page by clicking on the heart icon. 

* When users add a product to their favorites, they are directed to the "My Favorites" page. If they return to the product page, they can see that the heart icon is solid, indicating that the product has already been added to favorites. Users can also remove a product from their favorites either on the "Favorites" page or by clicking on the solid heart icon on the "Product" or "Product Information" page.

__Favorites products page__

![Favorites products page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_existing_prod_products_page.png)

__Favorites Product information page__

![Favorites Product information page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_existing_prod_info.png)

__Favorites page__

![Favorites page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_product_added.png)


_10.	As a shopper I want to be able to submit an inquiry so that I can ask about my order status or inquiry about products on the site._

* Logged in users can create an inquiry, by clicking on account icon in the upper right corner which opens a drop-down menu and the user can select “My Inquiries”.
* The user can fill out the form and submit the request. They can see an update from Taste of Romania directly in the request and they can also send a “Reply” and ask for updates. 

__My inquiries access__
![My inquiries](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar_loggedin_regular_user.png)

__My inquiries page__
![My inquiries page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_inquiries_page.png)

__My inquiry page__

![My inquiry details](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_inquiry_details.png)

__EPIC: Product Categorization and Searching__

_11.	As a shopper I want to be able to search for a product by name or description so that I can find the product I want to purchase._

* Users can search for products using the Search bar located at the top of the page. The search bar is available on all pages. 
* On smaller devices the user can access the bar by clicking on the “Search icon” 

![Search bar](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar.png)
![Search bar small devices](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/search_smaller_devices.png)

![Search results](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/search_results.png)

_12.	As a shopper I want to be able to view products by specific product category so that I can easily find the product I am looking for._

* Users can view products by Category. They can click choose the categories from the navigation menu or from the “Choose a category" section. 

![Navbar menu category](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar_menu_categorization.png)

![Choose Category](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/choose_category_homepage.png)

_13.	As a shopper I want to be able to sort all products so that I can quickly identify the products based on their price, category, or rating._

* When on the Products page, users have the option to sort products using the dropdown menu located on the top right side.

![Sort by](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/products_sortby.png)

14.	As a shopper I want to be able to sort an individual product category so that I can find the best priced, rated or sort them by name.

* The shopper can sort products within an individual category from the dropdown menu located on the top right side.

![Category- sort_by](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/product_category.png)

[Back to table of contents](#table-of-contents)

__EPIC: Ordering and Checkout__

_15.	As a shopper I want to be able to view the items and prices when they are added to the cart so that I can always view the total cost._

* When a product is added to the cart, a message is displayed in the upper right corner, beneath the shopping cart icon, showing the added items and the total cost.

![Shopping cart alert](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/shopping_cart.png)

_16.	As a shopper I want to be able to view the cart so that I can view the items added to the cart and the total cost._

* The shopper can access the shopping cart, by clicking on the shopping cart icon. 

![Shopping cart page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/shopping_cart_page.png)

_17.	As a shopper I want to be able to easily adjust the product quantity added to the cart so that I can make the necessary adjustments to my purchase before checkout._

* Shoppers can adjust the quantity by changing the number and clicking on “Update”. Additionally, they have the option to remove the product from the shopping cart.

![Shopping cart](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/shopping_cart_page.png)

_18.	As a shopper I want to be able to place an order without been logged in so that I can place an order without having to create an account._

* Shoppers have the option to place an order as guest users, eliminating the need to create an account for purchasing products.

![Checkout page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/checkout_page.png)

_19.	As a shopper I want to be able to enter my payment information so that I can check out and place the order allowing me to quickly place the order._

* On the checkout page the users can add their contact information and credit card details. 

![Checkout page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/checkout_page.png)

_20.	As a shopper I want to be able to see an order confirmation displayed after completing the checkout so that I can view the order placed._

* After placing an order, users will be directed to the Order Confirmation page, where they can review the order details. 

![Order confirmation](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/order_confirmation.png)

_21.	As a shopper I want to be able to receive a confirmation email after checking out so that I can have a copy of the order confirmation email for my reference._

* When placing an order, users will automatically receive an email confirmation with their order details.


[Back to table of contents](#table-of-contents)

__EPIC: Product Comment and Rating__

_22.	As a site user, I want to be able to view comments and ratings so that I can view other shoppers’ opinions on the quality of the products._

* All users can view the comments added to a product, which are accessible on the individual product page beneath the product details and image.

![View Review](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/view_review_unregistered_user.png)

_23.	As a shopper and frequent site user I want to be able to add, edit, delete comments so that I can give my feedback on quality of products and the services offered by the store, edit my comments, and remove mistakes or inaccurate information._

* Registered users can add, edit, delete comments. When the log in the comment form will be displayed on the individual product page under the product details and image.
* After adding a comment, they will have two buttons, “Edit” and “Delete”. Users can only delete and edit their own comments. 

![Comments submit](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/reviews_comment_loggedin_user.png)

__EPIC: Subscribe to Newsletter__

_24.	As a site user, I want to be able to subscribe to the newsletter so that I can be up to date with the latest offers and products added to the store._

* Any user can subscribe to the newsletter by providing their email address without having to be a registered user. 

![Subscribe newsletter](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/footer.png)

__EPIC: Front-end Store Administration__

25.	As a store owner I want to be able to add a product on from the frontend site so that I can easily add new products to the store without having to access the backend.

* Admins can add a product from the front-end. “Product Administration” features are located under “My account” dropped down menu.
 
 ![Product Administration-My account](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/myaccount_signed_in_admin.png)

 ![Add product](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/add_product_admin.png)

26.	As a store owner I want to be able to edit a product from the frontend site so that I can easily edit products details accordingly without having to access the backend.

* Administrators can edit a product either from the Products page or the Product information page.
* When logged in, they will see the “Edit” option displayed under the category tag.

![Edit product - products page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/products_edit_product_admin.png)
![Edit product - product info](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/product_info_edit_product_admin.png)

27.	As a store owner I want to be able to delete a product from the frontend site so that I can easily delete products that are no longer available without having to access the backend.

* Administrators can delete a product either from the Products page or the Product information page.
* When logged in, they will see the “Delete” option displayed under the category tag.

![Delete product - products page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/products_edit_product_admin.png)
![Delete product - product info](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/product_info_edit_product_admin.png)


[Back to table of contents](#table-of-contents)

## Testing Responsiveness

* Chrome DevTools was used for testing responsiveness on desktop, tablets, and smartphones.

* The page layout, images, search button, inquiry form, comment form, login, register/logout, ordering process, email verification process, favorite/unfavorite, modal message popup when user is not logged in and tries to add to favorites a product are all displayed correctly, as expected. 

* The testing on various devices has ensured that the site functions properly and provides the desired user experience.

### Responsiveness on devices

| Responsiveness                           | Desktop >1200px | Desktop 1024px | Devices >= 700 iPad Air/Mini, Surface Pro 7 | Devices <699 iPhone SE/ XR/12 Pro/X, Pixel, Samsung Galaxy S8+/ A51/71/Fold |
| ---------------------------------------- | --------------- | -------------- | ------------------------------------------- | --------------------------------------------------------------------------- |
| Links, icons and buttons work                               | Yes             | Yes            | Yes                                         | Yes                                                                         |
| Login,logout, register functions work                              | Yes             | Yes            | Yes                                         | Yes                                                                         |
| Images, Layout and Content displayed as expected | Yes             | Yes            | Yes                                         | Yes|
| Ordering process and checkout | Yes             | Yes            | Yes                                         | Yes|
| Send an inquiry, add user reply and admin reply  | Yes             | Yes            | Yes                                         | Yes|
| Product administration, add, edit, delete product  | Yes             | Yes            | Yes                                         | Yes|

[Back to table of contents](#table-of-contents)


## Bugs

__Favorites feature__

* The user could add the products to favorites from both the main products page and the individual product information page. However, there was an issue where the heart icon did not transition from an outline to a solid form. Consequently, users were unable to visually confirm whether a product had been successfully added to their favorites.

* The "add to favorites" functionality was technically functioning, but the corresponding products were not being visually identified as favorites. This was due to a missing condition in both the products and product information views that would mark a product as a favorite.

![Add to favorite - bug](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/add_tofav_bug.png)

![Add to favorite - bug](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/add_to_fav_product_info_bug.png)

* I addressed this by introducing the necessary conditions in the views. I consulted the threads on Stackoverflow: https://stackoverflow.com/questions/8651336/marking-favorites-in-django-object-set and https://stackoverflow.com/questions/67493992/django-add-products-to-favorite-list 

* As a result, users can now determine which products have been added to their favorites by the presence of a solid heart icon.

![Add to favorite-solved ](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/add_to_fav_solved.png)

__User Reply__

* On the "My Inquiry" page, users could submit the reply form without entering any content. 

![User reply - bug ](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/inquiry_details_user_reply_notrequired_bug.png)

I found a [Stackoverflow thread](https://stackoverflow.com/questions/72266306/i-want-to-place-a-placeholder-in-my-forms-textarea-in-django) on this topic, I implemented the fix by including "required=True" in the UserReply form. As a result, the user reply field is now mandatory, preventing users from submitting an empty reply.

![User reply - solved](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/inquiry_details_user_reply_notrequired_solved.png)


__Order History__

* During testing, I noticed that any user could access an order number attached to a user profile with the required order number without needing to be logged in. 

![Order History - bug](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/order_history_bug.png)

* To address this issue, I applied the "@login_required" decorator. This resolution ensures that users are now obligated to log in before accessing the order.

![Order History - solved](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/order_history_solved.png)

[Back to table of contents](#table-of-contents)

Return to the [README.md](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/README.md) file.