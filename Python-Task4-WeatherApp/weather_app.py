from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests


def data_get():
    city = city_name.get().strip()
    if city == "":
        messagebox.showwarning("Warning", "Please select a city.")
        return

    API_key = "da309f06856ae40e2e4419b4846e0119"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code != 200:
            messagebox.showerror(
                "Error",
                data.get("message", "Unable to fetch weather data.")
            )
            return

        weather_label_1.config(
            text=data["weather"][0]["main"])
        
        w_descrip_label_1.config(
            text=data["weather"][0]["description"])

        temp_label_1.config(
            text=f"{data['main']['temp'] - 273.15:.2f} °C")

        temp_min_label_1.config(
            text=f"{data['main']['temp_min'] - 273.15:.2f} °C")

        temp_max_label_1.config(
            text=f"{data['main']['temp_max'] - 273.15:.2f} °C")

        feel_label_1.config(
            text=f"{data['main']['feels_like'] - 273.15:.2f} °C")

        pre_label_1.config(
            text=f"{data['main']['pressure']} hPa")
        
        hum_label_1.config(
            text=f"{data['main']['humidity']} %")
        
        visi_label_1.config(
            text=f"{data['visibility'] / 1000:.1f} km")
        
        speed_label_1.config(
            text=f"{data['wind']['speed']} m/s")

    except requests.exceptions.RequestException:
        messagebox.showerror(
            "Network Error",
            "Please check your internet connection.")


win = Tk()

win.title("My Weather")
win.config(bg="#00b0ff")
win.geometry("500x660")

name_label = Label(win,text = "Basic Weather App",font = ("Time New Roman",30, "bold"))
name_label.place(x=50,y=50,height=50,width=400)

city_name= StringVar()
list_name = india_cities = [
    # Andaman and Nicobar Islands
    "Port Blair",
    # Andhra Pradesh
    "Anantapur",
    "Chittoor",
    "Eluru",
    "Guntur",
    "Kakinada",
    "Kurnool",
    "Nellore",
    "Ongole",
    "Rajahmundry",
    "Tirupati",
    "Vijayawada",
    "Visakhapatnam",
    "Vizianagaram",
    # Arunachal Pradesh
    "Itanagar",
    "Naharlagun",
    "Pasighat",
    "Tawang",
    # Assam
    "Dibrugarh",
    "Guwahati",
    "Jorhat",
    "Nagaon",
    "Silchar",
    "Tezpur",
    "Tinsukia",
    # Bihar
    "Arrah",
    "Begusarai",
    "Bhagalpur",
    "Darbhanga",
    "Gaya",
    "Muzaffarpur",
    "Patna",
    "Purnia",
    # Chandigarh
    "Chandigarh",
    # Chhattisgarh
    "Bhilai",
    "Bilaspur",
    "Durg",
    "Korba",
    "Raipur",
    "Rajnandgaon",
    # Dadra and Nagar Haveli and Daman and Diu
    "Daman",
    "Diu",
    "Silvassa",
    # Delhi (NCT)
    "Delhi",
    "New Delhi",
    # Goa
    "Margao",
    "Panaji",
    "Vasco da Gama",
    # Gujarat
    "Ahmedabad",
    "Anand",
    "Bhavnagar",
    "Gandhinagar",
    "Jamnagar",
    "Junagadh",
    "Rajkot",
    "Surat",
    "Vadodara",
    # Haryana
    "Ambala",
    "Faridabad",
    "Gurugram",
    "Hisar",
    "Karnal",
    "Panipat",
    "Rohtak",
    # Himachal Pradesh
    "Dharamshala",
    "Mandi",
    "Shimla",
    "Solan",
    # Jammu and Kashmir
    "Anantnag",
    "Baramulla",
    "Jammu",
    "Srinagar",
    "Udhampur",
    # Jharkhand
    "Bokaro Steel City",
    "Dhanbad",
    "Hazaribagh",
    "Jamshedpur",
    "Ranchi",
    # Karnataka
    "Ballari",
    "Belagavi",
    "Bengaluru",
    "Davangere",
    "Hubballi",
    "Kalaburagi",
    "Mangaluru",
    "Mysuru",
    "Shivamogga",
    "Tumakuru",
    # Kerala
    "Alappuzha",
    "Kannur",
    "Kochi",
    "Kollam",
    "Kottayam",
    "Kozhikode",
    "Palakkad",
    "Thiruvananthapuram",
    "Thrissur",
    # Ladakh
    "Kargil",
    "Leh",
    # Lakshadweep
    "Kavaratti",
    # Madhya Pradesh
    "Bhopal",
    "Gwalior",
    "Indore",
    "Jabalpur",
    "Ratlam",
    "Rewa",
    "Sagar",
    "Satna",
    "Ujjain",
    # Maharashtra
    "Ahmednagar",
    "Akola",
    "Amravati",
    "Aurangabad",
    "Chandrapur",
    "Jalgaon",
    "Kolhapur",
    "Latur",
    "Mumbai",
    "Nagpur",
    "Nanded",
    "Nashik",
    "Navi Mumbai",
    "Pune",
    "Solapur",
    "Thane",
    # Manipur
    "Imphal",
    # Meghalaya
    "Shillong",
    "Tura",
    # Mizoram
    "Aizawl",
    # Nagaland
    "Dimapur",
    "Kohima",
    # Odisha
    "Balasore",
    "Berhampur",
    "Bhubaneswar",
    "Cuttack",
    "Puri",
    "Rourkela",
    "Sambalpur",
    # Puducherry
    "Karaikal",
    "Puducherry",
    # Punjab
    "Amritsar",
    "Bathinda",
    "Jalandhar",
    "Ludhiana",
    "Mohali",
    "Pathankot",
    "Patiala",
    # Rajasthan
    "Ajmer",
    "Alwar",
    "Bhilwara",
    "Bikaner",
    "Jaipur",
    "Jodhpur",
    "Kota",
    "Sikar",
    "Udaipur",
    # Sikkim
    "Gangtok",
    # Tamil Nadu
    "Chennai",
    "Coimbatore",
    "Erode",
    "Madurai",
    "Nagercoil",
    "Salem",
    "Thanjavur",
    "Thoothukudi",
    "Tiruchirappalli",
    "Tirunelveli",
    "Tiruppur",
    "Vellore",
    # Telangana
    "Hyderabad",
    "Karimnagar",
    "Khammam",
    "Mahbubnagar",
    "Nizamabad",
    "Warangal",
    # Tripura
    "Agartala",
    # Uttar Pradesh
    "Agra",
    "Aligarh",
    "Ayodhya",
    "Bareilly",
    "Firozabad",
    "Ghaziabad",
    "Gorakhpur",
    "Jhansi",
    "Kanpur",
    "Lucknow",
    "Mathura",
    "Meerut",
    "Moradabad",
    "Noida",
    "Prayagraj",
    "Saharanpur",
    "Varanasi",
    # Uttarakhand
    "Dehradun",
    "Haridwar",
    "Haldwani",
    "Nainital",
    "Rishikesh",
    "Roorkee",
    # West Bengal
    "Asansol",
    "Bardhaman",
    "Durgapur",
    "Howrah",
    "Kharagpur",
    "Kolkata",
    "Malda",
    "Siliguri",
]
combo_box = ttk.Combobox(win,text = "Basic Weather App",values =list_name,font = ("Time New Roman",13, "bold"),textvariable=city_name)
combo_box.place(x=100,y=120,height=30,width=300)

#1
weather_label = Label(win,text = "Weather Climate ",font = ("Time New Roman",10))
weather_label.place(x=110,y=230,height=30,width=140)

weather_label_1 = Label(win,text = "",font = ("Time New Roman",10))
weather_label_1.place(x=260,y=230,height=30,width=140)

#2
w_descrip_label = Label(win,text = "Weather Description ",font = ("Time New Roman",10))
w_descrip_label.place(x=110,y=270,height=30,width=140)

w_descrip_label_1 = Label(win,text = "",font = ("Time New Roman",10))
w_descrip_label_1.place(x=260,y=270,height=30,width=140)

#3
temp_label = Label(win,text = "Temperature ",font = ("Time New Roman",10))
temp_label.place(x=110,y=310,height=30,width=140)

temp_label_1 = Label(win,text = "",font = ("Time New Roman",10))
temp_label_1.place(x=260,y=310,height=30,width=140)

#4
temp_min_label = Label(win,text = "Minimim Temperature ",font = ("Time New Roman",10))
temp_min_label.place(x=110,y=350,height=30,width=140)

temp_min_label_1 = Label(win,text = "",font = ("Time New Roman",10))
temp_min_label_1.place(x=260,y=350,height=30,width=140)

#5
temp_max_label = Label(win,text = "Maximum Temperature ",font = ("Time New Roman",10))
temp_max_label.place(x=110,y=390,height=30,width=140)

temp_max_label_1 = Label(win,text = "",font = ("Time New Roman",10))
temp_max_label_1.place(x=260,y=390,height=30,width=140)

#6
feel_label = Label(win,text = "Feel like",font = ("Time New Roman",10))
feel_label.place(x=110,y=430,height=30,width=140)

feel_label_1 = Label(win,text = "",font = ("Time New Roman",10))
feel_label_1.place(x=260,y=430,height=30,width=140)

#7
pre_label = Label(win,text = "Pressure",font = ("Time New Roman",10))
pre_label.place(x=110,y=470,height=30,width=140)

pre_label_1 = Label(win,text = "",font = ("Time New Roman",10))
pre_label_1.place(x=260,y=470,height=30,width=140)

#8
hum_label = Label(win,text = "Humidity",font = ("Time New Roman",10))
hum_label.place(x=110,y=510,height=30,width=140)

hum_label_1 = Label(win,text = "",font = ("Time New Roman",10))
hum_label_1.place(x=260,y=510,height=30,width=140)

#9
visi_label = Label(win,text = "Visibility",font = ("Time New Roman",10))
visi_label.place(x=110,y=550,height=30,width=140)

visi_label_1 = Label(win,text = "",font = ("Time New Roman",10))
visi_label_1.place(x=260,y=550,height=30,width=140)

#10
speed_label = Label(win,text = "Wind Speed",font = ("Time New Roman",10))
speed_label.place(x=110,y=590,height=30,width=140)

speed_label_1 = Label(win,text = "",font = ("Time New Roman",10))
speed_label_1.place(x=260,y=590,height=30,width=140)


#Button
button_check = Button(win,text = "Check",font = ("Time New Roman",10, "bold"),command=data_get)
button_check.place(x=210,y=160,height=30,width=80)

win.mainloop()