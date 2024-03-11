
# Gedöns-import

import random
from random import choices
import locale
import time
import os
import sys
import colorama
from colorama import *
init(autoreset=False)


# Definitionen

def warten():
    time.sleep(0.8)

def warten2():
    time.sleep(5)

def warten3():
    time.sleep(4)


def clear():
    os.system("cls" if os.name == "nt"
              else "clear"
              )

# Gameplay
if __name__ == "__main__":

    while True:

        def raum_start1():
            warten()
            print (Fore.GREEN + "\nWillkommen bei ZEIT DER ZÜNFTE: SCHAFES BRUDER! \n \n")
            warten3()
            print("Dies ist das erste Mini-Abenteuer im Zeit-Der-Zünfte-System von Vitali Hänisch. \n")
            warten2()
            print("Es ist ein kurzes Textabenteuer, das mit Python 3 erstellt wurde und zu Testzwecken dient – sowohl fürs Programmieren als auch für das System selbst. :) \n")
            warten2()
            print("Hier sind die Regeln: An vielen Stellen der Geschichte wirst du aufgerufen, eine Antwort einzugeben. \n")
            warten2()
            print("Bitte tu dies nach den Regeln der deutschen Sprache. \n")
            warten2()
            print("Die möglichen Antworten sind dir in diesem Abenteuer meistens vorgegeben, bitte wähle eine davon aus.\n")
            warten2()
            print("In der Ausgestaltung hast du allerdings freie Hand.\n")
            warten2()
            print("Wenn die Aufforderung etwa 'willst du gehen oder bleiben?' lautet, fühl dich frei, mit der konkreten Formulierung zu experimentieren.\n Bedenke allerdings, dass das Spiel auf bestimmte Schlüsselwörter achtet.\n")
            warten2()
            print("Zum guten Ton würde aber zum Beispiel eine Antwort wie 'ich gehe.' bzw. 'ich bleibe.' ohne die Anführungszeichen gehören.\n")
            warten2()
            raum_start2()

        def raum_start2():
            befehl = input("Testen wir das doch gleich mal aus! Gib 'Spiel starten' ein, um fortzufahren. \n >").strip().lower()
            if "start" in befehl:
                warten()
                print("\nPrima! Dann legen wir los. \n \n")
                warten2()
                raum_start2_1()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")
                raum_start2()

        def raum_start2_1():
            befehl = input("Willst du ein paar Tipps zu diesem Spiel erfahren? (Optionen: ja, nein)\n > ").lower()
            if "ja" in befehl:
                warten3()
                print("\nIn dieser Geschichte spielst du als Olig Schäferstund, ein Bauer aus einem kleinen nicht näher bestimmten Dorf irgendwo im Nordland-Imperium der Spielwelt, Yarus.\n")
                warten2()
                print("Die Geschichte entwickelt sich abhängig von deinen Antworten.\n")
                warten2()
                print("Manche Ereignisse werden aber – wie in fast jedem Rollenspielsystem, und diesem Abenteuer liegt eines zugrunde – mit einem Würfelwurf entschieden. \n")
                warten2()
                print("Überlege also gut, was du tust. \n")
                warten2()
                print("Aber wo wir gerade dabei sind: Mach das Programmfenster ein bisschen breiter, um den Text ordentlich lesen zu können.\n")
                warten2()
                print("Und ansonsten... Mach's dir bequem, hol dir was zu trinken,\nmach am besten irgendeine 'dungeon-taugliche' Musik deiner Wahl an, und genieße das Amateur-Therater.\n")
                warten2()
                print("Und damit geht unser imaginärer Vorhang auf...\n \n")
                warten2()
                raum_start3()
            elif "nein" in befehl:
                warten3()
                print("\nDann geht unser imaginärer Vorhang jetzt auf...\n")
                warten3()
                raum_start3()
                pass
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")
                pass
                warten2()
                raum_start2_1()


        def raum_start3():
            befehl=input("Gib nun 'weiter' ein, um das Abenteuer zu beginnen.\n > ").lower()
            if befehl=="weiter":
                warten2()
                raum_start4()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")
                raum_start3()


        def raum_start4():
            print("\n \nDu spürst, wie deine Beine langsam müde werden. \n")
            warten2()
            print("Seit Sonnenaufgang bist du schon unterwegs, auf der Suche nach deinem Schaf, Dolly. \n")
            warten2()
            print("Du kannst dir nicht erklären, wer sie gestohlen hat. \n")
            warten2()
            print("Oder warum. \n")
            warten2()
            print("Dass man sie gestohlen hat, steht jedoch außer Frage. \n")
            warten2()
            print("Du hast den Stall gut abgeschlossen und gesichert, alleine wäre sie nicht ausgebrochen. \n")
            warten3()
            print("Als einfacher Bauer kannst du dir auch kein neues Schaf leisten. \n")
            warten2()
            print("Der Winter naht, du brauchst die Wolle. \n")
            warten2()
            print("Dabei bist du dir noch nicht sicher, wofür genau. \n")
            warten2()
            print("Etwas Neues zum Überziehen wäre sicherlich praktisch.\n")
            warten2()
            print("Aber du kennst auch genug Leute, die dafür eine ganze Handvoll Ran ausgeben würden. \n")
            warten2()
            print("Vielleicht sogar einen ganzen Bur! \n")
            warten2()
            print("Das ist eine Menge Geld. Vielleicht würde die Wolle aber auch für Beides reichen, du hast ja nicht umsonst das fluffigste Schaf im ganzen Dorf. \n")
            warten2()
            print("Vielleicht sogar im ganzen Imperium, wenn man dich fragt.\n")
            warten3()
            print("Bis jetzt fehlt von Dolly aber jede Spur. \n")
            warten2()
            print("Langsam fragst du dich, ob du sie überhaupt noch finden kannst. \n")
            warten3()
            raum_start5()

        def raum_start5():
            befehl = input("Willst du noch einen letzten Versuch wagen? (ja, nein)\n > ").lower().strip()
            if befehl == "nein":
                print("Tja… Die Suche ist wohl zwecklos. \n")
                warten2()
                print("Du glaubst nicht, dass du Dolly noch finden wirst. \n")
                warten2()
                print("Außerdem hast du noch andere Tiere, die versorgt werden müssen. \n")
                warten2()
                print("So traurig das auch ist – Dolly ist weg. \n")
                warten2()
                print("Ein weiterer unglücklicher Tag im Leben eines Bauern. \n")
                warten2()
                print("Aber gut, das Leben geht weiter, und den Winter kriegt man schon irgendwie überstanden, nicht wahr? \n  \n")
                warten2()
                print("Ende \n")
                warten2()
                befehl = input("Willst du noch einmal spielen?\n > ").lower()
                if befehl == "ja":
                    raum_start4()
                elif befehl == "nein":
                    quit()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                    raum_start5()
            elif befehl == "ja":
                print("\nEinen letzten Versuch willst du noch wagen. \n")
                warten2()
                print("Du strengst dich an und lässt einen genauen Blick über das Feld schweifen. \n")
                warten2()
                print("Zum Glück ist es nicht das erste Mal, dass du ein Tier suchst. \n")
                warten2()
                print("Dein Blick ist für solche Dinge eigentlich gut trainiert. \n")
                warten3()
                print("[Willkommen bei deinem ersten Fertigkeitswurf des Spiels.]\n")
                warten2()
                print("[Dieser Wurf testet deine Wahrnehmung. Kannst du irgendwelche Spuren erkennen, um dein Schaf zu finden?]\n")
                warten2()
                print("[Fertigkeitswürfe werden mit einem 12-seitigen Würfel (W12) abgelegt. Dein Charakter hat einen Bonus, um etwas mit den Augen zu erkennen. Bei einem Wurf wird dieser auf das Ergebnis angerechnet.] \n ")
                warten2()
                befehl = input("[Gib nun 'würfeln ein' ein, um den Wurf abzulegen.] \n > ")
                if befehl == "würfeln".lower():
                    #spieler.wurf_w12()
                    warten2()
                    print("Bonus: " + str(int(spieler.grips/2) + spieler.augen) + "\n")
                    warten2()
                    #spieler.wurf_erkennen()
                    warten2()
                    if spieler.wurf_erkennen() < 10:
                        print("\n[MISSERFOLG] \n")
                        warten2()
                        print("Tja… Die Suche ist wohl zwecklos. \n")
                        warten2()
                        print("Du glaubst nicht, dass du Dolly noch finden wirst. \n")
                        warten2()
                        print("Außerdem hast du noch andere Tiere, die versorgt werden müssen. \n")
                        warten2()
                        print("So traurig das auch ist – Dolly ist weg. \n")
                        warten2()
                        print("Ein weiterer unglücklicher Tag im Leben eines Bauern. \n")
                        warten2()
                        print("Aber gut, das Leben geht weiter, und den Winter kriegt man schon irgendwie überstanden, nicht wahr?\n")
                        warten2()
                        print("Ende \n")
                        warten2()
                        befehl = input("Willst du noch einmal spielen?\n > ").lower()
                        if befehl == "ja":
                            warten2()
                            raum_start4()
                        elif befehl == "nein":
                            quit()
                        else:
                            print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                            raum_start5()
                    else:
                        print("[ERFOLG] \n")
                        warten2()
                        print("Und als es schien, es gebe keine Hoffnung mehr, entdeckst du etwas: Spuren! \n")
                        warten()
                        print("Natürlich sind Spuren auf einem Waldweg nichts Besonderes, aber so große Spuren können eigentlich nur Orks oder Sim’iari hinterlassen, und Letztere lassen sich hier nicht blicken. \n")
                        warten2()
                        print("Und das aus gutem Grund.\n")
                        warten2()
                        print("In der Stadt mögen sie inzwischen anerkannte Untertanen des Imperiums sein. \n")
                        warten2()
                        print("Hier auf dem Land haben die Leute aber noch nicht vergessen, was sie hier vor noch gar nicht so langer Zeit getan haben. \n")
                        warten2()
                        print("Aber gut, sich darüber zu beklagen bringt nichts. \n")
                        warten2()
                        print("Dann musst du dem mutmaßlichen Entführer eben folgen und Dolly zurückholen. \n")
                        warten2()
                        print("Die Spuren führen zu einer großen Höhle.\n")
                        warten2()
                        print("Die 'Säuselhöhle', wie man sie nennt.\n")
                        warten2()
                        print("Eigentlich kennst du sie gut, früher war sie ein beliebter Spielort für Kinder. \n")
                        warten2()
                        print("Dann kam der Vorfall mit Maika und… Naja, egal, unangenehme Erinnerungen kannst du gerade nicht gebrauchen. \n")
                        warten2()
                        print("Fakt ist aber: Du warst lange nicht mehr da.\n")
                        warten2()
                        print("Vieles hat sich verändert, und vielleicht täuscht dich auch dein Gedächtnis. \n")
                        warten2()
                        print("Bist du überhaupt dafür ausgerüstet, hineinzugehen? Ein Seil, eine Axt und eine Fackel samt Zeug zum Anzünden, mehr hast du momentan nicht am Leib. \n")
                        warten2()
                        print("Vielleicht solltest du erst deine Rüstung anlegen und dich besser vorbereiten, und dann zurückkehren? \n")
                        warten2()
                        print("Dann wiederum, vielleicht ist es bis dahin zu spät! \n")
                        warten2()
                        print("Wer weiß, was der Unhold mit der armen Dolly anstellen will? \n")
                        warten2()
                        print("Außerdem wird es langsam dunkel. Deine Augen werden in der Höhle nicht viel erkennen. \n")
                        warten2()
                        print("Deine Fackel würde das Problem beheben, aber falls du schnell sein oder kämpfen musst, könnte es zum Problem werden. \n")
                        warten2()
                        print("Oder… Moment, weißt du noch, wie dieser eine Zauber ging? \n")
                        warten2()
                        print("Klar, du bist kein Zauberer, aber du hast mal diesen einen Typen von der Akademie eine Weile mietfrei bei dir wohnen lassen, als er sein Studiengedöns durchgeführt hat.\n")
                        warten2()
                        print("Aus Dankbarkeit hat er dir damals beigebracht, wie man sich eine Lichtquelle erschafft.\n")
                        warten2()
                        print("Du hast eigentlich magisches Geschick, aber so etwas Einfaches könntest du unter Umständen gerade noch hinkriegen.\n")
                        warten2()
                        print("Du könntest damit zum Beispiel deine Axt zum Leuchten bringen.\n")
                        warten2()
                        print("Zumindest könntest du es versuchen, gemacht hast du ja noch nie. \n")
                        warten2()
                        print("Und würde dich das nicht unter Umständen verraten, falls du eher vorsichtig und heimlich vorgehen willst? \n")
                        warten2()
                        print("Schwierig. Einen Versuch wert könnte es trotzdem sein! \n")
                        raum_start6()
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")
                raum_start5()

        def raum_start6():
            befehl = input("Was willst du tun? (Optionen: weggehen, Fackel anzünden, zaubern) \n > ").lower().strip()
            if "gehe" and "weg" in befehl:
                print("Du kehrst um und kommst am nächsten Morgen in voller Montur wieder. \n")
                warten2()
                print("Mit der richtigen Ausrüstung lässt sich die Höhle ohne Probleme passieren und findest schließlich Dolly. \n")
                warten2()
                print("Was von ihr übrig ist. \n")
                warten2()
                print("Von dem Ork fehlt jede Spur. \n")
                warten2()
                print("Egal, was immer du später erzählst: Du wirst der Szenerie, die du gesehen hast, niemals gerecht werden. \n")
                warten2()
                print("Eigentlich willst du das Bild auch nicht realitätsnah wiedergeben. \n")
                warten2()
                print("Du willst nicht einmal daran denken, was du gesehen hast. \n")
                warten2()
                print("Es schien irgendeine Art Ritual gewesen zu sein, so viel kannst du noch sagen. \n")
                warten2()
                print("Und der Rest… Ist Schweigen. \n")
                warten2()
                print("Und was soll das auch bringen, in der Vergangenheit rumzustochern?\n")
                warten2()
                print("An der Gegenwart wird das nichts ändern. \n")
                warten2()
                print("Dolly ist weg. \n")
                warten2()
                print("Ein weiterer unglücklicher Tag im Leben eines Bauern. \n")
                warten2()
                print("Aber das Leben weiter, und den Winter… Den Winter kriegt man schon irgendwie überstanden. \n")
                warten2()
                print("Ende \n")
                warten2()
                befehl = input("Willst du noch einmal spielen?\n > ").lower()
                if befehl == "ja":
                    raum_start4()
                elif befehl == "nein":
                    quit()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                    warten()
                    raum_start6()
            elif "fackel" in befehl:
                print("Du kramst in deinem kleinen Beutelchen nach Zündzeug. Gut, dass du zumindest dafür vorgesorgt hast! \n")
                warten2()
                print("Du brauchst ein paar Versuche, dann leuchtet sich die Fackel auf. \n")
                warten2()
                print("Sie spendet genug Licht, um die Höhle ordentlich zu erkunden. \n")
                warten2()
                print("Wenn du jetzt noch zögerst, sie zu betreten, liegt es zumindest nicht (mehr) an der Dunkelheit. \n")
                warten2()
                raum_kreuzung1()
            elif "zauber" in befehl:
                warten2()
                print("\nDu gehst einmal in dich und sammelst deine Kräfte. \n")
                warten2()
                print("Langsam, aber sicher fokussierst du deine innere Gefühlswelt und lässt dich von magischen Strömen durchdringen. \n")
                warten2()
                print("Jetzt musst du sie nur noch in etwas umwandeln, das du willst: Licht. \n")
                warten2()
                print("[Nun versuchen wir es mit einem magischen Wurf.]\n")
                warten2()
                print("[Jeder Zauber braucht einen bestimmten Kontrollwert (abgelegt mit einem W6) und den Einsatz von Zauberkraft (diese wird von deinen Werten und der Charakterklasse bestimmt).]\n")
                warten2()
                print("[Eigentlich solltest du als einfacher Bauer nicht in der Lage sein, zu zaubern.]\n")
                warten2()
                print("[Aber wir machen hier mal eine Ausnahme, zumal 'Licht' ein sehr einfacher Zauber ist.]\n")
                warten2()
                befehl = input("[Gib nun 'würfeln' ein, um den Wurf abzulegen.] \n > ")
                if befehl == "würfeln":
                    wuerfel_w6 = random.randint(1, 6)
                    warten2()
                    print("\nDein Wurf (Kontrolle): " + str(wuerfel_w6) + "\n")
                    warten2()
                    if wuerfel_w6 < 4:
                        print("[MISSERFOLG] \n")
                        warten2()
                        print("Leider schaffst du es nicht, diesen letzten Schritt zu machen. \n")
                        warten2()
                        print("Bei der Ätherischen Magie macht Übung eben den Meister, und du bist darin nicht einmal ein Lehrling. \n")
                        warten2()
                        print("Nun gut, du hast immer noch deine Fackel. \n")
                        warten2()
                        print("Du zündest sie an und betrittst die Säuselhöhle. \n")
                        warten2()
                        raum_kreuzung1()
                    else:
                        print("[ERFOLG] \n")
                        warten2()
                        print("Du hast zwar noch nie gezaubert, instinktiv weißt du aber trotzdem, was du tun musst. \n")
                        warten2()
                        print("Eine Welle unbeschreiblicher Euphorie, ja gar Erregung, überkommt dich, während deine Finger die richtigen Bewegungen machen. \n")
                        warten2()
                        print("Einige Sekunden später leuchtet dein Leinenhemd auf. Eigentlich wolltest du deine Axt zum Leuchten bringen, aber nun gut, zumindest hast du Licht. \n")
                        warten2()
                        print("Du zuckst einmal mit den Schultern und betrittst die Säuselhöhle. \n")
                        warten2()
                        raum_kreuzung1()
                else:
                    print("Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")
                    raum_start6()
            else:
                print("Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")
                raum_start6()


        def raum_eingang_hoehle2():
                    print ("Du gehst nach Norden und verlässt die Säuselhöhle. \n")
                    warten2()
                    print("Vor dir erstreckt sich ein schmaler Gang. Du spürst - und hörst - sofort den Windzug, der dir entgegen bläst. \n")
                    warten2()
                    print("Das Pfeifen erinnert dich mal wieder daran, woher die Höhle ihren Namen hat. \n")
                    warten2()
                    print("Verunsichert gehst du trotzdem weiter und kommst raus der Höhle, die jetzt hinter dir im Süden liegt. \n")
                    warten2()
                    print("Du fragst dich, warum du wieder rausgegangen bist. \n")
                    warten2()
                    print("Vielleicht waren die verblassten Erinnerungen zu schmerzhaft, vielleicht bist du aber auch nicht bereit. \n")
                    warten2()
                    print("Nicht bereit, dich der Gefahr zu stellen, oder du willst dich doch besser vorbereiten. \n")
                    warten2()
                    print("Du kannst also umkehren oder in den Süden gehen. \n")
                    warten2()
                    befehl = input("Was willst du tun? (Optionen: Weggehen, Süden) \n >").lower()
                    if "weg" in befehl:
                        print("Du kehrst um und kommst am nächsten Morgen in voller Montur wieder. \n")
                        warten2()
                        print("Mit der Ausrüstung lässt sich die Höhle ohne Probleme passieren und findest schließlich Dolly. \n")
                        warten2()
                        print("Was von ihr übrig ist. \n")
                        warten2()
                        print("Von dem Ork fehlt jede Spur. \n")
                        warten2()
                        print("Egal, was immer du später erzählst: Du wirst der Szenerie, die du gesehen hast, niemals gerecht werden. \n")
                        warten2()
                        print("Eigentlich willst du das Bild auch nicht realitätsnah wiedergeben. \n")
                        warten2()
                        print("Du willst nicht einmal daran denken, was du gesehen hast. \n")
                        warten2()
                        print("Es schien irgendeine Art Ritual gewesen zu sein, so viel kannst du noch sagen. \n")
                        warten2()
                        print("Und der Rest… Ist Schweigen. \n")
                        warten2()
                        print("Und was soll das auch bringen, in der Vergangenheit rumzustochern?\n")
                        warten2()
                        print("An der Gegenwart wird das nichts ändern. \n")
                        warten2()
                        print("Dolly ist weg. \n")
                        warten2()
                        print("Ein weiterer unglücklicher Tag im Leben eines Bauern. \n")
                        warten2()
                        print("Aber das Leben geht weiter, und den Winter… Den Winter kriegt man schon irgendwie überstanden. \n")
                        warten2()
                        print("Ende \n")
                        warten2()
                        befehl = input("Willst du noch einmal spielen?\n > ").lower()
                        if befehl == "ja":
                            raum_start4()
                        elif befehl == "nein":
                            quit()
                        else:
                            print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                    elif "süd" in befehl:
                        warten()
                        raum_kreuzung3()
                    else:
                        print ("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")


        def raum_suedkorridor1():
            print("[Du befindest dich im südlichen Gang.]\n")
            warten2()
            print("Der Gang windet sich schlangenartig, scheinbar unendlich lange.\n")
            warten2()
            print("Zunächst siehst du ein paar Malereien, Moosbestände und andere Zeichen von vergangenen Höhlenbesuchen.\n")
            warten2()
            print("Doch je weiter du dem Gang folgst, desto seltener werden diese Spuren.\n")
            warten2()
            print("Bis irgendwann nichts mehr übrig bleibt, nur nacktes und lebloses Gestein.\n")
            warten2()
            print("Langsam kommst es dir vor, als sei das Leben hier völlig zum Stillstand gekommen.\n")
            warten2()
            print("Verloren in der Zeit.\n")
            warten2()
            print("Verloren im Raum.\n")
            warten2()
            print("Vielleicht auch einfach nur verloren.\n")
            warten3()
            print("Plötzlich musst du anhalten.\n")
            warten2()
            print("Vor dir erstreckt sich ein riesiges Loch.\n")
            warten2()
            print("Du schaust in die Dunkelheit unter dir, entdeckst aber nichts außer der schwarzen Leere.\n")
            warten2()
            print("Mehr noch: Du bekommst das Gefühl, dass die Dunkelheit vielmehr dich betrachtet als du sie.\n")
            warten2()
            print("Auf der anderen Seite führt der Gang weiter.\n")
            warten2()
            print("Du siehst keine Möglichkeit, das Loch zu überwinden... Außer, du springst.\n")
            warten2()
            print("So haben die Übeltäter Dolly natürlich ganz sicher nicht geführt.\n")
            warten2()
            print("Aber wer weiß, was auf der anderen Seite ist?\n")
            warten2()
            print("Du rechnest einmal kurz deine Chancen aus und kommst zu dem Schluss, dass du das Loch überspringen könntest.\n")
            warten2()
            print("Wenn du Glück hast.\n")
            warten2()
            print ("Das ist nicht ideal, aber ansonsten bleibt dir nur der ganze Weg zurück zur Kreuzung.\n")
            warten2()
            befehl=input("Was willst du tun? (Optionen: springen, zurückgehen)\n > ").lower()
            if "gehe" in befehl:
                raum_kreuzung4()
            elif "springe" in befehl:
                raum_suedkorridor1_wurf()

            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")

        def raum_suedkorridor1_wurf():
            print("[Nun brauchen wir wieder einen Wurf, um zu sehen, ob du den Sprung schaffst.]\n")
            warten2()
            print("[Dieses Mal testen wir also dein Geschick.]\n")
            warten2()
            print("[Gut, eigentlich wäre der Wurf für die Fertigkeit 'Sportlichkeit'.]\n")
            warten2()
            print("[Als einfacher Bauer hast du diese allerdings nicht trainiert.]\n")
            warten2()
            print("[Dein Geschick-Bonus muss also reichen.]\n")
            warten2()
            befehl = input("[Gib nun bitte 'würfeln' ein.]\n > ").lower()
            warten2()
            if "würfeln" in befehl:
                wurf_sportlichkeit = spieler.wurf_sportlichkeit()
                if wurf_sportlichkeit >= 14:
                    print("[ERFOLG]\n")
                    warten2()
                    print("Du nimmst Anlauf und springst.\n")
                    warten2()
                    print("Das Loch war breiter als gedacht, aber zum Glück kommst gut auf der anderen Seite an.\n")
                    warten2()
                    print("Du schaust dich um. Auf dem gleichen Wege kommst du schon mal nicht zurück, selbst wenn du Dolly findest.\n")
                    warten2()
                    print("Es bleibt dir also nichts Anderes übrig, als weiterzugehen.\n")
                    raum_suedkorridor2()
                    pass
                elif wurf_sportlichkeit in range(2, 13):
                    print("[MISSERFOLG]\n")
                    warten2()
                    print("Du nimmst Anlauf und springst.\n")
                    warten2()
                    print("Das Loch ist breiter als gedacht.\n")
                    warten2()
                    print("Du verschätzt dich knapp und fällst runter.\n")
                    warten2()
                    print("[Nun hast du deinen Fertigkeitswurf nicht bestanden.]\n")
                    warten2()
                    print("[Das ist eindeutig suboptimal, aber noch ist nicht alles verloren.]\n")
                    warten2()
                    print("[Dafür sieht das Spielsystem Rettungs- und Glückswürfe vor.] \n")
                    warten2()
                    print("[Schaffst du den Rettungswurf, kannst du gerade noch so den Rand auf der anderen Seite greifen und dich hochziehen.]\n")
                    warten2()
                    print("[Verfehlst du nur ganz knapp, dann hast du den Glückswurf geschafft und kannst zumindest das Schlimmste verhindern.]\n")
                    warten2()
                    print("[Und ansonsten... Nun ja, es hat dich ja niemand gezwungen, einfach drauf loszuspringen, nicht wahr?] \n")
                    warten2()
                    print("[Zum Glück hast du als Bauer ziemlich starke Arme. Deine Chancen stehen also gar nicht mal so schlecht.]\n")
                    warten2()
                    befehl = input("[Gib nun 'würfeln' ein.] \n > ").lower()
                    if befehl == "würfeln":
                        wurf_reflex = spieler.reflexwurf()
                        if wurf_reflex >= 14:
                            print("\n[ERFOLG: RETTUNGSWURF]\n")
                            warten2()
                            print("Zum Glück war Sprung gut genug, dass es fast geschafft hast.\n")
                            warten2()
                            print("Du kommst zwar nicht auf der anderen Seite an, kannst aber den Felsboden fest mit beiden Händen greifen.\n")
                            warten2()
                            print("Du ziehst sich hoch und schaust dich um.\n")
                            warten2()
                            print("Auf dem gleichen Wege kommst du schon mal nicht zurück, selbst wenn du Dolly findest.\n")
                            warten2()
                            print("Es bleibt dir also nichts Anderes übrig, weiterzugehen.\n")
                            warten2()
                            raum_suedkorridor2()
                        elif wurf_reflex in range(12, 13):
                            print("\n[ERFOLG: GLÜCKSWURF]\n")
                            warten2()
                            print("Zum Glück war der Sprung gut genug, dass du es fast geschafft hast.\n")
                            warten2()
                            print("Du kommst zwar nicht auf der anderen Seite an, kannst aber den Felsboden mit einer Hand greifen.\n")
                            warten2()
                            print("Nun musst es irgendwie schaffen, dich hochzuziehen.\n")
                            warten2()
                            if befehl == "würfeln":
                                wurf_kraft = spieler.kraftwurf()
                                if wurf_kraft >= 14:
                                    print("[ERFOLG]\n")
                                    warten2()
                                    print("Mit etwas Mühe kannst du den Rand des Bodens mit der zweiten Hand greifen und dich mit beiden Händen hochzuziehen.\n")
                                    warten2()
                                    print("Du schaust dich um.\n")
                                    warten2()
                                    print("Auf dem gleichen Wege kommst du schon mal nicht zurück, selbst wenn du Dolly findest.\n")
                                    warten2()
                                    print("Es bleibt dir also nichts Anderes übrig, weiterzugehen.\n")
                                    raum_suedkorridor2()
                                else:
                                    print("\n[MISSERFOLG]\n")
                                    warten2()
                                    print("Du versuchst, dich hochzuziehen, doch deine Hand rutscht ab, bevor mit der zweiten nach dem Rand des Boden greifen kannst.\n")
                                    warten2()
                                    print("Du fällst und verschwindest im Loch, auf ewig verloren in der schwarzen Leere.\n")
                                    warten2()
                                    print("Vielleicht werden dir die Götter Gnade walten lassen, die du im Leben nicht kanntest.\n")
                                    warten2()
                                    print("Dein Abenteuer in der Welt der Lebenden ist aber hiermit zu Ende.\n")
                                    warten2()
                                    print("Der Lebensfaden abrupt abgeschnitten. Durch den eigenen Fehler.\n")
                                    warten2()
                                    print("Ende \n")
                                    warten2()
                                    befehl = input("Willst du noch einmal spielen?\n > ").lower()
                                    if befehl == "ja":
                                        raum_start4()
                                    elif befehl == "nein":
                                        quit()
                                    else:
                                        print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                            else:
                                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                else:
                    print("\n[KRITISCHER MISSERFOLG]\n")
                    warten2()
                    print("Du nimmst Anlauf und springst, verschätzt dich allerdings und fliegst nicht weit genug.\n")
                    warten2()
                    print("Du hast dich gerade mal stark genug verschätzt, dass nichts greifen kannst, um deinen Fall aufzuhalten.\n")
                    warten2()
                    print("Du verschwindest im Loch, auf ewig verloren in der schwarzen Leere.\n")
                    warten2()
                    print("Vielleicht werden dir die Götter Gnade walten lassen, die du im Leben nicht kanntest.\n")
                    warten2()
                    print("Dein Abenteuer in der Welt der Lebenden ist aber hiermit zu Ende.\n")
                    warten2()
                    print("Der Lebensfaden abrupt abgeschnitten. Durch den eigenen Fehler.\n")
                    warten2()
                    print("Ende \n")
                    warten2()
                    befehl = input("Willst du noch einmal spielen?\n > ").lower()
                    if befehl == "ja":
                        warten2()
                        raum_start4()
                    elif befehl == "nein":
                        quit()
                    else:
                        print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")

        def raum_suedkorridor2():
            print ("[Du folgst dem südlichen Gang.]\n")
            warten2()
            print("Der Gang führt schließlich zu einer größeren Höhle.\n")
            warten2()
            print("Was du dort erblickst, lässt sich kaum beschreiben.\n")
            warten2()
            print("Du siehst Dolly - angebunden, mitten in einem Kreis aus einer roten Substanz.\n")
            warten2()
            print("Neben dem Kreis erkennst du einen Tisch mit irgendwelchen Werkzeugen.\n")
            warten2()
            print("Das Ganze sieht verdächtig nach einer Art Opfer-Ritual aus.\n")
            warten2()
            print("Den Übeltäter kannst du auch erkennen.\n")
            warten2()
            print ("Ein großer schwarzer Ork ist gerade dabei, eine Klinge zu schärfen.\n")
            warten2()
            print("Dieser Bastard!\n")
            warten2()
            print("Arme Dolly! Du musst sie unbedingt da rausholen!\n")
            warten2()
            print("Er scheint sich dabei mit jemandem zu unterhalten, und schon bald siehst du, mit wem.\n")
            warten2()
            print("Einem Zwerg, den du sofort erkennst.\n")
            warten2()
            print("Wessin. Dein Bauernhof-Nachbar.\n")
            warten2()
            print("Was um alles in der Welt passiert hier eigentlich?\n")
            warten2()
            print("Was immer es ist: Die Zeit ist knapp!\n")
            warten2()
            print("Die beiden Übeltäter bemerken dein Licht und schauen dich an.\n")
            warten2()
            print("Jetzt hast du eigentlich nur zwei Optionen:\n")
            warten2()
            print("Du kannst die Entführer natürlich stellen und versuchen, Dolly mit Worten zurückzuholen.\n")
            warten2()
            print("Würden sie darauf hören? Irgendwie hast du da deine Zweifel. Aber man weiß ja nie.\n")
            warten2()
            print("Du kannst natürlich auch deine Axt greifen direkt losschwingen.\n")
            warten()
            print("Je schneller du mit dem Ork fertig wirst, desto besser.\n")
            warten2()
            print("Den Rest kannst du später klären.\n")
            warten2()
            print("Immerhin hast du Glück: Der Ork hat keine Rüstung an. Sein Lederpanzer liegt neben dem Tisch.\n")
            warten2()
            befehl=input("Was willst du tun? (Optionen: reden, angreifen)\n > ").lower()
            if "rede" in befehl:
                szene_dialog1()
            elif "greife" in befehl:
                szene_bosskampf1()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
            pass

        def szene_bosskampf2():
            warten2()
            print("[Nun befindest du dich im Kampf.]\n")
            warten2()
            befehl = input("Willst du die Regeln dazu erfahren? \n > ").lower()
            if "ja" in befehl:
                warten2()
                print("[Wie in den meisten Rollenspielen auch, ist der Kampf hier in Runden gegliedert.]\n")
                warten3()
                print("[Wer zuerst angreifen darf, wird gleich über die sogenannte 'Initiative' entschieden.]\n")
                warten3()
                print("[Um den gegner zu besiegen, musst du seine Lebenskraft auf 0 reduzieren.]\n")
                warten3()
                print("[Dafür musst du mit deinem Wurf seinen Verteidigungswert überwinden.]\n")
                warten3()
                print("[Ziemlich viel Zufallsprinzip? Ja, willkommen in der Welt der Rollenspiele!]\n")
                warten3()
                print("[Aber du kannst das Ergebnis mit deinen Entscheidungen beeinflussen.]\n")
                warten2()
                print("[Der Kampf für dieses Abenteuer ist allerdings vereinfacht.]\n")
                warten3()
                print("[Eigentlich sieht das ZdZ-System fünf verschiedene Kampfstile vor.]\n")
                warten3()
                print("[Nicht zu vergessen: Viele verschiedene Aktionen, die man im Kampf machen kann:\n")
                warten3()
                print("[Kampfbewegung, Boni, Waffenverhalten, Vorteile und Vieles mehr.]\n")
                warten3()
                print("[Vielleicht wird das alles im nächsten Abenteuer eingebaut, aber vorerst bleiben wir bei den Grundlagen.]\n")
                warten3()
                print("[Aber als kleiner Vorgeschmack:\n")
                warten3()
                print("Ruhige Angriffe sind der Standard für jeden Kampfteilnehmer.]\n")
                warten3()
                print("[Gehst du aggressiv vor, achtest du mehr auf deine Treffsicherheit und Schaden als die eigene Verteidigung.]\n")
                warten3()
                print("[Bei vorsichtigen Angriffen ist es umgekehrt.]\n")
                warten3()
                print("[Bei schnellen Angriffen vernachlässigst du Beides, um mehr Schläge in der gleichen Zeitspanne auszuführen.] \n")
                warten3()
                print("[Natürlich kannst du auch versuchen, einfach mal nicht getroffen zu werden.]\n")
                warten3()
                print("[Hier sind die Regeln: Jeder Kampfteilnehmer hat 2 Aktionen zur Verfügung.]\n")
                warten3()
                print("[Normalerweise kann man sie für alles Mögliche benutzen, aber hier werden sie alle für den Kampf ausgegeben.]\n")
                warten3()
                print("[Außerdem hat jeder Kämpfer eine bestimmte Ausdauer, also eine Kraftreserve, die mit jeder Aktion beim Kämpfen verbraucht wird.]\n")
                warten3()
                print("[Fällt sie auf 0, wirst du erschöpft. Dass das mitten im Kampf passiert, willst du nicht.]\n")
                warten3()
                print("[Wirklich nicht.]\n")
                warten3()
                print("[Die Ausdauer erholt sich aber, wenn du nicht kämpfst bzw. gar nichts machst.]\n")
                warten3()
                print("[Um den Gegner zu besiegen, muss du ihn gut erwischen. Deine Axt ist für diese Aufgabe gut geeignet.]\n")
                warten3()
                print("[Allerdings verbraucht sie auch mehr Ausdauer als, sagen wir, das Kurzschwert, das der Ork in der Hand hält.]\n")
                warten3()
                print("[Und jedes halbwegs schlaue Lebewesen weiß: Orks haben eine höhere Ausdauer als Menschen.]\n")
                warten3()
                print("[Erschwerend kommt noch die Lederrüstung des Orks hinzu.]\n")
                warten3()
                print ("[Lange wird sie gegen deine Axt nicht halten, einen gewissen Schutz beschwert sie ihm aber schon.]\n")
                warten3()
                print("[Und damit legen wir dann los.]\n")
                warten2()
                befehl = input("[Gib bitte 'weiter' ein, um fortzufahren.]\n > ").lower()
                if befehl == "weiter":
                    raum_bosskampf2()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
            if "nein" in befehl:
                warten2()
                print("\n[Gut, dann gehen wir davon aus, dass du diese bereits kennst. Nervige Tutorials können wir also überspringen.]\n")
                warten2()
                befehl = input("[Gib bitte 'weiter' ein, um fortzufahren.]\n > ").lower()
                if befehl == "weiter":
                    raum_bosskampf2()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")


        def raum_bosskampf2():
            spieler_initiative = spieler.wuerfel_w12 + spieler.initiative_bonus
            ork_initiative = ork.wuerfel_w12 + ork.initiative_bonus
            befehl = input("\n[Und nun: Gib bitte 'würfeln' ein, um die Initiative auszuwürfeln.]\n > ").lower()
            if befehl == "würfeln":
                print("Dein Initiativwurf: " + str(spieler_initiative))
                warten2()
                print("Initiativwurf des Gegners: " + str(ork_initiative) + "\n")
                if spieler_initiative >= ork_initiative:
                    reset_spieler2()
                else:
                    reset_gegner2()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")
            pass

        def szene_dialog1():
            print("Du gehst einen Schritt auf die Entführer zu und stellt sie zur Rede.\n")
            warten2()
            print("Was soll dieses Kurzling-Theater hier?\n")
            warten2()
            print("Was um Národs Willen geht hier vor?\n")
            warten2()
            print("Die Antwort fällt nicht sehr verständlich aus, aber du begreifst die wichtigen Dinge.\n")
            warten2()
            print("Sie bereiten ein Opferritual vor.\n")
            warten2()
            print("Es ist für irgendeinen orkischen Gott, dessen Namen du dir nicht gemerkt hast.\n")
            warten2()
            print("Den Zweck verstehst du aber:\n")
            warten2()
            print("Wessin ist eifersüchtig auf deine Wolle, das hast du schon immer gewusst.\n")
            warten2()
            print("Seit er ins Dorf gezogen ist, konntest du dich seiner Blicke auf Dolly nicht erwehren.\n")
            warten2()
            print("Jetzt will er sie opfern, um seinen Schafen die gleiche Fluffigkeit zu verleihen.\n")
            warten2()
            print("Würde das denn helfen? Religion war nie deine Stärke.\n")
            warten2()
            print("Du warst immer vielmehr damit beschäftigt, den Bauernhof am Laufen zu halten.\n")
            warten2()
            print("Überlegungen geistlicher Natur muss man sich leisten können.\n")
            warten2()
            print("Diesen Luxus hast du nicht.\n")
            warten2()
            print("Dieser Giftzwerg, Wessin, offenbar schon.\n")
            warten2()
            print("Kein Wunder, dass sich sein Bauernhof gerade noch so über Wasser halten kann.\n")
            warten2()
            print("Aber das spielt sowieso keine Rolle. Wessin und sein Ork-Söldner sind zu weit gegangen.\n")
            warten2()
            print("Du könntest ihnen natürlich eine letzte Warnung aussprechen. Aber ob sie etwas bringen würde?\n")
            warten2()
            print("Ansonsten bleibt dir nur, Dolly mit Gewalt zu befreien.\n")
            warten2()
            print("Die Beiden haben dir zwar schon einen Rückzieher angeboten, aber das ist keine Option.\n")
            warten2()
            befehl=input("Was willst du tun? (Optionen: überreden, angreifen)\n > ").lower()
            if "greife" in befehl:
                warten2()
                print("Nach kurzer Überlegung zum Schluss, dass du viel zu lange überlegst.\n")
                warten2()
                print("Wessin ist wahrlich zu weit gegangen. Das ist Wahnsinn!\n")
                warten2()
                print("Du hattest eine leise Hoffnung, dass das hier noch gewaltlos ausgeht.\n")
                warten2()
                print("Aber du hast schwere Arbeit noch nie gescheut. Die Beiden kommen hier NICHT mehr lebend raus.\n")
                warten2()
                print("Du umklammerst deine Axt und stürmst auf den Ork zu.\n")
                szene_bosskampf1()
            elif "rede" in befehl:
                warten2()
                print("Du hast zwar noch nie schwere Arbeit gescheut.\n")
                warten2()
                print("Wenn es aber eine Möglichkeit gibt, Dolly ohne Blutvergießen zurückzuholen, dann willst du es versuchen.\n")
                warten2()
                print("Also sagst du es noch einmal deutlich:\n")
                warten2()
                print("Dolly ist der Stolz deines Bauernhofs.\n")
                warten2()
                print("Ja, auch deine Einnahmequelle.\n")
                warten2()
                print("Aber auch gewissermaßen ein Familienmitglied.\n")
                warten2()
                print("Vielleicht kannst du die Beiden besiegen, vielleicht auch nicht.\n")
                warten2()
                print("Aber du würdest lieber hier im Kampf sterben, als Dolly im Stich zu lassen.\n")
                warten2()
                print("Du bist dir plötzlich nicht mehr sicher, dass du damit nur Dolly meinst.\n")
                warten2()
                print("Alte Erinnerungen blitzen wieder vor deine Augen auf.\n")
                warten2()
                print("Maika...\n")
                warten2()
                print("Damals hast du versagt, in ebendieser Höhle.\n")
                warten2()
                print("Diese Erinnerung hat dich schon immer geplagt.\n")
                warten2()
                print("Nun gibt sie dir aber überraschend Kraft.\n")
                warten2()
                print("Keinen Schritt zurück!\n")
                warten3()
                print("[Nun sind deine Überredungskünste gefragt.]\n")
                warten2()
                print("[Als einfacher Bauer ist Überzeugen eigentlich nicht deine Stärke.]\n")
                warten2()
                print("[Der Einsatz von ungeübten Fertigkeiten wird normalerweise von einem Malus begleitet.]\n")
                warten2()
                print("[Als tierlieber Mensch legst du aber immerhin eine gewisse Empathie an den Tag.]\n")
                warten2()
                print("[Diese wird dir einen kleinen Bonus auf den Wurf bescheren.]\n")
                warten2()
                befehl=input("[Gib nun 'würfeln' ein, um den Überredungsversuch zu starten.]\n > ").lower()
                if befehl=="würfeln":
                    warten2()
                    wurf_ueberreden = spieler.wurf_ueberreden()
                    warten2()
                    if wurf_ueberreden >=12:
                        print("[ERFOLG]\n")
                        warten2()
                        print("Du hättest zwar nicht damit gerechnet, aber dein Rede scheint den Ork beeindruckt zu haben.\n")
                        warten2()
                        print("Diese Ungeheuer sind nicht gerade für Empathie bekannt, aber sie respektieren Willensstärke.\n")
                        warten2()
                        print("Der Ork-Söldner erkennt deine Entschlossenheit an.\n")
                        warten2()
                        print("Vermutlich könnte er dich hier töten. Aber nicht heute.\n")
                        warten2()
                        print("Es komme selten vor, dass er einen Menschen mit dem Mut deines Orks treffe.\n")
                        warten2()
                        print("Sein Auftrag war ohnehin nur die Entführung.\n")
                        warten2()
                        print("Diesen hat er erfüllt, das Geld ist kassiert.\n")
                        warten2()
                        print("Drama sei langweilig, die Sache könnt ihr unter euch ausmachen.\n")
                        warten2()
                        print("Und damit entfernt sich der Ork vom Tatort.\n")
                        warten2()
                        print("Du lässt ihn vorbei. Scheinbar gibt es selbst unter Orks so etwas wie Ehre.\n")
                        warten2()
                        szene_sieg()
                        pass
                    else:
                        warten2()
                        print("[MISSERFOLG]\n")
                        warten2()
                        print("Natürlich stoßen deine Worte auf taube Ohren.\n")
                        warten2()
                        print("Nicht, dass es überraschend wäre.\n")
                        warten2()
                        print("Wessin ist fest entschlossen, das Ritual durchzuführen.\n")
                        warten2()
                        print("Dem Söldner-Ork geht es zwar nur ums Geld, aber du kannst ihn nicht bezahlen.\n")
                        warten2()
                        if spieler.edelsteine==False:
                            print("Ohne Blutvergießen wird es also nicht gehen.\n")
                            warten2()
                            print("Du machst dich bereit zum Kampf.\n")
                            warten2()
                            szene_bosskampf1()
                        else:
                            print ("[Edelsteine: Ja] \n")
                            warten2()
                            print("Oder doch?\n")
                            warten2()
                            print("Du hast doch vorhin ein paar Edelsteine gefunden!\n")
                            warten2()
                            print("Du weißt nicht, was deren Wert ist, aber vielleicht kannst du den Ork damit bezahlen.\n")
                            warten2()
                            befehl=input("Willst du versuchen, den Ork zu bestechen?\n > ").lower()
                            warten2()
                            if "ja" in befehl:
                                befehl = input("[Gib nun 'würfeln' ein, um den Überredungsversuch zu starten.]\n > ").lower()
                                if befehl == "würfeln":
                                    warten2()
                                    wurf_ueberreden_2 = spieler.wurf_ueberreden()
                                    warten2()
                                    if wurf_ueberreden_2 >= 8:
                                        print("[ERFOLG]\n")
                                        warten2()
                                        print("Der Ork schaut einmal auf die Edelsteine, die du ihm zeigst.\n")
                                        warten2()
                                        print("Er ist kurz verwirrt, aber er scheint deren Wert zu kennen.\n")
                                        warten2()
                                        print("Du bietest sie ihm an, wenn er nur weggeht.\n")
                                        warten2()
                                        print("Er denkt kurz nach. Dann nickt er, nimmt die Steine und verlässt den Tatort.\n")
                                        warten2()
                                        print("Weder Söldner noch Orks haben Ehre, das war dir schon immer klar.\n")
                                        warten2()
                                        print("Geld ist aber eine Sprache, die beide Gruppen verstehen.\n")
                                        spieler.edelsteine=False
                                        szene_sieg()
                                    elif wurf_ueberreden_2 == 1:
                                        print("[KRITISCHER MISSERFOLG]\n")
                                        warten2()
                                        print("Der Ork schaut einmal auf die Edelsteine, die du ihm zeigst.\n")
                                        warten2()
                                        print("Er ist kurz verwirrt, aber er scheint deren Wert zu kennen.\n")
                                        warten2()
                                        print("Du bietest sie ihm an, wenn er nur weggeht.\n")
                                        warten2()
                                        print("Er denkt kurz nach. Dann nickt er, und scheint auf den Angebot einzugehen.\n")
                                        warten2()
                                        print("Als er die Steine in die Hand nehmen will, greift er jedoch blitzschell nach seinem Messer.\n")
                                        warten2()
                                        print("Er versucht, ihn dir direkt zwischen die Rippen zu bohren.\n")
                                        warten2()
                                        ork_angriff=ork.wuerfel_w12+ork.geschick+ork.angriffsbonus
                                        print("Würfel: " + str(ork.wuerfel_w12) + "\n")
                                        warten2()
                                        print("Überraschnungsangriff: " + str(ork_angriff) + "\n")
                                        warten2()
                                        if ork_angriff>=spieler.verteidigung:
                                            print("Du siehst den Angriff kommen, kannst aber nicht mehr rechtzeitig reagieren.\n")
                                            warten2()
                                            ork_schaden=random.randint(1,4)
                                            print("Der ehrlose Bastard erwischst dich und verletzt dich um " + str(ork_schaden) + "Punkte Stichschaden.\n")
                                            warten2()
                                            print("Deine Lebenskraft: " + str(spieler.lebenskraft) + "/" + str(spieler.max_lebenskraft) + "\n")
                                            warten2()
                                            print("Verletzt springst du reflexartig zurück.\n")
                                            warten2()
                                            print("Deine Brust schmerzt so stark, dass du dir am liebsten die Seele aus dem Leib schreien würdest.\n")
                                            warten2()
                                            print("Dein Herz hat er aber zum Glück verfehlt.\n")
                                            warten2()
                                            print("Jetzt ist klar: Nur einer von euch wird diese Höhle lebend verlassen.\n")
                                            warten2()
                                            print("Du klammerst dich an deine zweihändige Axt und machst dich bereit zum Kampf.\n")
                                            szene_bosskampf1()
                                        else:
                                            print("Zum Glück kannst du den Angriff kommen sehen und kannst gerade noch einen Schritt zurück machen.\n")
                                            warten2()
                                            print("So eine Hinterlist! Haben Ork-Söldner nicht mal einen Tropfen Anstand?\n")
                                            warten2()
                                            print("Jetzt ist dir absolut klar: Nur einer von euch wird diese Höhle lebend verlassen.\n")
                                            warten2()
                                            print("Du klammerst dich an deine zweihändige Axt und machst dich bereit zum Kampf.\n")
                                            warten2()
                                            szene_bosskampf1()
                                    else:
                                        print("[MISSERFOLG]\n")
                                        warten2()
                                        print("Der Ork schaut einmal auf die Edelsteine, die du ihm zeigst.\n")
                                        warten2()
                                        print("Er ist kurz verwirrt, aber er scheint deren Wert zu kennen.\n")
                                        warten2()
                                        print("Du bietest sie ihm an, wenn er nur weggeht.\n")
                                        warten2()
                                        print("Er denkt kurz nach. Dann sagt er, dein Angebot sei gut.\n")
                                        warten2()
                                        print("Aber warum würde er darauf eingehen, wenn er die Steine doch auch von einer Leiche nehmen könne?\n")
                                        warten2()
                                        print("Tja, Weder Söldner noch Orks wissen, was Ehre ist. Das war dir schon immer klar.\n")
                                        warten2()
                                        print("Ohne Blutvergießen wird es also nicht gehen.\n")
                                        warten2()
                                        print("Du machst dich bereit zum Kampf.\n")
                                        warten2()
                                        szene_bosskampf1()
                            elif "nein" in befehl:
                                print("Nein. Diese Blöße wirst du dich nicht geben.\n")
                                warten2()
                                print("Ohne Blutvergießen wird es also nicht gehen.\n")
                                warten2()
                                print("Du machst dich bereit zum Kampf.\n")
                                warten2()
                                szene_bosskampf1()
                            else:
                                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                                pass

                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                    pass
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                pass

            pass

        def szene_sieg():
            print("Du atmest auf.\n")
            warten2()
            print("Dann wieder aus.\n")
            warten2()
            print("Schwer.\n")
            warten2()
            print("Aber erleichtert.\n")
            warten2()
            print("Du hättest fast nicht gedacht, dass du es mit einem Ork aufnehmen könntest.\n")
            warten3()
            print("Aber du hast es geschafft!\n")
            warten3()
            print("Es ist vorbei.\n")
            warten3()
            print("Allerdings bleibt noch die Frage, was du jetzt mit Wessin machen willst.\n")
            warten3()
            print("Er steht vor dir. Eingeschüchtert, unsicher.\n")
            warten3()
            print("Unter anderen Umständen würdest du zweimal nachdenken, bevor du dich mit einem Zwerg anlegst.\n")
            warten3()
            print("Orks sind schlimm genug, aber die meisten sind kaum mehr als tollwütige Wildtiere.\n")
            warten3()
            print("Zumindest gibt es nichts, das dich vom Gegenteil überzeugen könnte.\n")
            warten3()
            print("Zwerge sind anders.\n")
            warten3()
            print("Vielleicht nicht so stark, dafür um Einiges robuster und eindeutig schlauer.\n")
            warten3()
            print("Einem zwergischen Krieger solltest du wirklich aus dem Weg gehen, wenn du kannst.\n")
            warten3()
            print("Wessin ist aber kein Krieger.\n")
            warten3()
            print("Genau genommen ist er nicht einmal ein richtiger Bauer.\n")
            warten3()
            print("Ohne seinen Ork-Söldner stellt er für dich keine Gefahr mehr dar.\n")
            warten3()
            print("Dennoch kannst du hier nicht einfach mit Dolly wieder rausgehen.\n")
            warten3()
            print("Irgendwas musst du mit ihm also machen.\n")
            warten3()
            befehl=input("Wie richtest du über Wessin? (Optionen: töten, verletzen, bewusstlos schlagen, melden, ignorieren)\n > ").lower()
            warten3()
            if "töte" in befehl:
                print("Du überlegst kurz, was du mit dem hinterhältigen Zwerg machst.\n")
                warten3()
                print("Du ringst mit dir selbst, kommst aber zu dem Schluss, dass er für seine Tat bezahlen muss.\n")
                warten3()
                print("Du könntest ihn natürlich laufen lassen oder dem Dorfältesten melden.\n")
                warten3()
                print("Aber nein. Es ist zu viel passiert.\n")
                warten3()
                print("Er schaut dich verängstigt an, während du mit der Axt in der auf ihn zugehst.\n")
                warten3()
                print("Du willst dich dabei nicht auf das Niveau eines Orks begeben, aber das Leben als Bauer hat dich auf diesen Moment vorbereitet.\n")
                warten3()
                print("Die Säuselhöhle wird nur selten von jemandem aufgesucht.\n")
                warten3()
                print("Falls jemand ihn hier findet, wird wahrscheinlich sehr viel Zeit vergehen.\n")
                warten3()
                print("Niemand wird erfahren, was hier passiert ist.\n")
                warten3()
                print("Wie so oft, kannst du ein Geheimnis für dich behalten.\n")
                warten3()
                print("Du holst aus.\n")
                warten3()
                print("Ein einziger sauberer Schlag...\n")
                warten3()
                print("Und es ist vollbracht.\n")
                warten3()
                print("Du atmest aus und wischst dir den Schweiß von der Stirn.\n")
                warten3()
                print("Hier gibt es nichts mehr für dich.\n")
                warten3()
                print("Du findest Dolly und bindest sie los.\n")
                warten3()
                print("Alles, was bleibt, ist von hier zu verschwinden.\n")
                warten3()
                szene_epilog()
            elif "verletze" in befehl:
                print("Du überlegst kurz, was du mit dem hinterhältigen Zwerg machst.\n")
                warten3()
                print("Du ringst mit dir selbst, kommst aber zu dem Schluss, dass er für seine Tat bezahlen muss.\n")
                warten3()
                print("Du könntest ihn natürlich laufen lassen oder dem Dorfältesten melden.\n")
                warten3()
                print("Aber nein. Es ist zu viel passiert.\n")
                warten3()
                print("Eigentlich hätte er eine Schädelspaltung verdient, nach dem, was er getan hat.\n")
                warten3()
                print("Aber du bist kein Mörder.\n")
                warten3()
                print("Du schwingst deine Axt, achtest aber darauf, keine wichtigen Organe zu treffen.\n")
                warten3()
                print("Falls er es in diesem Zustand aus der Höhle schaffen sollte, kann er gerne selbst erklären, was passiert ist.\n")
                warten3()
                print("Dich wird er jedenfalls nicht beschuldigen können, ohne selbst bestraft zu werden.\n")
                warten3()
                print("Du wendest dich von dem elendig stöhnenden Zwerg ab und gehst weiter, um Dolly zu holen.\n")
                warten3()
                print("Sobald du sie findest, bindest du sie los.\n")
                warten3()
                print("Alles, was bleibt, ist von hier zu verschwinden.\n")
                warten3()
                szene_epilog()
            elif "bewusst" in befehl:
                print("Du überlegst kurz, was du mit dem hinterhältigen Zwerg machst.\n")
                warten3()
                print("Du ringst mit dir selbst, kommst aber zu dem Schluss, dass er für seine Tat bezahlen muss.\n")
                warten3()
                print("Allerdings bist du kein Mörder. Ihn einfach zu erschlagen und hier liegen zu lassen wäre falsch.\n")
                warten3()
                print("Aber du kannst ihn auch nicht davonkommen lassen.\n")
                warten3()
                print("Du gehst schnell auf den verängstigten Zwerg zu und schlägst ihn mit der stumpfen Seite deiner Axt bewusstlos.\n")
                warten3()
                print("Was du mit ihm machst, wirst du später entscheiden.\n")
                warten3()
                print("Das Einzige, was jetzt zählt, ist Dolly.\n")
                warten3()
                print("Sobald du sie findest, bindest du sie los.\n")
                warten3()
                print("Alles, was bleibt, ist von hier zu verschwinden.\n")
                warten3()
                szene_epilog()
            elif "melde" in befehl:
                print("Du überlegst kurz, was du mit dem hinterhältigen Zwerg machst.\n")
                warten3()
                print("Du ringst mit dir selbst, kommst aber zu dem Schluss, dass er für seine Tat bezahlen muss.\n")
                warten3()
                print("Allerdings bist du kein Mörder. Ihn einfach zu erschlagen und hier liegen zu lassen wäre falsch.\n")
                warten3()
                print("Natürlich kannst du ihn nicht davonkommen lassen.\n")
                warten3()
                print("Aber es liegt nicht an dir, über ihn zu richten.\n")
                warten3()
                print("Du willst ihn dem Dorfältesten melden.\n")
                warten3()
                print("So sehr du ihn zur Rechenschaft ziehen willst: Dafür gibt es nur einen richtigen Weg.\n")
                warten3()
                print("Sein Schicksal liegt nun in den Händen der Gesetzeshüter.\n")
                warten3()
                print("Natürlich will Wessin protestieren, der Anblick deiner Axt ist aber ein gewichtiges Argument.\n")
                warten3()
                print("Während er sich zum Ausgang aus der Säuselhöhle begibt, gehst du weiter, um Dolly zu holen.\n")
                warten3()
                print("Sobald du sie findest, bindest du sie los.\n")
                warten3()
                print("Alles, was bleibt, ist von hier zu verschwinden.\n")
                warten3()
                szene_epilog()
            elif "ignor" in befehl:
                print("Du überlegst kurz, was du mit dem hinterhältigen Zwerg machst.\n")
                warten3()
                print("Du ringst mit dir selbst, kommst aber zu dem Schluss, dass er deine Mühe nicht wert ist.\n")
                warten3()
                print("Du hast Dolly beinahe wieder. Das ist alles, was zählt.\n")
                warten3()
                print("Du wirfst ihm einen bösen Blick zu und gehst wortlos an ihm vorbei.\n")
                warten3()
                print("Du findest Dolly und willst sie losbinden.\n")
                warten3()
                print("Während du dabei bist, hörst du aber Schritte dir.\n")
                warten3()
                print("Du drehst dich um, und siehst Wessin, der mit einem Messer auf dich zuläuft.\n")
                warten3()
                print("Seine Hand schnellt nach deiner Brust, die Klinge so scharf wie Orkzähne.\n")
                warten3()
                wuerfel_w12= random.randint(1,12)
                feind_angriff=wuerfel_w12+4
                reflexwurf_spieler = spieler.wuerfel_w12 + spieler.reflexe
                print ("[Nun musst du einen Wurf auf deine Reflexe ablegen.]\n")
                warten2()
                print("[Reflexe geben an, wie schnell dein Charakter in einer Gefahrensituation reagieren kann.]\n ")
                befehl=input("[Gib nun 'würfeln' ein, um herauszufinden, wie gut du mit dem Angreifer fertig wirst.]\n > ").lower()
                if befehl =="würfeln":
                    print ("Wessins Würfel: " + str(wuerfel_w12) +"\n")
                    warten2()
                    print("Wessins Angriffswurf: " + str(feind_angriff) + "\n")
                    warten2()
                    print("Dein Würfel: " + str(spieler.wuerfel_w12) + "\n")
                    warten2()
                    print("Dein Reflexwurf: " + str(reflexwurf_spieler) + "\n")
                    warten2()
                    if feind_angriff > reflexwurf_spieler or wuerfel_w12== 12:
                        print("[MISSERFOLG]\n")
                        warten2()
                        print("Du siehst den Angriff kommen, kannst aber nicht rechtzeitig reagieren.\n")
                        warten2()
                        print("Wessins Messer bohrt sich in deine Brust.\n")
                        warten2()
                        wessin_schaden=random.randint(1,4)
                        print("Schaden: " + str(wessin_schaden) + "\n")
                        warten2()
                        spieler.lebenskraft=spieler.lebenskraft - wessin_schaden
                        print("Deine Lebenskraft: " + str(spieler.lebenskraft) + "/" + str(spieler.max_lebenskraft) + "\n")
                        if spieler.lebenskraft <= 0:
                            print("Die Luft bleibt dir weg.\n")
                            warten3()
                            print("Sie wird geradezu aus deiner Brust gepresst.\n")
                            warten3()
                            print("Du schaust in Wessins Augen.\n")
                            warten3()
                            print("Diese hasserfüllten Augen.\n")
                            warten3()
                            print("Dann kippst du nach hinten und ringst um Luft. \n")
                            warten3()
                            print("Vor deinen Augen wird es langsam dunkel.\n")
                            warten3()
                            print("Das Letzte, was du siehst, ist Wessin.\n")
                            warten3()
                            print("Er macht einen Schritt auf dich zu und holt sein Messer aus deiner Brust.\n")
                            warten3()
                            print("Dann verlässt er dein Blickfeld.\n")
                            warten3()
                            print("Arme Dolly! Du warst so kurz davor!\n")
                            warten3()
                            print("Vielleicht werden dir die Götter Gnade walten lassen, die du im Leben nicht kanntest.\n")
                            warten3()
                            print("Dein Abenteuer in der Welt der Lebenden ist aber hiermit zu Ende.\n")
                            warten3()
                            print("Dein Lebenspfad durch hinterhältigen Verrat abrupt abgeschnitten.\n")
                            warten3()
                            befehl = input("Willst du noch einmal spielen?\n > ").lower()
                            if befehl == "ja":
                                raum_start4()
                            elif befehl == "nein":
                                quit()
                            else:
                                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                        else:
                            print("Deine Brust brennt, als hätte man sie gerade gebrandmarkt.\n")
                            warten3()
                            print("Du brauchst vermutlich einen guten Medikus, und das ziemlich bald.\n")
                            warten3()
                            print("Noch kannst du aber stehen.\n")
                            warten3()
                            print("Mit einem Messer in der Brust kannst du gerade nicht viel tun.\n")
                            warten3()
                            print("Dir ist aber klar, dass Wessin nicht mehr nachlassen wird.\n")
                            warten3()
                            print("Nur einer von euch kann die Säuselhöhle lebendig verlassen.\n")
                            warten3()
                            print("Deine Hände schnellen reflexartig nach dem Hals des Zwergs.\n")
                            warten3()
                            print("Selbst in diesem geschwächten Zustand bist du stärker als er.\n")
                            warten3()
                            print("Vom Andrenalinrausch ganz zu schweigen.\n")
                            warten3()
                            print("Wessin versucht sich verzweifelt zu befreien.\n")
                            warten3()
                            print("Schließlich verlassen ihn seine Kräfte jedoch, und der Zwerg erstarrt.\n")
                            warten3()
                            print("Du stehst auf und atmest schwer aus.\n")
                            warten3()
                            print("Es ist vollbracht.\n")
                            warten3()
                            print("Alles, was bleibt, ist Dolly zu holen und von hier zu verschwinden.\n")
                            warten3()
                            szene_epilog()
                    else:
                            print("Du siehst den Angriff kommen und kannst zum Glück noch rechtzeitig reagieren.\n")
                            warten3()
                            print ("Du rollst zur Seite, stehst auf und reißt ihm das Messer aus der Hand.\n")
                            warten3()
                            print("Du warst eben schon immer stärker, auch wenn Wessin ein Zwerg ist.\n")
                            warten3()
                            print("Du willst die Situation friedlich lösen, aber dir wird klar, dass er niemals aufgeben wird.\n")
                            warten3()
                            print("Es kann nur auf eine Weise enden.\n")
                            warten3()
                            print("Du nimmst das rituelle Messer.\n")
                            warten3()
                            print("Das gleiche Messer, mit der erst Dolly und dann dicht erstechen wollte...\n")
                            warten3()
                            print("Dann rammst du es ihm in die Brust.\n")
                            warten3()
                            print("Wessin schaut dich mit einem hasserfüllten Blick an.\n")
                            warten3()
                            print("Dann wird er leer und glasig.\n")
                            warten3()
                            print("Wessin kippt nach hinten und bleibt regungslos liegen.\n")
                            warten3()
                            print("Du stehst auf und atmest schwer aus.\n")
                            warten3()
                            print("Es ist vollbracht.\n")
                            warten3()
                            print("Alles, was bleibt, ist Dolly zu holen und von hier zu verschwinden.\n")
                            warten3()
                            szene_epilog()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")

        def szene_epilog():
            print("Du verlässt endlich die Säuselhöhle, Dolly brav am Seil an deiner Seite.\n")
            warten3()
            print("Du blickst nicht zurück, deine Augen sind auf dein Dorf in der Ferne fixiert.\n")
            warten3()
            print("Dir fällt dabei auf, dass die Lichtverhältnisse nach deinem Abenteuer in etwa gleich geblieben sind.\n")
            warten3()
            print("Es müsste also wieder Morgendämmerung sein.\n")
            warten3()
            print("Warst du wirklich die ganze Nacht weg?\n")
            warten3()
            print("Und tatsächlich: Mit der langsam abfallenden Anspannung spürst du immer mehr die Müdigkeit.\n")
            warten3()
            print("Für den Schlaf bleibt dir leider keine Zeit - dein Bauernhof muss versorgt werden.\n")
            warten3()
            print("Du seufzt. Das wird ein langer Tag,\n")
            warten3()
            print("Vielleicht ist es aber auch besser so.\n")
            warten3()
            print("Du musst die Ereignisse der letzten Nacht erst einmal verarbeiten, das machst du am besten bei der Arbeit.\n")
            warten3()
            print("Die Säuselhöhle... Du kannst nur hoffen, dass du nie wieder dorthin zurückkehren musst.\n")
            warten3()
            print("Zu viele Geister der Vergangenheit... Maika, Orks, Zwerge, Kulte, Schmuggler...\n")
            warten3()
            print("Du hast dir immer so viel Mühe gegeben, dich nicht in solche Dinge einzumischen.\n")
            warten3()
            print("Du wolltest dich nur um deine Nächsten kümmern. Das ist die Welt, die du verstehst.\n")
            warten3()
            print("Vermutlich solltest du trotzdem mit dem Dorfältesten darüber reden, was du dort gesehen hast.\n")
            warten3()
            print("Du wirst das Gefühl nicht los, dass sich das ruhige Dorfleben schon bald ändern wird.\n")
            warten3()
            print("Aber vorerst... Vorerst hast du alles, was du brauchst.\n")
            warten3()
            if spieler.edelsteine==True:
                print("[Edelsteine: Ja]\n")
                warten3()
                print("Du holst die Edelsteine raus, die du vorhin eingesteckt hast, und spielst damit auf deiner Handfläche.\n")
                warten3()
                print("Vielleicht hast du sogar mehr, als du brauchst.\n")
                warten3()
                print("Du weißt nicht, wie viel Geld dir diese Steinchen einbringen können.\n")
                warten3()
                print("Aber irgendwas sagt dir, dass du dir Einiges davon leisten kannst.\n")
                warten3()
                print("Wie es aussieht, wird der Winter doch recht angenehm.\n")
                warten3()
            else:
                print("[Edelsteine: Nein]\n")
                warten3()
                pass
            print("So gehst du gedankenversunken weiter.\n")
            warten3()
            print("Dir fällt eine schöne Melodie aus deiner Kindheit ein.\n")
            warten3()
            print("Du hast schon lange nicht mehr an sie gedacht, doch jetzt ertappst du dich dabei, dass du sie summst.\n")
            warten3()
            print("Du blickst kurz gen Ost und siehst die langsam aufgehende Sonne.\n")
            warten3()
            print("Das bedeutet, du hast noch einen langen Arbeitstag, ehe du wieder etwas Schlaf bekommen kannst.\n")
            warten3()
            print("Aber das ist in Ordnung.\n")
            warten3()
            print("Du gehst nach Hause.\n")
            warten3()
            print ("Ende\n")
            warten3()
            print("[Herzlichen Glückwunsch!]\n")
            warten()
            print("[Du hattest den Mut, dich einem gefährlichen Feind zu stellen, und hast die arme Dolly zurückgeholt.]\n")
            warten()
            print("[Nun kann das fluffige Wesen sein weiteres Schaf-Dasein genießen, und Olig kehrt in sein normales Bauernleben zurück.]\n")
            warten()
            print("[Die Spielregeln und die Handlung des Zeit-Der-Zünfte-Systems zu Testzwecken waren stark vereinfacht.]\n")
            warten()
            print("[Hoffentlich hat dir die Erfahrung trotzdem gefallen.]\n")
            warten()
            print("[Wenn ja: Hast du auch alles mitbekommen und entdeckt, was die Säuselhöhle zu bieten hatte?]\n")
            warten()
            print("[Und was noch wichtiger ist: Hat das Spiel ordnungsgemäß funktioniert?]\n")
            warten()
            print("[Gib dem Entwickler doch gerne eine Rückmeldung. Lief das Programm irgendwo nicht korrekt?]\n")
            warten()
            print("[Welcher Weg und welche Entscheidungen führten deinen Charakter schließlich zum Ziel?]\n")
            warten()
            print("[Und überhaupt: Wenn du etwas mitzuteilen hast, gib dem Entwickler gerne Bescheid!]\n")
            warten()
            print("Und nun: die wichtigste Frage aller Fragen...]\n")
            warten2()
            befehl = input("Willst du noch einmal spielen?\n > ").lower()
            if befehl == "ja":
                raum_start4()
            elif befehl == "nein":
                quit()
            else:
                print(

                    "[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
            pass

        def raum_westkorridor1():
            print ("[Du befindest dich nun im westlichen Gang] \n")
            warten2()
            print ("Der schmale Gang führt weiter in die Tiefen der Säuselhöhle. \n")
            warten2()
            print("Die Wände sind feucht und stark mit Moos bewachsen, und du spürst einen schwachen Windzug.\n")
            warten2()
            print("Du kannst keine Löcher im Gestein erkennen, aber irgendwo müssten die eigentlich sein.\n")
            warten2()
            print("Der Wind zieht mit einem tiefen Ton an dir vorbei, viel tiefer als das hohe Pfeifen am Eingang. \n")
            warten2()
            print("An diesen Ort kannst du dich erinnern, vor allem die Moosschlachten gehörten damals zu euren Lieblingsspielen.\n")
            warten2()
            print("Oh, wie sauer die Eltern damals doch waren!\n")
            warten2()
            print("Aber zumindest hieß es auch, dass ihr nicht allzu tief in die Höhle vorgestoßen wart.\n")
            warten2()
            print("Niemand kam bei Moosschlachten um. Zumindest, soweit du das beurteilen kannst.\n")
            warten2()
            print("Kinder, die in diesen Gängen Versteckspiele mitmachten, hatten nicht immer so viel Glück. \n")
            warten2()
            print("Der lange Gang öffnet sich schließlich zu einer großen Höhle mit einer Weggabelung. So tief warst du hier noch nie.\n")
            warten2()
            print("Von hier aus führt ein Gang zu deiner Rechten nach Norden, links einer nach Süden. Natürlich kannst aber auch wieder zurückgehen.\n")
            warten2()
            befehl = input("Wo willst du hin? (Optionen: Norden, Süden, Osten) \n >").lower().strip()
            for i in befehl:
                if "nord" in befehl:
                    raum_westkorridor1_nord()
                elif "süd" in befehl:
                    raum_westkorridor1_sued()
                elif "ost" in befehl:
                    raum_kreuzung5()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                pass

        def raum_kreuzung5():
            print ("[Du befindest dich wieder an der Kreuzung.]\n")
            warten2()
            print("Du machst den ganzen scheinbar unendlichen Weg zurück und kommst schließlich wieder zur Kreuzung.]\n")
            warten2()
            print("Zu deiner Rechten geht es nach Osten, hinter dir liegt der Süden, und vor dir der Norden. Links geht nach Westen.\n")
            warten2()
            befehl = input("Wo willst du hin? (Optionen: Norden, Osten, Süden, Westen) \n > ").lower()
            if "nord" in befehl:
                raum_eingang_hoehle2()
            elif "west" in befehl:
                raum_westkorridor1()
            elif "süd" in befehl:
                raum_suedkorridor1()
            elif "ost" in befehl:
                raum_ostkorridor1()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")

        def raum_westkorridor1_sued():
            print("[Du folgst dem westlichen Gang nach Süden.]\n")
            warten2()
            print ("Du bist an der Weggabelung nach Süden ab und folgst einem überraschend breiten und ziemlich langen Gang.\n")
            warten2()
            print("Dir fällt auf, dass der Moos immer weniger wird, je weiter du in die Höhle vordringst.\n")
            warten2()
            print("Hier und da entdeckst du ein paar verwitterte Malereien.\n")
            warten2()
            print("Kinder, die früher in der Säuselhöhle gespielt haben, wagten sich nur selten so weit.\n")
            warten2()
            print ("Dabei fragst du dich, wie sie das überhaupt geschafft haben. Licht gibt do tief in der Höhle nämlich nicht. \n")
            warten2()
            print("Du überlegst, welche Nichtmenschen es damals im Dorf gab. Viele dürften es eigentlich nicht gewesen sein.\n")
            warten2()
            print("Ein paar Zwergenfamilien kamen erst vor etwa fünf Jahren hierher, Dunkelelfen hast du hier noch nie gesehen, und Orks waren hier noch nie willkommen.\n")
            warten2()
            print("Andere Rassen mit Dunkelsicht fallen dir nicht ein. Jedenfalls keine Sim'iari, Menschen sowieso nicht. \n")
            warten2()
            print("Elfen? Nicht, dass du wüsstest...\n")
            warten2()
            print ("Wie ist es bei Kurzlingen? Davon gibt es tatsächlich welche im Dorf. Du müsstest mal einen bei Gelegenheit fragen.\n")
            warten2()
            print("Du glaubst ebenfalls nicht, dass jemand einem Kind eine Fackel in die Hand geben würde.\n")
            warten2()
            print("Und Lampen sind zu teuer.\n")
            warten2()
            print ("Aber hier sind sie, die Hinterlassenschaften von Kinderspielen!\n")
            warten2()
            print("Irgendwie müssen sie es also hinbekommen haben.\n")
            warten2()
            print("Gedankenversunken kommst du also voran, die Zeit scheint dabei genau wie jegliche Geräusche von Draußen immer mehr zu verschwinden.\n")
            warten2()
            raum_westkorridor2_1()
            pass

        def raum_westkorridor1_sued_nach_nord():
            print("[Du folgst dem Gang nach Norden.]\n")
            warten2()
            print("Du gehst geradeaus und folgst einem überraschend breiten und ziemlich langen Gang.\n")
            warten2()
            print("Dir fällt auf, dass der Mooswuchs wieder zunimmt, je weiter du nach Norden vordringst.\n")
            warten2()
            print("Hier und da entdeckst du ein paar verwitterte Malereien.\n")
            warten2()
            print("Kinder, die früher in der Säuselhöhle gespielt haben, wagten sich nur selten so weit.\n")
            warten2()
            print("Dabei fragst du dich, wie sie das überhaupt geschafft haben. Licht gibt do tief in der Höhle nämlich nicht. \n")
            warten2()
            print("Du überlegst, welche Nichtmenschen es damals im Dorf gab. Viele dürften es eigentlich nicht gewesen sein.\n")
            warten2()
            print("Ein paar Zwergenfamilien kamen erst vor etwa fünf Jahren hierher.\n")
            warten2()
            print("Dunkelelfen hast du hier noch nie gesehen.\n")
            warten2()
            print("und Orks waren hier sowieso noch nie willkommen.\n")
            warten2()
            print("Andere Rassen mit Dunkelsicht fallen dir nicht ein. Jedenfalls keine Sim'iari, Menschen sowieso nicht. \n")
            warten2()
            print("Elfen? Nicht, dass du wüsstest...\n")
            warten2()
            print("Wie ist es bei Kurzlingen? Davon gibt es tatsächlich welche im Dorf. Du müsstest mal einen bei Gelegenheit fragen.\n")
            warten2()
            print("Du glaubst ebenfalls nicht, dass jemand einem Kind eine Fackel in die Hand geben würde.\n")
            warten2()
            print ("Und Lampen sind zu teuer.\n")
            warten2()
            print("Aber hier sind sie, die Hinterlassenschaften von Kinderspielen!\n")
            warten2()
            print("Irgendwie müssen sie es also hinbekommen haben.\n")
            warten2()
            print("Gedankenversunken kommst du also voran, die Zeit scheint dabei geradezu zu verschwinden, die Naturgeräusche von Draußen sind aber langsam wieder zu hören.\n")
            warten2()
            raum_westkorridor2_1()
            pass

        def raum_westkorridor1_sued_zurueck():
            print("[Du befindest dich nun im westlichen Gang] \n")
            warten2()
            print("Du folgst dem kurvigen Gang und kommst wieder zur Weggabelung.\n")
            warten2()
            print("Nun geht es in Richtung Osten zurück zur Kreuzung, Es gäbe allerdings auch den Weg nach Norden.\n")
            warten2()
            print("Natürlich kannst auch dem Gang nach Süden folgen.\n")
            warten2()
            befehl = input("Wo willst du hin? (Optionen: Norden, Osten, Süden)? \n > ").lower()
            if "nord" in befehl:
                raum_westkorridor1_nord()
            elif "süd" in befehl:
                raum_westkorridor1_sued()
            elif "ost" in befehl:
                raum_kreuzung4()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
            pass

        def raum_westkorridor2_1():
            print ("[Du befindest dich in der Tempelhöhle.]\n")
            warten2()
            print("Vor die öffnet sich eine große Höhle, die genug Platz für eine ganze Dorfversammlung bieten würde.\n")
            warten2()
            print("Mit dem bisschen Licht kannst du leider nicht viel erkennen - aber scheinbar hatte jemand das so ähnlich gesehen.\n")
            warten2()
            print("Auf dem Boden entdeckst du Spuren: Rituelle Markierungen, Reste irgendwelcher Werkzeuge, hier und da eine Art Kleidung oder Stoffreste.\n")
            warten2()
            print("Wie es aussieht, war dieser Ort früher von einer Art Kult benutzt. Aber von wem?\n")
            warten2()
            print("Leider kennst du dich in Sachen Religion nicht überhaupt nicht aus. Die Symbole kommen dir trotzdem bekannt vor...\n")
            warten2()
            print("[Jetzt kannst du dich in Sachen Religion ausprobieren.]\n")
            warten2()
            print("[Als einfacher Bauer kennst du dich hast du in deiner Religionsfertigkeit keine Punkte, einen kleinen Bonus hast du drauf trotzdem.]\n")
            warten2()
            befehl=input("[Gib nun bitte 'würfeln ein.] \n > ").lower()
            if befehl=="würfeln":
                wurf_religion = spieler.wurf_religion()
                warten2()
                if wurf_religion >=14:
                    print("[ERFOLG]\n")
                    warten2()
                    print("Du kannst natürlich nur mutmaßen, aber die Symbole scheinen auf einen Bes hinzudeuten.\n")
                    warten2()
                    print ("Dich schaudert's.")
                    warten()
                    print("Bessy...böswillige Geister, stets auf der Suche nach Gelegenheiten zum Unheilstiften...\n")
                    warten2()
                    print("Und manchmal nach einer guten Abmachung mit den Menschen.\n")
                    warten2()
                    print("Du wusstest gar nicht, dass sie regelrechte Kulte anziehen.\n")
                    warten()
                    print ("Und um welchen Bes es sich dabei handeln soll, kannst du sowieso beim besten Willen nicht sagen.\n")
                    warten2()
                    print("Vielleicht solltest aber später mit dem Dorfältesten sprechen - die Spuren scheinen gar nicht so lange her zu sein.\n")
                    warten2()
                    raum_westkorridor2_2()
                else:
                    print("[MISSERFOLG]\n")
                    warten2()
                    print("Nein. Es fällt dir beim besten Willen nicht ein.\n")
                    warten2()
                    print("Vielleicht solltest aber später mit dem Dorfältesten sprechen - die Spuren scheinen gar nicht so lange her zu sein.\n")
                    warten2()
                    raum_westkorridor2_2()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
            pass

        def raum_westkorridor2_2():
            print("Soweit du es beurteilen kannst, hat diese Höhle nur zwei Ausgänge, die du ohne weitere Ausrüstung erreichen kannst.\n")
            warten2()
            print("Der Gang im Nordosten des Raums führt nach Norden, im Südosten entdeckst du aber noch einen Gang.\n")
            warten2()
            befehl=input("Wo willst du hin? (Optionen: Norden, Osten)\n > ").lower()
            if "ost" in befehl:
                raum_westkorridor3()
            elif "nord" in befehl:
                raum_westkorridor1_sued_nach_nord()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                pass

        def raum_westkorridor3():
            warten2()
            print("\n[Du dringst tief in die Säuselhöhle vor.]\n")
            warten2()
            print("Du folgst dem östlichen Gang noch eine Weile.\n")
            warten2()
            print("Außer leblosem Gestein entdeckst du soweit nichts.\n")
            warten2()
            print("Es scheint fast, als würde sämtliches Leben hier zum Stillstand kommen.\n")
            warten2()
            print("Dann musst du plötzlich anhalten.\n")
            warten2()
            print("Vor dir erstreckt sich ein riesiges Loch.\n")
            warten2()
            print("Du schaust in die Dunkelheit unter dir, entdeckst aber nichts außer der schwarzen Leere.\n")
            warten2()
            print("Mehr noch: Du bekommst das Gefühl, dass die Dunkelheit vielmehr dich betrachtet als du sie.\n")
            warten2()
            print("Zum Glück siehst du auch eine breite Holzbrücke, die über das Loch führt.\n")
            warten2()
            print("Du fragst dich, wer sie gebaut hat.\n")
            warten2()
            print("Und wofür. Wann?\n")
            warten2()
            print("Du gehst du über die Brücke und siehst schließlich etwas.\n")
            warten2()
            print("Licht!\n")
            warten2()
            print("Du kommst dem Licht näher und stehst wieder vor einer grö0eren Höhle.\n")
            warten2()
            print ("Was du dort erblickst, lässt sich kaum beschreiben.\n")
            warten2()
            print("Du siehst Dolly - angebunden, mitten in einem Kreis aus einer roten Substanz.\n")
            warten2()
            print("Neben dem Kreis erkennst du einen Tisch mit irgendwelchen Werkzeugen.\n")
            warten2()
            print("Das Ganze sieht verdächtig nach einer Art Opfer-Ritual aus.\n")
            warten2()
            print("Da kommt auch das Licht her. Rituelle Kerzen.\n")
            warten2()
            print("Fast hättest du dich schon gewundert. Orks können ja bekannterweise perfekt im Dunkeln sehen.\n")
            warten2()
            print("Genau wie Zwerge und Dunkelelfen.\n")
            warten2()
            print("Den Übeltäter kannst du auch erkennen.\n")
            warten2()
            print("Ein großer schwarzer Ork ist gerade dabei, eine Klinge zu schärfen.\n")
            warten2()
            print("Dieser Bastard!\n")
            warten2()
            print ("Arme Dolly! Du musst sie unbedingt da rausholen!\n")
            warten2()
            print ("Der Ork scheint sich dabei mit jemandem zu unterhalten, und schon bald siehst du, mit wem.\n")
            warten2()
            print("Einem Zwerg, den du sofort erkennst.\n")
            warten2()
            print("Wessin. Dein Bauernhof-Nachbar.\n")
            warten2()
            print("Was um alles in der Welt passiert hier eigentlich?\n")
            warten2()
            print("Was immer es ist: Die Zeit ist knapp!\n")
            warten2()
            print("Du hast mehrere Optionen:\n")
            warten2()
            print("Du kannst die Entführer natürlich stellen und versuchen, Dolly mit Worten zurückzuholen.\n")
            warten2()
            print("Würden sie darauf hören? Irgendwie hast du da deine Zweifel. Aber man weiß ja nie.\n")
            warten2()
            print("Du kannst natürlich auch deine Axt rausholen und direkt los schwingen.\n")
            warten2()
            print("Je schneller du mit dem Ork fertig wirst, desto besser.\n")
            warten2()
            print("Den Rest kannst du später klären.\n")
            warten2()
            print("Oder wie wäre es mit einem Überraschungsangriff? Du hast immer noch deine Fackel!\n")
            warten2()
            print("Du hast sie noch nie als Waffe benutzt, aber du hast gehört, dass man sie auch werfen kann.\n")
            warten2()
            print("Einen Versuch könnte es jedenfalls wert sein.\n")
            warten2()
            print("Bis jetzt scheinen dich die Beiden nicht zu bemerken.\n")
            warten2()
            print("Außerdem hast du Glück: Der Ork hat keine Rüstung an. Sein Lederpanzer liegt neben dem Tisch.\n")
            warten2()
            print ("Beides kann sich aber jederzeit ändern.\n")
            warten2()
            befehl=input("Was willst du tun? (Optionen: reden, angreifen, Fackel werfen) \n > ").lower()
            if "rede" in befehl:
                warten2()
                szene_dialog1()
            elif "greife" in befehl:
                warten2()
                print("Nach kurzer Überlegung zum Schluss, dass du viel zu lange überlegst.\n")
                warten2()
                print("Was immer die Beiden vorhatten, sie kommen hier NICHT mehr lebend raus.\n")
                warten2()
                print("Du umklammerst deine Axt und stürmst auf den Ork zu.\n")
                szene_bosskampf1()
            elif "fackel" or "werfe" in befehl:
                warten2()
                print ("Du überlegst nicht lange, dann wirfst deine Fackel nach dem schwarzen Unhold.\n")
                warten2()
                print("Wenn sie noch nicht brannte, tut sie es spätestens jetzt.\n")
                warten2()
                angriffswurf=(spieler.geschick+spieler.wuerfel_w12)-3-2
                print("Würfel: " + str(spieler.wuerfel_w12))
                warten2()
                print("Angriffswurf: " + str(angriffswurf) + "\n")
                warten2()
                spieler.ausdauer -= 1
                print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                wuerfel_w4 = random.randint(1, 4)
                warten2()
                if spieler.wuerfel_w12 ==1:
                    print("Du versuchst, die Fackel zu werfen, doch sie gleitet dir vor lauter Aufregung aus der Hand und fällt runter.\n")
                    warten2()
                    print("Sie macht Krach, und die Entführer werden auf dich aufmerksam.\n")
                    warten2()
                    print("Würfel: " + str(wuerfel_w4) + "\n")
                    warten2()
                    if wuerfel_w4 == 4:
                        print("Aber nicht, bevor deine eigene Fackel deine Kleidung in Brand steckt.\n")
                        warten2()
                        feuerschaden = random.randint(1, 6)
                        print("Du kannst das Feuer zwar ausklopfen, erleidest dabei jedoch " + str(feuerschaden) + " Punkte Feuerschaden.\n")
                        warten2()
                        spieler.lebenskraft = spieler.lebenskraft - feuerschaden
                        print("Deine Lebenskraft: " + str(spieler.lebenskraft) + "/" + str(spieler.max_lebenskraft))
                        warten2()
                    else:
                        pass
                    print ("Das Missgeschick hat dich eindeutig nicht gerade bedrohlich aussehen lassen.\n")
                    warten2()
                    print ("Für einen Rückzieher ist aber zu spät.\n")
                    warten2()
                    print("Natürlich kannst du aber immer noch versuchen, mit den Beiden zu reden und Dolly ohne Gewalt zurückholen.\n")
                    warten2()
                    befehl = input("Was willst du tun? (Optionen: reden, angreifen) \n > ").lower()
                    if "rede" in befehl:
                        szene_dialog1()
                    elif "greife" in befehl:
                        warten2()
                        print("Nach kurzer Überlegung zum Schluss, dass du viel zu lange überlegst.\n")
                        warten2()
                        print("Was immer die Beiden vorhatten, sie kommen hier NICHT mehr lebend raus.\n")
                        warten2()
                        print("Du umklammerst deine Axt und stürmst auf den Ork zu.\n")
                        szene_bosskampf1()
                elif angriffswurf >= ork.verteidigung or spieler.wuerfel_w12==12:
                    print("[ERFOLG]\n")
                    warten2()
                    print ("Deine Fackel dreht sich im Flug, trifft das Scheusal dann aber doch mit der Flamme direkt ins Gesicht, bevor er reagieren kann.\n")
                    warten2()
                    wuerfel_w6_1=random.randint(1,6)
                    wuerfel_w6_2 = random.randint(1, 6)
                    wuerfel_w6_3 = random.randint(1, 6)
                    schaden= wuerfel_w6_1+wuerfel_w6_2+wuerfel_w6_3
                    ork.lebenskraft=ork.lebenskraft-schaden
                    print ("Würfel: " + str(wuerfel_w6_1) + str(wuerfel_w6_2) + str(wuerfel_w6_3) + "\n")
                    warten2()
                    print("Schaden: " + str(schaden) + "\n")
                    warten2()
                    print("Lebenskraft des Gegners: " + str(ork.lebenskraft) + "/" + str(ork.max_lebenskraft) + "\n")
                    warten2()
                    print ("Der Ork schreit entsetzlich auf. Selbst wenn er hier lebendig wieder herauskommt, wird ihn die Verbrennung dieses Treffen nive vergessen lassen.\n")
                    warten2()
                    print ("[DER ORK ERHÄLT 2 PUNKTE DEGENERATION.]\n")
                    warten2()
                    print("[Die Degeneration bezeichnet die körperliche Entstellung, die deinem Charakter widerfahren kann.\n")
                    warten2()
                    print("[Steigt sie zu hoch, kann sich der Charakter nicht mehr unter Leuten blicken lassen.]")
                    warten2()
                    print("[Mehr dazu irgendwann im nächsten Abenteuer.]")
                    warten2()
                    wuerfel_w4 = random.randint(1, 4)
                    print("Würfel: " + str(wuerfel_w4))
                    warten2()
                    if wuerfel_w4 == 4:
                        print("Während die Fackel von seinem verbrannten Gesicht runterfällt, berührt sie ihm Fall seine Kleidung.\n")
                        warten2()
                        feuerschaden = random.randint(1, 6)
                        print("Sie fängt sofort Feuer, brennt an seiner Haut und verursacht " + str(feuerschaden) +" Punkte Feuerschaden, ehe er das Feuer ausklopfen kann.\n")
                        warten2()
                        ork.lebenskraft=ork.lebenskraft-feuerschaden
                        if ork.lebenskraft <= 0:
                            print("Bevor der Ork reagieren kann, breitet sich das feuer aus.\n")
                            warten2()
                            print ("scheinbar hatte er sich mit etwas eingeölt.\n")
                            warten2()
                            print ("Möglicherweise für das Ritual, das hier stattfinden soll.\n")
                            warten2()
                            print("Letztlich spielt es aber keine Rolle.\n")
                            warten2()
                            print ("Der orkische Bastard versucht verzweifelt, das Feuer zu löschen, sinkt dann aber auf die Knie, \n"
                                   "fällt auf den Boden und erstarrt inmitten der lichterloh brennenden Flammen.\n")
                            warten2()
                            print ("Du hättest nicht gedacht, dass dein Überrraschungsangriff so gut funktioniert.\n")
                            warten2()
                            print ("Aber du beschwerst dich auch nicht gerade über das Ergebnis.\n")
                            warten2()
                            szene_sieg()
                        else:
                            print("Der Ork bleckt seine Zähne und stürmt grunzend auf dich zu.\n")
                            warten2()
                            print("Deine Hände umklammern reflexartig deine zweihändige Axt.\n")
                            warten2()
                            print("Du machst dich bereit zum Kampf.\n")
                            warten2()
                            raum_bosskampf1()
                    else:
                        print("Der Ork bleckt seine Zähne und stürmt grunzend auf dich zu.\n")
                        warten2()
                        print("Deine Hände umklammern reflexartig deine zweihändige Axt.\n")
                        warten2()
                        print("Du machst dich bereit zum Kampf.\n")
                        warten2()
                        raum_bosskampf1()
                else:
                    print("[MISSERFOLG]\n")
                    warten2()
                    print("Deine Fackel fliegt direkt am Ork vorbei und landet irgendwo zwischen ihm und Wessin.\n")
                    warten2()
                    print("Du fragst dich, was du dir bei dieser Aktion eigentlich erhofft hast.\n")
                    warten2()
                    print("Aber gut. Einen Versuch war es wert.\n")
                    warten2()
                    print("Nun schauen dich die beiden Entführer an.\n")
                    warten2()
                    print ("Spätestens jetzt wissen sie, dass du hier bist.\n")
                    warten2()
                    print("Du könntest jetzt natürlich versuchen, wegzurennen.\n")
                    warten2()
                    print("Aber jetzt bist du schon so weit gekommen!\n")
                    warten2()
                    print("Außerdem stehen die Chancen für einen Menschen, einem Ork davonzulaufen, in der Regel ziemlich schlecht.\n")
                    warten2()
                    print ("Nein, jetzt gibt es kein Zurück mehr!\n")
                    warten2()
                    print("Du könntest allerdings noch einen letzten Diplomatieversuch wagen.\n")
                    warten2()
                    befehl = input("Was willst du tun? (Optionen: reden, angreifen) \n > ").lower()
                    if "rede" in befehl:
                        szene_dialog1()
                    elif "greife" in befehl:
                        warten2()
                        print("Nach kurzer Überlegung zum Schluss, dass du viel zu lange überlegst.\n")
                        warten2()
                        print("Was immer die Beiden vorhatten, sie kommen hier NICHT mehr lebend raus.\n")
                        warten2()
                        print("Du umklammerst deine Axt und stürmst auf den Ork zu.\n")
                        szene_bosskampf1()
                    else:
                        print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                        pass

            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                pass

        def raum_westkorridor1_nord():
            print ("Der zunächst gerade Gang biegt schon bald nach links ab.\n")
            warten2()
            print("Die Geräusche von draußen verstummen langsam, bis nur deine eigenen Schritte zum einzigen Geräusch werden, das du hören kannst.\n")
            warten2()
            print("Der schlängelt sich eine Weile, bis er wieder nach links abbiegt.\n")
            warten2()
            print("Kurz darauf siehst du zu deiner Linken eine Abzweigung, der Gang vor dir führt aber noch weiter.\n")
            warten2()
            print("Hinter dir ginge es aber wieder zurück zur Weggabelung, wenn du lieber zurückgehen willst. \n")
            warten2()
            befehl =input("Wo willst du hin? (Optionen: Norden, Süden, Osten) \n >").lower()
            if "nord" in befehl:
                raum_westkorridor1_nord_zurueck()
            elif "süd" in befehl:
                raum_westkorridor1_nord3()
            elif "ost" in befehl:
                raum_schmugglerhoehle()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                pass

        def raum_westkorridor1_nord_von_sued():
            print("[Du befindest dich im westlichen Gang.]\n")
            warten2()
            print("Du sinnierst darüber, ob du runterspringen willst, überlegst es dir aber doch anders und gehst ein Stück zurück.\n")
            warten2()
            print("Wenn du jetzt weiter geradeaus gehst, Richtung Norden, kommst du wieder zur Weggabelung.\n")
            warten2()
            print("Zu deiner Rechten befindet sich aber eine kleine Abzweigung.\n")
            warten2()
            print("Und natürlich könntest du doch noch dein Glück mit dem tiefen Sprung versuchen.\n")
            warten2()
            befehl=input("Wo willst du hin? (Optionen: Osten, Norden, Süden)\n > ").lower()
            if "ost" in befehl:
                raum_schmugglerhoehle()
            elif "nord" in befehl:
                raum_westkorridor1_nord_zurueck()
                pass
            elif "süd" in befehl:
                raum_westkorridor1_nord3()
            else:
                print(
                    "[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")


        def raum_westkorridor1_nord3():
            print ("Du folgst dem Gang weiter Richtung Süden.\n")
            warten2()
            print ("Dabei fällt dir auf, dass dir nichts auffällt.\n")
            warten2()
            print("Kein Moos, keine Spuren.\n")
            warten2()
            print("Gar nichts.\n")
            warten2()
            print("Es ist, als hätte sich noch nie jemand hierher getraut.\n")
            warten2()
            print("Nicht einmal Pflanzen.\n")
            warten2()
            print("Dolly und ihr Entführer schon gar nicht.\n")
            warten2()
            print("Verwundert, und vielleicht noch mehr eingeschüchtert, machst du trotzdem weiter.\n")
            warten2()
            print("Schon bald reißt der Boden ab.\n")
            warten2()
            print("Vor dir liegt eine ziemlich große Höhle.\n")
            warten2()
            print("In dieser Dunkelheit kannst du nicht viel erkennen, aber dort scheint es definitiv weiterzugehen.\n")
            warten2()
            print("Allerdings geht es dort recht tief runter. Vermutlich könntest du den Fall überstehen, wenn du runterspringst.\n")
            warten2()
            print("Sicher bist du dir dabei jedoch nicht.\n")
            warten2()
            print("Deine einzige andere Option wäre es allerdings, wieder zurückzugehen.\n")
            warten2()
            befehl=input("Was willst du tun? (Optionen: runterspringen, zurückgehen)\n > ")
            if "gehe" in befehl:
                raum_westkorridor1_nord_von_sued()
            elif "spring" in befehl:
                warten2()
                print("\n[Nun brauchen wir wieder einen Wurf, um zu sehen, ob du den Sprung überstehst.]\n")
                warten2()
                print("[Dieses Mal testen wir also deinen Körperbau.]\n")
                warten2()
                print("[Gut, eigentlich wäre der Wurf für die Fertigkeit 'Sportlichkeit'.]\n")
                warten2()
                print("[Als einfacher Bauer hast du diese allerdings nicht trainiert.]\n")
                warten2()
                print ("[Dein Körperbau muss also reichen.]\n")
                warten2()
                befehl=input("[Gib nun bitte 'würfeln' ein.]\n > ").lower()
                if "würfeln" in befehl:
                    wurf_koerperbau = spieler.wurf_koerperbau()
                    warten2()
                    if wurf_koerperbau >= 15:
                        print("[ERFOLG]\n")
                        warten2()
                        print("Du springst runter und landest auf den Beinen.\n")
                        warten2()
                        print("Der Sprung war höher, als es aussah, aber zum Glück kommst du nur mit Schmerzen in den Beinen davon.\n")
                        warten2()
                        print("Du schaust dich um. Auf dem gleichen Wege kommst du schon mal nicht zurück, selbst wenn du Dolly findest.\n")
                        warten2()
                        print("Es bleibt also nichts Anderes übrig, als den Raum zu untersuchen.\n")
                        warten2()
                        raum_westkorridor2_1()
                        pass
                    elif wurf_koerperbau in range (12, 14):
                        print ("[ERFOLG]\n")
                        warten2()
                        print("Du springst runter und landest auf den Beinen, verlierst aber das Gleichgewicht und krachst auf den Boden.\n")
                        warten2()
                        print("Dein gesamter Körper tut weh.\n")
                        warten2()
                        print("Als wäre eine ganze Ochsenherde darüber gelaufen.\n")
                        warten2()
                        print("Irgendwann lässt der Schmerz aber nach.\n")
                        warten2()
                        print("Du hebst den Kopf und fasst dir an das von kleinen Steinen zerkratzte Gesicht.\n")
                        warten2()
                        print("Es tut weh.\n")
                        warten2()
                        print("Aber sich zu beklagen bringt jetzt nichts. Es war ja deine Entscheidung.\n")
                        warten2()
                        print("Du schaust dich um. Der Sprung war höher, als du dachtest.\n")
                        warten2()
                        print("Auf dem gleichen Wege kommst du schon mal nicht zurück, selbst wenn du Dolly findest.\n")
                        warten2()
                        print("Es bleibt also nichts Anderes übrig, als den Raum zu untersuchen.\n")
                        warten2()
                        raum_westkorridor2_1()
                    elif wurf_koerperbau ==1:
                        print("[KRITISCHER MISSERFOLG]\n")
                        warten2()
                        print("Du springst runter und fällst auf den Kopf.\n")
                        warten2()
                        print("Bevor du begreifst, was los ist, brichst du dir das Genick.\n")
                        warten2()
                        print("Vielleicht werden dir die Götter Gnade walten lassen, die du im Leben nicht kanntest.\n")
                        warten2()
                        print("Dein Abenteuer in der Welt der Lebenden ist aber hiermit zu Ende.\n")
                        warten2()
                        print("Der Lebensfaden abrupt abgeschnitten. Durch den eigenen Fehler.\n")
                        warten2()
                        print("Ende \n")
                        warten2()
                        befehl = input("Willst du noch einmal spielen?\n > ").lower()
                        if befehl == "ja":
                            warten2()
                            raum_start4()
                        elif befehl == "nein":
                            quit()
                        else:
                            print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                    else:
                        print("[MISSERFOLG]\n ")
                        warten2()
                        print("Du springst runter, aber der Sprung ist eindeutig höher, als du gedacht hast.\n")
                        warten2()
                        print("Du landest ziemlich unglücklich und brichst dir die Beine.\n")
                        warten2()
                        print("Dein Körper tut höllisch weh.\n")
                        warten2()
                        print("Als du dich an den Schmerz langsam gewöhnst, begreift du, dass du nicht weitermachen kannst.\n")
                        warten2()
                        print("So schmerzhaft es ist, Dolly hier zurückzulassen, ist Überleben jetzt deine Priorität.\n")
                        warten2()
                        print("Du kannst nicht gehen, aber wenn du nur nur durchhältst, kannst du dich vielleicht mir den Armen aus der Höhle rausziehen.\n")
                        warten2()
                        print("Und hoffen, dass dich jemand findet.\n")
                        warten2()
                        print("[Herzlichen Glückwunsch! Jetzt hast du dich in eine brenzlige Lage hineinmanövriert. Und das ganz ohne Fremdhilfe.]\n")
                        warten2()
                        print("[Aber es ist noch nicht alles verloren.]\n")
                        warten2()
                        print("[Jetzt testen wir dein Durchhaltevermögen.]\n")
                        warten2()
                        print("[Als Bauer hast du schon ziemlich starke Arme. Aber wird das Ausreichen?]\n")
                        warten()
                        print("[Der Wurf, den du jetzt ablegen sollst, ist für deine Willenskraft.]\n")
                        warten2()
                        befehl=input("[Gib nun 'würfeln' ein.] \n > ").lower()
                        if befehl=="würfeln":
                            warten2()
                            willenswurf = spieler.wurf_willen()
                            if willenswurf >= 14:
                                print("[ERFOLG]\n ")
                                warten2()
                                print("Es kostet dich unfassbare Mühe, aber irgendwie schaffst du es, aus der Höhle zu kriechen.\n")
                                warten2()
                                print("Immer wieder mit Pausen, dafür unerbittlich kamst du langsam voran, in nahezu vollständiger Dunkelheit.\n")
                                warten2()
                                print("Und schließlich, erreichst du irgendwann dank der schieren Willenskraft den Ausgang und kriechst noch ein Stück weiter.\n")
                                warten2()
                                print("Dann brichst du zusammen.\n")
                                warten2()
                                print("Erst am nächsten Morgen findet man dich wieder.\n")
                                warten2()
                                print("Du hast die Säuselhöhle überlebt, zumindest das kannst als einen kleinen Trostpreis nach Hause mitnehmen.\n")
                                warten2()
                                print("Dolly siehst du allerdings nie wieder.\n")
                                warten2()
                                print("Damit musst du dich nun abfinden, aber das ist ohnehin nicht mehr dein größtes Problem.\n")
                                warten2()
                                print("Außer Dolly hast du nämlich auch andere Tiere, die versorgt werden müssen.\n")
                                warten2()
                                print("Kannst du das mit gebrochenen Beinen machen?\n")
                                warten2()
                                print("Du hast die Wahl: Gibst du deine Ersparnisse für Futter, einen Gehilfen oder einen Arzt aus?\n")
                                warten2()
                                print("Kriegst du so den Winter überstanden? Du weißt es nicht.\n")
                                warten2()
                                if spieler.edelsteine == True:
                                    print("[Edelsteine: Ja]\n")
                                    warten2()
                                    print("Aber zumindest hast du in ein paar Edelsteine gefunden.\n")
                                    warten2()
                                    print("Du weißt nicht, wie wertvoll sie sind, aber irgendwas sagt dir, dass du sie für gutes Geld verkaufen kannst.\n")
                                    warten2()
                                    print("Damit sind deine Aussichten für den Winter zumindest weniger schlimm.\n")
                                    warten2()
                                    print("Es wird schwer. Aber schwere Arbeit hast du noch nie gescheut.\n")
                                    warten2()
                                    print("Ja. Den Winter wirst du irgendwie überstehen. Davon bist du überzeugt.\n")
                                    warten2()
                                    print ("Und danach... nun...\n")
                                print("Dein Schicksal ist jetzt einzig in den Händen der Götter...\n")
                                warten2()
                                print("Ende\n")
                                warten2()
                                befehl = input("Willst du noch einmal spielen?\n > ").lower()
                                if befehl == "ja":
                                    warten2()
                                    raum_start4()
                                elif befehl == "nein":
                                    quit()
                                else:
                                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                            else:
                                print("[MISSERFOLG]\n ")
                                warten2()
                                print("Du versuchst, selbst in diesem Zustand einen Weg aus der Säuselhöhle zu finden.\n")
                                warten2()
                                print("Deine Arme sind stark, und du du kommst zunächst gut voran.\n")
                                warten2()
                                print("Irgendwann lassen aber selbst deine Kräfte nach.\n")
                                warten2()
                                print("Schließlich brichst du zusammen, allein, in nahezu vollständiger Dunkelheit.\n")
                                warten2()
                                print("Du kannst einfach keine Kraft mehr aufbringen.\n")
                                warten2()
                                print("Du weißt in etwa, wo du hin musst, aber der Ausgang scheint unvorstellbar weit weg.\n")
                                warten()
                                print("Du kannst nicht mehr.\n")
                                warten2()
                                print("Du bleibst einfach hier.\n")
                                warten2()
                                print("Für immer.\n")
                                warten2()
                                print("Das letzte, woran du dich erinnerst, ist das Säuseln des Windzugs über deinem Kopf.\n")
                                warten2()
                                print("Vielleicht werden dir die Götter Gnade walten lassen, die du im Leben nicht kanntest.\n")
                                warten2()
                                print("Dein Abenteuer in der Welt der Lebenden ist aber hiermit zu Ende.\n")
                                warten2()
                                print("Der Lebensfaden abrupt abgeschnitten. Durch den eigenen Fehler.\n")
                                warten2()
                                print("Ende \n")
                                warten2()
                                befehl = input("Willst du noch einmal spielen?\n > ").lower()
                                if befehl == "ja":
                                    warten2()
                                    raum_start4()
                                elif befehl == "nein":
                                    quit()
                                else:
                                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")

                        pass
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                    pass
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                raum_westkorridor1_nord3()

        def raum_schmugglerhoehle():
            print ("[Du befindest dich in der Schmugglerhöhle.] \n")
            warten2()
            print ("Die kurze und überraschend breite Abzweigung führt zu einer kleinen Nebenhöhle. \n")
            warten2()
            print("Plötzlich reißt der Boden ab, und du kannst gerade noch rechtzeitig anhalten.\n")
            warten2()
            print("Der Raum vor dir liegt etwa einen Meter tiefer, als hätte ein Stück der Nebenhöhle einfach eingestampft.\n")
            warten2()
            print("Von diesem Raum hast du schon mal gehört. \n")
            warten2()
            print("Dieser Raum soll schon so manchen Menschen - und nicht nur Menschen - das Leben gekostet haben. \n")
            warten2()
            print("Die Schauergeschichten kennt man allzu gut. \n")
            warten2()
            print("Abenteuerlustige, die die Säuselhöhle erkunden wollten...\n")
            warten2()
            print("Kinder, die hier früher gespielt haben...\n")
            warten2()
            print("Manchmal hat konnte man die Unglücklichen noch lebend wieder rausholen.\n")
            warten2()
            print("Meistens nicht.\n")
            warten2()
            print("Bei Kindern war es meistens der Sturz, war die Säuselhäöhle doch einer der ersten Orten, an denen man nach verschwundenen Kindern gesucht hatte.\n")
            warten2()
            print("Schlecht vorbereitete Wanderer waren vielmehr verhungert oder verdurstet.\n")
            warten2()
            print("Dabei war der Sturz selbst oft gar nicht so schlimm, heißt es.\n")
            warten2()
            print("Die Dala... Stola... Stalagmiten, so hießen die Teile! \n")
            warten2()
            print("An denen haben sich die Unglückseelen viel eher verletzt.\n")
            warten2()
            print("Manchmal war allein das schon tödlich, andere haben sich nur stark genug verletzt, dass sie selbst nicht mehr herauskamen.\n")
            warten2()
            print("Bald nach dem... Vorfall... Hat die Säuselhöhle aber einen richtig schlimmen Ruf bekommen. \n")
            warten2()
            print("Die Erwachsenen tadelten Ausflüge auf's Schärfste, Kinder hatten Angst, und Fremde wurden sofort entmutigt.\n")
            warten2()
            print("Nun wird sie nur selten von jemandem aufgesucht.\n")
            warten2()
            print("Und wie es scheint, haben sich Andere diese Tatsache zu Nutzen gemacht. \n")
            warten2()
            print("Vor dir erstecken sich nämlich mehrere Fässer und Truhen unbekannter Herkunft. \n")
            warten2()
            print("Außerdem hat jemand sogar daran gedacht, hier eine Strickleiter anzubringen.\n")
            warten2()
            print("Soweit du es beurteilen kannst, sehen die Sachen eher nach Schmuggelware aus.\n")
            warten2()
            print("Es wäre nicht das erste Mal, dass sich Schmuggler in der Gegend niederlassen, liegt dein Dorf doch nahe einer Imperialen Straße.\n")
            warten2()
            print("Außerdem haben sich die Unbekannten einen richtig guten Ort dafür ausgesucht, wo sich doch praktisch niemand mehr so tief in die Höhle traut.\n")
            warten2()
            print("Aber wenn du so drüber nachdenkst: Wer auch immer die Ware hier abgestellt hat, scheint momentan nicht da zu sein. \n")
            warten()
            print("Da wärst du doch fast versucht, die Ware zu untersuchen!\n")
            warten2()
            print("Dann wiederum: Schmuggler bringen schlechte Neuigkeiten. \n")
            warten2()
            print("Das letzte Mal hat der Schmuggeln direkt die Imperiale Garde auf den Plan gerufen.\n")
            warten2()
            print("Das kann für niemanden gut enden. \n")
            warten2()
            print("Vielleicht solltest du das Ganze hier einfach zerstören, bevor es Ärger gibt!\n")
            warten2()
            print("Zumindest in einem der Fässer scheint Schwarzer Sand zu sein. \n")
            warten2()
            print("Alles, was du tun musst, ist eine Spur aus dieser Substanz zu als Lunte legen und mit deiner Fackel anzuzünden.\n")
            warten2()
            print("Andererseits könnte es später zu noch mehr Ärger führen. \n")
            warten2()
            print("Und eigentlich geht dich das Ganze auch nichts an. Dein Ziel ist Dolly. \n")
            warten2()
            befehl = input ("Was willst du tun? (Optionen: untersuchen, anzünden, weggehen) \n > ").lower()
            if "gehe" in befehl:
                raum_westkorridor1_nord2()
            elif "zünde" in befehl:
                    raum_flucht1()
            elif "untersuche" in befehl:
                spieler.edelsteine=True
                print ("Du untersuchst den Inhalt der Behälter.\n")
                warten2()
                print("In dem Fässern ist hauptsächlich Schwarzer Sand - eine brennbare und gar explosive Substanz, die im Bergbau und einigen Waffen verwendet wird.\n")
                warten2()
                print("In den Truhen liegt alles Mögliche: Kleidung, Edelsteine, einige Waffen, Alkohol.\n")
                warten2()
                print("Leider kannst du außer ein-zwei Edelsteinen nichts davon mitnehmen, dafür bist du einfach nicht ausgerüstet.\n")
                warten2()
                print("Vielleicht solltest du das Versteck später melden.\n")
                warten2()
                print("Oder du lässt es.\n")
                warten2()
                print("Oder du jagst das Ganze Zeug hier direkt in die Luft und ersparst allen gleich das Problem.\n")
                warten2()
                print("So oder so: Du verstehst nicht viel von Edelsteinen, aber du solltest jetzt zumindest um ein-zwei Bur reicher sein.\n")
                warten2()
                print("Für den Winter können diese wörtlich zwischen Leben und Tod entscheiden.\n")
                warten2()
                befehl = input ("Was willst du tun? (Optionen: anzünden, weggehen)\n > ").lower()
                if "weg" and "gehen" in befehl:
                    raum_westkorridor1_nord2()
                elif "zünde" in befehl:
                    raum_flucht1()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                pass
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                raum_schmugglerhoehle()

        def raum_flucht1():
            print ("Du legst eine Spur aus Schwarzem Sand, den du in den Fässern findest, und zündest sie an.\n")
            warten2()
            print ("Allerdings bist du weder Bergbauer noch Krieger. Du hättest nicht gedacht, dass die Spur so schnell kürzer wird.\n")
            warten2()
            print ("Oh, Mist! Die Substanz brennt wirklich schnell! \n")
            warten2()
            print ("Schnell, du musst sofort hier raus! \n")
            warten2()
            warten2()
            print ("[Herzlichen Glückwunsch!]\n")
            warten2()
            print("[Jetzt hast du dich in eine brenzlige Lage hineinmanövriert, und zwar ganz ohne Fremdhilfe.]\n")
            warten2()
            print("[Dein Spielleiter ist stolz auf dich, und erfüllt mit kindlicher Schadenfreude.]\n")
            warten2()
            print("[Aber keine Angst!] \n")
            warten()
            print("[Also... Doch, besorgt solltest du schon sein. Aber noch ist nicht alles verloren!]\n")
            warten2()
            print("[Wenn du Glück hast, kannst du der nahenden Explosion entkommen.]\n")
            warten2()
            print("[Dafür sieht das Spielsystem Rettungs- und Glückswürfe vor.] \n")
            warten2()
            print ("[Schaffst du den Rettungswurf, kannst du schneller rennen als die Explosion.]\n")
            warten2()
            print("[Verfehlst du nur ganz knapp, dann hast du den Glückswurf geschafft und kannst zumindest das Schlimmste verhindern.]\n")
            warten2()
            print ("[Und ansonsten... Nun ja, es hat dich ja niemand gezwungen, die Lunte anzuzünden, nicht wahr?] \n")
            warten2()
            print ("[Oh, und BETE, dass du dabei keine 1 würfelst!]\n")
            warten2()
            befehl=input("[Und nun: Gib bitte 'würfeln' ein.] \n > ").lower()
            if befehl == "würfeln":
                wurf_reflex = spieler.reflexwurf()
                warten2()
                if wurf_reflex >= 14:
                    print("[ERFOLG: RETTUNGSWURF]\n")
                    warten2()
                    print ("Du begreifst den Ernst der Situation und nimmst die Beine in die Hand. Du rennst so schnell du kannst.\n")
                    warten2()
                    print ("Du kannst es zwar selbst nicht glauben, aber durch irgendein Wunder schaffst du es, der Explosion hinter dir zu entkommen.\n")
                    warten2()
                    print("Wenn die Fässer explodieren, bist du schon längst am Rennen.\n")
                    warten2()
                    print("Allerdings löst die Explosion ein Beben in der Höhle aus. Von der Höhlendecke fallen nun große Steine.\n")
                    warten2()
                    befehl=input("[Gib nun wieder 'würfeln' für einen zweiten Rettungswurf ein.]\n > ").lower()
                    if befehl == "würfeln":
                        wurf_reflex_2 = spieler.reflexwurf()
                        warten2()
                        if wurf_reflex_2 >= 14:
                            print("[ERFOLG: RETTUNGSWURF]\n")
                            warten2()
                            print("Unglaublig, aber du schaffst es, allen Gefahren zum Trotz zurück bis zur Kreuzung zu rennen.\n")
                            warten2()
                            print("Unbeschadet!\n")
                            warten2()
                            print ("Außer Atem, aber heilfroh, kommst du zum Stehen.\n")
                            warten2()
                            print("Doch kaum hattest du Luft geholt, hörst du aus den Tiefen der Höhle schwere Schritte.\n")
                            warten2()
                            print("Dann zeigt er sich: Ein großer schwarzer Ork.\n")
                            warten2()
                            print ("Er bleckt seine scharfen Zähne und schaut dich wütend an.\n")
                            warten2()
                            print ("Dolly ist nirgends zu sehen, aber du erkennst eine andere Gestalt neben ihm.\n")
                            warten2()
                            print ("Wessin. Dein Bauernhof-Nachbar.\n")
                            warten2()
                            print("Was um alles in der Welt macht er hier? Was ist hier los?\n")
                            warten2()
                            print ("Auf Reden scheinen die beiden leider nicht aus zu sein.\n")
                            warten2()
                            print ("So hast du es dir nicht vorgestellt, aber die Würfel sind gefallen.\n")
                            warten2()
                            print ("Du machst dich auf einen Kampf gefasst. \n")
                            warten2()
                            raum_bosskampf1()
                        elif wurf_reflex_2 in range (12, 13):
                            print("[ERFOLG: GLÜCKSWURF]\n")
                            warten2()
                            print ("Du schaffst es zwar, den großen fallenden Steinen auszuweichen, wirst aber von einem Haufen köleiner scharfer Steinchen getroffen.\n")
                            warten2()
                            print ("Wenn du Glück hast, bekommst du nur ein paar Kratzer, im schlimmsten Fall werden auch später ein-zwei hässliche Narben bleiben.\n")
                            warten2()
                            print("Außer Atem, aber heilfroh kommst du zum Stehen.\n")
                            warten2()
                            print("Doch kaum hattest du Luft geholt, hörst du aus den Tiefen der Höhle schwere Schritte.\n")
                            warten2()
                            print("Dann zeigt er sich: Ein großer schwarzer Ork.\n")
                            warten2()
                            print("Er bleckt seine scharfen Zähne und schaut dich wütend an.\n")
                            warten2()
                            print("Dolly ist nirgends zu sehen, aber du erkennst eine andere Gestalt neben ihm.\n")
                            warten2()
                            print("Wessin. Dein Bauernhof-Nachbar.\n")
                            warten2()
                            print("Was um alles in der Welt macht er hier? Was ist hier los?\n")
                            warten2()
                            print("Auf Reden scheinen die beiden leider nicht aus zu sein.\n")
                            warten2()
                            print("So hast du es dir nicht vorgestellt, aber die Würfel sind gefallen.\n")
                            warten2()
                            print("Du machst dich auf einen Kampf gefasst. \n")
                            warten2()
                            raum_bosskampf1()
                        else:
                            print("[MISSERFOLG]\n")
                            warten2()
                            print("Du versuchst, dich in Sicherheit zu bringen.\n")
                            warten2()
                            print("Erst sieht es danach aus, als würdest du hier doch noch heil rauskommen.\n")
                            warten2()
                            print("Dann wirst du aber von einem großen Stein erwischt.\n")
                            warten2()
                            print("Du taumelst, verlierst das Tempo.\n")
                            warten2()
                            print("Und bevor du weißt, was passiert ist, wirst du im einstürzenden Tunnel begraben.\n")
                            warten2()
                            print ("Vielleicht werden dir die Götter Gnade walten lassen, die du im Leben nicht kanntest.\n")
                            warten2()
                            print ("Dein Abenteuer in der Welt der Lebenden ist aber hiermit zu Ende.\n")
                            warten2()
                            print ("Der Lebensfaden abrupt abgeschnitten. Durch den eigenen Fehler.\n")
                            warten2()
                            print("Ende \n")
                            warten2()
                            befehl = input("Willst du noch einmal spielen?\n > ").lower()
                            if befehl == "ja":
                                raum_start4()
                            elif befehl == "nein":
                                quit()
                            else:
                                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                elif wurf_reflex in range (12, 13):
                    print("[ERFOLG: GLÜCKSWURF]\n")
                    warten2()
                    print("Du begreifst den Ernst der Situation und nimmst die Beine in die Hand. Du rennst so schnell du kannst.\n")
                    warten2()
                    print("Du kannst es zwar selbst nicht begreifen, aber durch irgendein Wunder schaffst du es, der Explosion hinter dir zu entkommen.\n")
                    warten2()
                    print("Wenn die Fässer explodieren, bist du schon längst am Rennen.\n")
                    warten2()
                    print ("Allerdings wirst du nun von der Flammenwolke durch die Gänge verfolgt.\n")
                    warten2()
                    befehl=input("[Gib nun wieder 'würfeln' für einen zweiten Rettungswurf ein.]\n > ").lower()
                    if befehl == "würfeln":
                        wurf_reflex_3 = spieler.reflexwurf()
                        warten2()
                        if wurf_reflex_3 >= 12:
                            print("[ERFOLG: RETTUNGSWURF]\n")
                            warten()
                            print("Die Flammen bleiben dir dicht auf den Fersen, aber du schaffst es durch unglaubliches Glück, immer einen Schritt voraus zu sein.\n")
                            warten2()
                            print("Allerdings löst die Explosion ein Beben in der Höhle aus. Von der Höhlendecke fallen nun große Steine.\n")
                            warten2()
                            befehl=input("[Gib nun wieder 'würfeln' für einen dritten Rettungswurf ein.]\n > ").lower()
                            if befehl == "würfeln":
                                spieler.reflexwurf()
                                warten2()
                                if spieler.reflexwurf() >= 14:
                                    print("\n[ERFOLG: RETTUNGSWURF]\n")
                                    warten2()
                                    print("Unglaublig, aber du schaffst es, allen Gefahren zum Trotz zurück bis zur Kreuzung zu rennen.\n")
                                    warten2()
                                    print("Unbeschadet!\n")
                                    warten2()
                                    print("Außer Atem, aber heilfroh kommst du zum Stehen.\n")
                                    warten2()
                                    print("Doch kaum hattest du Luft geholt, hörst du aus den Tiefen der Höhle schwere Schritte.\n")
                                    warten2()
                                    print("Dann zeigt er sich: Ein großer schwarzer Ork.\n")
                                    warten2()
                                    print("Er bleckt seine scharfen Zähne und schaut dich wütend an.\n")
                                    warten2()
                                    print("Dolly ist nirgends zu sehen, aber du erkennst eine andere Gestalt neben ihm.\n")
                                    warten2()
                                    print("Wessin. Dein Bauernhof-Nachbar.\n")
                                    warten2()
                                    print("Was um alles in der Welt macht er hier? Was ist hier los?\n")
                                    warten2()
                                    print("Auf Reden scheinen die beiden leider nicht aus zu sein.\n")
                                    warten2()
                                    print("So hast du es dir nicht vorgestellt, aber die Würfel sind gefallen.\n")
                                    warten2()
                                    print("Du machst dich auf einen Kampf gefasst. \n")
                                    warten2()
                                    raum_bosskampf1()
                                elif spieler.reflexwurf() in range(12, 13):
                                    print("[ERFOLG: GLÜCKSWURF]\n")
                                    warten2()
                                    print("Du schaffst es zwar, den großen fallenden Steinen auszuweichen, wirst aber von einem Haufen köleiner scharfer Steinchen getroffen.\n")
                                    warten2()
                                    print("Wenn du Glück hast, bekommst du nur ein paar Kratzer, im schlimmsten Fall werden auch später ein-zwei hässliche Narben bleiben.\n")
                                    warten2()
                                    print("Außer Atem, aber heilfroh kommst du zum Stehen.\n")
                                    warten2()
                                    print("Doch kaum hattest du Luft geholst, hörst du aus den Tiefen der Höhle schwere Schritte.\n")
                                    warten2()
                                    print("Dann zeigt er sich: Ein großer schwarzer Ork.\n")
                                    warten2()
                                    print("Er bleckt seine scharfen Zähne und schsut dich wütend an.\n")
                                    warten2()
                                    print("Dolly ist nirgends zu sehen, aber du erkennst eine andere Gestalt neben ihm.\n")
                                    warten2()
                                    print("Wessin. Dein Bauernhof-Nachbar.\n")
                                    warten2()
                                    print("Was um alles in der Welt macht er hier? Was ist hier los?\n")
                                    warten2()
                                    print("Auf Reden scheinen die beiden leider nicht aus zu sein.\n")
                                    warten2()
                                    print("So hast du es dir nicht vorgestellt, aber die Würfel sind gefallen.\n")
                                    warten2()
                                    print("Du machst dich auf einen Kampf gefasst. \n")
                                    warten2()
                                    raum_bosskampf1()
                                else:
                                    print("[MISSERFOLG]\n")
                                    warten2()
                                    print("Du versuchst, dich in Sicherheit zu bringen.\n")
                                    warten2()
                                    print("Erst sieht es danach aus, als würdest du hier doch noch heil rauskommen.\n")
                                    warten2()
                                    print("Dann wirst du aber von einem großen Stein erwischt.\n")
                                    warten2()
                                    print("Du taumelst, verlierst das Tempo.\n")
                                    warten2()
                                    print("Und bevor du weißt, was passiert ist, wirst du im einstürzenden Tunnel begraben.\n")
                                    warten2()
                                    print("Vielleicht werden dir die Götter Gnade walten lassen, die du im Leben nicht kanntest.\n")
                                    warten2()
                                    print("Dein Abenteuer in der Welt der Lebenden ist aber hiermit zu Ende.\n")
                                    warten2()
                                    print("Der Lebensfaden abrupt abgeschnitten. Durch den eigenen Fehler.\n")
                                    warten2()
                                    print("Ende \n")
                                    warten2()
                                    befehl = input("Willst du noch einmal spielen?\n > ").lower()
                                    if befehl == "ja":
                                        warten2()
                                        raum_start4()
                                    elif befehl == "nein":
                                        quit()
                                    else:
                                        print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")

                            else:
                                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                        elif wurf_reflex_3 in range (10, 11):
                            print("[ERFOLG: GLÜCKSWURF]\n")
                            warten2()
                            print("Die Flammen lecken deinen Rücken, deine Beine, deinen Kopf.\n")
                            warten2()
                            print ("Erst sieht es aus, als würden sie dich gänzlich verschlingen.\n")
                            warten2()
                            print ("Nur durch schiere Willenskraft schaffst du es trotzdem irgendwie, weiterzurennen, un einen Flammen einen halben Schritt voraus zu sein.\n")
                            warten2()
                            print("Allerdings löst die Explosion ein Beben in der Höhle aus. Von der Höhlendecke fallen nun große Steine.\n")
                            warten2()
                            befehl=input("[Gib nun wieder 'würfeln' für einen dritten Rettungswurf ein.]\n > ").lower()
                            if befehl == "würfeln":
                                wurf_reflex_4 = spieler.reflexwurf()
                                if wurf_reflex_4 >= 14:
                                    print("[ERFOLG: RETTUNGSWURF]\n")
                                    warten2()
                                    print("Unglaublig, aber du schaffst es, allen Gefahren zum Trotz zurück bis zur Kreuzung zu rennen.\n")
                                    warten2()
                                    print("Unbeschadet!\n")
                                    warten2()
                                    print("Außer Atem, aber heilfroh kommst du zum Stehen.\n")
                                    warten2()
                                    print("Doch kaum hattest du Luft geholt, hörst du aus den Tiefen der Höhle schwere Schritte.\n")
                                    warten2()
                                    print("Dann zeigt er sich: Ein großer schwarzer Ork.\n")
                                    warten2()
                                    print("Er bleckt seine scharfen Zähne und schaut dich wütend an.")
                                    warten2()
                                    print("Dolly ist nirgends zu sehen, aber du erkennst eine andere Gestalt neben ihm.\n")
                                    warten2()
                                    print("Wessin. Dein Bauernhof-Nachbar.\n")
                                    warten2()
                                    print("Was um alles in der Welt macht er hier? Was ist hier los?\n")
                                    warten2()
                                    print("Auf Reden scheinen die beiden leider nicht aus zu sein.\n")
                                    warten2()
                                    print("So hast du es dir nicht vorgestellt, aber die Würfel sind gefallen.\n")
                                    warten2()
                                    print("Du machst dich auf einen Kampf gefasst. \n")
                                    warten2()
                                    raum_bosskampf1()
                                elif wurf_reflex_4 in range(12, 13):
                                    print("[ERFOLG: GLÜCKSWURF]\n")
                                    warten2()
                                    print("Du schaffst es zwar, den großen fallenden Steinen auszuweichen, wirst aber von einem Haufen köleiner scharfer Steinchen getroffen.\n")
                                    warten2()
                                    print("Wenn du Glück hast, bekommst du nur ein paar Kratzer, im schlimmsten Fall werden auch später ein-zwei hässliche Narben bleiben.\n")
                                    warten2()
                                    print("Außer Atem, aber heilfroh kommst du zum Stehen.\n")
                                    warten2()
                                    print("Doch kaum hattest du Luft geholt, hörst du aus den Tiefen der Höhle schwere Schritte.\n")
                                    warten2()
                                    print("Dann zeigt er sich: Ein großer schwarzer Ork.\n")
                                    warten2()
                                    print("Er bleckt seine scharfen Zähne und schaut dich wütend an.\n")
                                    warten2()
                                    print("Dolly ist nirgends zu sehen, aber du erkennst eine andere Gestalt neben ihm.\n")
                                    warten2()
                                    print("Wessin. Dein Bauernhof-Nachbar.\n")
                                    warten2()
                                    print("Was um alles in der Welt macht er hier? Was ist hier los?\n")
                                    warten2()
                                    print("Auf Reden scheinen die beiden leider nicht aus zu sein.\n")
                                    warten2()
                                    print("So hast du es dir nicht vorgestellt, aber die Würfel sind gefallen.\n")
                                    warten2()
                                    print("Du machst dich auf einen Kampf gefasst. \n")
                                    warten2()
                                    raum_bosskampf1()
                                else:
                                    print("[MISSERFOLG]\n")
                                    warten2()
                                    print("Du versuchst, dich in Sicherheit zu bringen.\n")
                                    warten2()
                                    print("Erst sieht es danach aus, als würdest du hier doch noch heil rauskommen.\n")
                                    warten2()
                                    print("Dann wirst du aber von einem großen Stein erwischt.\n")
                                    warten2()
                                    print("Du taumelst, verlierst das Tempo.\n")
                                    warten2()
                                    print("Und bevor du weißt, was passiert ist, wirst du im einstürzenden Tunnel begraben.\n")
                                    warten2()
                                    print("Vielleicht werden dir die Götter Gnade walten lassen, die du im Leben nicht kanntest.\n")
                                    warten2()
                                    print("Dein Abenteuer in der Welt der Lebenden ist aber hiermit zu Ende.\n")
                                    warten2()
                                    print("Der Lebensfaden abrupt abgeschnitten. Durch den eigenen Fehler.\n")
                                    warten2()
                                    print("Ende \n")
                                    warten2()
                                    befehl = input("Willst du noch einmal spielen?\n > ").lower()
                                    if befehl == "ja":
                                        warten2()
                                        raum_start4()
                                    elif befehl == "nein":
                                        quit()
                                    else:
                                        print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                        else:
                            print("[MISSERFOLG]\n")
                            warten2()
                            print("Du versuchst, den Flammen zu entkommen, bist aber nicht schnell genug.\n")
                            warten2()
                            print("Die Flammen holen dich ein und verschlingen dich.\n")
                            warten2()
                            print("Als das Feuer verschwindet, liegst du da. Auf dem kalten Boden. \n")
                            warten2()
                            print("Schwer verletzt von der Explosion. Verbrannt von den Flammen.\n")
                            warten2()
                            print("Du kannst dich nicht mehr bewegen. \n")
                            warten2()
                            print ("Selbst wenn jetzt noch jemand zu deiner Rettung kommen würde, könnte man wahrscheinlich nichts mehr tun.\n")
                            warten2()
                            print("Das letzte, was du siehst, sind große Steine, die auf dich fallen. \n")
                            warten2()
                            print("Die Explosion hat den Gang zum Einsturz gebracht.\n")
                            warten2()
                            print("Vielleicht werden dir die Götter Gnade walten lassen, die du im Leben nicht kanntest.\n")
                            warten2()
                            print("Dein Abenteuer in der Welt der Lebenden ist aber hiermit zu Ende.\n")
                            warten2()
                            print("Der Lebensfaden abrupt abgeschnitten. Durch den eigenen Fehler.\n")
                            warten2()
                            print("Ende \n")
                            warten2()
                            befehl = input("Willst du noch einmal spielen?\n > ").lower()
                            if befehl == "ja":
                                warten2()
                                raum_start4()
                            elif befehl == "nein":
                                quit()
                            else:
                                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                elif wurf_reflex == 1:
                    print ("[KRITISCHER MISSERFOLG]\n")
                    warten2()
                    print ("Du versuchst, aus der Nebenhöhle zu entkommen, aber dein Fuß bleibt in der Strickleiter hängen.\n")
                    warten2()
                    print ("Verzweifelt versuchst, dich zu befreien.\n")
                    warten2()
                    print("Aber es ist zu spät.\n")
                    warten2()
                    print("Die Explosion reißt dich in Stücke und bringt den gesamten Gang zum Einstürzen.\n")
                    warten2()
                    print("Vielleicht werden dir die Götter Gnade walten lassen, die du im Leben nicht kanntest.\n")
                    warten2()
                    print("Dein Abenteuer in der Welt der Lebenden ist aber hiermit zu Ende.\n")
                    warten2()
                    print("Der Lebensfaden abrupt abgeschnitten. Durch den eigenen Fehler.\n")
                    warten2()
                    print("Ende\n")
                    warten2()
                    befehl = input("Willst du noch einmal spielen?\n > ").lower()
                    if befehl == "ja":
                        warten2()
                        raum_start4()
                    elif befehl == "nein":
                        quit()
                    else:
                        print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                elif wurf_reflex == 12:
                    print ("[KRITISCHER ERFOLG]\n")
                    warten2()
                    print ("Das Glück ist wahrlich mit den Dummen!\n")
                    warten2()
                    print("Oder zumindest mit den Fahrlässigen.\n")
                    warten2()
                    print ("Durch ein schieres Wunder schaffst du es irgendwie, nicht nur der Explosion zu entkommen, sondern auch stets den Flammenzungen hinter dir einige Schritte voraus zu sein.\n")
                    warten2()
                    print ("Selbst den fallenden Steinen des Gangs, der vor deinen Augen einstürzt, kannst du ausweichen.\n")
                    warten2()
                    print("Unfassbar! Aber auch wahr.\n")
                    warten2()
                    print("Außer Atem, aber heilfroh kommst du zum Stehen.\n")
                    warten2()
                    print("Doch kaum hattest du Luft geholt, hörst du aus den Tiefen der Höhle schwere Schritte.\n")
                    warten2()
                    print("Dann zeigt er sich: Ein großer schwarzer Ork.\n")
                    warten2()
                    print("Er bleckt seine scharfen Zähne und schaut dich wütend an.\n")
                    warten2()
                    print("Dolly ist nirgends zu sehen, aber du erkennst eine andere Gestalt neben ihm.\n")
                    warten2()
                    print("Wessin. Dein Bauernhof-Nachbar.\n")
                    warten2()
                    print("Was um alles in der Welt macht er hier? Was ist hier los?\n")
                    warten2()
                    print("Auf Reden scheinen die beiden leider nicht aus zu sein.\n")
                    warten2()
                    print("So hast du es dir nicht vorgestellt, aber die Würfel sind gefallen.\n")
                    warten2()
                    print("Du machst dich auf einen Kampf gefasst. \n")
                    warten2()
                    raum_bosskampf1()
                else:
                    print ("\n[MISSERFOLG]\n")
                    warten2()
                    print ("Du versuchst, der Explosion zu entkommen, aber du bist nicht schnell genug.\n")
                    warten2()
                    print ("Du hörst einen lauten Knall hinter dir, dann wirst du von einer Druckwelle und den Flammen erwischt.\n")
                    warten2()
                    print("Du liegst da. Auf dem kalten Boden. \n")
                    warten2()
                    print("Schwer verletzt von der Explosion. Verbrannt von den Flammen.\n")
                    warten2()
                    print("Du kannst dich nicht mehr bewegen.\n")
                    warten2()
                    print("Selbst wenn jetzt noch jemand zu deiner Rettung kommen würde, könnte man wahrscheinlich nichts mehr tun.\n")
                    warten2()
                    print("Das letzte, was du siehst, sind große Steine, die auf dich fallen. Die Explosion hat den Gang zum Einstürzen gebracht.\n")
                    warten2()
                    print("Vielleicht werden dir die Götter Gnade walten lassen, die du im Leben nicht kanntest.\n")
                    warten2()
                    print("Dein Abenteuer in der Welt der Lebenden ist aber hiermit zu Ende.\n")
                    warten2()
                    print("Der Lebensfaden abrupt abgeschnitten. Durch den eigenen Fehler.\n")
                    warten2()
                    print("Ende \n")
                    warten2()
                    befehl=input("Willst du noch einmal spielen?\n > ").lower()
                    if befehl=="ja":
                        raum_start4()
                    elif befehl=="nein":
                        quit()
                    else:
                        print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")

            else:
                print(
                    "[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                raum_flucht1()


        def raum_westkorridor1_nord_zurueck():
            print("[Du befindest dich nun im westlichen Gang] \n")
            warten()
            print("Du folgst dem kurvigen Gang und kommst wieder zur Weggabelung.\n")
            warten2()
            print ("Nun geht es zu deiner Linken zurück zur Kreuzung, vor dir führt aber immer noch ein anderer Weg nach Süden.\n")
            warten2()
            print("Natürlich kannst auch wieder dem schlangenartigen Gang hinter dir folgen.\n")
            warten2()
            befehl = input("Wo willst du hin? (Optionen: Norden, Osten, Süden)? \n > ").lower()
            if "nord" in befehl:
                raum_westkorridor1_nord()
            elif "süd" in befehl:
                raum_westkorridor1_sued()
            elif "ost" in befehl:
                raum_kreuzung4()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
            pass


        def szene_bosskampf1():
            warten2()
            print("[Nun befindest du dich im Kampf.]\n")
            warten2()
            befehl=input("Willst du die Regeln dazu erfahren? \n > ").lower()
            if "ja" in befehl:
                warten2()
                print("[Wie in den meisten Rollenspielen auch, ist der Kampf hier in Runden gegliedert.]\n")
                warten3()
                print("[Wer zuerst angreifen darf, wird gleich über die sogenannte 'Initiative' entschieden.]\n")
                warten3()
                print ("[Dazu würfelt jeder einmal W12 und addiert seine Reflexe.]\n")
                warten3()
                print ("[Um den Gegner zu besiegen, musst du seine Lebenskraft auf 0 reduzieren.]\n")
                warten3()
                print ("[Dafür musst du mit deinem Wurf seinen Verteidigungswert überwinden.]\n")
                warten3()
                print ("[Ziemlich viel Zufallsprinzip? Ja, willkommen in der Welt der Rollenspiele!]\n")
                warten3()
                print("[Aber du kannst das Ergebnis mit deinen Entscheidungen beeinflussen.]\n")
                warten2()
                print("[Der Kampf für dieses Abenteuer ist allerdings vereinfacht.]\n")
                warten3()
                print ("[Eigentlich sieht das ZdZ-System fünf verschiedene Kampfstile vor.]\n")
                warten3()
                print("[Nicht zu vergessen: Viele verschiedene Aktionen, die man im Kampf machen kann:\n")
                warten3()
                print("[Kampfbewegung, Boni, Waffenverhalten, Vorteile und Vieles mehr.]\n")
                warten3()
                print("[Vielleicht wird das alles im nächsten Abenteuer eingebaut, aber vorerst bleiben wir bei den Grundlagen.]\n")
                warten3()
                print("[Aber als kleiner Vorgeschmack:\n")
                warten3()
                print("Ruhige Angriffe sind der Standard für jeden Kampfteilnehmer.]\n")
                warten3()
                print("[Gehst du aggressiv vor, achtest du mehr auf deine Treffsicherheit und Schaden als die eigene Verteidigung.]\n")
                warten3()
                print("[Bei vorsichtigen Angriffen ist es umgekehrt.]\n")
                warten3()
                print("[Bei schnellen Angriffen vernachlässigst du Beides, um mehr Schläge in der gleichen Zeitspanne auszuführen.] \n")
                warten3()
                print("[Natürlich kannst du auch versuchen, einfach mal nicht getroffen zu werden.]\n")
                warten3()
                print ("[Hier sind die Regeln: Jeder Kampfteilnehmer hat 2 Aktionen zur Verfügung.]\n")
                warten3()
                print("[Normalerweise kann man sie für alles Mögliche benutzen, aber hier werden sie alle für den Kampf ausgegeben.]\n")
                warten3()
                print("[Außerdem hat jeder Kämpfer eine bestimmte Ausdauer, also eine Kraftreserve, die mit jeder Aktion beim Kämpfen verbraucht wird.]\n")
                warten3()
                print("[Fällt sie auf 0, wirst du erschöpft. Dass das mitten im Kampf passiert, willst du nicht.]\n")
                warten3()
                print("[Wirklich nicht.]\n")
                warten3()
                print ("[Die Ausdauer erholt sich aber, wenn du nicht kämpfst bzw. gar nichts machst.]\n")
                warten3()
                print("[Um den Gegner zu besiegen, muss du ihn gut erwischen. Deine Axt ist für diese Aufgabe gut geeignet.]\n")
                warten3()
                print("[Allerdings verbraucht sie auch mehr Ausdauer als, sagen wir, das Messer, das der Ork in der Hand hält.]\n")
                warten3()
                print ("[Und jedes halbwegs schlaue Lebewesen weiß: Orks haben eine höhere Ausdauer als Menschen.]\n")
                warten3()
                print("[Dabei hast du noch Glück, dass er keine Rüstung trägt - sie würde ihn nämlich einigermaßen schützen.]\n")
                warten3()
                print("[Und damit legen wir dann los.]\n")
                befehl=input("[Gib bitte 'weiter' ein, um fortzufahren.]\n > ").lower()
                if befehl=="weiter":
                    raum_bosskampf1()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
            if "nein" in befehl:
                warten2()
                print("[Gut, dann gehen wir davon aus, dass du diese bereits kennst. Nervige Tutorials können wir also überspringen.]\n")
                warten2()
                befehl = input("[Gib bitte 'weiter' ein, um fortzufahren.]\n > ").lower()
                if befehl == "weiter":
                    warten2()
                    raum_bosskampf1()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")

    # Hier sind die Charakter-Daten.

        class charakter:
            def __init__(self, kraft, geschick, koerperbau, grips, empathie, magie, stufe, klasse, max_ausdauer,
                         ausdauer, zauberkraft,
                         verteidigung, willen, reflexe_bonus, reflexe, widerstand, max_lebenskraft, lebenskraft,
                         initiative_bonus,
                         aktionen_nummer, angriffsbonus, schadensbonus, max_ruestung, ruestung, edelsteine, augen, fertigkeit_sportlichkeit, fertigkeit_ueberreden, fertigkeit_religion):
                self.kraft = kraft
                self.geschick = geschick
                self.koerperbau = koerperbau
                self.grips = grips
                self.empathie = empathie
                self.magie = magie
                self.stufe = 1
                self.klasse = klasse
                self.max_ausdauer = self.kraft + self.koerperbau + self.stufe
                self.ausdauer = max_ausdauer
                self.zauberkraft = self.empathie + self.magie + self.stufe
                self.verteidigung = 10 + stufe + reflexe_bonus
                self.willen = self.empathie + self.stufe
                self.reflexe_bonus = reflexe_bonus
                self.reflexe = self.geschick + self.stufe + self.reflexe_bonus
                self.widerstand = self.willen + self.koerperbau
                self.max_lebenskraft = self.koerperbau + self.stufe
                self.lebenskraft = max_lebenskraft
                self.initiative_bonus = reflexe
                self.aktionen_nummer = 2
       #        self.waffe = waffe
                self.angriffsbonus = 0
                self.wuerfel_w12 = random.randint(1, 12)
                self.max_ruestung = max_ruestung
                self.ruestung=max_ruestung
                self.edelsteine = edelsteine
                self.augen = augen
                self.fertigkeit_sportlichkeit = fertigkeit_sportlichkeit
                self.fertigkeit_ueberreden = fertigkeit_ueberreden
                self.fertigkeit_religion = fertigkeit_religion

            def wurf_w12(self):
                wurf = random.randint(1, 12)
                print ("Würfel: " + str((wurf)) + "\n")
                return wurf

            def wurf_erkennen(self):
                wurf_w12_erkennen = (self.wurf_w12())
                wurf_auf_erkennen = wurf_w12_erkennen + self.augen + int(self.grips/2)
                print("Dein Wurf (Erkennen): " + str(wurf_auf_erkennen) + "\n")
                return wurf_auf_erkennen

            def wurf_koerperbau(self):
                wurf_w12_koerperbau = (self.wurf_w12())
                koerperbauwurf = wurf_w12_koerperbau + self.koerperbau
                if wurf_w12_koerperbau == 1:
                    koerperbauwurf = 1
                print("Dein Wurf (Körperbau): " + str(koerperbauwurf) + "\n")
                return koerperbauwurf

            def kraftwurf(self):
                wurf_w12_kraft = (self.wurf_w12())
                wurf_auf_kraft = wurf_w12_kraft + self.kraft
                print("Dein Wurf (Kraft): " + str(wurf_auf_kraft) + "\n")
                return wurf_auf_kraft

            def reflexwurf(self):
                wurf_w12_reflex = (self.wurf_w12())
                wurf_auf_reflexe = wurf_w12_reflex + self.reflexe
                if wurf_w12_reflex == 1:
                    wurf_auf_reflexe = 1
                elif wurf_w12_reflex == 12:
                    wurf_auf_reflexe =12
                print ("Dein Wurf (Reflexe): " + str(wurf_auf_reflexe) + "\n")
                return wurf_auf_reflexe


            def wurf_sportlichkeit(self):
                wurf_w12_sportlichkeit = (self.wurf_w12())
                sportlichkeitswurf = wurf_w12_sportlichkeit + self.fertigkeit_sportlichkeit + int(self.geschick/2)
                if spieler.fertigkeit_sportlichkeit == 0:
                    sportlichkeitswurf -=3
                print("Dein Wurf (Sportlichkeit): " + str(sportlichkeitswurf) + "\n")
                return sportlichkeitswurf

            def wurf_ueberreden(self):
                wurf_w12_ueberreden = (self.wurf_w12())
                ueberredungswurf = wurf_w12_ueberreden + self.fertigkeit_ueberreden + int(self.empathie/2)
                if wurf_w12_ueberreden == 1:
                    ueberredungswurf = 1
                elif wurf_w12_ueberreden == 12:
                    ueberredungswurf = 12
                print("Dein Wurf (Überreden): " + str(ueberredungswurf) + "\n")
                return ueberredungswurf

            def wurf_religion(self):
                wurf_w12_religion = (self.wurf_w12())
                religionswurf = wurf_w12_religion + self.fertigkeit_religion + int(self.empathie/2)
                if spieler.fertigkeit_religion == 0:
                    religionswurf -= 3
                print("Dein Wurf (Religion): " + str(religionswurf) + "\n")
                return religionswurf

            def wurf_willen(self):
                wurf_w12_willen = (self.wurf_w12())
                willenswurf = self.willen + wurf_w12_willen
                print("Dein Wurf (Willen): " + str(willenswurf) + "\n")
                return willenswurf

            def angriffswurf_nahkampf(self):
                print(self.geschick + self.wurf_w12 + self.angriffsbonus)


        spieler = charakter(5,
                            5,
                            6,
                            5,
                            5,
                            2,
                            1,
                            0,
                            12,
                            12,
                            8,
                            18,
                            6,
                            2,
                            8,
                            18,
                            7,
                            7,
                            8,
                            2,
                            0,
                            0,
                            0,
                            0,
                            False,
                            4,
                            0,
                            0,
                            0)

        ork = charakter(10,
                        3,
                        10,
                        3,
                        2,
                        0,
                        1,
                        0,
                        21,
                        21,
                        0,
                        16,
                        3,
                        2,
                        6,
                        13,
                        11,
                        11,
                        6,
                        2,
                        0,
                        0,
                        0,
                        0,
                        False, 0, 0, 0, 0)

        ork2 = charakter(10,
                        3,
                        10,
                        3,
                        2,
                        0,
                        1,
                        0,
                        21,
                        21,
                        0,
                        16,
                        3,
                        2,
                        6,
                        13,
                        11,
                        11,
                        6,
                        2,
                        0,
                        0,
                        20,
                        0,
                        "False", 0, 0, 0, 0)

        # Hier sind die Waffen. Gattung und Reichweite sind soweit nur Flavour. Sie sollen sich aber unterscheidlich verhalten.
        # Der Spieler hat eine Axt. Die gibt +2 auf Angriff und Schaden, aber -2 auf Verteidigung.

        class waffen:
            def __init__(self, gattung, reichweite, schaden, angriff_bonus, schadensart, verteidigung,
                         ausdauer_verbrauch):
                gattung = None
                reichweite = None
                schaden = None
                angriff_bonus = None
                schadensart = None
                verteidigung = None
                ausdauer_verbrauch = None


        zweihaendige_axt = waffen("Äxte", None, int(random.randint(1, 12) + random.randint(1, 12)), -2, "H", -4, -2, )
        messer = waffen("Leichte und Wurfwaffen", None, random.randint(1, 4), 0, "H/S", None, 0)

        # Das ist der Kampfablauf.
        # Die Idee ist, dass jeder Kämpfer 2 Aktionen hat, wobei die zweite mit einem Malus passiert.
        # Wenn die Aktionen auf 0 fallen, soll das Spiel den Zug an den jeweils anderen Kämpfer übergeben und die Angriff und Verteidigung zurücksetzen.
        # Alle Aktionen verbrauchen Ausdauer. Fällt sie auf 0, ist es schlecht.
        # Außerdem gibt es mehrere Kampfstile, die Auswirkungen auf Aktionen, Angriff und Verteidigung haben.

        def raum_bosskampf1():
            spieler_initiative = spieler.wuerfel_w12 + spieler.initiative_bonus
            ork_initiative = ork.wuerfel_w12 + ork.initiative_bonus
            befehl = input("\n[Und nun: Gib bitte 'würfeln' ein, um die Initiative auszuwürfeln.]\n > ").lower()
            if befehl == "würfeln":
                print("Dein Initiativwurf: " + str(spieler_initiative))
                warten2()
                print("Initiativwurf des Gegners: " + str(ork_initiative)+"\n")
                if spieler_initiative >= ork_initiative:
                    warten3()
                    reset_spieler()
                else:
                    warten3()
                    reset_gegner()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")
            pass

        def aktion_schadenswurf_spieler():
            wuerfel1 = random.randint(1, 12)
            wuerfel2 = random.randint(1, 12)
            schaden = wuerfel1 + wuerfel2 + spieler.schadensbonus
            warten2()
            ork.lebenskraft = ork.lebenskraft - schaden
            print("Würfel: " + str(wuerfel1) + ", " + str(wuerfel2))
            warten2()
            print("Schadensbonus: " + str(spieler.schadensbonus))
            warten2()
            print("Du erwischst das Ungeheuer mit deiner Axt und richtest " + str(schaden) + " Punkte Hiebschaden an.\n")
            warten2()
            print("Lebenskraft des Gegners: " + str(ork.lebenskraft) + "/" + str(ork.max_lebenskraft) + "\n")
            warten2()
            if ork.lebenskraft <= 0:
                warten2()
                szene2_bosskampf()
            else:
                warten2()
                zug_spieler()

        def aktion_schadenswurf_spieler2():
            wuerfel1 = random.randint(1, 12)
            wuerfel2 = random.randint(1, 12)
            schaden = wuerfel1 + wuerfel2 + spieler.schadensbonus
            warten2()
            if ork2.ruestung > 0:
                ork2.ruestung = ork2.ruestung-schaden
                if ork2.ruestung < 0:
                    ork2.lebenskraft=ork2.lebenskraft+ork2.ruestung
            else:
                ork2.lebenskraft = ork2.lebenskraft - schaden
            print("Würfel: " + str(wuerfel1) + ", " + str(wuerfel2))
            warten()
            print("Schadensbonus: " + str(spieler.schadensbonus))
            warten2()
            print("Du erwischst das Ungeheuer mit deiner Axt und richtest " + str(schaden) + " Punkte Hiebschaden an.\n")
            warten2()
            print("Rüstung des Gegners: " + str(ork2.ruestung) + "/" + str(ork2.max_ruestung))
            warten2()
            print("Lebenskraft des Gegners: " + str(ork2.lebenskraft) + "/" + str(ork2.max_lebenskraft) + "\n")
            warten2()
            if ork2.lebenskraft <= 0:
                warten2()
                szene2_bosskampf()
            else:
                warten2()
                zug_spieler2()


        def aktion_schadenswurf_gegner():
            schaden = int(random.randint(1, 4)) + ork.schadensbonus
            spieler.lebenskraft = spieler.lebenskraft - schaden
            warten2()
            print("Der Ork sticht dich mit seinem Messer und verletzt dich um " + str(schaden) + " Punkte Stichschaden.\n")
            warten()
            print("Deine Lebenskraft: " + str(spieler.lebenskraft) + "/" + str(spieler.max_lebenskraft) + "\n")
            warten2()
            if spieler.lebenskraft <= 0:
                warten2()
                szene_niederlage1()
            else:
                warten2()
                zug_gegner()

        def aktion_schadenswurf_gegner2():
            schaden = int(random.randint(1, 8)) + ork2.schadensbonus
            spieler.lebenskraft = spieler.lebenskraft - schaden
            warten2()
            print("Der Ork erwischt dich mit seinem Kurzschwert und verletzt dich um " + str(schaden) + " Punkte Hiebschaden.\n")
            warten()
            print("Deine Lebenskraft: " + str(spieler.lebenskraft) + "/" + str(spieler.max_lebenskraft) + "\n")
            warten3()
            if spieler.lebenskraft <= 0:
                warten2()
                szene_niederlage1()
            else:
                warten3()
                zug_gegner2()


        def szene_niederlage1():
            warten2()
            print("Du spürst die tiefe Wunde, die der letzte Schlag des Orks öffnet.\n")
            warten2()
            print("Dein Blick gleitet ungewollt zur Einstichstelle, und du siehst das daraus sickernde Blut.\n")
            warten2()
            print("Du hebst den Blick und schaust du den Ork an, suchst nach irgendeiner Emotion.\n")
            warten2()
            print("Nichts.\n")
            warten2()
            print("Für ihn ist das nur ein weiterer Arbeitstag.\n")
            warten2()
            print("Er dreht sich um und geht wieder zurück. Zu Dolly.\n")
            warten2()
            print("Du streckst deine Hand aus und versuchst ihn aufzuhalten.\n")
            warten2()
            print("Doch deine Kräfte verlassen dich.\n")
            warten2()
            print("Du sackst auf die Knie, dann fällst du zu Boden.\n")
            warten2()
            print("Das letzte, was du siehst, ist der weggehende Ork. Daneben der erfreute Wessin.\n")
            warten2()
            print("Und eine Lache aus deinem eigenen Blut.\n")
            warten2()
            print("Vielleicht werden dir die Götter Gnade walten lassen, die du im Leben nicht kanntest.\n")
            warten2()
            print("Dein Abenteuer in der Welt der Lebenden ist aber hiermit zu Ende.\n")
            warten2()
            print("Der Lebensfaden abrupt abgeschnitten.\n")
            warten2()
            print("Arme Dolly!\n")
            warten2()
            print("Möge der Zorn der Götter die Beiden niederstrecken!\n")
            warten2()
            print("Für einen letzten Fluch hast du gerade noch Kraft.\n")
            warten2()
            print("Angeblich haben solche Flüche eine gewisse Macht.\n")
            warten2()
            print("Hoffnung ist ein Luxus, den sich nur Wenige leisten können.\n")
            warten2()
            print("Vergeltung ist zumindest leichter zu erfahren...\n")
            warten3()
            print("Ende \n")
            warten2()
            befehl = input("Willst du noch einmal spielen?\n > ").lower()
            if befehl == "ja":
                raum_start4()
            elif befehl == "nein":
                quit()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")

            pass


        def szene2_bosskampf():
            warten2()
            befehl=input("Wie willst du dem Ork den Garaus geben?\n("
                         "Optionen: Kopfschlag, Enthauptung, Seitenhieb, Bauchhieb, Verstümmelung mit Überlebensschance, bewusstlos schlagen)\n > ").lower()
            if "kopf" in befehl:
                warten2()
                print("Du holst aus und rammst deine mächtige Axt in den Orkschädel, begleitet von einem lauten Knacken und einem ekeligen nassen Geräusch.\n")
                warten3()
                print("Der Ork sackt zappelnd zusammen, fällt auf den Boden und erstarrt in einer Lache aus seinem eigenen Blut.\n")
                warten3()
                print("Genauer musst du nicht hinsehen. \n")
                warten3()
                print("Als Bauer hast du genug Tiere geschlachtet, um zu wissen, wie sein Kopf jetzt aussieht.\n")
                warten3()
                szene_sieg()
            elif "haupt" in befehl:
                warten2()
                print("Du erkennst eine Öffnung in seiner Verteidigung.\n")
                warten3()
                print("Du holst aus und schwingst dort, wo du seinen Hals treffen willst.\n")
                warten3()
                print("Zu deiner eigenen Überraschung schlägt ihm der Angriff direkt den Kopf ab...\n")
                warten3()
                print("begleitet von einem ekeligen nassen Geräusch und schwachen Blutspritzern, sie aus seinem Hals schnellen.\n")
                warten3()
                print("Der Kopf des Orks fliegt irgendwohin, du kannst diese Stelle nicht ausmachen.\n")
                warten3()
                print("Nicht, dass du wirklich danach suchen würdest.\n")
                warten3()
                print("Der Körper steht noch ein paar Sekunden da, dann fällt er blutend zu Boden.\n")
                warten3()
                szene_sieg()
            elif "seite" in befehl:
                warten2()
                print("Du erkennst eine günstige Gelegenheit und rammst deine mächtige Axt in die Seite des Orks.\n")
                warten3()
                print("Der Ork stößt Luft aus, als wäre sie ihm einfach so aus den Lungen gewichen.\n")
                warten3()
                print("Er schaut dich an, verwundert.\n")
                warten3()
                print("Er hat ganz offensichtlich nicht damit gerechnet, sein Ende auf diese Weise zu finden.\n")
                warten3()
                print("Der Ork steht kurz da und hält sich an der Seite, dann fällt er zu Boden, während sich unter ihm eine Blutlache ausbreitet.\n")
                warten3()
                print("Er streckt seine Hand nach dir aus, als würde er zurückschlagen wollen.\n")
                warten3()
                print("Aber du hast als Bauer genug Tiere geschlachtet und versorgt, um zu wissen, dass er nichts mehr macht.\n")
                warten3()
                print("Was immer seine letzten Anstrengungen sind: Sie sind vergeblich.\n")
                warten3()
                print("Die einzige Frage, die sich stellt, ist nur, ob du ihm Gnade walten und ihn von seinen Schmerzen erlösen willst.\n")
                warten3()
                befehl=input("Willst du dem Ork Gnade walten lasen? (Optionen: Ja, Nein) \n > ").lower()
                if befehl=="ja":
                    warten3()
                    print("Ja. Du bist Vieles, aber nicht grausam.\n")
                    warten3()
                    print("So viel kannst du für den besiegten Feind noch tun.\n")
                    warten3()
                    print("Ein Schlag. Schnell. Sauber. Schmerzlos.\n")
                    warten3()
                    print("Ein Schlag, und der Ork erstarrt.\n")
                    warten3()
                    szene_sieg()
                if befehl=="nein":
                    warten3()
                    print("Nein. Nicht nach allem, was hier passiert ist.\n")
                    warten3()
                    print("Wie so Vieles auf dieser Welt, ist Gnade ein Luxus.\n")
                    warten3()
                    print("Für dieses Ungeheuer kannst du keine erübrigen.\n")
                    warten3()
                    print("Du wendest dich ab von dem krächszenden Ork und überlässt ihn seinem Schicksal.\n")
                    warten3()
                    szene_sieg()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
            elif "bauch" in befehl:
                warten2()
                print("Du erkennst eine günstige Gelegenheit und rammst deine mächtige Axt in den Bauch des Orks.\n")
                warten3()
                print("Der Ork stößt Luft aus, als wäre sie ihm einfach so aus den Lungen gewichen.\n")
                warten3()
                print("Er schaut dich an, verwundert.\n")
                warten3()
                print("Er hat ganz offensichtlich nicht damit gerechnet, sein Ende auf diese Weise zu finden.\n")
                warten3()
                print("Der Ork steht kurz da und hält sich am Bauch, dann fällt er zu Boden, während sich unter ihm eine Blutlache ausbreitet.\n")
                warten3()
                print("Er streckt seine Hand nach dir aus, als würde er zurückschlagen wollen.\n")
                warten3()
                print("Aber du hast als Bauer genug Tiere geschlachtet und versorgt, um zu wissen, dass er nichts mehr macht.\n")
                warten3()
                print("Was immer seine letzten Anstrengungen sind: Sie sind vergeblich.\n")
                warten3()
                print("Die einzige Frage, die sich stellt, ist nur, ob du ihm Gnade walten und ihn von seinen Schmerzen erlösen willst.\n")
                warten3()
                befehl = input("Willst du dem Ork Gnade walten lassen?\n > ").lower()
                if befehl == "ja":
                    warten3()
                    print("Ja. Du bist Vieles, aber nicht grausam.\n")
                    warten3()
                    print("So viel kannst du für den besiegten Feind noch tun.\n")
                    warten3()
                    print("Ein Schlag. Schnell. Sauber. Schmerzlos.\n")
                    warten3()
                    print("Ein Schlag, und der Ork erstarrt.\n")
                    warten3()
                    szene_sieg()
                if befehl == "nein":
                    warten3()
                    print("Nein. Nicht nach allem, was hier passiert ist.\n")
                    warten3()
                    print("Wie so Vieles auf dieser Welt, ist Gnade ein Luxus.\n")
                    warten3()
                    print("Für dieses Ungeheuer kannst du keine erübrigen.\n")
                    warten3()
                    print("Du wendest dich ab von dem krächszenden Ork und überlässt ihn seinem Schicksal.\n")
                    warten3()
                    szene_sieg()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
            elif "stümmel" in befehl:
                warten2()
                print("Du erkennst eine Schwäche in der Verteidigung des Orks.\n")
                warten3()
                print("Du könntest ihn jetzt mit einem gut platzierten Schlag töten.\n")
                warten3()
                print("Aber es ist nicht sein Leben, das du willst.\n")
                warten3()
                print("Allerdings kannst du es auch nicht zulassen, dass er dir in den Rücken fällt.\n")
                warten3()
                print("Also schlägst du ihm stattdessen ein Bein ab.\n")
                warten3()
                print("Der Schmerz ist zu viel für den stark verletzten Feind.\n")
                warten3()
                print("Er wird bewusstlos und fällt zu Boden, während sich unter ihm eine Blutlache ausbreitet.\n")
                warten3()
                print("Wenn du nichts tust, wird er verbluten.\n")
                warten3()
                print("Sein Tod würde aber nichts bringen.\n")
                warten3()
                print("Du nimmst dein Fackel und brennst seine Wunde schnell aus.\n")
                warten3()
                print("Vielleicht wird er trotzdem hier sterben, vielleicht auch nicht.\n")
                warten3()
                print("Verbluten wird er hier aber schon mal nicht.\n")
                warten3()
                print("Sein Schicksal ist jetzt in den Händen der Götter.\n")
                warten3()
                print("Und zum Teil auch in seinen eigenen.\n")
                warten3()
                szene_sieg()
            elif "bewusst" or "schlage" in befehl:
                warten2()
                print("Du erkennst eine Schwäche in der Verteidigung des Orks.\n")
                warten3()
                print("Du könntest ihn jetzt mit einem gut platzierten Schlag töten.\n")
                warten3()
                print("Aber es ist nicht sein Leben, das du willst.\n")
                warten3()
                print("Du schickst dich an, und verpasst ihm einen Schlag auf den Hinterkopf, mit der stumpfen Seite deiner Axt.\n")
                warten3()
                print("Der Ork grunzt einmal, dann wird bewusstlos und fällt zu Boden.\n")
                warten3()
                print("Vermutlich wird bald wieder aufwachen.\n")
                warten3()
                print("Vorerst ist er aber außer Gefecht.\n")
                warten3()
                print("Du hoffst, dass er es spätestens jetzt besser weiß, als sich noch einmal in diese Gegend zu trauen.\n")
                warten3()
                szene_sieg()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")

        def reset_spieler():
            spieler.aktionen_nummer = 2
            warten()
            zug_spieler()

        def reset_spieler2():
            spieler.aktionen_nummer = 2
            warten()
            zug_spieler2()

        def reset_gegner():
            ork.aktionen_nummer = 2
            warten()
            zug_gegner()

        def reset_gegner2():
            ork2.aktionen_nummer = 2
            warten()
            zug_gegner2()


        def zug_spieler():
            spieler.wuerfel_w12 = random.randint(1, 12)
            schneller_angriff = 0
            spieler.schadensbonus = 0
            if spieler.ausdauer <= 0:
                print("Du bist erschöpft, kannst aber aus letzter Kraft noch weiterkämpfen.\n")
                spieler.angriffsbonus = -5
                spieler.verteidigung = 13
                spieler.aktionen_nummer = spieler.aktionen_nummer - 1
                if spieler.aktionen_nummer == 0:
                    warten2()
                    reset_gegner()
            else:
                spieler.angriffsbonus = 0
                spieler.verteidigung = 18  # Das soll die Effekte aus der letzten Runde zurücksetzen.
            warten2()
            befehl = input("Was willst du tun? (Optionen: ausweichen, angreifen, Zug beenden) \n > ").lower()
            if spieler.aktionen_nummer <= 0:
                warten2()
                print("Du hast in diesem Zug keine Aktionen mehr zur Verfügung. Dein Gegner ist dran.\n")
                reset_gegner2()
            elif "weiche" in befehl:
                spieler.aktionen_nummer = spieler.aktionen_nummer - 2
                spieler.ausdauer = spieler.ausdauer - 1
                spieler.verteidigung = spieler.verteidigung + 2
                print("Du konzentrierst dich darauf, nicht getroffen zu werden.\n")
                warten()
                print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                reset_gegner()
                # Ausweichen beendet den Zug mit einem Bonus auf Verteidigung.
            elif "zug" in befehl:
                warten2()
                print("Du setzt deinen Zug aus.\n")
                if spieler.ausdauer < 12 and spieler.aktionen_nummer == 2:
                    spieler.ausdauer = spieler.ausdauer + 1
                    print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                    reset_gegner()
                elif spieler.ausdauer < 12 and spieler.aktionen_nummer < 2 and spieler.aktionen_nummer > 0:
                    print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                    reset_gegner()
                elif spieler.ausdauer < 0 and spieler.aktionen_nummer == 1:
                    spieler.ausdauer = spieler.ausdauer + 1
                    print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                    reset_gegner2()
                else:
                    spieler.ausdauer = 12
                print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                reset_gegner()
            elif "greife" in befehl:
                befehl = input("Wie willst du angreifen? (Optionen: ruhig, aggressiv, vorsichtig, schnell)\n > ").lower()
                if "ruhig" in befehl:
                    spieler.aktionen_nummer = spieler.aktionen_nummer - 1
                    spieler.ausdauer = spieler.ausdauer - 3
                    angriffswurf = spieler.geschick + spieler.wuerfel_w12 + spieler.angriffsbonus
                    print("Würfel: " + str(spieler.wuerfel_w12) + "\n")
                    warten()
                    print("Dein Angriffswurf: " + str(angriffswurf) + "\n")
                    warten2()
                    print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                    if spieler.wuerfel_w12 == 1:
                        print("Du schwingst kolossal daneben. \nDeine Axt gleitet dir fast aus der Hand, du kannst sie gerade noch so festhalten.\n")
                        if spieler.aktionen_nummer <= 0:
                            warten()
                            reset_gegner()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            warten()
                            zug_spieler()
                            pass
                    elif angriffswurf > ork.verteidigung or spieler.wuerfel_w12 == 12:
                        aktion_schadenswurf_spieler()
                    else:
                        warten2()
                        print("Du schwingst deine Axt, doch der Gegner weicht aus.\n")
                        if spieler.aktionen_nummer <= 0:
                            warten()
                            reset_gegner()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            warten()
                            zug_spieler()
                            pass
                elif befehl == "aggressiv":
                    warten2()
                    spieler.verteidigung = spieler.verteidigung - 4
                    spieler.schadensbonus = 2
                    spieler.angriffsbonus = 2
                    spieler.ausdauer = spieler.ausdauer - 3
                    spieler.aktionen_nummer = spieler.aktionen_nummer - 1
                    angriffswurf = spieler.geschick + spieler.wuerfel_w12 + spieler.angriffsbonus
                    print("Würfel: " + str(spieler.wuerfel_w12) + "\n")
                    warten2()
                    print("Dein Angriffswurf: " + str(angriffswurf) + "\n")
                    warten2()
                    print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                    if angriffswurf == 1:
                        print(
                            "Du schwingst kolossal daneben. \nDeine Axt gleitet dir fast aus der Hand, du kannst sie gerade noch so festhalten.\n")
                        if spieler.aktionen_nummer <= 0:
                            warten()
                            reset_gegner()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            warten()
                            zug_spieler()
                            pass
                    elif angriffswurf > ork.verteidigung or spieler.wuerfel_w12 == 12:
                        warten()
                        aktion_schadenswurf_spieler()
                    else:
                        print("Du schwingst deine Axt, doch der Gegner weicht aus.\n")
                        if spieler.aktionen_nummer <= 0:
                            warten()
                            reset_gegner()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            warten()
                            zug_spieler()
                            pass
                elif "vorsichtig" in befehl:
                    spieler.ausdauer = spieler.ausdauer - 3
                    spieler.aktionen_nummer = spieler.aktionen_nummer - 1
                    spieler.verteidigung = spieler.verteidigung + 2
                    spieler.angriffsbonus = -2
                    angriffswurf = spieler.geschick + spieler.wuerfel_w12 + spieler.angriffsbonus
                    print("Würfel: " + str(spieler.wuerfel_w12) + "\n")
                    warten()
                    print("Dein Angriffswurf: " + str(angriffswurf) + "\n")
                    warten()
                    print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                    warten()
                    if angriffswurf == 1:
                        print(
                            "Du schwingst kolossal daneben. \nDeine Axt gleitet dir fast aus der Hand, du kannst sie gerade noch so festhalten.\n")
                        if spieler.aktionen_nummer <= 0:
                            warten()
                            reset_gegner()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            warten()
                            zug_spieler()
                            pass
                    elif angriffswurf > ork.verteidigung or spieler.wuerfel_w12 == 12:
                        warten()
                        aktion_schadenswurf_spieler()
                    else:
                        warten2()
                        print("Du schwingst deine Axt, doch der Gegner weicht aus.\n")
                        if spieler.aktionen_nummer <= 0:
                            warten()
                            reset_gegner()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            warten()
                            zug_spieler()
                            pass
                elif "schnell" in befehl:
                    spieler.ausdauer = spieler.ausdauer - 3
                    spieler.aktionen_nummer = spieler.aktionen_nummer - 0.5
                    spieler.verteidigung = spieler.verteidigung - 4
                    spieler.angriffsbonus = -4
                    angriffswurf = spieler.geschick + spieler.wuerfel_w12 + spieler.angriffsbonus
                    print("Würfel: " + str(spieler.wuerfel_w12) + "\n")
                    warten()
                    print("Dein Angriffswurf: " + str(angriffswurf) + "\n")
                    warten()
                    print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                    warten()
                    if angriffswurf == 1:
                        print(
                            "Du schwingst kolossal daneben. \nDeine Axt gleitet dir fast aus der Hand, du kannst sie gerade noch so festhalten.\n")
                        if spieler.aktionen_nummer <= 0:
                            warten()
                            reset_gegner()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            warten()
                            zug_spieler()
                            pass
                    elif angriffswurf > ork.verteidigung or spieler.wuerfel_w12 == 12:
                        warten()
                        aktion_schadenswurf_spieler()
                    else:
                        warten2()
                        print("Du schwingst deine Axt, doch der Gegner weicht aus.\n")
                        warten()
                        if spieler.aktionen_nummer == 0:
                            reset_gegner()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            zug_spieler()
                            pass
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                    warten()
                    if spieler.aktionen_nummer <= 0:
                        reset_gegner()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                    else:
                        zug_spieler()
                        pass
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                warten()
                if spieler.aktionen_nummer <= 0:
                    reset_gegner()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                else:
                    zug_spieler()
                    pass

        def zug_spieler2():
            spieler.wuerfel_w12 = random.randint(1, 12)
            schneller_angriff = 0
            spieler.schadensbonus = 0
            if spieler.ausdauer <= 0:
                print("Du bist erschöpft, kannst aber aus letzter Kraft noch weiterkämpfen.\n")
                spieler.angriffsbonus = -5
                spieler.verteidigung = 13
                spieler.aktionen_nummer = spieler.aktionen_nummer - 1
                if spieler.aktionen_nummer == 0:
                    reset_gegner2()
            else:
                spieler.angriffsbonus = 0
                spieler.verteidigung = 18  # Das soll die Effekte aus der letzten Runde zurücksetzen.
            warten2()
            befehl = input("Was willst du tun? (Optionen: ausweichen, angreifen, zug beenden) \n > ").lower()
            if spieler.aktionen_nummer <= 0:
                warten2()
                print("Du hast in diesem Zug keine Aktionen mehr zur Verfügung. Dein Gegner ist dran.\n")
                reset_gegner2()
            elif "weiche" in befehl:
                spieler.aktionen_nummer = spieler.aktionen_nummer - 2
                spieler.ausdauer = spieler.ausdauer - 1
                spieler.verteidigung = spieler.verteidigung + 2
                print("Du konzentrierst dich darauf, nicht getroffen zu werden.\n")
                warten()
                print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                warten()
                reset_gegner2()
                # Ausweichen beendet den Zug mit einem Bonus auf Verteidigung.
            elif "zug" in befehl:
                warten2()
                print("Du setzt deinen Zug aus.\n")
                if spieler.ausdauer < 12 and spieler.aktionen_nummer==2:
                    spieler.ausdauer = spieler.ausdauer + 1
                    print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                    warten()
                    reset_gegner2()
                elif spieler.ausdauer < 12 and spieler.aktionen_nummer < 2:
                    print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                    warten()
                    reset_gegner2()
                elif spieler.ausdauer < 0 and spieler.aktionen_nummer == 1:
                    spieler.ausdauer = spieler.ausdauer + 1
                    print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                    warten()
                    reset_gegner2()
                else:
                    spieler.ausdauer = 12
                print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                warten()
                reset_gegner2()
            elif "greife" in befehl:
                befehl = input("Wie willst du angreifen? (Optionen: ruhig, aggressiv, vorsichtig, schnell)\n > ").lower()
                if "ruhig" in befehl:
                    spieler.aktionen_nummer = spieler.aktionen_nummer - 1
                    spieler.ausdauer = spieler.ausdauer - 3
                    angriffswurf = spieler.geschick + spieler.wuerfel_w12 + spieler.angriffsbonus
                    print("Würfel: " + str(spieler.wuerfel_w12))
                    warten()
                    print("Dein Angriffswurf: " + str(angriffswurf))
                    warten2()
                    print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                    if spieler.wuerfel_w12 == 1:
                        print("Du schwingst kolossal daneben. \nDeine Axt gleitet dir fast aus der Hand, du kannst sie gerade noch so festhalten.\n")
                        warten()
                        if spieler.aktionen_nummer <= 0:
                            reset_gegner2()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            zug_spieler2()
                            pass
                    elif angriffswurf > ork2.verteidigung or spieler.wuerfel_w12 == 12:
                        warten()
                        aktion_schadenswurf_spieler2()
                    else:
                        warten2()
                        print("Du schwingst deine Axt, doch der Gegner weicht aus.\n")
                        warten()
                        if spieler.aktionen_nummer <= 0:
                            reset_gegner2()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            zug_spieler2()
                            pass
                elif befehl == "aggressiv":
                    warten2()
                    spieler.verteidigung = spieler.verteidigung - 4
                    spieler.schadensbonus = 2
                    spieler.angriffsbonus = 2
                    spieler.ausdauer = spieler.ausdauer - 3
                    spieler.aktionen_nummer = spieler.aktionen_nummer - 1
                    angriffswurf = spieler.geschick + spieler.wuerfel_w12 + spieler.angriffsbonus
                    print("Würfel: " + str(spieler.wuerfel_w12))
                    warten()
                    print("Dein Angriffswurf: " + str(angriffswurf) + "\n")
                    warten2()
                    print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                    warten()
                    if spieler.wuerfel_w12 == 1:
                        print("Du schwingst kolossal daneben. \nDeine Axt gleitet dir fast aus der Hand, du kannst sie gerade noch so festhalten.\n")
                        warten()
                        if spieler.aktionen_nummer <= 0:
                            reset_gegner2()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            zug_spieler2()
                            pass
                    elif angriffswurf > ork2.verteidigung or spieler.wuerfel_w12 == 12:
                        warten()
                        aktion_schadenswurf_spieler2()
                    else:
                        print("Du schwingst deine Axt, doch der Gegner weicht aus.\n")
                        warten()
                        if spieler.aktionen_nummer <= 0:
                            reset_gegner2()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            zug_spieler2()
                            pass
                elif "vorsichtig" in befehl:
                    spieler.ausdauer = spieler.ausdauer - 3
                    spieler.aktionen_nummer = spieler.aktionen_nummer - 1
                    spieler.verteidigung = spieler.verteidigung + 2
                    spieler.angriffsbonus = -2
                    angriffswurf = spieler.geschick + spieler.wuerfel_w12 + spieler.angriffsbonus
                    print("Würfel: " + str(spieler.wuerfel_w12))
                    warten()
                    print("Dein Angriffswurf: " + str(angriffswurf))
                    warten()
                    print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                    if spieler.wuerfel_w12 == 1:
                        print("Du schwingst kolossal daneben. \nDeine Axt gleitet dir fast aus der Hand, du kannst sie gerade noch so festhalten.\n")
                        warten()
                        if spieler.aktionen_nummer <= 0:
                            reset_gegner2()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            zug_spieler2()
                            pass
                    elif angriffswurf > ork2.verteidigung or spieler.wuerfel_w12 == 12:
                        warten()
                        aktion_schadenswurf_spieler2()
                    else:
                        warten2()
                        print("Du schwingst deine Axt, doch der Gegner weicht aus.\n")
                        warten()
                        if spieler.aktionen_nummer <= 0:
                            reset_gegner2()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            zug_spieler2()
                            pass
                elif "schnell" in befehl:
                    spieler.ausdauer = spieler.ausdauer - 3
                    spieler.aktionen_nummer = spieler.aktionen_nummer - 0.5
                    spieler.verteidigung = spieler.verteidigung - 4
                    spieler.angriffsbonus = -4
                    angriffswurf = spieler.geschick + spieler.wuerfel_w12 + spieler.angriffsbonus
                    print("Würfel: " + str(spieler.wuerfel_w12))
                    warten()
                    print("Dein Angriffswurf: " + str(angriffswurf))
                    warten()
                    print("Deine Ausdauer: " + str(spieler.ausdauer) + "/" + str(spieler.max_ausdauer) + "\n")
                    if spieler.wuerfel_w12 == 1:
                        print("Du schwingst kolossal daneben. \nDeine Axt gleitet dir fast aus der Hand, du kannst sie gerade noch so festhalten.\n")
                        warten()
                        if spieler.aktionen_nummer <= 0:
                            reset_gegner2()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            zug_spieler2()
                            pass
                    elif angriffswurf > ork2.verteidigung or spieler.wuerfel_w12 == 12:
                        warten()
                        aktion_schadenswurf_spieler2()
                    else:
                        warten2()
                        print("Du schwingst deine Axt, doch der Gegner weicht aus.\n")
                        warten()
                        if spieler.aktionen_nummer == 0:
                            reset_gegner2()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                        else:
                            zug_spieler2()
                            pass
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                    warten()
                    if spieler.aktionen_nummer <= 0:
                        reset_gegner2()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                    else:
                        zug_spieler2()
                        pass
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                warten()
                if spieler.aktionen_nummer <= 0:
                    reset_gegner2()  # Wenn die Aktionen verbraucht sind, ist der Gegner dran.
                else:
                    zug_spieler2()
                    pass

        def zug_gegner():
            warten2()
            print("Der Ork ist am Zug.\n")
            schneller_angriff = 0
            ork.verteidigung = 16  # Das soll die Effekte aus der letzten Runde zurücksetzen.
            ork.angriffsbonus = 5
            ork.schadensbonus = 0
            ork.wuerfel_w12 = random.randint(1, 12)
            angriffswurf = ork.geschick + ork.wuerfel_w12 + ork.angriffsbonus
            if ork.ausdauer <= 0:
                print("Der Ork ist sichtlich erschöpft, versucht aber dennoch, weiterzukämpfen.\n")
                ork.angriffsbonus = 0
                ork.verteidigung = 9
                ork.aktionen_nummer = ork.aktionen_nummer - 1
                if ork.aktionen_nummer <= 0:
                    reset_spieler()
            befehl = random.randint(1, 4)
            warten2()
            if befehl == 1:
                print("Er versucht, deinen Schlägen auszuweichen.\n")
                ork.aktionen_nummer = ork.aktionen_nummer - 2
                ork.ausdauer = ork.ausdauer - 1
                ork.verteidigung = ork.verteidigung + 2
                reset_spieler()
            else:
                befehl = random.randint(1, 4)
                if befehl == 1:  # Ein Versuch an der Ork-"KI".
                    print("Er greift dich an.\n")
                    ork.aktionen_nummer = ork.aktionen_nummer - 1
                    ork.ausdauer = ork.ausdauer - 1
                    angriffswurf = ork.geschick + ork.wuerfel_w12 + ork.angriffsbonus
                    warten2()
                    print("Würfel: " + str(ork.wuerfel_w12))
                    warten()
                    print("Angriffswurf: " + str(angriffswurf))
                    warten2()
                    if ork.wuerfel_w12==1:
                        print ("Der Ork greift dich mit seinem Messer an, schwingt aber kolossal daneben.\n")
                        warten()
                        if ork.aktionen_nummer <= 0:
                            reset_spieler()
                        else:
                            zug_gegner()
                            pass
                    elif angriffswurf >= spieler.verteidigung or ork.wuerfel_w12 == 12:
                        warten()
                        aktion_schadenswurf_gegner()
                    else:
                        print("Das Ork-Messer schwingt an dir vorbei.\n")
                        warten()
                        if ork.aktionen_nummer <= 0:
                            reset_spieler()
                        else:
                            zug_gegner()
                            pass
                elif befehl == 2:
                    warten2()
                    print("Er greift dich aggressiv an.\n")
                    ork.verteidigung = spieler.verteidigung - 4
                    ork.angriffsbonus = 7
                    angriffswurf = ork.geschick + ork.wuerfel_w12 + ork.angriffsbonus
                    ork.aktionen_nummer = ork.aktionen_nummer - 1
                    ork.verteidigung = ork.verteidigung - 4
                    ork.schadensbonus = 2
                    warten2()
                    print("Würfel: " + str(ork.wuerfel_w12))
                    warten()
                    print("Angriffswurf: " + str(angriffswurf))
                    warten2()
                    if ork.wuerfel_w12 == 1:
                        print("Der Ork greift dich mit seinem Messer an, schwingt aber kolossal daneben.\n")
                        if ork.aktionen_nummer <= 0:
                            reset_spieler()
                        else:
                            zug_gegner()
                            pass
                    elif angriffswurf >= spieler.verteidigung or ork.wuerfel_w12 == 12:
                        warten()
                        aktion_schadenswurf_gegner()
                    else:
                        print("Das Ork-Messer schwingt an dir vorbei.\n")
                        warten2()
                        if ork.aktionen_nummer <= 0:
                            reset_spieler()
                        else:
                            zug_gegner()
                            pass
                elif befehl == 3:
                    print("Er greift vorsichtig an.\n")
                    warten2()
                    ork.aktionen_nummer = ork.aktionen_nummer - 1
                    ork.ausdauer = ork.ausdauer - 1
                    angriffswurf = ork.geschick + ork.wuerfel_w12 + ork.angriffsbonus
                    ork.angriffsbonus = - 2
                    ork.verteidigung = ork.verteidigung + 2
                    warten2()
                    print("Würfel: " + str(ork.wuerfel_w12))
                    warten()
                    print("Angriffswurf: " + str(angriffswurf))
                    warten2()
                    if ork.wuerfel_w12 == 1:
                        print("Der Ork greift dich mit seinem Messer an, schwingt aber kolossal daneben.\n")
                        warten()
                        if ork.aktionen_nummer <= 0:
                            reset_spieler()
                        else:
                            zug_gegner()
                            pass
                    elif angriffswurf >= spieler.verteidigung or ork.wuerfel_w12 == 12:
                        aktion_schadenswurf_gegner()
                    else:
                        print("Das Ork-Messer schwingt an dir vorbei.\n")
                        warten()
                        if ork.aktionen_nummer <= 0:
                            reset_spieler()
                        else:
                            zug_gegner()
                            pass
                else:
                    print("Der Ork setzt bei seinem Angriff auf Geschwindigkeit.\n")
                    ork.ausdauer = ork.ausdauer - 1
                    ork.verteidigung = ork.verteidigung - 4
                    ork.aktionen_nummer = ork.aktionen_nummer - 0.5
                    ork.angriffsbonus = -4
                    angriffswurf = ork.geschick + ork.wuerfel_w12 + ork.angriffsbonus
                    warten2()
                    print("Würfel: " + str(ork.wuerfel_w12))
                    warten()
                    print("Angriffswurf: " + str(angriffswurf))
                    warten2()
                    if ork.wuerfel_w12 == 1:
                        print("Der Ork greift dich mit seinem Messer an, schwingt aber kolossal daneben.\n")
                        warten()
                        if ork.aktionen_nummer <= 0:
                            reset_spieler()
                        else:
                            zug_gegner()
                            pass
                    elif angriffswurf >= spieler.verteidigung or ork.wuerfel_w12 == 12:
                        warten()
                        aktion_schadenswurf_gegner()
                    else:
                        print("Das Ork-Messer schwingt an dir vorbei.\n")
                        if ork.aktionen_nummer <= 0:
                            reset_spieler()
                        else:
                            zug_gegner()
                            pass

        def zug_gegner2():
            warten2()
            print("Der Ork ist am Zug.\n")
            schneller_angriff = 0
            ork2.verteidigung = 16  # Das soll die Effekte aus der letzten Runde zurücksetzen.
            ork2.angriffsbonus = 5
            ork2.schadensbonus = 0
            if ork2.aktionen_nummer<=0:
                reset_spieler2()
           # ork2.max_ruestung=20
            ork2.wuerfel_w12 = random.randint(1, 12)
            angriffswurf = ork2.geschick + ork2.wuerfel_w12 + ork2.angriffsbonus
            if ork2.ausdauer <= 0:
                print("Der Ork ist sichtlich erschöpft, versucht aber dennoch, weiterzukämpfen.\n")
                ork2.angriffsbonus = 0
                ork2.verteidigung = 9
                ork2.aktionen_nummer = ork2.aktionen_nummer - 1
                if ork2.aktionen_nummer <= 0:
                    reset_spieler()
            befehl = random.randint(1, 4)
            warten2()
            if befehl == 1:
                print("Er versucht, deinen Schlägen auszuweichen.\n")
                ork2.aktionen_nummer = ork2.aktionen_nummer - 2
                ork2.ausdauer = ork2.ausdauer - 1
                ork2.verteidigung = ork2.verteidigung + 2
                reset_spieler2()
            else:
                befehl = random.randint(1, 4)
                if befehl == 1:  # Ein Versuch an der Ork-"KI".
                    print("Er greift dich an.\n")
                    ork2.aktionen_nummer = ork2.aktionen_nummer - 1
                    ork2.ausdauer = ork2.ausdauer - 1
                    angriffswurf = ork2.geschick + ork2.wuerfel_w12 + ork2.angriffsbonus
                    warten2()
                    print("Würfel: " + str(ork2.wuerfel_w12))
                    print("Angriffswurf: " + str(angriffswurf))
                    warten2()
                    if ork2.wuerfel_w12 == 1:
                        print("Der Ork greift dich mit seinem Schwert an, schwingt aber kolossal daneben.\n")
                        if ork2.aktionen_nummer <= 0:
                            reset_spieler2()
                        else:
                            zug_gegner2()
                            pass
                    elif angriffswurf >= spieler.verteidigung or ork2.wuerfel_w12 == 12:
                        aktion_schadenswurf_gegner2()
                    else:
                        print("Das Ork-Schwert verfehlt dich nur knapp.\n")
                        if ork2.aktionen_nummer <= 0:
                            reset_spieler2()
                        else:
                            zug_gegner2()
                            pass
                elif befehl == 2:
                    warten2()
                    print("Er greift dich aggressiv an.\n")
                    ork2.verteidigung = spieler.verteidigung - 4
                    ork2.angriffsbonus = 7
                    angriffswurf = ork2.geschick + ork2.wuerfel_w12 + ork2.angriffsbonus
                    ork2.aktionen_nummer = ork2.aktionen_nummer - 1
                    ork2.verteidigung = ork2.verteidigung - 4
                    ork2.schadensbonus = 2
                    warten2()
                    print("Würfel: " + str(ork2.wuerfel_w12))
                    warten()
                    print("Angriffswurf: " + str(angriffswurf))
                    warten2()
                    if ork2.wuerfel_w12 == 1:
                        print("Der Ork greift dich mit seinem Schwert an, schwingt aber kolossal daneben.\n")
                        if ork2.aktionen_nummer <= 0:
                            reset_spieler2()
                        else:
                            zug_gegner2()
                            pass
                    elif angriffswurf >= spieler.verteidigung or ork2.wuerfel_w12 == 12:
                        aktion_schadenswurf_gegner2()
                    else:
                        print("Das Ork-Schwert verfehlt dich nur knapp.\n")
                        warten2()
                        if ork2.aktionen_nummer <= 0:
                            reset_spieler2()
                        else:
                            zug_gegner2()
                            pass
                elif befehl == 3:
                    print("Er greift vorsichtig an.\n")
                    warten2()
                    ork2.aktionen_nummer = ork2.aktionen_nummer - 1
                    ork2.ausdauer = ork2.ausdauer - 1
                    angriffswurf = ork2.geschick + ork2.wuerfel_w12 + ork2.angriffsbonus
                    ork2.angriffsbonus = - 2
                    ork2.verteidigung = ork2.verteidigung + 2
                    warten2()
                    print("Würfel: " + str(ork2.wuerfel_w12))
                    warten()
                    print("Angriffswurf: " + str(angriffswurf))
                    warten2()
                    if ork2.wuerfel_w12 == 1:
                        print("Der Ork greift dich mit seinem Schwert an, schwingt aber kolossal daneben.\n")
                        if ork2.aktionen_nummer <= 0:
                            reset_spieler2()
                        else:
                            zug_gegner2()
                            pass
                    elif angriffswurf >= spieler.verteidigung or ork2.wuerfel_w12 == 12:
                        aktion_schadenswurf_gegner2()
                    else:
                        print("Das Ork-Schwert verfehlt dich nur knapp.\n")
                        if ork2.aktionen_nummer <= 0:
                            reset_spieler2()
                        else:
                            zug_gegner2()
                            pass
                else:
                    print("Der Ork setzt bei seinem Angriff auf Geschwindigkeit.\n")
                    ork2.ausdauer = ork2.ausdauer - 1
                    ork2.verteidigung = ork2.verteidigung - 4
                    ork2.aktionen_nummer = ork2.aktionen_nummer - 0.5
                    ork2.angriffsbonus = -4
                    angriffswurf = ork2.geschick + ork2.wuerfel_w12 + ork2.angriffsbonus
                    warten2()
                    print("Würfel: " + str(ork2.wuerfel_w12))
                    warten()
                    print("Angriffswurf: " + str(angriffswurf))
                    warten2()
                    if ork2.wuerfel_w12 == 1:
                        print("Der Ork greift dich mit seinem Schwert an, schwingt aber kolossal daneben.\n")
                        warten()
                        if ork.aktionen_nummer == 0:
                            reset_spieler2()
                        else:
                            zug_gegner2()
                            pass
                    elif angriffswurf >= spieler.verteidigung or ork2.wuerfel_w12 == 12:
                        aktion_schadenswurf_gegner2()
                    else:
                        print("Das Ork-Schwert verfehlt dich nur knapp.\n")
                        if ork2.aktionen_nummer <= 0:
                            reset_spieler2()
                        else:
                            zug_gegner2()
                            pass

    # Weiter geht's mit der Erkundung.

        def raum_westkorridor1_nord2():
            print ("[Du verlässt die Schmugglerhöhle und gehst zurück in den Gang.]\n")
            warten2()
            print("Der Gang zu deiner Linken führt nun nach Süden, der zu deiner Rechten nach Norden, zurück zum Ausgang.\n")
            warten2()
            print("Die Höhle mit der Schmuggelware liegt nun hinter dir.\n")
            warten2()
            befehl = input("Wo willst du hin? (Optionen: Norden, Süden, Osten) \n > ").lower()
            if "nord" in befehl:
                raum_westkorridor1_sued_zurueck()
            elif "süd" in befehl:
                raum_westkorridor1_nord3()
            elif "ost" in befehl:
                raum_schmugglerhoehle()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.] \n")
                raum_westkorridor1_nord2()

        def raum_kreuzung2():
            print("[Du folgst dem Höhlengang und kommst wieder zur Kreuzung.] \n")
            warten2()
            print("Der Gang führt dich etwa 20 Meter weiter, bevor er schließlich an dem engen Spalt endet. \n")
            warten2()
            print("Zu deiner Rechten geht es nach Norden, hinter dir liegt der Osten, und vor dir der Westen. \n")
            warten2()
            befehl = input("Wo willst du hin? (Optionen: Norden, Osten, Süden, Westen) \n > ").lower()
            if "nord" in befehl:
                raum_eingang_hoehle2()
            elif "west" in befehl:
                raum_westkorridor1()
            elif "süd" in befehl:
                raum_suedkorridor1()
            elif "ost" in befehl:
                print ("Du schaust noch einmal über die Schulter, fragst dich aber, warum.\n")
                warten2()
                print("Doch, eigentlich weißt du das - du willst es dir nur nicht eingestehen.\n")
                warten2()
                print("Maika.\n")
                warten2()
                print("Nach all diesen Jahren ist es immer noch nicht klar, wessen Schuld das war.\n")
                warten2()
                print("Anschuldigungen bringen inzwischen nichts mehr, aber vermutlich hatte jeder seinen Teil beigetragen.\n")
                warten2()
                print("Letztlich beschließt du, die Angelegenheit zu verdrängen. Darin bist du mittlerweile geübt.\n")
                warten2()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")



        def raum_kreuzung4():
            print ("[Du folgst dem Höhlengang und kommst wieder zur Kreuzung.] \n")
            warten()
            print("Der Gang moosbewachsene Gang lässt sich dich schließlich wieder raus an die minimal frischere Luft.\n")
            warten2()
            print("Nun stehst du wieder an der Kreuzung. \n")
            warten2()
            print("Zu deiner Rechten geht es nach Süden, hinter dir liegt der Westen, und vor dir der Osten. \n")
            warten2()
            befehl = input("Wo willst du hin (Optionen: Norden, Osten, Süden, Westen)? \n > ").lower()
            if "nord" in befehl:
                raum_eingang_hoehle2()
            elif "west" in befehl:
                raum_westkorridor1()
            elif "süd" in befehl:
                raum_suedkorridor1()
            elif "ost" in befehl:
                raum_ostkorridor1()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")

        def raum_ostkorridor1():
            print("\n[Du befindest dich im östlichen Gang.]\n")
            warten2()
            print("Nachdem du dich durch einen kurzen, aber sehr schmalen Gang zwängst, wird dein Weg wieder breiter. \n")
            warten2()
            print("Dolly hätte hier nie und nimmer durchgepasst, sodass du dich langsam fragst, was dich geritten hat, diesen Weg zu nehmen. \n")
            warten2()
            print("Aber jetzt bist du nun mal hier.\n")
            warten2()
            print("Vor dir erstreckt sich ein weiterer Gang, zu deiner Linken siehst du aber eine Abzweigung, gen Norden. \n")
            warten2()
            print("Natürlich könntest du auch immer noch umkehren und nach Westen gehen, zurück, in den Gang, aus dem du gekommen bist. \n")
            warten2()
            befehl = input("Wo willst du hin (Norden, Osten, Westen)? \n > ").lower()
            if "nord" in befehl:
                raum_aufgang_vorfall1_von_sued()
            if "ost" in befehl:
                raum_ostkorridor2()
            elif "west" in befehl:
                raum_kreuzung2()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")



        def raum_ostkorridor2():
            print ("[Du folgst dem östlichen Gang.] \n")
            warten2()
            print("Der Gang führt dich noch etwa 20 Meter weiter, bevor er schließlich endet. \n")
            warten2()
            print("An der Felswand siehst du weitere Malereien. \n")
            warten2()
            print("Seltsam. Du kannst dich gar nicht daran erinnern, hier mal gespielt zu haben. \n")
            warten2()
            print("Dann wiederum: Auf dem Boden liegen irgendwelche Scherben. \n")
            warten2()
            print("Vermutlich war das einmal Tongeschirr, vielleicht auch Tonspielzeug. Das Dorf ist schließlich für seine Tonpuppen in der Region bekannt. \n")
            warten2()
            print("Aber die dem auch immer sei, führt der Weg hier nicht mehr weiter. \n")
            warten2()
            print("Zu deiner Linken ist ein weiterer Gang, etwa schmaler als dieser hier, aber zumindest breit genug, dass du dich nicht zu sehr anstrengen musst. \n")
            warten2()
            print("Natürlich könntest du auch wieder umkehren – der erste Gang zu deiner Linken war immerhin etwas breiter. \n")
            warten2()
            befehl = input("Wo willst du hin? (Optionen: Norden, Westen) \n > ").lower()
            for i in befehl:
                if "nord" in befehl:
                    raum_aufgang_vorfall2_von_sued()
                if "west" in befehl:
                    raum_ostkorridor1()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")
                    break

        def raum_aufgang_vorfall1_von_sued():
            print("[Du folgst der ersten Abzweigung des Ostgangs.]\n")
            warten2()
            print("Der Weg windet sich mehr als die anderen, aber du kommst trotzdem gut durch. \n")
            warten2()
            print("Der Gang führt zu einer kleinen Lichtung. Oder so würdest du sie nennen, wenn du im Wald wärst. \n")
            warten2()
            print("Wie heißen solche Öffnungen in einer Höhle? \n")
            warten2()
            print("Du müsstest später jemanden fragen, jetzt fällt es dir nicht ein. \n")
            warten2()
            print("Dafür weißt du jetzt wieder, wo du bist. \n")
            warten2()
            print("In dieser Dämmerung würdest du ohne Licht nichts erkennen, tagsüber sollte hier aber alles einigermaßen sichtbar sein.\n")
            warten2()
            print("Zumindest deutet das hohe Pfeifen über dir auf jede Menge Löcher, durch die ein bisschen Tageslicht - und Regenwasser - eindringen könnte.\n")
            warten2()
            print("Die feuchte Felswand trägt immer noch Spuren von jenem Tag. \n")
            warten2()
            print("Nicht einmal die Feuchtigkeit und die Zeit konnten hier alles verwischen. \n")
            warten2()
            print("Oder die Spuren auf dem Boden, den schon lange niemand mehr berührte. \n")
            warten2()
            print("Oh, Maika… \n")
            warten2()
            print("Wenn du nur die Zeit zurückdrehen könntest. \n")
            warten2()
            print("Aber es ist zu spät. \n")
            warten2()
            print("Vielleicht war es ein Fehler, hierher zu kommen – zu viele Geister der Vergangenheit hier drin. \n")
            warten2()
            print("Du schüttelst deinen Kopf und zwingst dich zurück in das Hier und Jetzt. \n")
            warten2()
            print("Vielleicht kannst du später mit jemanden aus dem Dorf bei einem Glas Pfefferwodka darüber reden, aber jetzt musst du weiter. \n")
            warten2()
            print("Du kannst natürlich wieder zurückgehen, aber zu deiner Rechten führt noch ein Gang Richtung Osten. \n")
            warten2()
            befehl = input("Wo willst du hin? (Optionen: Süden, Osten) \n > ").lower()
            for i in befehl:
                if "süd" in befehl:
                    raum_ostkorridor1_zurueck()
                elif "ost" in befehl:
                    raum_aufgang_vorfall2_von_nord()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")
                    break


        def raum_aufgang_vorfall1_von_nord():
            print ("[Du verlässt den Ort des Vorfalls und folgst der vor dir liegenden Abzweigung nach Süden]")
            warten2()
            print("Der Gang windet sich mehr als die anderen, fühlt sich von der Länger her aber nur minimal länger an. \n")
            warten2()
            print("Du kommst zu einem weiteren Gang, der nach links führt. \n")
            warten2()
            print("Moment mal! \n")
            warten2()
            print("Von dir aus gesehen wäre links der Osten, und an den Wänden siehst du vertraute Spuren und Malereien... \n")
            warten2()
            print("Ach, verdammt! \n")
            warten2()
            print("Herzlichen Glückwunsch, du bist im Kreis gegangen! \n")
            warten2()
            print("Du kannst gar nicht beschreiben, wie sehr dich das gerade ärgert, so eine Zeitverschwendung! \n")
            warten2()
            print("Aber es bringt nichts, du musst immer noch weiter. \n")
            warten2()
            print("Zu deiner Linken geht es immer noch nach Osten, aber was ist der Sinn? \n")
            warten2()
            print("Du biegst nach rechts ab, gen Westen, und zwängst dich wieder durch den engen Spalt. \n")
            warten2()
            print("Nun stehst du wieder an der Kreuzung.\n")
            warten2()
            print("Du weißt, dass der Eingang in die Säuselhöhle im Norden liegt, von dir aus gesehen rechts. \n")
            warten2()
            print("Dementsprechend führt dich der gerade Weg also nach Westen. \n")
            warten2()
            print("Du deiner Linken liegt der Süden, und hinter dir geht es Richtung Ost. \n")
            warten2()
            raum_kreuzung2()



        def raum_aufgang_vorfall2_von_sued():
            print ("Du folgst der zweiten Abzweigung des Ostgangs.]\n")
            warten2()
            print("Der Gang ist schmal, aber du kommst trotzdem durch. \n")
            warten2()
            print("Er führt zu einer kleinen Lichtung. Oder so würdest du sie nennen, wenn du im Wald wärst. \n")
            warten2()
            print("Wie heißen solche Öffnungen in einer Höhle? Du müsstest später jemanden fragen, jetzt fällt es dir nicht ein. \n")
            warten2()
            print("Dafür weißt du jetzt wieder, wo du bist. \n")
            warten2()
            print("In dieser Dämmerung würdest du ohne Licht nichts erkennen, tagsüber sollte hier aber alles einigermaßen sichtbar sein.\n")
            warten2()
            print("Zumindest deutet das hohe Pfeifen über dir auf jede Menge Löcher, durch die ein bisschen Tageslicht - und Regenwasser - eindringen könnte.\n")
            warten2()
            print("Die feuchte Felswand trägt immer noch Spuren von jenem Tag. \n")
            warten2()
            print("Nicht einmal die Feuchtigkeit und die Zeit konnten hier alles verwischen. \n")
            warten2()
            print("Oder die Spuren auf dem Boden, den schon lange niemand mehr berührte. \n")
            warten2()
            print("Oh, Maika…  Wenn du nur die Zeit zurückdrehen könntest. \n")
            warten2()
            print("Aber es ist zu spät. \n")
            warten2()
            print("Vielleicht war es ein Fehler, hierher zu kommen – zu viele Geister der Vergangenheit hier drin. \n")
            warten2()
            print("Du schüttelst deinen Kopf und zwingst dich zurück in das Hier und Jetzt.\n")
            warten2()
            print("Vielleicht kannst du später mit jemanden aus dem Dorf bei einem Glas Pfefferwodka darüber reden, aber jetzt musst du weiter. \n")
            warten2()
            print("Du kannst natürlich wieder zurückgehen, aber zu deiner Linken - bzw. vor dir - führt noch ein Gang Richtung Westen und biegt nach Süden ab. \n")
            warten2()
            befehl = input("Wo willst du hin? (Optionen: Westen, Osten) \n > ").lower()
            if "ost" in befehl:
                raum_ostkorridor2_von_nord()
            elif "west" in befehl:
                raum_aufgang_vorfall1_von_nord()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")


        def raum_aufgang_vorfall2_von_nord():
            print("[Du verlässt den Ort des Vorfalls und folgst der vor dir liegenden Abzweigung nach Süden.]\n")
            warten2()
            print("Der Weg endet an einer Felswand. \n")
            warten2()
            print("Nach Osten geht es von hier aus nicht weiter, aber direkt vor dir führt ein schmaler Gang nach Süden.\n")
            warten2()
            print("Natürlich könntest du auch immer noch zurück nach Westen gehen.\n")
            warten2()
            befehl =  input("Wo willst du hin? (Optionen: Westen, Süden) \n > ").lower()
            if "süd" in befehl:
                raum_ostkorridor1_von_nord()
            elif "west" in befehl:
                raum_aufgang_vorfall1_von_sued()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")

        def raum_ostkorridor1_von_nord():
            print("Der Gang ist schmal, aber du kommst trotzdem durch. \n")
            warten2()
            print("Nach etwa 20 Schritten endet aber auch dieser Weg. \n")
            warten2()
            print("Zu deiner Rechten geht es aber weiter, gen West. \n")
            warten2()
            print("Und natürlich gäbe es noch den Weg zurück. \n")
            warten2()
            print("An der Felswand siehst du weitere Malereien. \n")
            warten2()
            print("Seltsam. Du kannst dich gar nicht daran erinnern, hier mal gespielt zu haben. \n")
            warten2()
            print("Dann wiederum: Auf dem Boden liegen irgendwelche Scherben. \n")
            warten2()
            print("Vermutlich war das einmal Tongeschirr, vielleicht auch Tonspielzeug.\n")
            warten2()
            print(" Das Dorf ist schließlich für seine Tonpuppen in der Region bekannt. \n")
            warten2()
            print("Aber wie dem auch immer sei, führt der Weg hier nicht mehr weiter. \n")
            warten2()
            print("Zu deiner Rechten ist ein weiterer Gang nach Westen. \n")
            warten2()
            print("Natürlich könntest du auch wieder umkehren, gen Norden, aber du wagst es nicht, diesen Ort noch einmal zu betreten. \n")
            warten2()
            print("Du gehst also weiter. Du kommst voran und siehst einen schmalen Spalt in der Felswand vor dir. \n")
            warten2()
            print("Moment mal... Ach, verdammt! \n")
            warten2()
            print("Herzlichen Glückwunsch, du bist im Kreis gegangen! \n")
            warten2()
            print("Du kannst gar nicht beschreiben, wie sehr dich das gerade ärgert, so eine Zeitverschwendung! \n")
            warten2()
            print("Aber es bringt nichts, du musst immer noch weiter. \n")
            warten2()
            print("Zu deiner Linken geht es immer noch nach Osten, aber was ist der Sinn? \n")
            warten2()
            print("Du gehst gerade aus, gen Westen, und zwängst dich wieder durch den engen Spalt. \n")
            warten2()
            print("[Du verlässt den östlichen Gang und kommst wieder zur Kreuzung, Gesicht gen West.] \n")
            warten2()
            print("Nun stehst du wieder an der Kreuzung. \n")
            warten2()
            print("Du weißt, dass der Eingang in die Säuselhöhle im Norden liegt, von dir aus gesehen rechts. \n")
            warten2()
            print("Dementsprechend führt dich der gerade Weg also nach Westen. \n")
            warten2()
            print("Du deiner Linken liegt der Süden, und hinter dir geht es Richtung Ost.\n")
            warten2()
            befehl = input("Wo willst du hin? (Optionen: Norden, Süden, Westen, Osten)? \n > ").lower()
            for i in befehl:
                if "west" in befehl:
                    raum_westkorridor1()
                elif "süd" in befehl:
                    raum_suedkorridor1()
                elif "nord" in befehl:
                    raum_eingang_hoehle2()
                elif "ost" in befehl:
                    print ("Du schaust noch einmal nach links, fragst dich aber, warum.\n")
                    warten2()
                    print("Doch, eigentlich weißt du das - du willst es dir nur nicht eingestehen.\n")
                    warten2()
                    print("Maika.\n")
                    warten2()
                    print("Nach all diesen Jahren ist es immer noch nicht klar, wessen Schuld das war.\n")
                    warten2()
                    print("Anschuldigungen bringen inzwischen nichts mehr, aber vermutlich hatte jeder seinen Teil beigetragen.\n")
                    warten2()
                    print("Letztlich beschließt du, die Angelegenheit zu verdrängen. Darin bist du mittlerweile geübt.\n")
                    warten2()
                    raum_ostkorridor1_von_nord()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")


        def raum_kreuzung1():
            print("[Du betrittst die Säuselhöhle und stehst an der Kreuzung, Gesicht gen Süd.] \n")
            warten2()
            print("Vor dir erstreckt sich ein schmaler Gang. Du spürst - und hörst - sofort den Windzug, der dir entgegen bläst. \n")
            warten2()
            print("Das Pfeifen erinnert dich sofort daran, woher die Höhle ihren Namen hat. \n")
            warten2()
            print("Verunsichert, vielleicht auch etwas verängstigt, gehst du trotzdem weiter. Dabei schaust du dich vorsichtig um. \n")
            warten2()
            print("Die Malereien der Dorfkinder sind ordentlich verblasst, die Farbe abgetragen vom Alter und Witterungsbedingungen. \n")
            warten2()
            print("Wer aber weiß, was diese Kritzeleien darstellen sollen, wird sie sofort wiedererkennen.\n")
            warten2()
            print("Nur wer sie genau gemalt hat, das kannst du nicht mehr feststellen. Es ist einfach zu lange her. \n")
            warten2()
            print("Ansonsten haben sich die Steinwände nicht verändert. \n")
            warten2()
            print("Die Säuselhöhle ist wie immer in ihrem alten Glanz.\n")
            warten2()
            print("Schon bald kommst du zu einer Weggabelung. Nein, eher einer Kreuzung. \n")
            warten2()
            print("Du weißt, dass der Eingang in die Säuselhöhle im Norden liegt. \n")
            warten2()
            print("Dementsprechend führt dich der gerade Weg also nach Süden. \n")
            warten2()
            print("Zu deiner Linken (Osten) und Rechten (Westen) ist aber jeweils noch ein Gang. \n")
            warten2()
            befehl = input("Wo willst du hin? (Optionen: Norden, Osten, Süden, Westen)? \n > ").lower()
            for i in befehl:
                if "ost" in befehl:
                    raum_ostkorridor1()
                elif "west" in befehl:
                    raum_westkorridor1()
                elif "süd" in befehl:
                    raum_suedkorridor1()
                elif "nord" in befehl:
                    raum_eingang_hoehle2()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")

        def raum_ostkorridor2_von_nord():
            print ("\n [Du verlässt den Ort des Vorfalls und kehrst zurück in den östlichen Gang, Gesicht gen Süd.] \n")
            warten2()
            print("Der Gang führt dich noch etwa 20 Meter weiter, bevor er schließlich endet. \n")
            warten2()
            print("An der Felswand siehst du weitere Malereien. \n")
            warten2()
            print("Seltsam. Du kannst dich gar nicht daran erinnern, hier mal gespielt zu haben. \n")
            warten2()
            print("Dann wiederum: Auf dem Boden liegen irgendwelche Scherben. \n")
            warten2()
            print("Vermutlich war das einmal Tongeschirr, vielleicht auch Tonspielzeug.\n")
            warten2()
            print("Das Dorf ist schließlich für seine Tonpuppen in der Region bekannt. \n")
            warten2()
            print("Aber die dem auch immer sei, führt der Weg hier nicht mehr weiter. \n")
            warten2()
            print("Hinter dir geht es wieder Richtung Norden... Zu jenem Ort.\n")
            warten2()
            print("Natürlich könntest du auch wieder ein Stück zurückgehen – der erste Gang zu deiner Rechten war immerhin etwas breiter. \n")
            warten2()
            befehl = input("Wo willst du hin? (Optionen: Norden, Westen) \n > ").lower()
            for i in befehl:
                if "nord" in befehl:
                    raum_aufgang_vorfall2_von_sued()
                if "west" in befehl:
                    raum_ostkorridor1_von_nord()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.\n]")
                    pass

        def raum_kreuzung3():
            print ("\n [Du betrittst die Säuselhöhle und an an der Kreuzung, Gesicht gen SÜd.] \n")
            warten2()
            print("Vor dir erstreckt sich ein schmaler Gang. Du spürst sofort den Windzug, der dir entgegen bläst. \n")
            warten2()
            print("Das Pfeifen erinnert dich sofort daran, woher die Höhle ihren Namen hat. \n")
            warten2()
            print("Verunsichert, vielleicht auch etwas verängstigt, gehst du trotzdem weiter.\n")
            warten2()
            print("Dabei schaust du dich vorsichtig um. \n")
            warten2()
            print("Die Malereien der Dorfkinder sind ordentlich verblasst, die Farbe abgetragen vom Alter und Witterungsbedingungen. \n")
            warten2()
            print("Wer aber weiß, was diese Kritzeleien darstellen sollen, wird sie sofort wiedererkennen.\n")
            warten2()
            print("Nur wer sie genau gemalt hat, das kannst du nicht mehr feststellen. Es ist einfach zu lange her. \n")
            warten2()
            print("Ansonsten haben sich die Steinwände nicht verändert. Die Säuselhöhle ist wie immer in ihrem alten Glanz.\n")
            warten2()
            print("Schon bald kommst du einer Weggabelung. Nein, eher einer Kreuzung. \n")
            warten2()
            print("Du weißt, dass der Eingang in die Säuselhöhle im Norden liegt. \n")
            warten2()
            print("Dementsprechend führt dich der gerade Weg also nach Süden. \n")
            warten2()
            print("Zu deiner Linken (Osten) und Rechten (Westen) ist aber jeweils noch ein Gang. \n")
            warten2()
            befehl = input("Wo willst du hin? (Optionen: Norden, Osten, Süden, Westen)? \n > ").lower()
            for i in befehl:
                if "ost" in befehl:
                    print ("Du schaust noch einmal nach links, fragst dich aber, warum.\n")
                    warten2()
                    print("Doch, eigentlich weißt du das - du willst es dir nur nicht eingestehen.\n")
                    warten2()
                    print("Maika.\n")
                    warten2()
                    print("Nach all diesen Jahren ist es immer noch nicht klar, wessen Schuld das war.\n")
                    warten2()
                    print("Anschuldigungen bringen inzwischen nichts mehr, aber vermutlich hatte jeder seinen Teil beigetragen.\n")
                    warten2()
                    print("Letztlich beschließt du, die Angelegenheit zu verdrängen. Darin bist du mittlerweile geübt.\n")
                    warten2()
                elif "west" in befehl:
                    raum_westkorridor1()
                elif "süd" in befehl:
                    raum_suedkorridor1()
                elif "nord" in befehl:
                    raum_eingang_hoehle2()
                else:
                    print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")
                    pass

        def raum_ostkorridor1_zurueck():
            print ("Du gehst zurück nach Süden und wieder am Spalt, durch den du in den Ostgang gekommen bist.\n")
            warten2()
            print("Nachdem du dich durch einen kurzen, aber sehr schmalen Gang zwängst, wird dein Weg wieder breiter. \n")
            warten2()
            print("Dolly hätte hier nie und nimmer durchgepasst, sodass du dich langsam fragst, was dich geritten hat, diesen Weg zu nehmen. \n")
            warten2()
            print("Aber jetzt bist du nun mal hier. Vor dir erstreckt sich ein weiterer Gang, zu deiner Linken siehst du aber eine Abzweigung, gen Norden. \n")
            warten2()
            print("Natürlich könntest du auch immer noch umkehren und nach Westen gehen, zurück, in den Gang, aus dem du gekommen bist. \n")
            warten2()
            befehl = input("Wo willst du hin (Norden, Osten, Westen)? \n > ").lower()
            if "nord" in befehl:
                raum_aufgang_vorfall1_von_sued()
            if "ost" in befehl:
                raum_ostkorridor2()
            elif "west" in befehl:
                raum_kreuzung2()
            else:
                print("[Hoppla! Wie es scheint, hat dein erbarmungsloser dunkler Overlord (auch bekannt als Spielleiter) diese Antwortmöglichkeit nicht vorgesehen.]\n")




        # Spielstart
        raum_start1()
        pass