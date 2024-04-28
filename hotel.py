import pandas as pd
import tkinter as tk
from tkinter import scrolledtext

# Load the dataset
dataset = pd.read_csv('C:/Users/Arya Jadhav/Desktop/travel.csv')

# Global variable to store the current hotel name
current_hotel = None

# Define functions to handle different types of queries
def get_hotel_info(hotel_name):
    global current_hotel
    # Extract hotel info (description, rating, address) from the dataset based on hotel name and return it
    hotel_info = dataset[dataset['similar_hotel'].str.lower() == hotel_name.lower()]
    if not hotel_info.empty:
        current_hotel = hotel_name
        description = hotel_info['hotel_description'].values[0]
        rating = hotel_info['hotel_star_rating'].values[0]
        address = hotel_info['address'].values[0]
        return f"Description: {description}\nRating: {rating}\nAddress: {address}"
    else:
        return "Hotel not found."

def get_room_types():
    global current_hotel
    if current_hotel:
        room_types = dataset.loc[dataset['similar_hotel'].str.lower() == current_hotel.lower(), 'room_type']
        if not room_types.empty:
            return "\n".join(room_types)
        else:
            return "Room types not found for this hotel."
    else:
        return "Please specify a hotel name first."

# Main function to process user queries
def process_query(user_query):
    global current_hotel
    if user_query.lower() in ["hi", "hello", "hey"]:
        return "Hello! Welcome to our hotel booking service. How can I assist you today?"
    elif user_query.lower() == "get hotel info":
        return "Sure! Please specify the hotel name for which you want to get information."
    elif user_query.lower() == "get room type":
        return get_room_types()
    else:
        return get_hotel_info(user_query.strip())

# GUI function
def chat():
    user_query = user_input_text.get("1.0", tk.END).strip()
    response = process_query(user_query)
    chat_history_text.configure(state=tk.NORMAL)
    chat_history_text.insert(tk.END, "👤 You: " + user_query + "\n")
    chat_history_text.insert(tk.END, "🤖 Bot: " + str(response) + "\n")
    chat_history_text.configure(state=tk.DISABLED)
    user_input_text.delete("1.0", tk.END)

# Create GUI
root = tk.Tk()
root.title("Hotel info chtbot")

chat_history_text = scrolledtext.ScrolledText(root, width=50, height=20, state=tk.DISABLED)
chat_history_text.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

user_input_text = tk.Text(root, width=40, height=3)
user_input_text.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=chat)
send_button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
