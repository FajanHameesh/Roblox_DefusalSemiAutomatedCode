import streamlit as st
from pathlib import Path

baseDir = Path(__file__).resolve().parent

if 'page' not in st.session_state:
    st.session_state.page = 'home'

def home():
    st.title("Roblox Defusal - Coded Algorithm")
    col1,col2,col3,col4,col5 = st.columns(5)
    col6,col7,col8,col9,col10 = st.columns(5)
    col11,col12,col13,col14,col15 = st.columns(5)
    col16,col17,col18,col19,col20 = st.columns(5)

    with col1:
        st.image(baseDir/"assets/fuse.png")

        if st.button("Fuses"):
            st.session_state.page = "fuse_page"
            st.rerun()
    with col2:
        st.image(baseDir/'assets/button.png')

        if st.button("Button"):
            st.session_state.page = "button_page"
            st.rerun()
    with col3:
        st.image(baseDir/'assets/light.png')

        if st.button('Light'):
            st.session_state.page = 'light_page'
            st.rerun() 
    with col4:
        st.image(baseDir/"assets/binary.png")

        if st.button("Binary"):
            st.session_state.page = "binary_page"
            st.rerun()
    with col5:
        st.image(baseDir/'assets/caesar.png')

        if st.button("Caesar"):
            st.session_state.page = "caesar_page"
            st.rerun()
    with col6:
        st.image(baseDir/'assets/colorcode.png')

        if st.button('ColorCode'):
            st.session_state.page = 'colorcode_page'
            st.rerun() 
    with col7:
        st.image(baseDir/"assets/hexadecimal.png")

        if st.button("Hexadecimal"):
            st.session_state.page = "hexadecimal_page"
            st.rerun()
    with col8:
        st.image(baseDir/'assets/mathematicss.png')

        if st.button("Mathematics"):
            st.session_state.page = "mathematics_page"
            st.rerun()
    with col9:
        st.image(baseDir/'assets/meter.png')

        if st.button('Meter'):
            st.session_state.page = 'meter_page'
            st.rerun() 
    with col10:
        st.image(baseDir/"assets/resistor.png")

        if st.button("Resistor"):
            st.session_state.page = "resistor_page"
            st.rerun()
    with col11:
        st.image(baseDir/'assets/temperature.png')

        if st.button("Temperature"):
            st.session_state.page = "temperature_page"
            st.rerun()
    with col12:
        st.image(baseDir/'assets/tiles.png')

        if st.button('Tiles'):
            st.session_state.page = 'tiles_page'
            st.rerun() 
    with col13:
        st.image(baseDir/'assets/timing.png')

        if st.button("Timing"):
            st.session_state.page = "timing_page"
            st.rerun()
    with col14:
        st.image(baseDir/'assets/wires.png')

        if st.button('Wires'):
            st.session_state.page = 'wires_page'
            st.rerun() 
    with col15:
        st.image(baseDir/'assets/multibutton.png')

        if st.button('multibutton'):
            st.session_state.page = 'multibutton_page'
            st.rerun() 
    with col16:
        st.image(baseDir/'assets/multibutton.png')

        if st.button('Sliders'):
            st.session_state.page = 'sliders_page'
            st.rerun() 
    with col17:
        st.image(baseDir/'assets/multibutton.png')

        if st.button('Divisibility'):
            st.session_state.page = 'divisibility_page'
            st.rerun() 
    
def fuse_page():
    from modules.fuses import fuses
    st.title('Fuses')
    inp1 = st.text_input("Colors: ")
    inp2 = st.text_input("Wired at: ")
    result = fuses(inp1,inp2)

    st.success(result)

    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()

def button_page():
    from modules.Button import button
    st.title("Button")
    inp1 = st.text_input("Color: ")
    inp2 = st.text_input("Text: ")
    st.success(button(inp2,inp1))

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

def light_page():
    from modules.light import light
    st.title("Light")
    inp1 = st.text_input("Start Color: ")
    inp2 = st.text_input("Last Serial Number: ")
    result = light(inp1,inp2)
    st.success(result)

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

def binary_page():
    from modules.binary import binary
    st.title("Binary")
    inp = st.text_input("Code: ")
    result = f'Klik {binary(inp)} kali.'
    st.success(result)

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

def caesar_page():
    from modules.caesar import caesar
    st.title("Caesar")
    inp1 = st.text_input("Code: ")
    inp2 = st.text_input("Serial Numbers: ")
    st.success(caesar(inp1,inp2))

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

def colorcode_page():
    from modules.colorcode import colorcode
    st.title("ColorCode")
    inp1 = st.text_input("Colors: ")
    inp2 = st.text_input("Text: ")
    st.success(f'Click {colorcode(inp1,inp2)} times.')

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

def hexadecimal_page():
    from modules.hexadecimal import hexa
    st.title("HexaDecimal")
    inp = st.text_input("Code: ")
    st.success(hexa(inp))

    if st.button('Back'):
        st.session_state.page = 'home'
        st.rerun()

def mathematics_page():
    from modules.mathematics import mathematicss
    st.title("Mathematics")
    inp = st.text_input("Text: ")
    st.success(mathematicss(inp))

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

def meter_page():
    from modules.meter import meter
    st.title("Meter")
    inp = st.number_input("Psi: ")
    st.success(meter(inp))

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

def resistor_page():
    from modules.Resistor import resistor
    st.title("Resistor")
    inp = st.text_input("Colors: ")
    st.success(resistor(inp))

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

def sliders_page():
    from modules.sliders import sliders
    st.title("Sliders")
    inp1 = st.text_input("Code: ")
    inp2 = st.text_input("Serial Numbers: ")
    st.success(sliders(inp1,inp2))

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

def temperature_page():
    from modules.temperature import temp
    st.title("Temperature")
    inp = st.text_input("Code: ")
    st.success(temp(inp))

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

def tiles_page():
    from modules.Tiles import tiles
    st.title("Tiles")
    inp = st.text_input("Code: ")
    st.success(tiles(inp))

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

def timing_page():
    from modules.timing import timing
    st.title("Timing")
    inp = st.text_input("Code: ")
    st.success(timing(inp))

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

def wires_page():
    from modules.wires import wires
    st.title("Wires")
    inp = st.text_input("Colors: ")
    st.success(wires(inp))

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

def multibutton_page():
    from modules.multibutton import multi
    st.title("Mutlibutton")
    inp = st.text_input("Code: ")
    st.success(multi(inp))

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

def divisibility_page():
    from modules.divisibility import divisibility
    inp = st.text_input("Number: ")
    st.success(divisibility(inp))

    if st.button("Back"):
        st.session_state.page = 'home'
        st.rerun()

if st.session_state.page == 'home':
    home()
elif st.session_state.page == 'fuse_page':
    fuse_page()
elif st.session_state.page == 'button_page':
    button_page()
elif st.session_state.page == 'light_page':
    light_page()
elif st.session_state.page == 'binary_page':
    binary_page()
elif st.session_state.page == 'caesar_page':
    caesar_page()
elif st.session_state.page == 'colorcode_page':
    colorcode_page()
elif st.session_state.page == 'hexadecimal_page':
    hexadecimal_page()
elif st.session_state.page == 'light_page':
    light_page()
elif st.session_state.page == 'mathematics_page':
    mathematics_page()
elif st.session_state.page == 'meter_page':
    meter_page()
elif st.session_state.page == 'resistor_page':
    resistor_page()
elif st.session_state.page == 'sliders_page':
    sliders_page()
elif st.session_state.page == 'temperature_page':
    temperature_page()
elif st.session_state.page == 'tiles_page':
    tiles_page()
elif st.session_state.page == 'timing_page':
    timing_page()
elif st.session_state.page == 'wires_page':
    wires_page()
elif st.session_state.page == 'multibutton_page':
    multibutton_page()
elif st.session_state.page == 'divisibility_page':
    divisibility_page()