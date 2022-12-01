

from tkinter.font import names


namelist = '''
        Coral
    Brian
    Jerod
    Tayler
    Samuel
    Keri
    Jana
    Sebastien 
    Jaycee
    Elisa
    Tori
    Deasia
    Kylah
    Dominique
    Analisa
    Kristi
    Kaylah
    Kelsey
    Jairo
    Baylie
    Felipe
    Mackenzie
    Darrius
    Kevon
    Jaren
    Colten
    London
    Saige
    Braydon
    Kyara
    Tia
    Deon
    Meghan
    Rory
    Lauryn
    Summer
    Anders
    Brissa
    Phoebe
    Alanna
    Rafael
    Margaret
    Desirae
    Kaylea
    Slade
    Sawyer
    Angelina
    Jeffrey
    Ximena
    Cale
    Annie
    Lesli
    Angelo
    Cannon
    Dameon
    Sheila
    Maranda
    Colin
    Remington
    Virginia
    Rianna
    Kim
    Zion
    Ayanna
    Kimberlee
    Augustine
    Yasmine
    Duane
    Madalyn
    Kristian
    Brookelyn
    Raven
    Dayne
    Rowan
    Jalin
    Kaleb
    Trenton
    Tristin
    Marvin
    Nadine
    Sierra
    Jake
    Joel
    Eliezer
    Shakayla
    Sherman
    Michele
    Emmett
    Mikayla
    Emanuel
    Dalia
    Nick
    Elexis
    Bailey
    Keenan
    Angel
    Amina
    Cameron
    Cristal
    Trayvon
    Sonya
    Connor
    Bo
    Oscar
    Antonio
    Abigale
    Haleigh
    Mekhi
    Shawn
    Ameer
    Leighton
    Alayna
    Mitchell
    Sana
    Madysen
    Kyleigh
    Breeanna
    Coby
    Daria
    Antoinette
    Citlali
    Jordon
    Hayden
    Stuart
    Abel
    Rocky
    Samson
    Makiya
    Makala
    Donna
    Tess
    Nicole
    Xander
    Eliza
    Demond
    Audra
    Tevin
    Keaton
    Ricardo
    Leann
    Alissa
    Dustin
    Amaya
    Linnea
    Jazlyn
    Kaeli
    Tyrique
    Yaquelin
    Erica
    Carlo
    Leslie
    Daisha
    Mateo
    Robyn
    Terry
    Leigha
    Marcos
    Alana
    Lainey
    Vaughn
    Kassandra
    Zaire
    Kaytlin
    Annemarie
    Ana
    Dayton
    Jonah
    America
    Fallon
    Marco
    Lorenzo
    Allyssa
    Leilani
    Dejuan
    Anya
    Liam
    Denisse
    Hazel
    Micheal
    Shemar
    Doris
    Reilly
    Addison
    Lazaro
    Judy
    Elliott
    Carlton
    Greyson
    Alexcia
    Blake
    Tyrone
    Maximillian
    Josephine
    Janessa
    Heather
    Heath
    Eileen
    Sammy
    Britany
    Erik
    Jay
    Dezmond
    Carson
    Daryl
    Myah
    Jamir
    Makenna
    Mykala
    Morgan
    Emelia
    Lucy
    Aislinn
    Moses
    Elisha
    Gemma
    Mickayla
    Marla
    Kaylee
    Anderson
    Patrick
    Darrin
    Graham
    Raekwon
    Kolton
    Tristen
    Tayla
    Lacie
    Jamel
    Damian
    Dorian
    Dymond
    Philip
    Trinity
    Claire
    Kaytlyn
    Dion
    Alia
    Gladys
    Briar
    Rashad
    Reagan
    Luisa
    Harry
    Charles
    Zakary
    Angeles
    Demetrius
    Shanya
    Baby
    Robin
    Selene
    Chasity
    Janine
    Aliza
    Nathanial
    Tylor
    Brennan
    Bridger
    Julius
    Jailyn
    Shawna
    Carlie
    Dajah
    Drew
    Frank
    Dane
    Nicolas
    Emmalee
    Melina
    Karley
    Marcus
    Blair
    Abbigail
    Pamela
    Kassie
    Sharon
    Gilberto
    Naomi
    Lonnie
    Jeanette
    Yazmin
    Lexus
    Stephanie
    Selena
    Cherokee
    Bradford
    Theron
    Bayleigh
    Sasha
    Shyann
    Sergio
    Abby
    Tahj
    Francisco
    Monserrat
    Mike
    Immanuel
    Darin
    Paula
    Deshawn
    Alisa
    Vladimir
    Jaelyn
    Valentin
    Babygirl
    Quincy
    Tristan
    Lillie
    Shaylee
    Alanis
    Cristina
    Ashlynn
    Leon
    Cooper
    Delia
    Martina
    Ali
    Adriel
    Keith
    Gino
    Dexter
    Joy
    Keana
    Devonta
    Kenan
    Tonya
    Bridget
    Brenna
    Sydney
    Braeden
    Alexandra
    Andrew
    Isis
    Serenity
    Shyanne
    Darian
    Easton
    Damon
    Ben
    Francesca
    Dalton
    Annika
    Jaden
    Erich
    Liana
    Valentina
    Trystan
    Sylvia
    Nadia
    Alliyah
    Julian
    Kayla
    Brylee
    Kennedy
    Madilyn
    Kendell
    Lindsay
    Marcelo
    Amira
    Moises
    Giavanna
    Damien
    Gissel
    Keona
    Maryjane
    Luca
    Kristofer
    Hattie
    Jaleel
    Shianne
    Braiden
    Shirley
    Deshaun
    Jazmine
    Mckinley
    Garrison
    Humberto
    Arthur
    Armand
    Lizbeth
    Jordy
    Jessie
    Brianna
    Alfredo
    Brody
    Jolie
    Luke
    Mariano
    Brea
    Tavion
    Tyler
    Malika
    Savana
    Kiley
    Diego
    Elle
    Juanita
    Kurt
    Maximus
    Sydnie
    Fernando
    Jacinda
    Kalen
    Raul
    Esteban
    Pedro
    Mallory
    Isabela
    Camila
    Joelle
    Jamie
    Savannah
    Natalya
    Kasandra
    Isela
    Stephen
    Menachem
    Mayra
    Tina
    Valencia
    Ingrid
    Adelaide
    Miguelangel
    Ayesha
    Trever
    Cierra
    Shaelyn
    Lionel
    Amanda
    Macie
    Kadin
    Wesley
    Carter
    Julieta
    Jose
    Ronnie
    Adamaris
    Yulisa
    Cade
    Rosemarie
    Chancellor
    Monica
    Seth
    Neha
    Esther
    Shannon
    Reed
    Marc
    Anne
    Shania
    Kole
    Jamal
    Antoine
    Alan
    Dontae
    Dahlia
    Jordin
    Franco
    Declan
    Nikolas
    Jorden
    Gisel
    Ricky
    Regina
    Jaliyah
    Yamilet
    Reid
    Frankie
    Anita
    Braden
    Saira
    Frederick
    John
    Keely
    Marquis
    Kourtney
    Johnathon
    Randolph
    Alena
    Dallas
    Joselin
    Tyrese
    Andy
    Fatima
    Aysha
    Kendra
    Gianni
    Kinsey
    Meredith
    Madelyne
    Glen
    Thaddeus
    Rebeca
    Laken
    Berenice
    Alison
    Shivani
    Justine
    Tyreke
    Devontae
    Krista
    Ryley
    Hamza
    Payton
    Galen
    Abril
    Tate
    Reese
    Samira
    Kari
    Peter
    Ryleigh
    Yusuf
    Priya
    Angelica
    Jaidyn
    Vincenzo
    Isabella
    Aidan
    Gerald
    Korbin
    Shlomo
    Guy
    Markus
    Sterling
    Vivian
    Randy
    Kerry
    Hope
    Griffin
    Alessandra
    Eleanor
    Jalen
    Drake
    Azaria
    Zoey
    Belinda
    Keegan
    Elvis
    Liberty
    Marian
    Raymundo
    Infant
    Rita
    Bernardo
    Rhianna
    Zain
    Alexis
    Maxwell
    Kalia
    Allyson
    Oswaldo
    Alden
    Malaysia
    Curtis
    Andrea
    Ryder
    Gabriel
    Lukas
    Demarcus
    Karah
    Santana
    Eduardo
    Edgar
    Selina
    Juliette
    Lucia
    Gregorio
    Elissa
    Astrid
    Brieanna
    Kevin
    Albert
    Stone
    Keanu
    Charlie
    Noe
    Muhammad
    Deborah
    Jonas
    China
    Teresa
    Tariq
    Bruno
    Donte
    Catrina
    Tristian
    Shay
    Shayna
    Alani
    Tierney
    Phoenix
    Yosef
    Estefany
    Marcel
    Simeon
    Levi
    Marie
    Beth
    Khalid
    Stephan
    Carley
    Nathaniel
    Chaz
    Gabriella
    Naya
    Cullen
    Ronald
    Tyriq
    Juan
    Daren
    Haily
    Rosalie
    Uriel
    Camden
    Ivan
    Bryant
    Joe
    Aleena
    Kyra
    Jesus
    Gonzalo
    David
    Leanne
    Rolando
    Alexandro
    Bryana
    Dean
    Estevan
    Delaney
    Terrell
    Skyler
    Angelique
    Roland
    Hanna
    Catherine
    Harlee
    Ebony
    Caiden
    Mikael
    Davin
    Paola
    Issac
    Averie
    Cortez
    Josue
    Bridgett
    Parker
    Lesley
    Gisselle
    Juliann
    Armando
    Roger
    Janaya
    Caitlyn
    Terra
    Maureen
    Ivonne
    Kasey
    Kent
    George
    Warren
    Hudson
    Dejon
    Aja
    Sunny
    Irene
    Baylor
    Truman
    Malia
    Justin
    Hakeem
    Aldo
    Sean
    Willow
    Mariah
    Abdul
    Timmy
    Markell
    Monika
    Kacie
    Danny
    Ciera
    Sherry
    Nichole
    Pierre
    Grayson
    Kaleigh
    Aimee
    Chelsie
    Corey
    Keshawn
    Jaylin
    Zack
    Benny
    Rachelle
    Barrett
    Scott
    Amalia
    Mika
    Beau
    Krystal
    Louis
    Lamar
    Clyde
    Fiona
    Kia
    Brennon
    Kameron
    Alex
    Darien
    Aaliyah
    Annalise
    Caden
    Sydni
    Lana
    Jade
    Isaiah
    Eliseo
    Felix
    Keyshawn
    Shamya
    Benton
    Bryson
    James
    Bryce
    Susana
    Karleigh
    Jamarcus
    Daquan
    Brisa
    Kalista
    Zavier
    Edwin
    Raphael
    Mauricio
    Dana
    Amara
    Brock
    Carl
    Silas
    Rosario
    Glenn
    Abbie
    Zahra
    Shamar
    Charlene
    Nyla
    Fredy
    Lacy
    Peyton
    Sophia
    Brynn
    Gissell
    Bianca
    Simon
    Brooke
    Xavier
    Jaela
    Joaquin
    Daron
    Ernesto
    Jayden
    Marissa
    Makena
    Demonte
    Hassan
    Annmarie
    Stephany
    Bryan
    Rubi
    Nayeli
    Dara
    Yamileth
    Jonathan
    Renae
    Aliana
    Jamari
    Angeline
    Jamila
    Lucille
    Michael
    Noemi
    Darrian
    Maribel
    Laurel
    Tai
    Nathalie
    Karina
    Dimitri
    Mandy
    Elena
    Katelyn
    Adrian
    Nathaly
    Jeremy
    Tyra
    Kirsten
    Maria
    Kimberley
    Kirk
    Samara
    Erick
    Charity
    Whitley
    Brittani
    Braedon
    Owen
    Jericho
    Elmer
    Jacquez
    Kerrigan
    Marquise
    Clinton
    Amirah
    Caylin
    Gretchen
    Vicky
    Annabella
    Killian
    Josh
    Nicholas
    Holden
    Douglas
    Jordan
    Andre
    Bailee
    Zariah
    Maci
    Kendrick
    Tanisha
    Christie
    Jewel
    Kristy
    Tionna
    Jayson
    Brittany
    Titus
    Tea
    Cain
    Nautica
    Orlando
    Enzo
    Omari
    Ezekiel
    Madison
    Journey
    Dajuan
    Kahlil
    Tobias
    Gavin
    Avery
    Ariel
    Deisy
    Jamya
    Evelin
    Augustus
    Tasha
    Meaghan
    Kyndall
    Hasan
    Daijah
    Lynsey
    Kirstyn
    Calista
    Taylor
    Wendy
    Deonte
    Rivka
    Nolan
    Bradly
    Keelan
    Jaylon
    Ilana
    Ashton
    Caylee
    Brayan
    Rodrigo
    Jaila
    Theodore
    Katlyn
    Stewart
    Kaitlin
    Breana
    Asya
    Porter
    Paige
    Layla
    Dandre
    Iliana
    Briley
    Brooklynn
    Shayne
    Aniya
    Ruth
    Dallin
    Shira
    Elyse
    Cristofer
    Devante
    Bennett
    Lanie
    Prince
    Edna
    Andie
    Joann
    Keandre
    Billie
    Lydia
    Alexandria
    Mallorie
    Tyson
    Cara
    Rhys
    Jaylan
    Isaias
    Carla
    Sanjana
    Janay
    Winston
    Destany
    Haven
    Keira
    Marlen
    Chassidy
    Darnell
    Latrell
    Yadira
    Danna
    Lexy
    Halle
    Presley
    Alisha
    Sahil
    Tyshawn
    Mikaela
    Gerardo
    Maxim
    Francesco
    Alyson
    Dequan
    Desiree
    Emilia
    Symone
    Adrianne
    Jase
    Crystal
    Nelson
    Kamren
    Nya
    Shaina
    Trevor
    Colt
    Chelsea
    Alysa
    Lena
    Abraham
    Jaycob
    Carrie
    Tanner
    Dorien
    Alysha
    Jaylynn
    Matthew
    Stevie
    Keyonna
    Maximiliano
    Jill
    Javion
    Chynna
    Mona
    Joseph
    Alvaro
    Gabrielle
    Leanna
    Thea
    Teagan
    Jesse
    Harris
    Dariana
    Trevin
    Ciara
    Conrad
    Haden
    Joey
    Joanna
    Stetson
    Nevin
    Javon
    Dwayne
    Cali
    Alexa
    Julia
    Alora
    Joana
    Shelby
    Marcello
    Olivia
    Laura
    Kimberly
'''

name_lst = [name.strip() for name in namelist.split('\n')]