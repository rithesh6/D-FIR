import streamlit as st
from pytezos import pytezos
import streamlit.components.v1 as components


pytezos = pytezos.using(shell='https://jakartanet.smartpy.io',
                        key='edskRv1Ac5psqCpJ5GVkYbbnJgbjmhGHU6axTVezNK41Yj8XUBNhmswzcg75MMrTDkUvBagUS8kfSsDbD2T1tafSgmsgkEaR24')
contract = pytezos.contract('KT1P1kj39a24DLFDuZpq3kLuRrXbMEjfVkcT')


def welcome():
    return "Welcome To Decentralised FIR lodging system"


def addFIR():

  uid = st.text_input("Enter your Unique aadhar Id")
  name = st.text_input("Full Name")
  fathersName = st.text_input("Father's Name")
  PhoneNumber = st.number_input(
      "Enter the Contact Number", step=1, min_value=1)
  age = st.number_input("Enter Age", step=1, min_value=1)
  gender = st.text_input("Enter Gender")
  address = st.text_input("Address")
  st.text("Place of Occurance")
  DisPs = st.text_input("Distance from the police station")
  Dirps = st.text_input("Direction from the police station")
  st.text("Date and Hour of Occurrence: ")
  Date1 = st.text_input("Enter the date of Occurrence")
  time = st.text_input("Enter the time of Occurrence in HH:MM:SS format")
  st.text("Offence")
  NoO = st.text_input("Nature of offence eg:murder, theft, rape, etc.")
  Section = st.text_input("Section")
  pop = st.text_input(
      "Particulars of the property (in case one has got stolen):")
  Doa = st.text_input("Description of the accused :")
  Dow = st.text_input(" Details of witnesses (if any)")
  Complaint = st.text_input(
      "Complaint: Briefly lay down the facts regarding the incident reported in an accurate way")

  if st.button("Register FIR"):
    a = pytezos.using(shell='https://jakartanet.smartpy.io',
                      key='edskRv1Ac5psqCpJ5GVkYbbnJgbjmhGHU6axTVezNK41Yj8XUBNhmswzcg75MMrTDkUvBagUS8kfSsDbD2T1tafSgmsgkEaR24')
    contract = a.contract('KT1P1kj39a24DLFDuZpq3kLuRrXbMEjfVkcT')

    contract.addFir(Complaint=Complaint, DisPs=DisPs, Dirps=Dirps, Dow=Dow, Date1=Date1, Doa=Doa, pop=pop, time=time, NoO=NoO, Section=Section, age=age,
                    gender=gender, name=name, fathersName=fathersName, PhoneNumber=PhoneNumber, address=address, uid=uid).with_amount(0).as_transaction().fill().sign().inject()


def ViewFirData():
  uid = st.text_input("Enter Unique aadhar Id")
  if st.button("View Records"):
    usds = pytezos.using(
        shell='https://jakartanet.smartpy.io').contract('KT1P1kj39a24DLFDuZpq3kLuRrXbMEjfVkcT')
    try:
        st.text("Name: " + usds.storage[uid]['name']())
        st.text("Father's Name:"+usds.storage[uid]['fathersName']())
        st.text("Phone Number: "+str(usds.storage[uid]['PhoneNumber']()))
        st.text("Age: "+str(usds.storage[uid]['age']()))

        st.text("Gender: "+usds.storage[uid]['gender']())

        st.text("Address: "+usds.storage[uid]['address']())

        st.text("Distance from police station where the incident took place: " +
                usds.storage[uid]['DisPs']())

        st.text("Direction from police station where the incident took place: " +
                usds.storage[uid]['Dirps']())

        st.text("Date: "+usds.storage[uid]['Date1']())

        st.text("Time: "+usds.storage[uid]['time']())

        st.text("Nature of offence: "+usds.storage[uid]['NoO']())

        st.text("Section applicable: "+usds.storage[uid]['Section']())

        st.text("Particulars of the property: "+ usds.storage[uid]['pop']())

        st.text("Description of the accused: "+usds.storage[uid]['Doa']())

        st.text("Witness: "+usds.storage[uid]['Dow']())
        st.text("Complaint: "+usds.storage[uid]['Complaint']())

    except:
        st.text("OOPS No such data found !")

def main():
    
    st.set_page_config(page_title="Decentralised FIR Records")
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
    

    st.title("Blockchain Based FIR Records")

    HtmlFile = open("af.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code)
    # st.markdown(
    #     '''<div>VADDA</div
    #     ''',
    #     unsafe_allow_html=True,
    # )

    st.markdown(
        """<p style='text-align: center;font-family:Helvetica;font-size:30px'>
                   This project greatly decreases any chances of misuse or the manipulation of the FIR Records</p>""",
            
        unsafe_allow_html=True,
    )

    st.sidebar.title("Choose your entry point")
    st.sidebar.markdown("Select the entry point accordingly:")

    algo = st.sidebar.selectbox(
        "Select the Option", options=[
            "Register FIR",
            "View FIR Data"
        ]
    )

    if algo == "Register FIR":
        addFIR()
    if algo == "View FIR Data":
        ViewFirData()


if __name__ == "__main__":
  main()
