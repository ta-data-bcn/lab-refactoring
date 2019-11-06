import random
import turtle
#1st create a list to know the possibilities of words
words = ["contact","business","online","first","services","click","service","price","people","state","email","health","world","products","music","should","product","system","policy","number","please","support","message","after","software","video","where","rights","public","books","school","through","links","review","years","order","privacy","items","company","group","under","general","research","january","reviews","program","games","could","great","united","hotel","center","store","travel","comments","report","member","details","terms","before","hotels","right","because","local","those","using","results","office","national","design","posted","internet","address","within","states","phone","shipping","reserved","subject","between","forum","family","based","black","check","special","prices","website","index","being","women","today","south","project","pages","version","section","found","sports","house","related","security","county","american","photo","members","power","while","network","computer","systems","three","total","place","download","without","access","think","north","current","posts","media","control","water","history","pictures","personal","since","guide","board","location","change","white","small","rating","children","during","return","students","shopping","account","times","sites","level","digital","profile","previous","events","hours","image","title","another","shall","property","class","still","money","quality","every","listing","content","country","private","little","visit","tools","reply","customer","december","compare","movies","include","college","value","article","provide","source","author","press","learn","around","print","course","canada","process","stock","training","credit","point","science","advanced","sales","english","estate","select","windows","photos","thread","category","large","gallery","table","register","however","october","november","market","library","really","action","start","series","model","features","industry","human","provided","required","second","movie","forums","march","better","yahoo","going","medical","friend","server","study","staff","articles","feedback","again","looking","issues","april","never","users","complete","street","topic","comment"]
#Dictionary to do a hint (in the last attempt)
dict_hints = {"contact":"contacto","business":"negocio","online":"en línea","first":"primero","services":"servicios","click":"hacer clic","service":"Servicio","price":"precio","people":"personas","state":"estado","email":"correo electrónico","health":"salud","world":"mundo","products":"productos","music":"música","should":"debería","product":"producto","system":"sistema","policy":"política","number":"número","please":"Por favor","support":"apoyo","message":"mensaje","after":"después","software":"software","video":"vídeo","where":"dónde","rights":"derechos","public":"público","books":"libros","school":"colegio","through":"mediante","links":"Enlaces","review":"revisión","years":"años","order":"orden","privacy":"intimidad","items":"artículos","company":"empresa","group":"grupo","under":"debajo","general":"general","research":"investigación","january":"enero","reviews":"comentarios","program":"programa","games":"juegos","could":"podría","great":"Excelente","united":"unido","hotel":"hotel","center":"centrar","store":"Tienda","travel":"viaje","comments":"comentarios","report":"reporte","member":"miembro","details":"detalles","terms":"condiciones","before":"antes de","hotels":"hoteles","right":"derecho","because":"porque","local":"local","those":"aquellos","using":"utilizando","results":"resultados","office":"oficina","national":"nacional","design":"diseño","posted":"al corriente","internet":"Internet","address":"habla a","within":"dentro","states":"estados","phone":"teléfono","shipping":"Envío","reserved":"reservado","subject":"tema","between":"Entre","forum":"foro","family":"familia","based":"establecido","black":"negro","check":"cheque","special":"especial","prices":"precios","website":"sitio web","index":"índice","being":"siendo","women":"mujer","today":"hoy","south":"sur","project":"proyecto","pages":"paginas","version":"versión","section":"sección","found":"encontró","sports":"Deportes","house":"casa","related":"relacionado","security":"seguridad","county":"condado","american":"americano","photo":"foto","members":"miembros","power":"poder","while":"mientras","network":"red","computer":"computadora","systems":"sistemas","three":"Tres","total":"total","place":"sitio","download":"descargar","without":"sin","access":"acceso","think":"pensar","north":"norte","current":"actual","posts":"publicaciones","media":"medios de comunicación","control":"controlar","water":"agua","history":"historia","pictures":"imágenes","personal":"personal","since":"ya que","guide":"guía","board":"tablero","location":"ubicación","change":"cambio","white":"blanco","small":"pequeña","rating":"clasificación","children":"niños","during":"durante","return":"regreso","students":"estudiantes","shopping":"compras","account":"cuenta","times":"veces","sites":"sitios","level":"nivel","digital":"digital","profile":"perfil","previous":"anterior","events":"eventos","hours":"horas","image":"imagen","title":"título","another":"otro","shall":"deberá","property":"propiedad","class":"clase","still":"todavía","money":"dinero","quality":"calidad","every":"cada","listing":"listado","content":"contenido","country":"país","private":"privado","little":"pequeño","visit":"visitar","tools":"herramientas","reply":"respuesta","customer":"cliente","december":"diciembre","compare":"comparar","movies":"películas","include":"incluir","college":"Universidad","value":"valor","article":"artículo","provide":"proporcionar","source":"fuente","author":"autor","press":"prensa","learn":"aprender","around":"alrededor","print":"impresión","course":"curso","canada":"Canadá","process":"proceso","stock":"valores","training":"formación","credit":"crédito","point":"punto","science":"Ciencias","advanced":"avanzado","sales":"ventas","english":"Inglés","estate":"inmuebles","select":"seleccionar","windows":"ventanas","photos":"fotos","thread":"hilo","category":"categoría","large":"grande","gallery":"galería","table":"mesa","register":"registro","however":"sin embargo","october":"octubre","november":"noviembre","market":"mercado","library":"biblioteca","really":"De Verdad","action":"acción","start":"comienzo","series":"serie","model":"modelo","features":"caracteristicas","industry":"industria","human":"humano","provided":"previsto","required":"necesario","second":"segundo","movie":"película","forums":"foros","march":"marzo","better":"mejor","yahoo":"yahoo","going":"yendo","medical":"médico","friend":"amigo","server":"servidor","study":"estudiar","staff":"personal","articles":"artículos","feedback":"realimentación","again":"de nuevo","looking":"mirando","issues":"cuestiones","april":"abril","never":"Nunca","users":"los usuarios","complete":"completar","street":"calle","topic":"tema","comment":"comentario"}
cpu_chose = random.choice(words)
#number of attempts to finish the game.
limit_attempts=9
#increasing, to track how many attempts does the player take to guess the word
attempts=0
#increasing, as long as there are guesses
correct_letters=0
print("Hello!!! Welcome to the Hangman Game by Maria. The objective of the game is: \n     - Guess the word"
      
      "\nThat's the only objective, easy right?"
      "\nWell, let's see!!! You will have to guess the word from a list of +200 words, ready???"
      "\nA little, detail: "
      "\n    · You only have 9 attempts, each time you enter an incorrect letter, you will have 1 attempt left, hurry up and don't hang the poor man :("
      "\nAfter guessing/failing to guess one word you will be able to guess the word but if you introduce the incorrect word, you lose!!!"
      "\n"
      "\nI wish you the best of luck - Maria (Game Designer)"
      "\n"
      "---------------------------------"
      "\n"
      "\n")
print(f"The word you have to guess has {len(cpu_chose)} letters")
#List of word created to transform it into a hashed list (con guiones).
intro_list = list(cpu_chose)

#List created to check where the correct letter goes.
check_list=list(cpu_chose)

#The main challenges of hangman were when there are repeated letters and the order where it's printed. The best idea was to access it through index but it doesn't work with repeated values and hence, creating a dictionary of an enumerate is the best thing to do.
dict_cpu_chose = dict(enumerate(cpu_chose))

#Transformation of list into an empty _ list.
for i in range(len(intro_list)):
    intro_list[i]="__"
print(intro_list)
print("Let the games begin!!!")

#prints drawing of hangman
def hangman ():
    if attempts == 1:
        turtle.penup()
        turtle.setposition(-200,-100)
        turtle.pendown()
        turtle.setheading(90)
        turtle.fd(400)

    elif attempts == 2:
        turtle.setheading(0)
        turtle.fd(300)

    elif attempts == 3:
        turtle.setheading(270)
        turtle.fd(70)

    elif attempts == 4:
        turtle.penup()
        turtle.setheading(180)
        turtle.fd(0)
        turtle.pendown()
        turtle.circle(30)
        turtle.penup()
        turtle.setheading(270)
        turtle.fd(60)
        turtle.pendown()

    elif attempts == 5:
        turtle.fd(100)

    elif attempts == 6:
        turtle.setheading(90)
        turtle.fd(50)
        turtle.setheading(0)
        turtle.fd(50)

    elif attempts == 7:
        turtle.back(100)

    elif attempts == 8:
        turtle.fd(50)
        turtle.setheading(270)
        turtle.fd(50)
        turtle.setheading(0)
        turtle.fd(50)

    else:
        turtle.back(100)

#Guess a letter: It gathers the guess (checking and formating to the correct format
def guessletter():
    while True:
        p_guess = input("Make your guess, tell me a letter: ")
        p_guess=p_guess.lower()

        if p_guess.isalpha():
            return p_guess

        else:
            print("Sorry I don't understand you, enter another letter :(")


#Confirmation of guessing the word
def guesswordconsent():
    while True:
        p_guess1=input("\nDo you want to try to guess the word? Y, N: ")

        if p_guess1.isalpha():

            if p_guess1.lower() in ["yes", "y", "si", "sí", "yas", "s"]:
                p_guess1="yes"
                return p_guess1

            elif p_guess1.lower() in ["no", "n", "nou"]:
                p_guess1="no"
                return p_guess1

            else:
                print("Sorry I don't understand your answer, you have to type Y or N: ")

        else:
            print("-------------Sorry I don't understand you, enter Y or N")


#Try to guess the word
def guessword():
    while True:
        p_guess=input("\nEnter your guess of the word: ")
        p_guess=p_guess.lower()

        if p_guess.isalpha():
            return p_guess

        else:
            print("Sorry I don't understand you, enter another letter")

#Checker, it will run as long as correct letters < length of lista to be filled and as long as there are attempts
while correct_letters<len(intro_list) and attempts<(limit_attempts-1):
    user_letter = guessletter()

    if user_letter in check_list:
            for i,j in dict_cpu_chose.items():

                if dict_cpu_chose[i] == user_letter:
                    intro_list[i] = user_letter

            correct_letters += 1
            print(intro_list)
            print(f"CORRECT! you have {limit_attempts-attempts} attempts left.")

            if "__" in intro_list and guesswordconsent()=="yes" :
                if guessword() == cpu_chose:
                    correct_letters=len(intro_list)

                else:
                    attempts=10

    else:
        attempts+=1
        print(f"INCORRECT! you have {limit_attempts-attempts} attempts left.")
        print(intro_list)
        hangman()
        if guesswordconsent() == "yes":
            if guessword() == cpu_chose:
                correct_letters = len(intro_list)

            else:
                attempts = 10
else:
    if correct_letters<len(intro_list) and attempts == 8:
        print("LAST ATTEMPT!! Hey, look I see that you are having a problem, this is a hint for you and that's... the translation to Spanish: ", dict_hints[cpu_chose] )
        if guessword() == cpu_chose:
            correct_letters = len(intro_list)
            print("Congrats, you have won!!!!")

        else:
            attempts == 10
            print("YOU LOSE!!!")
            hangman()

    elif correct_letters==len(intro_list) and attempts <= limit_attempts:
        print("Congrats, you have won!!!!")

    else:
        print("Maria , you have done something wrong")

print("The correct word was: ", cpu_chose)






