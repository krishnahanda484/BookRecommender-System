from flask import Flask, render_template, request
import pickle
import numpy as np

# Load data
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_score.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values[:50]),
        author=list(popular_df['Book_Author'].values[:50]),
        image=list(popular_df['Image_URL_M'].values[:50]),
        votes=list(popular_df['num_ratings'].values[:50]),
        rating=list(popular_df['avg_rating'].values[:50])
    )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input', '').strip().lower()

    if not user_input:
        return render_template('recommend.html', error="Error: No book title provided. Please enter a title.")

    book_titles = books['Book-Title'].astype(str).str.strip().str.lower().tolist()

    if user_input not in book_titles:
        return render_template('recommend.html', error="Book not found. Please enter a valid title.")

    index = book_titles.index(user_input)

    if index >= len(similarity_scores):
        return render_template('recommend.html', error="Error: Book index out of bounds.")

    similar_items = sorted(
        enumerate(similarity_scores[index]),
        key=lambda x: x[1],
        reverse=True
    )[1:6]  # Top 5 recommendations

    data = []
    for i in similar_items:
        similar_book_index = i[0]

        if similar_book_index >= len(books):
            continue

        temp_df = books.iloc[[similar_book_index]]

        if temp_df.empty:
            continue

        book_title = temp_df['Book-Title'].iloc[0]
        book_author = temp_df['Book-Author'].iloc[0]
        book_image = temp_df['Image-URL-M'].iloc[0]

        data.append([book_title, book_author, book_image])

    if not data:
        return render_template('recommend.html', error="No similar books found.")

    return render_template('recommend.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
