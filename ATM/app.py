from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
 
# Initialize Flask app
app = Flask(__name__)
 
# Secret key for session and flash messages
app.config['SECRET_KEY'] = os.urandom(24)
 
# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databaseok.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
# Initialize SQLAlchemy
db = SQLAlchemy(app)
 
# Define User model for the database
class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for user creation
    password = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return f"<User {self.username}>"
 
 
 
####################################################################
 
# Home route to show all users
@app.route('/')
def index():
    users = User.query.all()  # Fetch all users
    return render_template('index.html', users=users)
 
# Create route for adding a new user
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Create a new user instance
        new_user = User(username=username, email=email, password=password)
 
        try:
            db.session.add(new_user)  # Add the user to the session
            db.session.commit()  # Commit to the database
            flash('User added successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Error adding user', 'error')
            return redirect(url_for('add_user'))
    
    return render_template('add_user.html')
 
# Edit route to update a user's details
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get(id)  # Fetch the user by ID
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        user.password = request.form['password']
 
        try:
            db.session.commit()  # Commit the changes to the database
            flash('User updated successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Error updating user', 'error')
            return redirect(url_for('edit_user', id=id))
 
    return render_template('edit_user.html', user=user)
 
# Delete route to remove a user
@app.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get(id)  # Fetch the user by ID
    if not user:
        flash('User not found', 'error')
        return redirect(url_for('index'))
 
    try:
        db.session.delete(user)  # Delete the user from the session
        db.session.commit()  # Commit the deletion to the database
        flash('User deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting user', 'error')
 
    return redirect(url_for('index'))
 
# Main entry point to run the Flask app
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the Flask development server
    app.run(debug=True)