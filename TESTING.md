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
  - [Testing Responsiveness](#testing-responsiveness)
   - [Responsiveness on devices](#responsiveness-on-devices)


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
| Checkout page  | Pass |
| Custom Error pages | Pass |

__Products page__

* Error received for the “login-modal” id. For the favorite icon, when the users are not logged in they have a pop-up modal that appears. I used JavaScript to show and close modal, however I used “getElementById” which rendered an error in the HTML validator as this applies to all products. 

![Products page error](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/products_page_modal.png)

* I have changed the “login-modal” to class and changed the JavaScript accordingly. The error is no longer displayed. 

![Products page solved](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/products_page_modal_solved.png)

__Product administration – Add product and Edit product__

* Error received for duplicate ID. I could not find the second ID in the code. I found that other colleagues had similar issues with this particular “id”. This error is also shown when editing a product. Refer to [thread](https://code-institute-room.slack.com/archives/C026VTHQDNY/p1677243978633509)
I was unable to locate the code containing the "id=id_image", and upon removing the id, I can no longer add the image on the site. This error is still displayed. 

![Product administration – Add product](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/html_validator_product_administration.png)

![Product administration – Edit product error](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/edit_product_product_admin.png)

__Shopping cart page__

* I encountered an error indicating a duplicate ID on the shopping cart page, which was also highlighted in the "boutique_ado" walkthrough. To resolve this issue, I modified the ID to a class and adjusted the JavaScript to target the class element. As a result, the error is no longer present.

![Shopping cart id error](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/html_validator_shopping_cart_error_id.png)

![Shopping cart solved](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/testingimages/html_validator_shopping_cart_solved.png)


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

Return to the [README.md](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/README.md) file.