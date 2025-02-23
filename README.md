# BookRecommender-System
This project is a simple book recommendation system that suggests books based on user input. It was built using Python, Flask, Pandas, and Scikit-learn. The system follows a content-based filtering approach, which means it recommends books similar to the one entered by the user.

The first step in building this project was preparing the dataset. A dataset containing book titles, authors, genres, ratings, and cover images was collected. The data was then cleaned and saved as a pickle file (books.pkl) to make it easier to load in the application.

Next, a recommendation model was created. The project uses a technique called TF-IDF (Term Frequency-Inverse Document Frequency) to convert book titles and descriptions into numerical values. Then, cosine similarity was calculated to find books that are most similar to each other. The similarity data was saved as a .npy file so that the application can access it quickly.

A Flask web application was then developed to handle user input and generate recommendations. When a user enters a book title, the application finds the top 5 most similar books and returns them as recommendations.

The frontend of the project was designed using HTML, CSS, and Bootstrap. The interface includes a simple search box where users can enter a book title. After submitting the title, the recommended books are displayed along with their titles, authors, and cover images.

Finally, the project was deployed locally using Flask. When the application runs, it can be accessed on http://127.0.0.1:5000/.

This project provides a basic but effective way to recommend books. It helps users discover books that are similar to the ones they already like, making it useful for book lovers.







