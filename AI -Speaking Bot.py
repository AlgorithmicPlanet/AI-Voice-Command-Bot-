import speech_recognition as sr
import webbrowser
import wolframalpha
import wikipedia
import time
import os
import pygame
import pyttsx3
import pyperclip
import win32com.client


r = sr.Recognizer()                                                                         #starting the speech_recognition recognizer
r.pause_threshold = 0.7                                                                     #it works with 1.2 as well
r.energy_threshold = 400
engine = pyttsx3.init()
engine.say('Hello! For a list of commands, plese say "keyword list"')
engine.runAndWait()
print("For a list of commands, please say: 'keyword list'...")
shell = win32com.client.Dispatch("WScript.Shell")                                           #to handle keyboard events


#List of Available Commands

keywd = 'keyword list'
google = 'search for'
acad = 'academic search'
sc = 'deep search'
wkp = 'wiki page for'
rdds = 'read this text'
sav = 'save this text'
bkmk = 'bookmark this page'
vid = 'video for'
wtis = 'what is'
wtar = 'what are'
whis = 'who is'
whws = 'who was'
when = 'when'
where = 'where'
how = 'how'
paint = 'open paint'
lsp = 'silence please'
lsc = 'resume listening'
stoplst = 'stop listening'


while True:                                                                                 #The main loop

    with sr.Microphone() as source:

        try:

            audio = r.listen(source, timeout = None)                                        #instantiating the Microphone, (timeout = None) can be an option
            message = str(r.recognize_google(audio))
            print('You said: ' + message)

            if google in message:                                                           #what happens when google keyword is recognized

                words = message.split()
                del words[0:2]
                st = ' '.join(words)
                print('Google Results for: '+str(st))
                url='http://google.com/search?q='+st
                webbrowser.open(url)
                engine = pyttsx3.init()
                engine.say('Google Results for: '+str(st))
                engine.runAndWait()


            elif acad in message:                                                           #what happens when acad keyword is recognized

                words = message.split()
                del words[0:2]
                st = ' '.join(words)
                print('Academic Results for: '+str(st))
                url='https://scholar.google.ro/scholar?q='+st
                webbrowser.open(url)
                engine = pyttsx3.init()
                engine.say('Academic Results for: '+str(st))
                engine.runAndWait()



            elif wkp in message:                                                            #what happens when wkp keyword is recognized

                try:

                    words = message.split()
                    del words[0:3]
                    st = ' '.join(words)
                    wkpres = wikipedia.summary(st, sentences=2)

                    try:

                        print('\n' + str(wkpres) + '\n')
                        engine = pyttsx3.init()
                        engine.say(wkpres)
                        engine.runAndWait()


                    except UnicodeEncodeError:
                        engine = pyttsx3.init()
                        engine.say(wkpres)
                        engine.runAndWait()

                except wikipedia.exceptions.DisambiguationError as e:
                    print (e.options)
                    engine = pyttsx3.init()
                    engine.say("Too many results for this keyword. Please be more specific and try again")
                    engine.runAndWait()
                    continue

                except wikipedia.exceptions.PageError as e:
                    print('The page does not exist')
                    engine = pyttsx3.init()
                    engine.say('The page does not exist')
                    engine.runAndWait()
                    continue

            elif sc in message:                                                             #what happens when sc keyword is recognized

                try:
                    words = message.split()
                    del words[0:1]
                    st = ' '.join(words)
                    scq = cl.query(st)
                    sca = next(scq.results).text
                    print('The answer is: '+str(sca))
                    #url='http://www.wolframalpha.com/input/?i='+st
                    #webbrowser.open(url)
                    engine = pyttsx3.init()
                    engine.say('The answer is: '+str(sca))
                    engine.runAndWait()


                except StopIteration:
                    print('Your question is ambiguous. Please try again!')
                    engine = pyttsx3.init()
                    engine.say('Your question is ambiguous. Please try again!')
                    engine.runAndWait()


                else:
                    print('No query provided')

            elif paint in message:                                                          #what happens when paint keyword is recognized
                os.system('mspaint')

            elif rdds in message:                                                           #what happens when rdds keyword is recognized
                print("Reading your text")
                engine = pyttsx3.init()
                engine.say(pyperclip.paste())
                engine.runAndWait()


            elif sav in message:                                                            #what happens when sav keyword is recognized
                with open('path to your text file', 'a') as f:
                    f.write(pyperclip.paste())
                print("Saving your text to file")
                engine = pyttsx3.init()
                engine.say("Saving your text to file")
                engine.runAndWait()


            elif bkmk in message:                                                           #what happens when bkmk keyword is recognized
                shell.SendKeys("^d")
                engine = pyttsx3.init()
                engine.say("Page bookmarked")
                engine.runAndWait()


            elif keywd in message:                                                          #what happens when keywd keyword is recognized

                print('')
                print('Say ' + google + ' to return a Google search')
                print('Say ' + acad + ' to return a Google Scholar search')
                print('Say ' + sc + ' to return a Wolfram Alpha query')
                print('Say ' + wkp + ' to return a Wikipedia page')
                print('Say ' + book + ' to return an Amazon book search')
                print('Say ' + rdds + ' to read the text you have highlighted and Ctrl+C (copied to clipboard)')
                print('Say ' + sav + ' to save the text you have highlighted and Ctrl+C-ed (copied to clipboard) to a file')
                print('Say ' + bkmk + ' to bookmark the page your are currently reading in your browser')
                print('Say ' + vid + ' to return video results for your query')
                print('For more general questions, ask them naturally and I will do my best to find a good answer')
                print('Say ' + stoplst + ' to shut down')
                print('')

            elif vid in message:                                                            #what happens when vid keyword is recognized

                words = message.split()
                del words[0:2]
                st = ' '.join(words)
                print('Video Results for: '+str(st))
                url='https://www.youtube.com/results?search_query='+st
                webbrowser.open(url)
                engine = pyttsx3.init()
                engine.say('Video Results for: '+str(st))
                engine.runAndWait()


            elif wtis in message:                                                           #what happens when wtis keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('The answer is: '+str(sca))
                    #url='http://www.wolframalpha.com/input/?i='+st
                    #webbrowser.open(url)
                    engine = pyttsx3.init()
                    engine.say('The answer is: '+str(sca))
                    engine.runAndWait()


                except UnicodeEncodeError:
                    engine = pyttsx3.init()
                    engine.say('The answer is: '+str(sca))
                    engine.runAndWait()




                except StopIteration:

                    words = message.split()
                    del words[0:2]
                    st = ' '.join(words)
                    print('Google Results for: '+str(st))
                    url='http://google.com/search?q='+st
                    webbrowser.open(url)
                    engine = pyttsx3.init()
                    engine.say('Google Results for: '+str(st))
                    engine.runAndWait()


            elif wtar in message:                                                           #what happens when wtar keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('The answer is: '+str(sca))
                    #url='http://www.wolframalpha.com/input/?i='+st
                    #webbrowser.open(url)
                    engine = pyttsx3.init()
                    engine.say('The answer is: '+str(sca))
                    engine.runAndWait()


                except UnicodeEncodeError:
                    engine = pyttsx3.init()
                    engine.say('The answer is: '+str(sca))
                    engine.runAndWait()



                except StopIteration:

                    words = message.split()
                    del words[0:2]
                    st = ' '.join(words)
                    print('Google Results for: '+str(st))
                    url='http://google.com/search?q='+st
                    webbrowser.open(url)
                    engine = pyttsx3.init()
                    engine.say('Google Results for: '+str(st))
                    engine.runAndWait()


            elif whis in message:                                                           #what happens when whis keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: '+str(sca)+'\n')
                    engine = pyttsx3.init()
                    engine.say('The answer is: '+str(sca))
                    engine.runAndWait()


                except StopIteration:

                    try:

                        words = message.split()
                        del words[0:2]
                        st = ' '.join(words)
                        wkpres = wikipedia.summary(st, sentences=2)
                        print('\n' + str(wkpres) + '\n')
                        engine = pyttsx3.init()
                        engine.say(wkpres)
                        engine.runAndWait()


                    except UnicodeEncodeError:
                        engine = pyttsx3.init()
                        engine.say(wkpres)
                        engine.runAndWait()



                    except:

                        words = message.split()
                        del words[0:2]
                        st = ' '.join(words)
                        print('Google Results (last exception) for: '+str(st))
                        url='http://google.com/search?q='+st
                        webbrowser.open(url)
                        engine = pyttsx3.init()
                        engine.say('Google Results for: '+str(st))
                        engine.runAndWait()



            elif whws in message:                                                           #what happens when whws keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: '+str(sca)+'\n')
                    engine = pyttsx3.init()
                    engine.say('The answer is: '+str(sca))
                    engine.runAndWait()


                except StopIteration:

                    try:

                        words = message.split()
                        del words[0:2]
                        st = ' '.join(words)
                        wkpres = wikipedia.summary(st, sentences=2)
                        print('\n' + str(wkpres) + '\n')
                        engine = pyttsx3.init()
                        engine.say(wkpres)
                        engine.runAndWait()


                    except UnicodeEncodeError:
                        engine = pyttsx3.init()
                        engine.say(wkpres)
                        engine.runAndWait()



                    except:

                        words = message.split()
                        del words[0:2]
                        st = ' '.join(words)
                        print('Google Results for: '+str(st))
                        url='http://google.com/search?q='+st
                        webbrowser.open(url)
                        engine = pyttsx3.init()
                        engine.say('Google Results for: '+str(st))
                        engine.runAndWait()


            elif when in message:                                                         #what happens when 'when' keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: '+str(sca)+'\n')
                    engine = pyttsx3.init()
                    engine.say('The answer is: '+str(sca))
                    engine.runAndWait()


                except UnicodeEncodeError:
                    engine = pyttsx3.init()
                    engine.say('The answer is: ' + str(sca))
                    engine.runAndWait()



                except:

                    print('Google Results for: '+str(message))
                    url='http://google.com/search?q='+str(message)
                    webbrowser.open(url)
                    engine = pyttsx3.init()
                    engine.say('Google Results for: '+str(message))
                    engine.runAndWait()


            elif where in message:                                                        #what happens when 'where' keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: '+str(sca)+'\n')
                    engine = pyttsx3.init()
                    engine.say('The answer is: '+str(sca))
                    engine.runAndWait()


                except UnicodeEncodeError:
                    engine = pyttsx3.init()
                    engine.say('The answer is: ' + str(sca))
                    engine.runAndWait()



                except:

                    print('Google Results for: '+str(message))
                    url='http://google.com/search?q='+str(message)
                    webbrowser.open(url)
                    engine = pyttsx3.init()
                    engine.say('Google Results for: '+str(message))
                    engine.runAndWait()


            elif how in message:                                                          #what happens when 'how' keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: '+str(sca)+'\n')
                    engine = pyttsx3.init()
                    engine.say('The answer is: '+str(sca))
                    engine.runAndWait()


                except UnicodeEncodeError:
                    engine = pyttsx3.init()
                    engine.say('The answer is: ' + str(sca))
                    engine.runAndWait()



                except:

                    print('Google Results for: '+str(message))
                    url='http://google.com/search?q='+str(message)
                    webbrowser.open(url)
                    engine = pyttsx3.init()
                    engine.say('Google Results for: '+str(message))
                    engine.runAndWait()


            elif stoplst in message:                                                        #what happens when stoplst keyword is recognized
                engine = pyttsx3.init()
                engine.say("I am shutting down")
                engine.runAndWait()
                print("Shutting down...")
                break

            elif lsp in message:

                engine = pyttsx3.init()
                engine.say('Listening is paused')
                engine.runAndWait()
                print('Listening is paused')
                r2 = sr.Recognizer()
                r2.pause_threshold = 0.7
                r2.energy_threshold = 400

                while True:

                    with sr.Microphone() as source2:

                        try:

                            audio2 = r2.listen(source2, timeout = None)
                            message2 = str(r.recognize_google(audio2))

                            if lsc in message2:
                                engine = pyttsx3.init()
                                engine.say('I am listening')
                                engine.runAndWait()

                                break

                            else:
                                continue

                        except sr.UnknownValueError:

                            print("Listening is paused. Say resume listening when you're ready...")

                        except sr.RequestError:
                            engine = pyttsx3.init()
                            engine.say("I'm sorry, I couldn't reach google")
                            engine.runAndWait()

                            print("I'm sorry, I couldn't reach google")


            else:
                pass

        except sr.UnknownValueError:
            print("For a list of commands, say: 'keyword list'...")

        except sr.RequestError:
            engine = pyttsx3.init()
            engine.say("I'm sorry, I couldn't reach google")
            engine.runAndWait()

            print("I'm sorry, I couldn't reach google")

    time.sleep(0.3)