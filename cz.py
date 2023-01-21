import streamlit as st
import datetime

def get_zodiac_sign(year):
    zodiac = ["Rat-鼠", "Ox-牛", "Tiger-虎", "Rabbit-兔", "Dragon-龍", "Snake-蛇", "Horse-馬", "Goat-羊", "Monkey-猴", "Rooster-雞", "Dog-狗", "Pig-豬"]
    return zodiac[(year - 4) % 12]

def main():
    st.title("Which Chinese Zodiac Sign You Belong?")
    birth_year = st.number_input("Enter your birth year:", step=1)
    zodiac_sign = get_zodiac_sign(birth_year)
    st.write("Your Chinese Zodiac sign is:", zodiac_sign)


if __name__ == "__main__":
    main()