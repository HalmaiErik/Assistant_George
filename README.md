# Assistant_George
 A voiced-activated virtual assistant named George.
 
 The application uses the speech_recognition package to recognize the command given by the user. For most of the commands, it uses Google search and Beautiful Soup to find the correct answer. As of now it also recognizes some special commands like "define <word>" (gives all the definitions of the word given by Google) and "weather in <location>" which gives the degrees in celsius. George will read the answer using win32com's Dispatch.
