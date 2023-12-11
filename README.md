
# Taste of Romania 

**Welcome to Taste of Romania!**

**A site of traditional Romanian products, food, and gifts**

Taste of Romania is a B2C e-commerce shop with Romanian traditional products, foods, and artisanal creations.

It addresses to Romanians seeking a taste of nostalgia or the perfect gift to share cultural aspects of Romania.

Customers can easily navigate the site by category, leave reviews, and add products to their favorites for a smooth shopping experience.

Visit deployed site here : https://taste-of-romania-5dd5a29030c4.herokuapp.com/

## Table of contents

- [Taste of Romania](#Taste-of-Romania)
- [Table of contents](#Table-of-contents)
- [User Experience](#User-Experience)
  - [The goal of the site owner](#The-goal-of-the-site-owner)
  - [The goal of the external user](#The-goal-of-the-external-user)
  - [User stories](#User-stories)
    - [EPIC: Back-end Store Administration](#EPIC-Back-end-Store-Administration)
    - [EPIC: Store viewing and navigation](#EPIC-Store-viewing-and-navigation)
    - [EPIC: User Login/Registration and Profile ](#EPIC-User-Login/Registration-and-Profile)
    - [EPIC: Product Categorization and Searching](#EPIC-Product-Categorization-and-Searching)
    - [EPIC: Ordering and Checkout](#EPIC-Ordering-and-Checkout)
    - [EPIC: Product Comment and Rating](#EPIC-Product-Comment-and-Rating)
    - [EPIC: Subscribe to Newsletter ](#EPIC-Subscribe-to-Newsletter )
    - [EPIC: Front-end Store Administration ](#EPIC-Front-end-Store-Administration)
  - [Future Features](#Future-Features)
  - [Design, colors and typography](#Design,-colors-and-typography)
- [Agile Methodology](#Agile-Methodology)
- [Wireframes and Database schema](#Wireframes-and-Database-schema)
  - [Wireframe](#Wireframe)
  - [Database schema](#Database-schema)
- [Business Model](#Business-Model)
- [Marketing Strategies](#Marketing-Strategies)
  - [SEO](#SEO)
    - [Keywords](#Keywords)
    - [Robots.txt and Sitemaps](#Robots.txt-and-Sitemaps)
  - [Content Marketing](#Content-Marketing)
  - [Social Media Marketing](#Social-Media-Marketing)
  - [Email Marketing](#Email-Marketing)
- [Existing Features](#Existing-Features)
  - [Home page](#Home-page)
    - [Navigation Bar](#Navigation-Bar)
    - [Search bar](#Search-bar)
      - [Search results](#Search-results)
      - [Search no results](#Search-no-results)
    - [Delivery threshold](#Delivery-threshold)
    - [Navbar menu](#Navbar-menu)
    - [Landing image](#Landing-image)
    - [About us](#About-us)
    - [Choose a category](#Choose-a-category)
    - [Payment, shipping and return](#Payment,-shipping-and-return)
    - [Footer](#Footer)
  - [Products page](#Products-page)
  - [Product Information page](#Product-Information-page)
  - [Reviews - comments](#Reviews-comments)
  - [Login page](#Login-page)
  - [Logout page](#Logout-page)
  - [Register Page](#Register-Page)
  - [Ordering process](#Ordering-process)
    - [Guest checkout](#Guest-checkout)
     - [Shopping cart](#Shopping-cart)
    - [Logged in user](#Logged-in-user)
  - [My Profile page](#My-Profile-page)
  - [My inquiries page](#My-inquiries-page)
  - [Inquiry details page](#Inquiry-details-page)
    - [User Reply](#User-Reply)
  -   [Admin Reply](#Admin-Reply)
  - [My Favorites page](#My-Favorites-page)
    - [Logged in user](#Logged-in-user)
    - [Product added to favorites](#Product-added-to-favorites)
    - [Existing favorites product:](#Existing-favorites-product)
    - [Remove product from favorites](#Remove-product-from-favorites)
    - [Guest users](#Guest-users)
  - [Product Administration page](#Product-Administration-page)
- [Languages](#Languages)
  - [Frameworks, Libraries and Programs used](#Frameworks,-Libraries-and-Programs-used)
- [Testing](#Testing)
- [Deployment](#Deployment)
  - [Gitpod](#Gitpod)
  - [Database](#Database)
    - [Attach the Database](#Attach-the-Database)
  - [Set up the environment and settings.py file](#Set-up-the-environment-and-settings.py-file)
  - [Store images to AWS](#Store-images-to-AWS)
  - [Identify and Access Management (IAM)](#Identify-and-Access-Management-(IAM))
  - [Connecting S3 to Django](#Connecting-S3-to-Django)
  - [Create app in Heroku](#Create-app-in-Heroku)
- [Credits](#Credits)
- [Acknowledgments](#Acknowledgments)


## User Experience

### The goal of the site owner

* To provide customers a wide range of Romanian products for Romanians leaving abroad or people that are interested in trying and tasting Romanian food. 

### The goal of the external user

* End customers aim to access and explore a varied range of Romanian products through a site that guarantees a user-friendly shopping experience for those interested in discovering and enjoying authentic Romanian products.

### User stories

* There were created 8 EPICs which were developed into 32 User stories. Out of the 31 stories, four were excluded from the project due to time constraints and were marked as "Won't Have" on the Kanban board on Github. The user stories can be accessed [here-Taste of romania User Stories](https://github.com/users/AdrianaStoi/projects/3)

#### EPIC: Back-end Store Administration 

1. As store owner, I can access an admin panel where I can view users, edit, delete, products, categories, orders, comments, and ratings and filter in the sections so that I can efficiently manage the store.

#### EPIC: Store viewing and navigation 

2. As a site user I want to be able to easily navigate on the site so that I can find the products available.
3. As a shopper I want to be able to view a list of products so that I can select the products I would like to purchase.
4. As a shopper I want to be able to view details of a product so that I can check the price, description, ingredients, comment, rating before buying. 

#### EPIC: User Login/Registration and Profile 

5. As a frequent site user, I can register on the site, so I can have an account to place an order, keep an order history and provide feedback on the products. 
6. As a frequent site user I want to be able to login or logout so that I can access my account information.
7. As a frequent site user I want to be able to recover my password in case I forget it so that I can recover my access account. 
8. As a registered in user I want to be able to access my user profile page, so that I can save my details for next purchases and view my orders.
9.  As a site user I want to be able to add the products to "Favorites" so that I can save the product in the profile and purchase it later.
10. As a shopper I want to be able to submit an inquiry so that I can ask about my order status or inquiry about products on the site. 

#### EPIC: Product Categorization and Searching

11. As a shopper I want to be able to search a product by name or description so that I can find the product I want to purchase. 
12. As a shopper I want to be able to view products by specific product category so that I can easily find the product I am looking for.
13. As a shopper I want to be able to sort all products so that I can quickly identify the products based on their price, category or rating.
14. As a shopper I want to be able to sort an individual product category so that I can find the best priced, rated or sort them by name. 


#### EPIC: Ordering and Checkout

15. As a shopper I want to be able to view the items and prices when they are added to the cart so that I can always view the total cost.
16. As a shopper I want to be able to view the cart so that I can view the items added to the cart and the total cost. 
17. As a shopper I want to be able to easily adjust the product quantity added to the cart so that I can make the necessary adjustments to my purchase before checkout.
18. As a shopper I want to be able to place an order without been logged in so that I can place an order without having to create a account.
19. As a shopper  I want to be able to enter my payment information so that I can check out and place the order allowing me to quickly place the order.  
20. As a shopper I want to be able to see an order confirmation displayed after completing the checkout so that I can view the order placed.
21. As a shopper I want to be able to receive a confirmation email after checking out so that I can have a copy of the order confirmation email for my reference.


#### EPIC: Product Comment and Rating

22. As a site user, I want to be able to view comments and ratings so that I can view other shoppers’ opinions on the quality of the products.
23. As a shopper and frequent site user I want to be able to add, edit, delete comments so that I can give my feedback on quality of products and the services offered by the store, edit my comments, and remove mistakes or inaccurate information.


#### EPIC: Subscribe to Newsletter 

24. As a site user, I want to be able to subscribe to the newsletter so that I can be up to date with the latest offers and products added to the store. 

#### EPIC: Front-end Store Administration 

25. As a store owner I want to be able to add a product on from the frontend site so that I can easily add new products to the store without having to access the backend.  
26. As a store owner I want to be able to edit a product from the frontend site so that I can easily edit products details accordingly without having to access the backend.  
27. As a store owner I want to be able to delete a product from the frontend site so that I can easily delete products that are no longer available without having to access the backend.  

[Back to table of contents](#table-of-contents)

### Future Features

* The user stories below were the ones not implemented in the project due to time constraints and were labelled as “Won’t Have” on the Kanban board on Github. These user stories and last EPIC will be implemented in the future:

    **EPIC: Store viewing and navigation**

28. As a shopper I want to be able to easily identify discounted products on the site so that I can take advantage of existing discounts. 

    **EPIC : Ordering and Checkout**

29. As a site user I want to be able to receive email notifications when a product is out of stock, so that I can be informed when the product becomes available again.

    **EPIC : Delivery options**

30. As a shopper I want to be able to choose Express delivery so that I can receive the products earlier than 3 to 5 days. 

  **EPIC: Product Comment and Rating**

31. As a shopper I want to be able to rate a product and the store’s services so that I can give my feedback on the quality of a product and the services offered by the store.

  **EPIC: User Login/Registration and Profile** 

32. As a registered user, when creating a new inquiry, I want to be able to add the order number to the request from a dropdown menu so that I can easily include it in my request.


### Design, colors and typography

The site's choice of black, white, and red is rooted in their significance in Romanian traditional clothing and culture, a palette that extends to the site's logo. 

The image on the landing page, with Romanian traditional motifs, offer a sense of familiarity to Romanian visitors and provides others with a chance to learn more about Romanian culture. This was inspired from the [blog - Ienationala](https://www.ienationala.ro/blog/index.php/2021/03/03/motive-traditionale-romanesti-care-sunt-principalele-simboluri-si-care-este-semnificatica-lor/)

* Color used for the navbar, landing page, footer, the body of the cards on the products page : #090601
* The text color scheme was black for the navbar menu and product description. White was used for the paragraphs that have as background color #8b181e and #090601.

* On the buttons I alternated and used the three colors 

* The color choices for the navigation bar, menu the different site sections and pages was selected to harmonize with the color of the static landing image on the homepage, ensuring a cohesive visual theme. 

Google fonts ‘'Amaranth’ and ‘Open Sans' were used. Specifically, ‘'Amaranth’ was employed for headings, navbar and buttons and ‘'Open Sans' was used for paragraphs. 
As per the [site-vandelaydesign] https://www.vandelaydesign.com/google-font-pairings/ these two fonts complement each other well. 

[Back to table of contents](#table-of-contents)

## Agile Methodology

* The development process, following an agile methodology, was managed using the GitHub Project.
* The link to the Project Kanban board can be accessed [here-Taste of romania User Stories](https://github.com/users/AdrianaStoi/projects/3). 
* Each user story was translated into a GitHub Issue, incorporating the EPIC, Acceptance Criteria, and Tasks. 
* To ensure clarity, every User Story includes well-defined acceptance criteria, further broken down into tasks for seamless execution. 
* Employing the MoSCoW prioritization technique, the User Stories were categorized from highest to lowest priority: "Must Have," "Should Have," "Could Have," and "Won't Have." 
* These stories were then assigned to corresponding milestones aligned with the project's sprint cycles.

## Wireframes and Database schema

### Wireframe

* I used Balsamiq Wireframes to create the wireframes for site layout. The wireframe can be found [here-Taste of Romania-balsamiq wireframes](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/wireframes/Taste_of_romania_wireframes.pdf): 
* The layout of the site has changed throughout the project development due to time constraints. As a result, some of the features originally outlined in the wireframe as the User Profile page are to be implemented in the future.

### Database schema

* In order to create and plan the databse structure, I used [Lucidchart](https://www.lucidchart.com/pages/) to create a Database ER diagram.

* The diagram is available [here-Taste of Romania-Lucidchart](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/wireframes/Taste_of_romania_lucidchart.pdf).

* I applied Object-Oriented Programming principles in the project, along with Django’s Class-based generic views. I created three additional custom models besides the ones from the walkthrough (Product, Order Line, Order, Category, User Profile). These new custom models are "Review", "Favorites" and "Inquiry". 
* I used Allauth library for the user authentication system.

* The **"Review"** model enables logged in users to comment on products. The Review comment model includes the fields "Comment" and "Rating". The "Product" custom model is linked as a Foreign Key ensuring that each comment is associated with a specific product.  Also, the ‘User’ built in model serves as a Foreign Key, as each comment is attributed to a single user.

* The "rating" field was not implemented in the project at this time due to time constraints. This feature is to be added at a later time.  

* The **"Favorite"** model includes a "product" field that serves as a foreign key, linking to the associated product. In addition, there is a "user" field, which acts as another foreign key, linking to the user who marked the product as a favorite. Finally, the model incorporates an "is_favorite" boolean field, which serves to indicate whether the associated product holds the status of a product marked as a favorite by the user.

* The **"Inquiry"** model is designed with fields to capture and manage user queries. It includes a user field, functioning as a Foreign Key and linking to the respective User involved in the inquiry. The profile field is also a Foreign Key.

* Contact details are recorded through the name CharField, email EmailField, and phone_number CharField. The subject CharField allows users to define the topic of their inquiry, while the message TextField accommodates detailed information. The order_number CharField is available for users to associate inquiries with specific orders. Admin responses are stored in the admin_reply TextField, facilitating communication between users and administrators. Additionally, the user_reply TextField offers the option for users to respond or provide further information. This comprehensive model ensures a structured approach to managing and responding to user inquiries effectively.

![Taste of Romania - Database Diagram](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/lucidchart_taste_of_romania.png)

[Back to table of contents](#table-of-contents)

## Business Model

* Taste of Romania has a Business to Consumer (B2C) Business Model with products sold directly from the shop to end consumers. This is a specialized online shop addressing a niche market. The typical customer of Taste of Romania is expected to be individuals who are Romanians residing abroad, those who have visited Romania, or individuals with Romanian friends and acquaintances. 

## Marketing Strategies

* Several Marketing strategies were used for the project which are SEO, Content Marketing, Social Media Marketing and Email Marketing. 

### SEO 

#### Keywords

* I conducted keyword research for the site, utilizing both short and long-tail keywords. Initially, I checked Google search results and wordtracker.com; however, due to the limitations of the free option on wordtracker.com, I relied more on Google searches for keyword research.

* To refine my list, I examined the number of results for each keyword and explored the "Related searches" and "People also ask" sections on Google. I created a list of relevant keywords, prioritizing those most suitable for improving the site's ranking in search engine results.

* These keywords were integrated into various elements of the site, including product descriptions, the navigation menu, and headings, all of which contribute significantly to SEO. Additionally, I incorporated meta keywords into my base HTML template, selecting the most pertinent and applicable keywords. To further improve SEO, the alt tag descriptions for the images include the product names, which are essential components of the keywords.

* The initial keyword list included: 

    __Short-tail keywords__

    * Romanian specialties
    * Romanian pottery
    * Romanian sweets
    * Mici
    * Romanian snacks
    * Blouse IE
    * Romanian chocolate
    * Romanian gifts
    * Tradition
    * Romanian zacusca
    * Romanian cheese
    * Romanian drinks
    * Visinata

    __Long-tail keywords__

    * Romanian online store
    * Products from Romania
    * Traditional Romanian gifts
    * Romanian traditional blouse ie
    * Romanian cheese buy online
    * Traditional Romanian products buy online
    * Where to buy Romanian mici
    * Buy Romanian food online
    * Artisanal and crafts from Romania
    * Romanian grocery online
    * Romanian products near me

#### Robots.txt and Sitemaps

* A robots.txt file was created for the site to instruct search engines about areas they should avoid while navigating on the site. This file is used for enhancing the site’s SEO ranking.

* A sitemap file was generated using xml-sitemaps.com to facilitate a clear understanding of the website’s structure search engines understand the website structure. The presence of a sitemap ensures that search engines crawl every important page on the site, contributing to comprehensive and efficient indexing.

### Content Marketing 

* As part of the content marketing strategy, I have integrated customer reviews for the products. 

* Particularly, user-generated content like product reviews plays a central role. By incorporating customer feedback into the content marketing approach, the goal is to establish trust, engage the audience, and impact potential customers by sharing experiences and opinions related to the site's products.

* The customer’s reviews can be accessed by any user on each product information page. 

### Social Media Marketing

* A Facebook Business Page has been created for the Taste for Romania site as part of organic social media marketing approach. 

* The Facebook page aligns very well with the design and information on the online shop. For the profile picture I have used the logo image and as cover I have chosen to add the landing page. 

* As “Action Button” I have chosen to add “Contact us” which directs users to the deployed website. While I wanted to include a “Buy now” or “Shop” button, I did not have the option to just add the link of the website. The options available required the use of third-party sites to connect and to then create the “Buy now” button. 

* The “Contact us” button also conveys with the purpose of directing potential customers to the site. 

* Interested customers can also reach the site by clicking on the site link added under the intro section.

* This was the link for the Facebook business page, which has been in the meantime deactivated : https://www.facebook.com/profile.php?id=61554418048295

![Taste of Romania - Facebook business page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/taste_of_romania_facebook.png)

![Taste of Romania - Facebook business page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/taste_of_romania_fb.png)

### Email Marketing 

* Mailchimp has been used to implement a newsletter signup feature on the site. Any user visiting the site can subscribe to the newsletter by providing their email address without requiring them to create an account. It serves as a means of communicating product updates and news, reaching both potential new customers and existing customers. 

[Back to table of contents](#table-of-contents)

## Existing Features

### Home page

#### Navigation Bar

* The navigation bar is present on all site pages. It is a fully responsive navigation bar which includes the links for easy user navigation to the “My Account”, “My Favorites”, “Shopping Cart” page. When users click on the “Taste of Romania” logo they will be directed to the “Home” page. With these features the user can navigate from page to page and does not have to use back to revert to the previous page. The navigation bar can be used on all device types: desktop, tablet, and smartphones.

![Image navbar](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar.png)

* When the unregistered user clicks on ‘My Account’, he has a dropdown menu with the options ‘Register’ and ‘Login’. 

![Image navbar My account](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar_myaccount_unregistered.png)

* Logged in user will have multiple options when clicking on My Account, which are My Profile, My Inquiries and Logout. These are the options based on user type.

* My Account options when the admin is signed in : 

![Image navbar- admin signed in](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/myaccount_signed_in_admin.png)

* My Account options when regular user is signed in : 

![Image navbar regular user signed in ](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar_loggedin_regular_user.png)

[Back to table of contents](#table-of-contents)

#### Search bar

* In the middle of the navbar the user can access a search bar, which remains accessible across all pages. 

![Image search](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar.png)

##### Search results

* This feature enables the user to search for products. On the products results page, there is a “Products Home” button to improve the user experience. This button allows users to easily return to the Products page.

![Search results](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/search_results.png)

##### Search no results

* If no products are found, a message is displayed stating “0 products found for.”

![Search no results](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/search_no_results.png)

#### Delivery threshold 

* At the top of the page the user can see the delivery threshold for free delivery. This has been added at the top of the page, so it is visible to the user and remains accessible across all pages.

![ Delivery threshold](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/delivery_threshold.png)

#### Navbar menu 

* Underneath the navbar, there is located the navbar menu with the different categorization types. The navigation menu is present on all site pages. 
* There is “All Products” dropdown menu with the options to view products “By Price”, “By Category” and “All Products”. 

![Navbar menu](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar_menu_categorization.png)

* Under Romanian specialties the user can go to categories: Cheese, Meat products, Sweets, Snacks Food Cupboard or All Romanian specialties. 

![Navbar menu](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar_menu_specialties.png)

* The Drinks section does not include a dropdown menu. This will lead to the Drinks page. 
* An lastly under the “Artisanal products” section, the user can choose to go to : Traditional clothing, Handmade pottery, Handmade bracelet or All Artisanal Products. 

![Navbar menu](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/navbar_menu_artisanal.png)

#### Landing image 

* The home page includes an image with Romanian motifs and a color palette predominantly composed of red, black, and white tones, aligning with the overall design aesthetics of the website.
*  Additionally, a welcoming message is displayed on the homepage and a button ‘See all products’ inviting the users to explore the shop.

![Landing image](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/landing_image.png)

#### About us

* This section provides information about the site owner’s scope. Reassuring the user that they are at the right place for buying Romanian products.

![Image about us section](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/about_us_section.png)

#### Choose a category 

* Under the About section the user can find “Choose a Category” section with three images that illustrate the category along with the corresponding product categories titles. 
* When the user clicks on the category titles, they are directed to the respective page displaying products related to those categories.

![Choose a category  section](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/choose_category_homepage.png)

#### Payment, shipping and return

* At the bottom of the page the user can find a payment and shipping information section alongn with the return information. This section is available on all pages so the user has access to this information at all times. 

![Payment, shipping and return](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/shipping_return_info.png)

#### Footer

* The last section is the footer where the user can find the contact details, Privacy policy, subscribe to the newsletter form and the social media icons. 

![Footer](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/footer.png)

* When the user clicks on the "Privacy Policy" the correspoding Privacy Policy terms for Taste of Romania will open in a separate tab.

![Privacy Policy](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/privacy_policy.png)

[Back to table of contents](#table-of-contents)

### Products page 

* On the "All Products" page, users can explore the entire range of products available on the site. In the top left corner, beneath the title, there is a "Product Home" button and the count of displayed products. This layout remains consistent across all product and category pages.
* For each product there is an image representation of the product. Underneath the image there is information about the product as : product title, price, category tag, heart icon which allows logged in users to add it to favorites and a “See product” button which leads the user to the respective product page. 

![Products](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/products_page.png)

* On the right side, there is a dropdown menu offering sorting options. Users can arrange the products by price, category name, or product name. This feature provides flexibility in organizing and finding items based on different criteria.

![Products sortby feature](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/products_sortby.png)

* When the user chooses one of the categories, he will have displayed all the products in that categories. The page will have the same elements as the All products page, meaning Product Home button, product count number, option to sort products. 

![Products by category](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/product_category.png)

[Back to table of contents](#table-of-contents)

### Product Information page 

* On the product information page, users will find a "Products Home" button at the top left corner. 
* To the left, there is an image displaying  the respective product. 
* On the right side, users can access detailed product information, including the product name, weight (if applicable), a heart icon for adding to favorites, price, description, ingredients (if applicable), size (if applicable), and a quantity section that allows them to adjust the quantity for purchase. The page also includes “Continue Shopping" and "Add to Cart" buttons for seamless navigation and purchasing.

![Product information](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/product_info_page.png)

![Product page clothing](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/products_page_clothing.png)

#### Reviews - comments

* Under the product information page there is the reviews section, which at the moment includes the Comments section. The rating feature has not been implemented at this time. 
In the Comments section, users who are not logged in will have read access to view the comments.

![Reviews guest user](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/reviews_unregistered_no_reviews.png)

* There is also a message displayed “Login or Register to like and leave a comment.” This message encourages users to engage with the community by providing feedback.
* If no comments are available, there is stated “No reviews yet.”

![No reviews](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/reviews_unregistered_no_reviews.png)

* When a user is logged in, they have the option to submit a comment using a comment form. After sending a comment, they will be prompted with the message “Review added successfully” 

![Review logged in user](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/reviews_loggedin_user.png)

![Review - submit success message](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/success_message_review_submitted.png)

* Once the comment is submitted, it will appear in the comment section, and the logged-in user will have the ability to “Edit” or “Delete” their comment.

![Comment submitted](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/comment_submitted.png)

* When editing the comment, the user is redirected to a new page where they can make the necessary changes. After editing, they are redirected to the previous page and they are be prompted with a success message alert.

![Edit comment](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/comment_edit.png)

![Edit alert message](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/success_message_edit_comment.png)

* When deleting a comment, the user is prompted with a confirmation message to confirm the deletion. After confirming, the comment will be deleted. They are redirected to the previous page and they are prompted with a success message alert.

![Confirm deletion](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/comment_deletion.png)
![Alert confirm deletion](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/success_message_deletion.png)

[Back to table of contents](#table-of-contents)

### Login page

* On the login page the user is asked to enter their username and password. If the user is not registered yet, they can click on “Register”.

![Login page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/login_page.png)

![Success login](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/success_message_signed_in.png)

* When user enters a wrong username or password, they are prompted with the message “The username and/or password you specified are not correct.”

![Login incorrect password](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/login_incorrect_password.png)

__Forgot password__

Users can reset their passwords when needed. When clicking on "Forget password" option on the “Login” page, they will be redirected to the “Password Reset” page. Subsequently, a link is sent to their email address, enabling them to change the password:

| Reset      |       |
| ---------- | ----- |
| ![Password Reset Page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/password_reset_page.png) | ![Password reset sent](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/password_reset_sent.png)|
|       |       |
| ![Change password](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/change_password_page.png) | ![Reset Done](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/password_reset_done.png) | 

* When users are logged in, at the top right corner their user name is displayed.

![Logged in user name](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/user_logged_in.png)

[Back to table of contents](#table-of-contents)

### Logout page

* When clicking on logout, users are redirected to a page that asks them to confirm their intention to log out. This step helps ensure that users do not accidentally log out and asks for them to confirm this action before proceeding.


![Log out](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/confirm_logout.png)

![Success message signed out](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/success_message_signed_out.png)

### Register Page

* On the register page, users are asked to enter their name, email and create a password: Once they are registered, they are prompted with the page “Verify your email address” and with a message alert. Once the email is verified the user can log in. 


![Register Page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/register_page.png)

* Verify your email address: 

![Verify email page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/verify_email_page.png)
![Alert message email sent](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/alert_message.png)

[Back to table of contents](#table-of-contents)

### Ordering process 
#### Guest checkout 
##### Shopping cart

* Guest users can place an order on the site without having to login. 

* Upon adding a product to the cart, a success message appears in the right corner. This message includes a summary of the shopping cart, presenting details such as the added product, quantity, price excluding delivery costs, a notification of the required amount to qualify for free delivery, and a "Secure Checkout" button.

![Shopping cart](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/shopping_cart.png)

* When clicking on “Secure checkout” button the user is redirected to the “Shopping cart page” which includes a summary of the cart, along with the options to update the quantiy and remove option under the quantity and the user is informed about the grand total of the order. 
* The user can continue the “Secure checkout” or can “Continue shopping” *this redirects the user back to products page”. 

![Shopping cart page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/shopping_cart_page.png)

* If the user continues and goes to the “Checkout” he will be prompted to add the personal details and card information.

![Secure checkout](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/checkout_page.png)

* Once the order is submitted, the guest user is directed to the order confirmation page where they can view the order details. They will also be prompted with a success message in the top left corner.
 
![Order confirmation](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/order_confirmation.png)

[Back to table of contents](#table-of-contents)

#### Logged in user

* The ordering process for the logged-in user is the same as for the guest user, with the difference being that on the checkout page, the logged-in user will only need to add their name and card details. The personal information will be prefilled with the details from their account.

![Checkout logged in user](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/checkout_loggedin_user.png)


### My Profile page

* On the profile page on the left side, the logged in user can find their default delivery information if they save it in their account along with the option to update the information. 

* On the right side the user can see their order history. If they click on the order number, they will be directed to the order confirmation page which displays their order details. 

![My Profile page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/myprofile_page.png)

[Back to table of contents](#table-of-contents)

### My inquiries page

* On the my inquiries page the user can send a request a request about their current order or just send a question to the shop. 
* On this page the logged in users can also find a history of their inquiries: 

![My inquiries page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_inquiries_page.png)

### Inquiry details page 

* On the Inquiry details page, the user can see their request details. They can add a reply to the existing request which will be added to the existing one. At this time, the reply option has been added as a string. It is added as a separate message line under the “Reply” section along with their name.

![Inquiry details page](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_inquiry_details.png)

#### User Reply 

Reply added to the request:

![Inquiry - Reply](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_inquiry_details_reply.png)

#### Admin Reply 

* When there is an update from the Taste of Romania, this will be displayed under the “Taste of Romania” section in the form. 
* At the moment the admin can add a message only within their Django admin panel. 
* The admin message will be displayed as per below: 

![Admin Reply ](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_inquiry_details_admin_reply.png)

The users have also the option to delete the request. When clicking on “Delete request”, they are prompted with a confirmation deletion page indicating the inquiry number. 

![Delete request button](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/delete_request_button.png) 

![Confirm deletion inquiry](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/confirm_deletion_inquiry.png) ![Confirm deletion alert inquiry](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/confirmation_deletion_inquiry_alert.png)

[Back to table of contents](#table-of-contents)

### My Favorites page

#### Logged in user

* Registered users can add products to favorites and also remove them. Products added to favorites will be saved in the “My Favorites” page. 
* If no products were added, the page will contain the default message “You have not added any products to your favorites yet.”

![My favorites - no products](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_empty.png)

* Logged in users can add a product to favorites from the “Products” page or “Products information” page by clicking on the heart icon. 
* Once clicked on the heart icon, the user is lead to the favorites page. If the user goes back to the “Products” page or that respective “Product information” page, the heart will be filled in and they can distinguish which product has been added to favorites and which not. 

##### Product added to favorites

![Product added to favorites](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_product_added.png)

##### Existing favorites product: 

![Existing favorites product info](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_existing_prod_info.png)

![Existing favorites product](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_existing_prod_products_page.png)

##### Remove product from favorites

The users can remove a product from favorites, either by going to the “My Favorites” page and click on the trash can icon or from the “Products” or “Product information” page by clicking on the solid red colored heart. This action will automatically remove the product from the “My favorites” page. 

![Remove favorites](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_remove.png)
![Favorites removed](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_removed.png)

#### Guest users

* Users who are not logged in cannot add products to their favorites. If they click on the heart icon, they will be prompted with a message instructing them to log in or register. Additionally, if they visit the "My Favorites" page, they will see a message inviting them to log in or register, along with the respective link.

![My favorites page- guest users](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_guest_users.png)
![Guest users popup message](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/my_favorites_guest_users_popup_message.png)

[Back to table of contents](#table-of-contents)

### Product Administration page 

* The administrator can add, modify, and remove products directly on the frontend using the "Product Administration" section. Upon selecting the product administration option, the admin is directed to the "Product Administration - Add Product" page.

![Product Administration- Add Product](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/add_product_admin.png)
![Product Administration- Add Product](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/add_product_admin_form.png)

* When adding a product, the admin is prompted with an alert success message, and it is directed to the product information page. When he does not add any image to the product, it will be added with the “noimage” product below: 

![Noimage product](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/add_product_noimage.png)

* The admin can edit the existing product by clicking on “Edit”. The Edit and remove options will be displayed on the All Products page under each product and under the Product information page. 
* When on the editing page the admin is being informed that he is editing the product. 

![Edit_product_alert](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/edit_product_alert.png)

* Once edited, he is prompted with success message: 

![Product edit success message](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/edit_product_success.png)

*  The admin can also delete a product. When clicking on "Delete," they are directed to a "Confirmation Deletion" page. Once deleted, they are prompted with a success message.

![Confirmation Deletion product admin](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/confirm_deletion_product_admin.png)

![Success message product deletion](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/documentation/readmeimages/message_deletion_product.png)

[Back to table of contents](#table-of-contents)

## Languages

* Skillset used for the project was HTML, CSS, JavaScript and Python.

### Frameworks, Libraries and Programs used

* [Gitpod](https://www.gitpod.io/) was used as the editor for developing the site.
* Django was used as Python framework in the development of the project.
* [ElephantSQL](https://www.elephantsql.com/) was used as a database for the project.
* [Django Allauth library](https://docs.allauth.org/en/latest/) was utilized for user authentication system.
* [AWS](https://aws.amazon.com/) was used as storage for dynamic images.
* Psycopg2 and gunicorn were installed as supporting libraries.
* [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html) was used for Django Forms.
* [Bootstrap 4.4.1](https://getbootstrap.com/docs/4.4/getting-started/introduction/) was used for general layout, spacing and buttons.
* [Heroku](https://dashboard.heroku.com/apps) was used as the cloud based hosting platform to deploy the site.
* [GitHub](https://github.com/AdrianaStoi) - The project's deployment history was tracked using Git commit messages on Github. GitHub also served as agile project management tool.
* [Lucidchart](https://www.lucidchart.com/pages/) was used to create and plan the database structure. The diagram is available here – Taste of Romania - Database Diagram.
* [Balsamiq Wireframes ](https://balsamiq.com) was used to create the wireframes for site layout. The wireframe can be found here: Taste of Romania -Wireframes
* [Stripe](https://stripe.com/en-de) used for payments system.
* [Mailchimp](https://mailchimp.com/de/) was used to create the newsletter.

[Back to table of contents](#table-of-contents)

## Testing

* Testing and results can be found in the [TESTING.md](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/TESTING.md) file [here](https://github.com/AdrianaStoi/Taste-of-Romania/blob/main/TESTING.md).

## Deployment

### Gitpod

* I used [Gitpod](https://www.gitpod.io/) to develop the project. Here are the steps to create the workspace and run the project:
* Log in to [Gitpod](https://www.gitpod.io/) using GitHub account
* On the Dashboard, click on “New Workspace” which can be found under “Workspaces” section
* Copy and paste the Repository URL created in GitHub by using the [CI PP5 Gitpod template](https://github.com/Code-Institute-Org/gitpod-full-template)  into the designated field
* Click on Create.
* New Workspace is created in Gitpod.
* To run and view the project written in Gitpod, click on “Terminal” in the upper left side bar, then select “New Terminal”.
* The New terminal will open at the bottom part of the page.
* Install Django by using the command “pip3 install 'django<4' gunicorn”
* Install supporting libraries: “pip3 install dj_database_url==0.5.0 psycopg2”
* Then create the Create requirements file by running the code “pip3 freeze --local > requirements.txt”
* Create Project by running “django-admin startproject project name (e.g. Taste of Romania) .”
* Create App by using the code “python3 manage.py startapp app name (e.g. home, products, favorites etc.)”
* In settings.py file add the app to installed apps and save.
* Migrate the changes in the terminal by using “python3 manage.py migrate”
* Run the server “python3 manage.py runserver”
* An error message will appear, copy the host name and add it to “ALLOWED_HOSTS” in the settings.py folder. "e.g. ALLOWED_HOSTS = []"

[Back to table of contents](#table-of-contents)

### Database

* I created a Database on ElephantSQL as follows:
* Log in to ElephantSQL account
* Click on “Create New Instance”
* Set up the plan:
  * Give the plan a Name (e.g. project name)
  * Select the "Tiny Turtle (Free) plan"
  * Leave the "Tags" field blank
  * Select “Select Region” and then select a data center near
  * Click on “Review”
* Check that details are correct and then click “Create instance”
* Return to the ElephantSQL dashboard and click on the database instance name
* Under the URL section, the database URL is available. Click on the copy icon to copy the URL.

#### Attach the Database

* In Gitpod terminal:
* Create "env.py" file on top level directory
* In "env.py" file import os library
* Set environment variables : “os.environ["DATABASE_URL"] = "Paste in ElephantSQL database URL"
* Add in secret key : “os.environ["SECRET_KEY"] = "Make up own randomSecretKey"

### Set up the environment and settings.py file

* In "settings.py" file in Gitpod:
  * Reference env.py
  * Create a Remove the insecure secret key and replace it with: “os.environ.get('SECRET_KEY') and add the secret key to env.py”
  * Comment out the old DataBases Section and replace it with the new Database
  * In the Gitpod terminal, save all files and Make Migrations using “python3 manage.py migrate”

### Store images to AWS
* Create an AWS account.
* Once the account go back to aws.amazon.com
* From the dashboard, click on “Services” in the upper left corner and search for "S3", select "S3"
* Or search for the  S3 through the search.
* Open s3 and create a new bucket
* Click "Create a new bucket", name the bucket to match Heroku app name if possible
* Select the closest region 
* Uncheck block all public access and acknowledge that the bucket will be public.
* Click "create bucket".
* Open the bucket created. On the "Properties" tab turn on static website hosting.
* Scroll to the bottom, locate the "Static website hosting" section, and select "edit". Switch the Static website hosting option to "enabled". Duplicate the default values for both the index and error documents, then click "save changes".
* Go to "Permissions" tab, scroll down to CORS (Cross-origin resource sharing)  
* Paste in a coors configuration:
    ```[ 
        { 
        "AllowedHeaders": [ 
        "Authorization" 
        ],
        "AllowedMethods": [
        "GET" 
        ], 
        "AllowedOrigins": [ 
        "*" 
        ], 
        "ExposeHeaders": [] 
            } 
    ] 
    ```
* Go to the "Bucket policy" tab.
* Select, policy generator to create a security policy for this bucket.
* As policy type choose "s3 bucket policy".
* Allow all principals by using a star.
* As action add "GetObject".
* Copy the ARN which stands for Amazon resource name from the other tab.
* And paste it into the ARN box at the bottom.
* Click on "Add statement."
* Click on "Generate policy".
* Copy this policy into the bucket policy editor.
* Add a slash star onto the end of the ‘resource key’ and click Save.
* Go to the Access Control list tab, click edit and enable List for Everyone (public access) and accept the warning box.

### Identify and Access Management (IAM)

* Go to the ‘Services’ menu and open IAM.
* Click on ‘User Groups’ then create a new group called manage-product-name.
* Click on create group.
* Click on Policies and then ‘Create policy’.
* Go to the JSON tab and then select ‘import managed policy’.
* Import one that AWS has pre-built for full access to s3.
* Search for s3 and then import the s3 full access policy.
* Get the bucket ARN from the bucket policy page in s3.
* Click on review policy.
* Give it a name and a description and then click create policy.
* Click on ‘User Groups’. Select the group, go to the ‘Permissions’ tab, open the ‘Add permissions’ dropdown, and click ‘Attach policies’. Select the policy and click ‘Add permissions’ at the bottom.
* On the user's page, click add user.
* Give the user programmatic access.
* And then select next and put the user in the created group. 
* To retrieve the CSV and access the keys, go to IAM and select 'Users'
* Select the user for whom you wish to create a CSV file. 
* Select the 'Security Credentials' tab.
* Scroll to 'Access Keys' and click 'Create access key'.
* Select 'Application running outside AWS', and click next. 
* On the next screen, you can leave the 'Description tag value' blank. Click 'Create Access Key' 
* Click the 'Download .csv file' button.

### Connecting S3 to Django
* In the Gitpod install ‘boto3’ and ‘django-storages’
* Update the requirements.txt file 
* Then add storages to the installed apps 
* Add an if statement in settigns.py: 
    ```if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'taste-of-romania-5dd5a29030c4'
    AWS_S3_REGION_NAME = 'eu-central-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com
    ```

* Add the AWS keys to Heroku to the config variables (refer to Create app in Heroku below).
* The  AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com' tells Django where the static files are coming from in production
* In order to tell django that in production it is needed to use s3 to store the  static files whenever someone runs collectstatic, the file ‘custom storages’ file is required.
* Create a file called custom storages and import both settings from django.conf as well as the s3boto3 storage class from django storages.
* Create a custom class called static storage :
    ```class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    ```

* Then go to “settings.py”:
     ``` STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```

* Next add the below at the beginning of the ‘USE_AWS’ is statement in the settings.py. This will tell the browser that it's okay to cache static files for a long time:

    ```AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
    }
    ```

* Go to s3 in the AWS bucket, and create a new folder called media.
* Inside it, click on "upload". Add files. And then select all the product images.
* Then under Permissions select the option "Grant public-read access" and then click upload. 
* The static files and media from the S3 AWS will be connected to the django project.

### Create app in Heroku

* I deployed the project on Heroku at the beginning of the project and the steps below were followed:
* Log into Heroku account or create new account.
* From the Heroku dashboard click on “New” on the upper right corner and then click on “Create new app”.
* Add app name (app name must be unique on Heroku).
* Then select the appropriate region e.g. “Europe” and then click on “Create app”.
* Then go to “Settings tab”.
* Add config vars:
    ```DATABASE_URL, and add the database URL from ElephantSQL as the value
    SECRET_KEY containing the secret key
    AWS_ACCESS_KEY_ID containing the AWS access key
    AWS_SECRET_ACCESS_KEY containing the AWS secret key
    EMAIL_HOST_USER containing the host user key from Google
    EMAIL_HOST_PASS containing the host user email address
    STRIPE_PUBLIC_KEY containing the stripe public key
    STRIPE_SECRET_KEY containing the stripe secret key
    STRIPE_WH_SECRET containing the stripe webhandler secret key
    USE_AWS - True
    ```
* In settings.py file in Gitpod:
  * Add AWS variables and configuration in the settings.py
  * Link file to the templates directory in Heroku.
  * Change the templates directory to TEMPLATES_DIR.
  * Add Heroku Hostname to ALLOWED_HOSTS.

* In Gitpod terminal:
  * Create media, static, templates folders on top level directory.
  * Create a Procfile on the top level diectory.
  * In Procfile add “web: gunicorn PROJ_NAME.wsgi”.
  * Add, commit and push changes to GitHub.

* Deploy to Heroku:
  * Go to Heroku account.
  * Go to “Deploy” tab located at the top of the page.
  * Under “Deployment method” section, select Github here, and then confirm connection to Github.
  * Search for the corresponding Github repository name, e.g. Taste of Romania and click “Search”.
  * Click on “Connect” to link up the Heroku app to the GitHub repository code.
  * Scroll down on the page, and there are two deployment options in this section: “Automatic deploys” and “Manual deploy”.
  * Under “Manual deploy”, click on “Deploy Branch”.
  * Once is deployed there is a message displayed “Your app was successfully deployed.” And a button “View”.
  * Click on “View” and you are directed to the app deployed and the link.

* Visit deployed site here: [Taste of Romania](https://taste-of-romania-5dd5a29030c4.herokuapp.com/)

[Back to table of contents](#table-of-contents)

## Credits

## Acknowledgments


[Back to table of contents](#table-of-contents)
