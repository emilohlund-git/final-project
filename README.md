# Collective Shop
[![Build Status](https://travis-ci.com/emilohlund-git/final-project.svg?branch=master)](https://travis-ci.com/emilohlund-git/final-project)

Collective shop is website where you would upload products that you wish to be sold, and as a user on the website be able to scour the site for products uploaded by othe users.

## UX

This website would be generally for anybody who has a product to sell, and would like to do easily. The main point of the project would be to make payments automated and deliver shipment details to the right person while having a legal backup doing so. 

The process itself would look like:
1. Make an account on the website via the 'Sign In' button the navigation bar.
2. Register a product which you would like to be sold by clicking your username in the navigation bar and pressing 'Add Item', then just fill out the form.
3. Another user finds your product in the shop (Shop button in navigation bar) and purchases it, adding to cart and pressing the 'checkout' button in the navigation bar.
4. Majority of the payment goes directly to you via direct transfer, small service fee is kept by company.
5. Shipment details is sent to the seller.
6. A digital contract would be signed when uploading a product to ensure that the buyer recieves it.

## Features

### Existing Features

- You can create an account on the website, as well as remove products that you've uploaded yourself from the profile page. (Your name in the navigation bar > Profile)
- You can change your password incase you forgot it by pressing 'Sign In' in the navigation bar followed by 'Forgot Password'. Fill out the form with your email address and you will be able to choose a new password by following the link sent with the email.
- You can add products to your cart on the 'Shop' page (navigation bar > Shop).
- You can remove the products from your cart at the checkout page (navigation bar > shopping bag symbol)
- You can fill out the form at the checkout page to confirm a purchase (Test only)
- You can search for products in the shop using the search bar.
- All static files are uploaded and running via AWS S3 web services, such as CSS, JS, media files.

### Features Left to Implement

- I don't feel like I have to add anything to this project, I could improve on the styling and add security features. But the website does what I wanted it to do.

## Technologies Used

This project is created with Django 3.0.6 and Python. I've used Bootstrap for most of the styling.

- [Link to Bootstrap](https://getbootstrap.com/)
- [Link to Django](https://www.djangoproject.com/download/)
- [AWS S3](https://aws.amazon.com/s3/)
- [Heroku](https://www.heroku.com/)

## Testing

A lot of manual testing has been done throughout this project. Everytime I added a feature I've made sure it worked as I intented it to, basically every step a bug appeared. For example.

There was a bug that occured when loading the checkout view, as I'm loading a product instance on that page for the review order section. So after I've visisted the page and wanted to remove the product from my profile page, it would give me an error that I can't delete a product which has an instance in another part of the project. So I had to make sure I removed the instance of that product first.

I had some issues getting the smtp servers to work for mailing the password reset form, I was trying to use my one.com mail account which wouldn't work. I basically just switched to gmail and it worked instantly. I would probably try to get it to work with my own domain, but for this project I don't feel it's nescessary.

There's a lot of unused requirements in the requirements.txt file, I'm not sure how to filter out everything I've used for previous Python projects.

## Deployment
- Added a requirements.txt file using 'pip freeze > requirements.txt', so that Heroku knows which apps to install to get the project running.
- Created a Procfile with 'web: gunicorn Emilohlund.wsgi:application' in it.
- Pushed everything to Github.
- Created an app at [Heroku](https://www.heroku.com). In the app I went to 'Settings' to hook up all the environmental variables that I'm using within the project.
- Next step was going to 'Deploy' in the menu on Heroku. At the deployment method, set it to GitHub.
- Then down to manual deploy and deploy branch.

## Credits

### Content
This navigation bar https://codepen.io/oskarborowski/pen/gZRLjV basically chose the style for my entire page, it was simple and nice, so I thought I'd roll with it. 

### Acknowledgements
Thanks a lot to the tutor support team for helping me with basically every bug that occured when I was writing this project!

