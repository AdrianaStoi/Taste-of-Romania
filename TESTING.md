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

[Back to table of contents](#table-of-contents)

## User stories Testing

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
| ![Password Reset Page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/password_reset_page.png) | ![]()                         | 
| ![]()          | ![]()                         | 


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

![]()

__EPIC: Product Comment and Rating__

_22.	As a site user, I want to be able to view comments and ratings so that I can view other shoppers’ opinions on the quality of the products._

* All users can view the comments added to a product, which are accessible on the individual product page beneath the product details and image.

![]()

_23.	As a shopper and frequent site user I want to be able to add, edit, delete comments so that I can give my feedback on quality of products and the services offered by the store, edit my comments, and remove mistakes or inaccurate information._

* Registered users can add, edit, delete comments. When the log in the comment form will be displayed on the individual product page under the product details and image.
* After adding a comment, they will have two buttons, “Edit” and “Delete”. Users can only delete and edit their own comments. 

![]()

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

![]()
![]()

27.	As a store owner I want to be able to delete a product from the frontend site so that I can easily delete products that are no longer available without having to access the backend.

* Administrators can delete a product either from the Products page or the Product information page.
* When logged in, they will see the “Delete” option displayed under the category tag.

![]()
![]()

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