# Ashkan Ghomizadeh Thursdays 14:00 - 18:00
# BMI FUNCTION (SESSION 3)
def bmi_info(jerme_karbar, ghadde_karbar):
    bmi_e_karbar = jerme_karbar / (ghadde_karbar**2)
    if bmi_e_karbar < 16.5:
        print(f'''Kamboode vazne shadid dari
Az kare va roghan be soorate roozane estefade kon
{bmi_e_karbar}''')
    elif bmi_e_karbar >= 16.5 and bmi_e_karbar < 18.5:
        print(f"Kambood vazn dari \n\
Carbohydrate ro be onvane base e zendegi gharar bede \n\
{bmi_e_karbar}")
    elif bmi_e_karbar >= 18.5 and bmi_e_karbar < 25:
        print(f'''Vazne ideali dari
Kari ke az dastemoon bar miad tabrik goftan be shomast
{bmi_e_karbar}''')
    elif 25 <= bmi_e_karbar < 30:
        print(f'''Ezafe vazn dari
Ye sar be bashgah bezan sham ham bikhial sho joone man
{bmi_e_karbar}''')
    elif 30 <= bmi_e_karbar < 35:
        print(f'''Chaghie noe 1 dari
Sham ke maaloume nahar ham bikhial sho
{bmi_e_karbar}''')
    elif bmi_e_karbar >= 35 and bmi_e_karbar < 40:
        print(f'''Chaghie noe 2 dari dooste man
Mokhlesetam hastim vali kollan chizi nakhor
{bmi_e_karbar}''')
    else:
        print(f'''CHAGHIE NOE 3
OTAGHE AMAL BI BORO BARGARD
{bmi_e_karbar}''')
bmi_info(float(input('''Salam dooste man
Jermet ro be Kilogram vared kon \n''')), float(input('''Vaysa hanooz karet daram
Ghaddet ham be meter vared kon \n''')))
